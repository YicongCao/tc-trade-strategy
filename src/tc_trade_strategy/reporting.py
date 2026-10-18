"""同一研究对象输出 Markdown 和离线 HTML；格式化逻辑只有一份。"""

import html
import json
from pathlib import Path

LABELS = {"weekly": "每周交易总结", "daily": "每日交易总结", "realtime": "What's happening"}


def fmt(value):
    if value is None:
        return "缺失"
    if isinstance(value, float):
        return f"{value:,.2f}"
    if isinstance(value, (list, dict)):
        return json.dumps(value, ensure_ascii=False)
    return str(value)


def blocks(data):
    w = data["window"]
    rows = [
        {"title": "研究结论", "text": data["summary"], "tag": "结论"},
        {
            "title": "时点与口径",
            "tag": "时点",
            "table": [
                ["项目", "内容"],
                ["模式", LABELS[w["mode"]]],
                ["常规交易窗口", f"{w['start_date']} → {w['end_date']}（纽约交易日）"],
                ["截止·纽约", w["cutoff_ny"]],
                ["截止·北京", w["cutoff_shanghai"]],
                ["实际生成时间", data["generated_at"]],
                ["市场阶段", w["market_phase"]],
                ["下一交易日", w["next_session"]],
                ["运行重点", data.get("focus", "全市场")],
                ["上一版本", data.get("previous_version") or "首次发布"],
                ["质量", data["quality"]],
            ],
        },
    ]
    if "indicators" in data:
        rows.append(
            {
                "title": "决策指标：趋势、相对强弱、波动与宏观",
                "tag": "指标",
                "table": [["ID", "数值", "单位", "观测日/时间", "质量", "定义", "来源"]]
                + [
                    [
                        r["id"],
                        r["value"],
                        r["unit"],
                        r.get("observation_date", r.get("observed_at")),
                        r["quality"],
                        r["definition"],
                        r["source"],
                    ]
                    for r in data["indicators"]
                ],
            }
        )
        rows.append(
            {
                "title": "指标历史比较（不同日期观测，非连续交易日）",
                "tag": "指标",
                "text": data.get("indicator_comparisons", []),
            }
        )
        for assessment in data.get("indicator_assessments", []):
            labels = {
                "question": "评估问题",
                "evidence_ids": "事实指标引用",
                "interpretation": "推断与解释",
                "counterevidence": "反证与缺口",
                "confirmation": "确认条件",
                "invalidation": "失效条件",
                "horizon": "观察期限",
                "guidance": "条件式指导",
                "confidence": "主观置信等级",
                "change_reason": "判断变化原因",
            }
            rows.append(
                {
                    "title": "判断依据 · " + assessment["question"],
                    "tag": "评估",
                    "table": [["要素", "记录"]] + [[labels[k], v] for k, v in assessment.items()],
                }
            )
    for item in data["themes"]:
        rows.append(
            {
                "title": item["title"] + " · " + item["status"],
                "tag": "主题",
                "table": [["主题要素", "内容"]]
                + [
                    [label, item[key]]
                    for label, key in [
                        ("事实：发生了什么", "event"),
                        ("事实：市场反应", "reaction"),
                        ("推断：解释", "interpretation"),
                        ("受益篮子", "beneficiaries"),
                        ("受损篮子", "adverse"),
                        ("反证", "counterevidence"),
                        ("下一催化剂", "next_catalyst"),
                        ("证据", "sources"),
                    ]
                ],
            }
        )
    rows.append(
        {
            "title": "tc 报价（供应商时戳不等于成交时戳）",
            "tag": "时点",
            "table": [["标的", "价格 USD", "变化%", "观测时间", "供应商时间", "抓取时间", "质量"]]
            + [
                [
                    q["symbol"],
                    q["value"],
                    q["change_pct"],
                    q["observed_at"],
                    q.get("provider_timestamp"),
                    q["retrieved_at"],
                    q["quality"],
                ]
                for q in data["quotes"]
            ],
        }
    )
    if data["window"]["mode"] == "weekly":
        rows.append(
            {
                "title": "完整交易周收益（兼容短周）",
                "tag": "轮动",
                "table": [["标的", "交易周收益%", "相对SPY pp", "同端点"]]
                + [
                    [
                        s,
                        v.get("return_week_pct"),
                        v.get("relative_spy_week_pp"),
                        v.get("week_endpoints"),
                    ]
                    for s, v in data["prices"].items()
                ],
            }
        )
    prices = data["prices"]
    rows.append(
        {
            "title": "核心行情与风险代理",
            "tag": "风险",
            "table": [["标的", "价格/指数", "单位", "观测日", "1日%", "5日%", "20日%", "质量"]]
            + [
                [
                    s,
                    p["value"],
                    p["unit"],
                    p["observation_date"],
                    p.get("return_1d_pct"),
                    p.get("return_5d_pct"),
                    p.get("return_20d_pct"),
                    p["quality"],
                ]
                for s, p in prices.items()
                if p["kind"] != "sector_etf"
            ],
        }
    )
    rows.append({"title": "跨资产风险解释", "tag": "风险", "text": data["risk_analysis"]})
    rows.append(
        {
            "title": "宏观与地缘风险指标",
            "tag": "风险",
            "table": [["指标", "数值", "单位", "观测日", "20次观测变化", "质量", "来源"]]
            + [
                [
                    s,
                    p["value"],
                    p["unit"],
                    p["observation_date"],
                    p.get("change_20_observations"),
                    p["quality"],
                    p["source"],
                ]
                for s, p in data["macro"].items()
            ],
        }
    )
    rows.append({"title": "CNN Fear & Greed", "tag": "风险", "text": data["fear_greed"]})
    rows.append(
        {
            "title": "19 板块与主题 ETF：价格量能证据",
            "tag": "轮动",
            "table": [
                [
                    "标的",
                    "板块",
                    "1日%",
                    "5日%",
                    "20日%",
                    "相对SPY 1日pp",
                    "相对SPY 5日pp",
                    "相对SPY 20日pp",
                    "成交量/前20日",
                    "观测日",
                ]
            ]
            + [
                [
                    s,
                    p["name"],
                    p.get("return_1d_pct"),
                    p.get("return_5d_pct"),
                    p.get("return_20d_pct"),
                    p.get("relative_spy_1d_pp"),
                    p.get("relative_spy_5d_pp"),
                    p.get("relative_spy_20d_pp"),
                    p.get("volume_vs_previous20_ratio"),
                    p["observation_date"],
                ]
                for s, p in prices.items()
                if p["kind"] == "sector_etf"
            ],
        }
    )
    rows.append({"title": "资金证据分层", "tag": "轮动", "text": data["rotation_analysis"]})
    rows.append(
        {
            "title": "最近可核验 ETF 申赎窗口",
            "tag": "轮动",
            "table": [["标的", "金额 USD million", "起始日", "结束日", "质量", "来源"]]
            + [
                [f["symbol"], f["value_million"], f["start"], f["end"], f["quality"], f["source"]]
                for f in data["flows"]
            ],
        }
    )
    for event in data["events"]:
        rows.append(
            {
                "title": event["question"],
                "tag": "事件",
                "table": [
                    ["事件要素", "内容"],
                    ["事件 / 合约 ID", f"{event.get('event_id')} / {event['id']}"],
                    ["Yes 概率 %", event["yes_probability"] * 100],
                    [
                        "供应商 1日 / 1周变化 pp（规则历史未核验）",
                        [event.get("change_1d_pp"), event.get("change_1w_pp")],
                    ],
                    ["与上一快照可比变化", event.get("comparison")],
                    [
                        "24h成交量 / 流动性 USD",
                        [event.get("volume24h_usd"), event.get("liquidity_usd")],
                    ],
                    ["价差 pp", event["spread"] * 100 if event.get("spread") is not None else None],
                    ["到期", event["end_at"]],
                    ["结算规则摘要", event["resolution_summary"]],
                    ["规则指纹", event["rule_hash"]],
                    ["质量", event["quality_flags"] or "通过启发式筛选"],
                    ["元数据更新（不是成交时间）", event.get("updated_at")],
                    ["抓取时间", event["retrieved_at"]],
                    ["来源", event["url"]],
                ],
            }
        )
    rows.append(
        {"title": "AI 压力：合约、经营与估值分开", "tag": "AI", "text": data["ai_analysis"]}
    )
    for company in data["valuations"]:
        base = company["inputs"]
        table = [
            ["估值要素", "内容"],
            ["状态", company["status"]],
            ["财务底稿", base.get("fiscal_period", "缺失")],
            ["披露检查", base.get("disclosure_check")],
            ["观测财务数据", base.get("observations", {})],
            ["来源", base.get("sources", [])],
            ["口径", base.get("accounting_policy", "未核验")],
            ["主观假设说明", base.get("assumption_note", "缺失")],
            ["权益桥额外假设", base.get("equity_bridge_assumptions", "无")],
        ]
        if company["status"] == "unavailable":
            table.append(["缺失原因", company["reason"]])
        else:
            table += [
                ["价格 USD", company["price"]],
                ["基期输入 USD million / million shares", base["base"]],
                ["反推五年收入增长", company["implied_growth"]],
            ]
        rows.append({"title": company["symbol"] + " · 五年 FCFF", "tag": "AI", "table": table})
        if company["status"] != "unavailable":
            scenario_table = [
                ["情景", "每股 USD", "相对现价%", "收入CAGR%", "第5年利润率%", "WACC%", "终值占EV%"]
            ]
            assumptions_table = [["情景", "假设（比例以小数表示）"]]
            for name, value in company["scenarios"].items():
                label = {"bear": "悲观", "base": "基准", "bull": "乐观"}[name]
                if value.get("status") == "unavailable":
                    scenario_table.append([label, value["reason"], None, None, None, None, None])
                    continue
                a = value["assumptions"]
                scenario_table.append(
                    [
                        label,
                        value["per_share"],
                        value["upside_pct"],
                        100 * a["growth"],
                        100 * a["operating_margin"],
                        100 * a["wacc"],
                        100 * value["terminal_value_share"],
                    ]
                )
                assumptions_table.append([label, a])
            rows.append(
                {"title": company["symbol"] + " · 情景结果", "tag": "AI", "table": scenario_table}
            )
            rows.append(
                {
                    "title": company["symbol"] + " · 可复算假设",
                    "tag": "AI",
                    "table": assumptions_table,
                }
            )
            rows.append(
                {
                    "title": company["symbol"] + " · 折现率与经营下修敏感性",
                    "tag": "AI",
                    "table": [["WACC%", "收入CAGR%", "每股 USD"]]
                    + [
                        [v["wacc"] * 100, v["growth"] * 100, v["per_share"]]
                        for v in company["sensitivity"]
                    ],
                }
            )
    for scenario in data["trade_scenarios"]:
        rows.append(
            {
                "title": scenario["title"],
                "tag": "剧本",
                "table": [["条件剧本", "内容"]]
                + [
                    [label, scenario[key]]
                    for label, key in [
                        ("催化剂", "catalyst"),
                        ("关联标的", "symbols"),
                        ("确认条件", "confirmation"),
                        ("失效条件", "invalidation"),
                        ("观察期限", "horizon"),
                        ("反证", "counterevidence"),
                        ("状态", "status"),
                    ]
                ],
            }
        )
    rows.append(
        {"title": "跨期比较与上期剧本复核", "tag": "变化", "text": data["comparison_analysis"]}
    )
    rows.append({"title": "可计算的跨期变化", "tag": "变化", "text": data["comparisons"]})
    rows.append({"title": "后续催化剂与发布后增量", "tag": "事件", "text": data["catalysts"]})
    rows.append(
        {
            "title": "新闻事件去重与时间",
            "tag": "新闻",
            "table": [["事件", "摘要", "发生时间（未知留空）", "各来源发布时间 / 抓取时间"]]
            + [[n["event_key"], n["summary"], n["event_at"], n["sources"]] for n in data["news"]],
        }
    )
    rows.append({"title": "覆盖范围与数据缺口", "tag": "缺口", "text": data["gaps"]})
    rows.append({"title": "来源、时间与核验记录", "tag": "来源", "text": data["sources"]})
    rows.append({"title": "付费信源建议（未订阅）", "tag": "来源", "text": data["paid_sources"]})
    return rows


