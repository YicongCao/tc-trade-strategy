"""五年 FCFF 情景和反向估值；所有金额以 USD million 计。"""

import math
from datetime import date

UNIVERSE = ("NVDA", "MSFT", "AMZN", "GOOGL", "META")


def standalone_quarters(facts: list[dict], cutoff: date) -> list[dict]:
    """同一起点的 YTD 相减；去重时只使用截止日以前已披露版本。"""
    unique = {}
    for f in facts:
        if f.get("filed", "9999") > str(cutoff) or not f.get("start"):
            continue
        key = f["start"], f["end"]
        if key not in unique or f["filed"] > unique[key]["filed"]:
            unique[key] = f
    result = {}
    for f in sorted(unique.values(), key=lambda x: (x["start"], x["end"])):
        start, end = date.fromisoformat(f["start"]), date.fromisoformat(f["end"])
        prior = [p for p in unique.values() if p["start"] == f["start"] and p["end"] < f["end"]]
        if prior:
            p = max(prior, key=lambda x: x["end"])
            duration = (end - date.fromisoformat(p["end"])).days
            value = f["val"] - p["val"]
        else:
            duration, value = (end - start).days + 1, f["val"]
        if 70 <= duration <= 110:
            candidate = {
                "end": f["end"],
                "value": value,
                "filed": f["filed"],
                "duration_days": duration,
            }
            if f["end"] not in result or f["filed"] >= result[f["end"]]["filed"]:
                result[f["end"]] = candidate
    return sorted(result.values(), key=lambda x: x["end"])


def trailing_twelve_months(quarters: list[dict]) -> float:
    tail = quarters[-4:]
    if len(tail) != 4 or not 340 <= sum(q["duration_days"] for q in tail) <= 385:
        raise ValueError("TTM 缺少四个完整季度")
    for previous, current in zip(tail, tail[1:]):
        if (
            not 70
            <= (date.fromisoformat(current["end"]) - date.fromisoformat(previous["end"])).days
            <= 110
        ):
            raise ValueError("TTM 季度不连续")
    return sum(q["value"] for q in tail)


def dcf(base: dict, scenario: dict) -> dict:
    """经营租赁作为经营费用；融资租赁资本化。SBC 不回加，稀释单列。"""
    required = ("revenue", "net_debt", "diluted_shares")
    if any(k not in base or not math.isfinite(base[k]) for k in required):
        raise ValueError("缺少或无效财务输入")
    if base["revenue"] <= 0 or base["diluted_shares"] <= 0:
        raise ValueError("收入和股数必须为正")
    fields = (
        "growth",
        "operating_margin",
        "tax_rate",
        "da_ratio",
        "capex_ratio",
        "working_capital_ratio",
        "wacc",
        "terminal_growth",
    )
    if any(
        k not in scenario
        or not isinstance(scenario[k], (int, float))
        or not math.isfinite(scenario[k])
        for k in fields
    ):
        raise ValueError("缺少或无效情景假设")
    if not 0 <= scenario["tax_rate"] <= 1 or scenario.get("dilution", 0) <= -1:
        raise ValueError("税率或稀释假设无效")
    if any(scenario[k] < 0 for k in ("da_ratio", "capex_ratio")):
        raise ValueError("折旧及资本开支比例不得为负")
    wacc, terminal = scenario["wacc"], scenario["terminal_growth"]
    if not 0 <= terminal < wacc or scenario["growth"] <= -1:
        raise ValueError("终值增长必须小于折现率，收入增长不能低于 -100%")
    revenue, pv, years = base["revenue"], 0, []
    for year in range(1, 6):
        prior = revenue
        revenue *= 1 + scenario["growth"]
        margin = (
            scenario.get("start_margin", scenario["operating_margin"])
            + (
                scenario["operating_margin"]
                - scenario.get("start_margin", scenario["operating_margin"])
            )
            * year
            / 5
        )
        nopat = revenue * margin * (1 - scenario["tax_rate"])

        def fade(key):
            start = scenario.get("start_" + key, scenario[key])
            return start + (scenario[key] - start) * year / 5

        da = revenue * fade("da_ratio")
        capex = revenue * fade("capex_ratio")
        working = (revenue - prior) * scenario["working_capital_ratio"]
        cash = nopat + da - capex - working
        pv += cash / (1 + wacc) ** year
        years.append({"year": year, "revenue": revenue, "fcff": cash})
    terminal_revenue = revenue * (1 + terminal)
    terminal_cash = (
        terminal_revenue
        * (
            scenario["operating_margin"] * (1 - scenario["tax_rate"])
            + scenario["da_ratio"]
            - scenario["capex_ratio"]
        )
        - revenue * terminal * scenario["working_capital_ratio"]
    )
    if terminal_cash <= 0 or years[-1]["fcff"] <= 0:
        raise ValueError("第五年或稳定期现金流非正，永续增长终值不适用")
    terminal_pv = terminal_cash / (wacc - terminal) / (1 + wacc) ** 5
    ev = pv + terminal_pv
    shares = base["diluted_shares"] * (1 + scenario.get("dilution", 0)) ** 5
    if shares <= 0:
        raise ValueError("股数无效")
    equity = ev - base["net_debt"] + base.get("non_operating_assets", 0)
    return {
        "enterprise_value": ev,
        "equity_value": equity,
        "per_share": equity / shares,
        "terminal_fcff": terminal_cash,
        "terminal_value_share": terminal_pv / ev if ev else None,
        "years": years,
    }


