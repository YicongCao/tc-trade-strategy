"""研究接口：prepare / build / publish / status。分析由 Codex 技能提供。"""

import argparse
import json
import subprocess
from datetime import UTC, date, datetime
from pathlib import Path

from .calendar import MODES, aware, daily_slot, research_window
from .evidence import deduplicate_news, probability_change, quote_quality, safe_public_data
from .fundamentals import check_filings, verify_workpaper
from .indicators import (
    compare_history,
    history_view,
    panel,
    record_history,
    validate_assessments,
)
from .intelligence import SECTORS, Collector
from .publishing import all_reports, publish, published_period, run_lock, save_report
from .recovery import comparable_prices
from .recovery import inspect as inspect_collection
from .recovery import merge as merge_supplements
from .valuation import UNIVERSE, evaluate_company


def load(path):
    return json.loads(path.read_text())


def validate_analysis(analysis):
    for field in (
        "summary",
        "themes",
        "risk_analysis",
        "rotation_analysis",
        "ai_analysis",
        "trade_scenarios",
        "comparison_analysis",
        "catalysts",
        "news",
        "sources",
        "gaps",
        "paid_sources",
        "flows",
        "event_reviews",
        "indicator_assessments",
    ):
        if field not in analysis:
            raise ValueError("研究输入缺少字段: " + field)
    if not analysis["summary"] or not analysis["themes"]:
        raise ValueError("缺少研究结论与主题")
    for theme in analysis["themes"]:
        if any(
            not theme.get(k)
            for k in (
                "title",
                "status",
                "event",
                "reaction",
                "interpretation",
                "beneficiaries",
                "adverse",
                "counterevidence",
                "next_catalyst",
                "sources",
            )
        ):
            raise ValueError("主题缺少事实、推断、反证或来源")
        if theme["status"] not in ("新增", "强化", "减弱", "失效", "首次基线", "待核验"):
            raise ValueError("未知主题状态")
    for scenario in analysis["trade_scenarios"]:
        if any(
            not scenario.get(k)
            for k in (
                "title",
                "catalyst",
                "symbols",
                "confirmation",
                "invalidation",
                "horizon",
                "counterevidence",
                "status",
            )
        ):
            raise ValueError("交易剧本条件不完整")
    for flow in analysis["flows"]:
        if not all(flow.get(k) for k in ("symbol", "start", "end", "source", "quality")) or flow[
            "quality"
        ] not in ("issuer_verified", "public_report", "estimate"):
            raise ValueError("资金数据缺少窗口、来源或证据等级")
    for source in analysis["sources"]:
        if not all(source.get(k) for k in ("url", "checked_at", "note")):
            raise ValueError("来源缺少核验记录")
        aware(source["checked_at"])
    safe_public_data(analysis)


def polymarket_watch(analysis, events, mode, cutoff):
    watch = analysis.get("polymarket_watch")
    if watch is None:
        if mode in ("weekly", "daily"):
            raise ValueError("周报/日报必须记录 Polymarket 搜索与三类观察，缺失时不能省略")
        return None
    categories = ("risk_signals", "reference_events", "upcoming_events")
    if (
        set(watch) != {"search_summary", *categories}
        or not isinstance(watch["search_summary"], str)
        or not watch["search_summary"].strip()
    ):
        raise ValueError("Polymarket 观察缺少搜索覆盖或栏目")
    by_id = {str(e["id"]): e for e in events}
    required = {
        "market_id",
        "reason",
        "transmission",
        "confirmation",
        "invalidation",
        "event_at",
        "event_time_source",
    }
    for category in categories:
        if not isinstance(watch[category], list):
            raise ValueError("Polymarket 栏目必须为数组，缺失时保留空数组")
        seen = set()
        for row in watch[category]:
            if set(row) != required or any(
                not row[k] for k in required - {"event_at", "event_time_source"}
            ):
                raise ValueError("Polymarket 观察缺少资产传导或确认/失效条件")
            market_id = str(row["market_id"])
            if market_id not in by_id:
                raise ValueError("Polymarket 观察引用未经核验或未采集的合约: " + market_id)
            if market_id in seen:
                raise ValueError("同一 Polymarket 栏目重复合约")
            seen.add(market_id)
            if bool(row["event_at"]) != bool(row["event_time_source"]):
                raise ValueError("事件时间必须附核验来源，未知时间和来源均为 null")
            if row["event_at"]:
                stamp = aware(row["event_at"])
                if category == "upcoming_events" and stamp <= cutoff:
                    raise ValueError("临近事件实际时间已过去，须复核结果而非仍称将发生")
    return watch