CSS = """body{margin:0;background:#f5f4ef;color:#182a35;font:16px/1.6 system-ui,sans-serif}
main{max-width:1240px;margin:auto;padding:40px 24px}header{border-bottom:3px solid #0a736d;padding-bottom:24px}
h1{font-size:36px;line-height:1.2}h2{font-size:21px}small,.muted{color:#596b73}section{background:#fff;padding:24px;margin:20px 0;border:1px solid #d9dfdd;border-radius:12px;overflow:auto}table{border-collapse:collapse;width:100%;font-size:14px}td,th{border-bottom:1px solid #e1e7e5;padding:10px;text-align:left;vertical-align:top;min-width:80px;max-width:700px;overflow-wrap:anywhere}th{color:#086c66}p{white-space:pre-wrap;overflow-wrap:anywhere}pre{white-space:pre-wrap;overflow-wrap:anywhere;font-size:13px}a{color:#08776f}nav{position:sticky;top:0;padding:12px;background:#f5f4eff5;display:flex;gap:12px;flex-wrap:wrap;z-index:2}input,select{padding:9px;border:1px solid #9caaa6;border-radius:6px;font:inherit}input{min-width:240px}.badge{font-size:12px;color:#097369;letter-spacing:.08em}section[hidden]{display:none}@media(max-width:600px){main{padding:18px 12px}h1{font-size:28px}section{padding:15px}}"""


