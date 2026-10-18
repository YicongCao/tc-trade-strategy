"""研究接口：prepare / build / publish / status。分析由 Codex 技能提供。"""

import argparse
import json
from datetime import UTC, date, datetime
from pathlib import Path

from .calendar import MODES, aware, research_window
from .evidence import deduplicate_news, probability_change, quote_quality, safe_public_data
from .fundamentals import check_filings, verify_workpaper
from .intelligence import SECTORS, Collector
from .publishing import all_reports, publish, published_period, run_lock, save_report
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
            "source": f"https://finance.yahoo.com/quote/{symbol}/history/",
            "retrieved_at": snapshot["retrieved_at"],
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
            benchmark = prices["SPY"].get("recent_closes", {})
            p["return_week_pct"] = None
            p["relative_spy_week_pp"] = None
            if start in history and window["end_date"] in history:
                p["return_week_pct"] = (history[window["end_date"]] / history[start] - 1) * 100
                p["week_endpoints"] = [start, window["end_date"]]
                if start in benchmark and window["end_date"] in benchmark:
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
            "retrieved_at": snapshot["retrieved_at"],
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
        }
        comparisons.append(
            {
                "mode": m,
                "baseline": p.relative_to(root).as_posix(),
                "baseline_cutoff": d["window"]["cutoff"],
                "close_change_pct": changes,
                "macro_change": {
                    s: {
                        "change": v["value"] - d["macro"][s]["value"],
                        "unit": v.get("unit"),
                        "observation_date": v["observation_date"],
                    }
                    for s, v in macro.items()
                    if s in d.get("macro", {}) and v.get("unit") == d["macro"][s].get("unit")
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
            retrieved_at=snapshot["polymarket"]["retrieved_at"],
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
    gaps += [f"{e['source']}: {e['error']}" for e in snapshot.get("errors", [])]
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
    safe_public_data(data)
    return data


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("command", choices=("prepare", "build", "publish", "status", "filings"))
    p.add_argument("--mode", choices=MODES, default="realtime")
    p.add_argument("--root", type=Path, default=Path.cwd())
    p.add_argument("--tc", type=Path)
    p.add_argument("--snapshot", type=Path)
    p.add_argument("--analysis", type=Path)
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
            else:
                if not args.tc:
                    p.error("需要 --tc 保存的 tc 市场数据包")
                tc = load(args.tc)
                window = research_window(args.mode, cutoff, tc["calendar"], args.date)
                done = published_period(root, args.mode, window["period"])
                if args.command == "status" or (
                    args.scheduled and done and args.mode != "realtime"
                ):
                    result = {"window": window, "published": done, "skip": done}
                elif args.command == "prepare":
                    output = root / "results/research-runs" / cutoff.strftime("%Y%m%dT%H%M%S.%fZ")
                    Collector(
                        output, date.fromisoformat(window["end_date"]), root / "config/events.json"
                    ).run(include_cnn=True)
                    result = {"snapshot": str(output / "snapshot.json"), "window": window}
                else:
                    if not args.snapshot or not args.analysis:
                        p.error("build 需要 --snapshot 和 --analysis")
                    data = assemble(
                        root,
                        args.mode,
                        cutoff,
                        tc,
                        load(args.snapshot),
                        load(args.analysis),
                        load(args.financials),
                        args.date,
                        args.focus,
                    )
                    directory = save_report(root, data)
                    result = {
                        "report": str(directory),
                        "quality": data["quality"],
                        "gaps": len(data["gaps"]),
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