def assemble(root, mode, cutoff, tc, snapshot, analysis, financials, target=None, focus="全市场"):
    validate_analysis(analysis)
    window = research_window(mode, cutoff, tc["calendar"], target)
    for stamp in (snapshot["retrieved_at"], tc["retrieved_at"]):
        if aware(stamp) > cutoff:
            raise ValueError("抓取晚于指定截止时点，不能伪造历史报告")
        if (cutoff - aware(stamp)).total_seconds() > 21600:
            raise ValueError("研究输入超过 6 小时，必须重新采集")
    prices = {}
    for symbol, original in snapshot.get("prices", {}).items():
        p = {
            **original,
            "source": original.get("source", f"https://finance.yahoo.com/quote/{symbol}/history/"),
            "retrieved_at": original.get("retrieved_at", snapshot["retrieved_at"]),
        }
        p["quality"] = "ok" if p["observation_date"] == window["end_date"] else "stale"
        if p["observation_date"] > window["end_date"]:
            raise ValueError("价格包含未完成或超出研究窗口的交易日")
        prices[symbol] = p
    if mode == "weekly":
        prior_days = [
            d["trade_date"]
            for d in tc["calendar"]["trading_days"]
            if d["trade_date"] < window["start_date"]
        ]
        start = max(prior_days) if prior_days else None
        for symbol, p in prices.items():
            history = p.get("recent_closes", {})
            benchmark = prices.get("SPY", {}).get("recent_closes", {})
            p["return_week_pct"] = None
            p["relative_spy_week_pp"] = None
            if start in history and window["end_date"] in history:
                p["return_week_pct"] = (history[window["end_date"]] / history[start] - 1) * 100
                p["week_endpoints"] = [start, window["end_date"]]
                if (
                    start in benchmark
                    and window["end_date"] in benchmark
                    and comparable_prices(p, prices.get("SPY", {}))
                ):
                    p["relative_spy_week_pp"] = (
                        p["return_week_pct"]
                        - (benchmark[window["end_date"]] / benchmark[start] - 1) * 100
                    )
    for p in prices.values():
        p.pop("recent_closes", None)
    if any(s not in prices or prices[s]["quality"] != "ok" for s in ("SPY", "QQQ")):
        raise ValueError("核心市场收盘状态无法核验，停止生成交易总结")
    quotes = []
    for batch in tc.get("quotes", []):
        for q in batch.get("quotes", []):
            quality, observed = quote_quality(q, cutoff, window)
            quotes.append(
                {
                    "symbol": q["symbol"].removesuffix(".US"),
                    "value": q["last"],
                    "change_pct": q.get("change_pct"),
                    "observed_at": None if quality == "unverified_trade_timestamp" else observed,
                    "provider_timestamp": observed,
                    "retrieved_at": tc["retrieved_at"],
                    "quality": quality,
                    "source": "tc MCP get_symbol_quotes",
                }
            )
    if window["market_phase"] in ("盘前", "盘中", "盘后"):
        if not any(q["symbol"] == "SPY" and q["quality"] == "ok" for q in quotes):
            raise ValueError("活跃交易时段缺少有效时戳的当前 SPY 报价，停止生成")
    macro = {
        s: {
            **p,
            "retrieved_at": p.get("retrieved_at", snapshot["retrieved_at"]),
            "quality": "lagged" if p["lag_calendar_days"] else "ok",
        }
        for s, p in snapshot.get("macro", {}).items()
    }
    prior = [(p, d) for p, d in all_reports(root) if aware(d["generated_at"]) < cutoff]
    same = [pair for pair in prior if pair[1]["window"]["mode"] == mode]
    previous = same[-1] if same else None
    comparisons = []
    # Realtime 与最近日报和实时报告分别比较；其他模式比较同模式。
    compare_modes = ("daily", "realtime") if mode == "realtime" else (mode,)
    for m in compare_modes:
        candidates = [pair for pair in prior if pair[1]["window"]["mode"] == m]
        if not candidates:
            comparisons.append({"mode": m, "status": "no_baseline"})
            continue
        p, d = candidates[-1]
        changes = {
            s: (v["value"] / d["prices"][s]["value"] - 1) * 100
            for s, v in prices.items()
            if s in d["prices"]
            and v.get("source") == d["prices"][s].get("source")
            and v.get("price_basis") == d["prices"][s].get("price_basis")
        }
        comparisons.append(
            {
                "mode": m,
                "baseline": p.relative_to(root).as_posix(),
                "baseline_cutoff": d["window"]["cutoff"],
                "close_change_pct": changes,
                "quote_change_pct": {
                    q["symbol"]: {
                        "change_pct": (q["value"] / old["value"] - 1) * 100,
                        "from_observed_at": old["observed_at"],
                        "to_observed_at": q["observed_at"],
                    }
                    for q in quotes
                    for old in d.get("quotes", [])
                    if q["symbol"] == old["symbol"]
                    and q["quality"] in ("ok", "last_session")
                    and old["quality"] in ("ok", "last_session")
                    and q["observed_at"]
                    and old["observed_at"]
                    and aware(q["observed_at"]) > aware(old["observed_at"])
                    and old["value"] > 0
                },
                "macro_change": {
                    s: {
                        "change": v["value"] - d["macro"][s]["value"],
                        "unit": v.get("unit"),
                        "observation_date": v["observation_date"],
                    }
                    for s, v in macro.items()
                    if s in d.get("macro", {})
                    and v.get("unit") == d["macro"][s].get("unit")
                    and v.get("source") == d["macro"][s].get("source")
                    and v.get("definition") == d["macro"][s].get("definition")
                },
                "event_probability_change": {
                    str(e["id"]): probability_change(e, old)
                    for e in snapshot.get("polymarket", {}).get("markets", [])
                    for old in d["events"]
                    if e["id"] == old["id"] and str(e["id"]) in analysis["event_reviews"]
                },
                "note": "收盘价快照变化；同一收盘日为零，不代表盘中没有变化",
            }
        )
    old_events = {e["id"]: e for e in previous[1]["events"]} if previous else {}
    reviews = analysis["event_reviews"]
    events = []
    for e in snapshot.get("polymarket", {}).get("markets", []):
        if str(e["id"]) not in reviews:
            continue
        review = reviews[str(e["id"])]
        if review.get("rule_hash") != e.get("rule_hash") or not review.get("resolution_summary"):
            raise ValueError("事件结算规则未核验或已变更: " + str(e["id"]))
        row = {k: v for k, v in e.items() if k != "description"}
        row.update(
            resolution_summary=review["resolution_summary"],
            retrieved_at=e.get("retrieved_at", snapshot["polymarket"]["retrieved_at"]),
        )
        row["comparison"] = (
            probability_change(e, old_events[e["id"]])
            if e["id"] in old_events
            else {"status": "no_baseline"}
        )
        events.append(row)
    values = []
    for symbol in UNIVERSE:
        inputs = financials.get(
            symbol, {"symbol": symbol, "status": "unavailable", "reason": "没有已核验财务底稿"}
        )
        reason = verify_workpaper(inputs, cutoff)
        if reason:
            inputs = {**inputs, "status": "unavailable", "reason": reason}
        quote = next((q for q in quotes if q["symbol"] == symbol and q["quality"] == "ok"), None)
        price = (
            quote["value"] if quote and mode == "realtime" else prices.get(symbol, {}).get("value")
        )
        values.append(evaluate_company(inputs, price))
    gaps = list(analysis["gaps"])
    gaps += ["原始采集存在请求失败，见采集质量记录"] if snapshot.get("errors") else []
    gaps += [f"{v['symbol']} 估值: {v['reason']}" for v in values if v["status"] == "unavailable"]
    missing_sectors = sorted(set(SECTORS) - set(prices))
    if missing_sectors:
        gaps.append("缺少板块行情: " + ", ".join(missing_sectors))
    coverage = snapshot.get("polymarket", {}).get("coverage", [])
    gaps += [
        f"Polymarket 查询 {q['query']} 达到页数上限，存在遗漏"
        for q in coverage
        if q.get("truncated")
    ]
    if tc.get("news", {}).get("has_more"):
        gaps.append("tc 新闻达到查询条数上限；仅社交平台线索，非完整财经新闻")
    for quality in sorted({q["quality"] for q in quotes} - {"ok", "last_session"}):
        symbols = ", ".join(q["symbol"] for q in quotes if q["quality"] == quality)
        gaps.append(f"tc 报价质量 {quality}: {symbols}；不作为新成交证据")
    for key, value in analysis.items():
        if key in ("sources", "news"):
            # 每条证据的抓取/核验不可晚于截止时间。
            for row in value:
                stamp = row.get("checked_at", row.get("retrieved_at"))
                if stamp and aware(stamp) > cutoff:
                    raise ValueError("证据核验晚于截止时间")
    data = {
        k: analysis[k]
        for k in (
            "summary",
            "themes",
            "risk_analysis",
            "rotation_analysis",
            "ai_analysis",
            "trade_scenarios",
            "comparison_analysis",
            "catalysts",
            "sources",
            "paid_sources",
            "flows",
        )
    }
    data.update(
        schema_version=1,
        window=window,
        generated_at=datetime.now(UTC).isoformat(),
        focus=focus,
        prices=prices,
        macro=macro,
        quotes=quotes,
        events=events,
        valuations=values,
        comparisons=comparisons,
        news=deduplicate_news(analysis["news"]),
        gaps=list(dict.fromkeys(gaps)),
        quality="partial" if gaps else "verified",
        previous_version=previous[0].relative_to(root).as_posix() if previous else None,
        fear_greed=analysis.get("fear_greed", "缺失：CNN 无可核验数据，不使用替代指数"),
        coverage={
            "polymarket": coverage,
            "tc_news_count": tc.get("news", {}).get("count"),
            "tc_news_has_more": tc.get("news", {}).get("has_more"),
            "tc_overview_updated_at": tc.get("overview", {}).get("updated_at"),
        },
        methodology=snapshot.get("limitations", []),
    )
    if "recovery" in snapshot:
        data["acquisition"] = snapshot["recovery"]
        data["gaps"] += [g["id"] + ": " + g["reason"] for g in snapshot["recovery"]["remaining"]]
    data["indicators"] = panel(data, analysis.get("indicator_observations", []))
    validate_assessments(analysis["indicator_assessments"], data["indicators"])
    data["indicator_assessments"] = analysis["indicator_assessments"]
    watch = polymarket_watch(analysis, events, mode, cutoff)
    if watch is not None:
        data["polymarket_watch"] = watch
        for key, label in (
            ("risk_signals", "风险预警"),
            ("reference_events", "参考事件"),
            ("upcoming_events", "临近事件"),
        ):
            if not watch[key]:
                data["gaps"].append("Polymarket " + label + "：本次未纳入合格合约，见搜索说明")
    # 公共报告只比较公开报告；绝不读取 sensitive 的本地历史或个人资料。
    data["indicator_comparisons"] = compare_history(
        data["indicators"], [d for _, d in prior], cutoff.isoformat()
    )
    missing_indicators = [
        r["id"] for r in data["indicators"] if r["quality"] not in ("ok", "lagged")
    ]
    if missing_indicators:
        data["gaps"].append("指标缺失/历史不足: " + ", ".join(missing_indicators))
    if not analysis.get("indicator_observations"):
        data["gaps"].append("外部广度、盈利修正及政策定价未补录；不得用 ETF 涨跌代替成分股广度")
    data["quality"] = "partial" if data["gaps"] else "verified"
    safe_public_data(data)
    return data


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "command",
        choices=("prepare", "build", "publish", "status", "filings", "indicators", "gaps"),
    )
    p.add_argument("--mode", choices=MODES, default="realtime")
    p.add_argument("--root", type=Path, default=Path.cwd())
    p.add_argument("--tc", type=Path)
    p.add_argument("--snapshot", type=Path)
    p.add_argument("--analysis", type=Path)
    p.add_argument("--supplements", type=Path, help="Codex公共补查证据；原始snapshot保持不变")
    p.add_argument("--financials", type=Path, default=Path("config/financials.json"))
    p.add_argument("--date", type=date.fromisoformat)
    p.add_argument("--cutoff", type=aware)
    p.add_argument("--focus", default="全市场")
    p.add_argument("--report", type=Path)
    p.add_argument("--scheduled", action="store_true")
    p.add_argument("--sec-user-agent", default="tc-market-research public-data client")
    args = p.parse_args()
    root = args.root.resolve()
    cutoff = args.cutoff or datetime.now(UTC)
    try:
        with run_lock(root):
            if args.command == "publish":
                if not args.report:
                    p.error("publish 需要 --report")
                result = publish(root, args.report)
            elif args.command == "filings":
                result = check_filings(
                    root / "results/financials" / cutoff.strftime("%Y%m%dT%H%M%SZ"),
                    args.sec_user_agent,
                )
            elif args.command == "indicators":
                # 只从固定 reports 路径导入公开报告，不扫描 sensitive 其他目录。
                for _, data in all_reports(root):
                    record_history(root, data)
                result = {"history": str(history_view(root))}
            else:
                if not args.tc:
                    p.error("需要 --tc 保存的 tc 市场数据包")
                tc = load(args.tc)
                window = research_window(args.mode, cutoff, tc["calendar"], args.date)
                slot = daily_slot(cutoff) if args.scheduled and args.mode == "daily" else None
                done = published_period(root, args.mode, window["period"], slot)
                if args.command == "status" or (
                    args.scheduled and done and args.mode != "realtime"
                ):
                    result = {
                        "window": window,
                        "delivery_slot": slot,
                        "published": done,
                        "skip": done,
                    }
                elif args.command == "gaps":
                    if not args.snapshot:
                        p.error("gaps 需要 --snapshot")
                    result = inspect_collection(load(args.snapshot), window, tc)
                elif args.command == "prepare":
                    output = root / "results/research-runs" / cutoff.strftime("%Y%m%dT%H%M%S.%fZ")
                    snapshot = Collector(
                        output, date.fromisoformat(window["end_date"]), root / "config/events.json"
                    ).run(include_cnn=True)
                    # 采集完成后重新计时，不能用采集开始时刻充当截止。
                    finished = datetime.now(UTC)
                    checked_window = research_window(args.mode, finished, tc["calendar"], args.date)
                    manifest = inspect_collection(snapshot, checked_window, tc)
                    (output / "gaps.json").write_text(
                        json.dumps(manifest, ensure_ascii=False, indent=2)
                    )
                    result = {
                        "snapshot": str(output / "snapshot.json"),
                        "window": checked_window,
                        "gaps": str(output / "gaps.json"),
                        "gap_count": len(manifest["gaps"]),
                    }
                else:
                    if not args.snapshot or not args.analysis:
                        p.error("build 需要 --snapshot 和 --analysis")
                    snapshot = load(args.snapshot)
                    if args.supplements:
                        supplement_path = args.supplements.resolve()
                        if not supplement_path.is_relative_to(root / "results"):
                            raise ValueError("补查输入只能位于本仓库 results/；禁止读取敏感目录")
                        snapshot = merge_supplements(snapshot, load(args.supplements), window, tc)
                    else:
                        snapshot["recovery"] = {
                            "attempts": [],
                            "remaining": inspect_collection(snapshot, window, tc)["gaps"],
                        }
                    data = assemble(
                        root,
                        args.mode,
                        cutoff,
                        tc,
                        snapshot,
                        load(args.analysis),
                        load(args.financials),
                        args.date,
                        args.focus,
                    )
                    if slot:
                        data["delivery_slot"] = slot
                    directory = save_report(root, data)
                    try:
                        indicator_path = record_history(root, data)
                        history_view(root)
                        history_status = str(indicator_path)
                    except (ValueError, OSError, subprocess.SubprocessError) as exc:
                        history_status = "本地指标留存失败（报告已保留）: " + str(exc)
                    result = {
                        "report": str(directory),
                        "quality": data["quality"],
                        "gaps": len(data["gaps"]),
                        "indicator_history": history_status,
                    }
            print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ValueError, RuntimeError, KeyError, OSError) as exc:
        failure = {
            "status": "failed",
            "command": args.command,
            "mode": args.mode,
            "actual_at": datetime.now(UTC).isoformat(),
            "reason": str(exc),
        }
        directory = root / "results/research-state"
        directory.mkdir(parents=True, exist_ok=True)
        (
            directory / ("failure-" + datetime.now(UTC).strftime("%Y%m%dT%H%M%S.%fZ") + ".json")
        ).write_text(json.dumps(failure, ensure_ascii=False, indent=2))
        print(json.dumps(failure, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