def cell_html(value):
    if isinstance(value, (list, dict)):
        return "<pre>" + html.escape(json.dumps(value, ensure_ascii=False, indent=2)) + "</pre>"
    text = fmt(value)
    if text.startswith(("https://", "http://")):
        return f'<a href="{html.escape(text, quote=True)}" rel="noreferrer">{html.escape(text)}</a>'
    return html.escape(text)


def render(data):
    title = f"{LABELS[data['window']['mode']]} · {data['window']['period']}"
    md, parts = [f"# {title}", ""], []
    for block in blocks(data):
        md += [f"## {block['title']}", ""]
        body = ""
        if "text" in block:
            value = block["text"]
            if isinstance(value, (list, dict)):
                text = json.dumps(value, ensure_ascii=False, indent=2)
                md += ["```json", text, "```", ""]
                body = "<pre>" + html.escape(text) + "</pre>"
            else:
                md += [value, ""]
                body = "<p>" + html.escape(value) + "</p>"
        if "table" in block:
            body += "<table>"
            for i, row in enumerate(block["table"]):
                md.append(
                    "| "
                    + " | ".join(fmt(x).replace("|", "\\|").replace("\n", " ") for x in row)
                    + " |"
                )
                if i == 0:
                    md.append("| " + " | ".join("---" for _ in row) + " |")
                tag = "th" if i == 0 else "td"
                body += "<tr>" + "".join(f"<{tag}>{cell_html(x)}</{tag}>" for x in row) + "</tr>"
            body += "</table>"
            md.append("")
        parts.append(
            f'<section data-tag="{block["tag"]}"><span class="badge">{block["tag"]}</span>'
            f"<h2>{html.escape(block['title'])}</h2>{body}</section>"
        )
    options = "".join(
        f"<option>{t}</option>" for t in dict.fromkeys(b["tag"] for b in blocks(data))
    )
    encoded = json.dumps(data, ensure_ascii=False, allow_nan=False).replace("<", "\\u003c")
    page = f"""<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><style>{CSS}</style></head><body><main><header><span class="badge">US MARKET RESEARCH · 数日至数周</span><h1>{html.escape(title)}</h1><p>{html.escape(data["summary"])}</p><small>实际生成 {data["generated_at"]} · {data["window"]["market_phase"]} · {data["quality"]}</small><p><a href="../../../index.html">历史与周期筛选</a> · <a href="report.md">Markdown</a> · <a href="evidence.json">证据数据</a></p></header><nav><label>内容 <select id="category"><option value="">全部</option>{options}</select></label><label>主题 / 事件 <input id="search" placeholder="搜索 NVDA、Fed、原油…"></label><span id="count"></span></nav>{"".join(parts)}<script id="research-data" type="application/json">{encoded}</script><script>
const cards=[...document.querySelectorAll('section')];
function filter(){{let n=0;for(const card of cards){{card.hidden=!!((category.value&&card.dataset.tag!==category.value)||(search.value&&!card.textContent.toLowerCase().includes(search.value.toLowerCase())));if(!card.hidden)n++;}}document.getElementById('count').textContent=n+' 个章节';}}
const category=document.getElementById('category'),search=document.getElementById('search');category.addEventListener('change',filter);search.addEventListener('input',filter);filter();
</script></main></body></html>"""
    return "\n".join(md), page