def implied_growth(base: dict, scenario: dict, price: float) -> dict:
    """仅在非负增长范围单调且存在根时求解，不制造无解的精确值。"""
    low, high = 0.0, 1.0
    samples = []
    try:
        for i in range(21):
            g = i / 20
            samples.append(dcf(base, {**scenario, "growth": g})["per_share"])
    except ValueError as exc:
        return {"status": "unavailable", "reason": str(exc)}
    if any(b <= a for a, b in zip(samples, samples[1:])):
        return {"status": "no_solution", "reason": "估值对增长不单调，资本开支假设需重审"}
    if not samples[0] <= price <= samples[-1]:
        return {"status": "no_solution", "reason": "0%–100% CAGR 搜索区间不存在根"}
    for _ in range(70):
        middle = (low + high) / 2
        if dcf(base, {**scenario, "growth": middle})["per_share"] < price:
            low = middle
        else:
            high = middle
    return {
        "status": "solved",
        "growth": (low + high) / 2,
        "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率",
    }


def evaluate_company(inputs: dict, price: float | None) -> dict:
    output = {"symbol": inputs["symbol"], "inputs": inputs, "scenarios": {}}
    if (
        inputs.get("status") != "reviewed"
        or price is None
        or not math.isfinite(price)
        or price <= 0
    ):
        return {
            **output,
            "status": "unavailable",
            "reason": inputs.get("reason", "财务底稿未核验或报价缺失"),
        }
    if set(inputs.get("scenarios", {})) != {"bear", "base", "bull"}:
        return {**output, "status": "unavailable", "reason": "缺少三情景假设"}
    for name, assumptions in inputs["scenarios"].items():
        try:
            value = dcf(inputs["base"], assumptions)
            output["scenarios"][name] = {
                "assumptions": assumptions,
                **value,
                "upside_pct": (value["per_share"] / price - 1) * 100,
            }
        except ValueError as exc:
            output["scenarios"][name] = {"status": "unavailable", "reason": str(exc)}
    base_case = inputs["scenarios"]["base"]
    output["implied_growth"] = implied_growth(inputs["base"], base_case, price)
    output["sensitivity"] = []
    for shift in [-0.02, 0, 0.02]:
        for growth_cut in [0, -0.05]:
            try:
                value = dcf(
                    inputs["base"],
                    {
                        **base_case,
                        "wacc": base_case["wacc"] + shift,
                        "growth": base_case["growth"] + growth_cut,
                    },
                )
                output["sensitivity"].append(
                    {
                        "wacc": base_case["wacc"] + shift,
                        "growth": base_case["growth"] + growth_cut,
                        "per_share": value["per_share"],
                    }
                )
            except ValueError:
                pass
    output.update(
        status="scenario_analysis",
        price=price,
        note="主观经营情景，非目标价承诺；公司整体估值不等于 AI 单一业务价值",
    )
    return output
