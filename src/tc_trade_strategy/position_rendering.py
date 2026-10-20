"""Offline private reading view; no remote assets or embedded account JSON."""

import html
import math

from .reporting import CSS, cell_html

LABELS = {
    "symbol": "标的", "quantity": "数量", "quantity_display": "页面数量",
    "market_value": "市值", "market_value_display": "页面市值",
    "last_price_display": "页面价格", "weight_pct": "占净值比例（%）",
    "source_label": "来源判断", "quote_time": "报价时点",
    "net_liquidation_positions_page": "净清算值（持仓页）",
    "net_liquidation_summary_page": "净清算值（摘要页）",
    "currency": "币种", "cash_display": "现金（页面值）",
    "settled_cash_display": "已结算现金", "excess_liquidity_display": "超额流动性",
    "maintenance_margin_display": "维持保证金", "buying_power_display": "购买力（不是现金）",
    "interpretation": "风险解读", "event": "事件", "event_at": "事件时间",
    "source": "来源", "checked_at": "核验时间", "impact": "关联逻辑",
    "upside_case": "改善情景", "downside_case": "恶化情景",
    "confirmation": "确认条件", "invalidation": "失效条件", "horizon": "观察期限",
    "guidance": "调整建议", "sources": "证据来源", "catalysts": "催化剂",
}


def readable(value):
    if isinstance(value, dict):
        return {LABELS.get(k, k): readable(v) for k, v in value.items()}
    if isinstance(value, list):
        return [readable(v) for v in value]
    return value


def markdown(value, depth=0):
    if isinstance(value, dict):
        return "\n".join(
            "  " * depth + "- **" + LABELS.get(k, k) + "**："
            + ("\n" + markdown(v, depth + 1) if isinstance(v, (list, dict)) else str(v))
            for k, v in value.items()
        )
    if isinstance(value, list):
        return "\n".join("  " * depth + "- " + markdown(v, depth + 1) for v in value)
    return "未核验" if value is None else str(value)


def finite_number(value):
    return (isinstance(value, (float, int)) and not isinstance(value, bool)
            and math.isfinite(value))


def allocation_chart(positions):
    # Only explicitly supplied weights: never guess a denominator or infer leverage.
    known = [p for p in positions if finite_number(p.get("weight_pct"))]
    missing = len(positions) - len(known)
    if not known:
        return '<p class="muted">缺少已核验的占净值比例，暂不绘制仓位图。</p>'
    scale = max(100, max(abs(p["weight_pct"]) for p in known))
    rows = []
    for p in sorted(known, key=lambda p: abs(p["weight_pct"]), reverse=True):
        weight = p["weight_pct"]
        label = html.escape(str(p["symbol"]))
        width = abs(weight) / scale * 100
        color = "#ad563e" if weight < 0 else "#08776f"
        rows.append(
            f'<div class="weight-row"><strong>{label}</strong>'
            f'<div class="track" role="img" aria-label="{label} 占净值 {weight:.2f}%">'
            f'<span style="width:{width:.4f}%;background:{color}"></span></div>'
            f'<span>{weight:.2f}%</span></div>'
        )
    return (f'<p class="muted">占净值比例 · 每条横轴 0–{scale:g}% · 非风险敞口</p>'
            + "".join(rows)
            + f'<p class="muted">{missing} 项比例缺失。负值单独标色；'
            '不合计成100%，不推算现金或杠杆敞口。报价时点与来源见详情。</p>')