def history_index(root: Path):
    entries = []
    for path in (root / "reports").glob("*/*/*/evidence.json"):
        d = json.loads(path.read_text())
        entries.append(
            (
                d["generated_at"],
                d["window"]["mode"],
                d["window"]["period"],
                path.parent.relative_to(root / "reports").as_posix(),
                d["summary"],
            )
        )
    entries.sort(reverse=True)
    md = [
        "# 研究报告历史",
        "",
        "| 模式 | 周期 | 实际生成时间 | 报告 |",
        "| --- | --- | --- | --- |",
    ]
    cards = []
    for stamp, mode, period, path, summary in entries:
        md.append(
            f"| {mode} | {period} | {stamp} | [Markdown]({path}/report.md) · [HTML]({path}/index.html) |"
        )
        cards.append(
            f'<section data-mode="{mode}" data-period="{period}"><span class="badge">{mode} · {period}</span><h2><a href="{path}/index.html">{html.escape(summary)}</a></h2><small>{stamp}</small></section>'
        )
    index = f"""<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>美股研究历史</title><style>{CSS}</style><main><header><span class="badge">US MARKET RESEARCH</span><h1>美股主观交易辅助器</h1><p>完整研究历史 · 按模式与周期筛选</p></header><nav><select id="mode"><option value="">全部模式</option><option>weekly</option><option>daily</option><option>realtime</option></select><input id="period" placeholder="周期，如 2026-W42 或 2026-10"></nav>{"".join(cards)}<script>const m=document.getElementById('mode'),p=document.getElementById('period');function f(){{document.querySelectorAll('section').forEach(x=>x.hidden=!!((m.value&&x.dataset.mode!==m.value)||(p.value&&!x.dataset.period.includes(p.value))))}}m.onchange=f;p.oninput=f;</script></main></html>"""
    (root / "reports/index.md").write_text("\n".join(md) + "\n")
    (root / "reports/index.html").write_text(index)