def render_private(payload):
    data = payload
    esc = html.escape
    risk = data["account_risk"]
    risk_text = risk.get("interpretation", "") if isinstance(risk, dict) else risk
    sections = [
        ("结论", data["summary"]), ("账户风险", risk),
        ("实际持仓与来源", data["positions"]),
        ("逐项催化剂、情景与调整建议", data["holding_reviews"]), ("缺口", data["gaps"]),
    ]
    md = ["# 私人持仓附录（仅本地）", "",
          "生成时间：" + data["generated_at"],
          "持仓观察时间：" + str(data["observed_at"]),
          "公共研究截止：" + data["public_cutoff"],
          "关联报告：" + data["public_report"], ""]
    for title, value in sections:
        md += ["## " + title, "", markdown(value), ""]
    cards = []
    for r in data["holding_reviews"]:
        sym = esc(r["symbol"])
        cards.append(
            f'<article class="holding" data-symbol="{sym}"><h3>{sym}</h3>'
            f'<p class="guidance">{esc(r["guidance"])}</p><div class="conditions">'
            f'<div><strong>确认条件</strong><p>{esc(r["confirmation"])}</p></div>'
            f'<div><strong>失效条件</strong><p>{esc(r["invalidation"])}</p></div></div>'
            f'<small>观察期限：{esc(r["horizon"])}</small>'
            '<details><summary>催化剂、情景与证据</summary>'
            + cell_html(readable({k: r[k] for k in (
                "catalysts", "impact", "upside_case", "downside_case", "sources"
            )})) + '</details></article>'
        )
    options = ''.join('<option>' + esc(p['symbol']) + '</option>' for p in data['positions'])
    reviewed = data['status'] == 'reviewed'
    body = '<section><h2>账户风险先看这里</h2>' + cell_html(risk_text) + '</section>'
    if reviewed:
        body += ('<section><h2>仓位分布</h2>' + allocation_chart(data['positions'])
                 + '<details><summary>持仓数值与来源</summary>'
                 + cell_html(readable(data['positions'])) + '</details></section>')
        body += ('<section><h2>逐项调整计划</h2><label>选择标的 <select id="holding-filter">'
                 '<option value="">全部</option>' + options + '</select></label>'
                 + '<div class="holdings">' + ''.join(cards) + '</div></section>')
    body += ('<section><h2>数据限制</h2>' + cell_html(data['gaps'])
             + '</section><section><details><summary>账户数据与核验记录</summary>'
             + cell_html(readable(risk)) + '</details></section>')
    style = """
.holding{border:1px solid #d9dfdd;border-radius:12px;padding:20px;margin-top:20px}
.holding h3{font-size:24px;margin:0}.guidance{font-size:17px}
.conditions{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.conditions>div{background:#f0f5f3;padding:14px;border-radius:8px}
.conditions>div:last-child{background:#fff3ed}.conditions p{margin-bottom:0}
.weight-row{display:grid;grid-template-columns:65px 1fr 75px;gap:12px;align-items:center;
margin:14px 0;font-variant-numeric:tabular-nums}.track{background:#e9eeeb;height:18px;
border-radius:4px;overflow:hidden}.track span{display:block;height:100%;min-width:1px}
.holding[hidden]{display:none}@media(max-width:600px){.conditions{grid-template-columns:1fr}
.holding{padding:14px}.weight-row{gap:6px;grid-template-columns:55px 1fr 65px}}
"""
    page = (
        '<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>私人持仓复查</title><style>' + CSS + style + '</style></head><body><main>'
        '<header><span class="badge">PRIVATE · 仅本地</span><h1>私人持仓复查</h1><p>'
        + esc(data['summary']) + '</p><small>持仓观察：' + esc(str(data['observed_at']))
        + ' · 生成：' + esc(data['generated_at']) + ' · '
        + ('已复核页面快照' if reviewed else '当前持仓不可用')
        + '</small><p class="muted">这是所标时点的复查，不是实时账户页面。</p>'
        '<details><summary>关联报告与文件</summary><p>公共截止：'
        + esc(data['public_cutoff']) + '</p><p>' + esc(data['public_report'])
        + '</p><a href="report.md">阅读文字版</a> · '
        '<a href="review.json">下载证据数据</a></details></header>' + body
        + '<script>const f=document.getElementById("holding-filter");'
        'if(f)f.addEventListener("change",()=>document.querySelectorAll(".holding")'
        '.forEach(c=>c.hidden=!!f.value&&c.dataset.symbol!==f.value));'
        '</script></main></body></html>'
    )
    return '\n'.join(md), page
