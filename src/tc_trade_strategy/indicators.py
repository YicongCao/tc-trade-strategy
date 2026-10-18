"""公开指标面板及本地历史副本；不从 sensitive 读取数据生成公共报告。"""

import html
import json
import math
import subprocess
from datetime import UTC, datetime

from .calendar import NY, aware
from .evidence import digest, safe_public_data

PRICE_FIELDS = (
    "value",
    "return_1d_pct",
    "return_5d_pct",
    "return_20d_pct",
    "return_60d_pct",
    "relative_spy_1d_pp",
    "relative_spy_5d_pp",
    "relative_spy_20d_pp",
    "relative_spy_60d_pp",
    "sma20",
    "sma50",
    "sma200",
    "distance_sma20_pct",
    "distance_sma50_pct",
    "distance_sma200_pct",
    "atr14_sma",
    "atr14_pct",
    "drawdown_from_63d_high_pct",
    "volume_vs_previous20_ratio",
)
ASSESSMENT_FIELDS = (
    "question",
    "evidence_ids",
    "interpretation",
    "counterevidence",
    "confirmation",
    "invalidation",
    "horizon",
    "guidance",
    "confidence",
    "change_reason",
)


def finite(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def panel(data, external=()):
    """只计算确定性事实；宏观解释和交易建议由研究技能给出。"""
    rows = []
    for group, fields in (("prices", PRICE_FIELDS), ("macro", ("value",))):
        for symbol, item in data[group].items():
            for field in fields:
                unit = (
                    "pp"
                    if field.endswith("_pp")
                    else "percent"
                    if field.endswith("_pct")
                    else "ratio"
                    if field.endswith("_ratio")
                    else item["unit"]
                )
                rows.append(
                    {
                        "id": f"{group}.{symbol}.{field}",
                        "value": item.get(field),
                        "unit": unit,
                        "observation_date": item["observation_date"],
                        "retrieved_at": item["retrieved_at"],
                        "source": item["source"],
                        "quality": item["quality"] if finite(item.get(field)) else "unavailable",
                        "definition": (
                            item.get("price_basis", "legacy_price_basis_unverified") + ":" + field
                            if group == "prices"
                            else "source_series_v1:" + symbol
                        ),
                        "session": "completed",
                        "universe": symbol,
                    }
                )
    for quote in data.get("quotes", []):
        phase = {"盘前": "premarket", "盘中": "intraday", "盘后": "afterhours"}.get(
            data["window"]["market_phase"], "last_session_quote"
        )
        rows.append(
            {
                "id": f"quotes.{quote['symbol']}.value",
                "value": quote["value"],
                "unit": "USD_per_share",
                "source": quote["source"],
                "observed_at": quote["observed_at"],
                "retrieved_at": quote["retrieved_at"],
                "quality": "ok" if quote["quality"] == "last_session" else quote["quality"],
                "definition": "tc_last_v1",
                "universe": quote["symbol"],
                "session": phase,
            }
        )
    # 外部广度、盈利修正、FedWatch 等只接受显式定义和可核验来源。
    for item in external:
        required = {
            "id",
            "value",
            "unit",
            "source",
            "observed_at",
            "retrieved_at",
            "quality",
            "definition",
            "universe",
            "session",
        }
        if set(item) != required or not finite(item["value"]):
            raise ValueError("外部指标字段不完整、含未知字段或数值无效")
        observed, retrieved = aware(item["observed_at"]), aware(item["retrieved_at"])
        cutoff = aware(data["window"]["cutoff"])
        if observed > retrieved or retrieved > cutoff:
            raise ValueError("外部指标时点超出抓取或研究截止")
        if item["quality"] not in ("ok", "stale", "lagged", "unverified"):
            raise ValueError("未知外部指标质量")
        if item["session"] not in ("completed", "intraday", "premarket", "afterhours"):
            raise ValueError("未知指标交易阶段")
        if (
            item["session"] == "completed"
            and str(observed.astimezone(NY).date()) > data["window"]["end_date"]
        ):
            raise ValueError("已完成指标超出研究窗口，盘中数据须单列")
        if any(not item[k] for k in required - {"value"}):
            raise ValueError("外部指标定义、时点和来源不得为空")
        rows.append(dict(item))
    if len({r["id"] for r in rows}) != len(rows):
        raise ValueError("指标 ID 重复")
    safe_public_data(rows)
    return rows


def validate_assessments(assessments, rows):
    ids = {r["id"] for r in rows if r["quality"] in ("ok", "lagged")}
    if not assessments:
        raise ValueError("缺少指标评估与条件式建议")
    for entry in assessments:
        if set(entry) != set(ASSESSMENT_FIELDS) or any(not v for v in entry.values()):
            raise ValueError("指标评估需包含证据、解释、反证、确认/失效、期限、指导及变化原因")
        if not isinstance(entry["evidence_ids"], list) or not set(entry["evidence_ids"]) <= ids:
            raise ValueError("指标评估引用不存在、陈旧或不可核验的指标")
        if entry["confidence"] not in ("low", "medium", "high"):
            raise ValueError("评估置信度须为 low/medium/high（主观等级）")
    safe_public_data(assessments)


def signature(row):
    return tuple(row.get(k) for k in ("id", "unit", "source", "definition", "universe", "session"))


def observation_day(row):
    if row.get("observation_date"):
        return row["observation_date"]
    stamp = row.get("observed_at")
    return str(aware(stamp).astimezone(NY).date()) if stamp else ""


def compare_history(rows, previous, cutoff):
    """同定义、同单位、同来源、同交易阶段的已完成观测；同日重跑不充当新样本。"""
    result = []
    for row in rows:
        if row["session"] != "completed" or row["quality"] not in ("ok", "lagged"):
            continue
        current_day = observation_day(row)
        by_day = {}
        for snapshot in previous:
            if aware(snapshot["generated_at"]) >= aware(cutoff):
                continue
            for old in snapshot.get("indicators", []):
                day = observation_day(old)
                if (
                    signature(old) == signature(row)
                    and day < current_day
                    and old["quality"] in ("ok", "lagged")
                    and finite(old["value"])
                ):
                    by_day[day] = old
        ordered = sorted(by_day.items())
        changes = []
        for n in (1, 5, 20, 60):
            if len(ordered) >= n:
                day, old = ordered[-n]
                changes.append(
                    {
                        "prior_distinct_observations": n,
                        "from": day,
                        "to": current_day,
                        "change": row["value"] - old["value"],
                        "unit": row["unit"],
                    }
                )
        result.append(
            {
                "id": row["id"],
                "available_prior_observations": len(ordered),
                "changes": changes,
                "status": "comparable" if ordered else "no_baseline",
            }
        )
    return result


def record_history(root, data):
    """调用方持有 run_lock。只写固定子目录；拒绝符号链接及非忽略/已跟踪路径。"""
    target = root / "sensitive/market-indicators"
    for path in (root / "sensitive", target, target / "snapshots"):
        if path.is_symlink():
            raise ValueError("指标目录不允许符号链接")
    probe = "sensitive/market-indicators/snapshots/probe.json"
    ignored = subprocess.run(
        ["git", "-C", str(root), "check-ignore", "-q", "--", probe], capture_output=True
    )
    tracked = subprocess.run(
        ["git", "-C", str(root), "ls-files", "--", "sensitive/market-indicators"],
        capture_output=True,
        text=True,
        check=True,
    )
    if ignored.returncode or tracked.stdout.strip():
        raise ValueError("指标目录必须被 Git 忽略且没有已跟踪文件")
    # 仅投影公开研究对象；不接收任意本地文件，也不复制账户/新闻全文/原始响应。
    rows = data.get("indicators")
    if rows is None:
        rows = panel(data)
    payload = {
        "schema_version": 1,
        "generated_at": data["generated_at"],
        "recorded_at": datetime.now(UTC).isoformat(),
        "mode": data["window"]["mode"],
        "period": data["window"]["period"],
        "cutoff": data["window"]["cutoff"],
        "indicators": rows,
        "indicator_assessments": data.get("indicator_assessments", []),
        "note": "仅公开市场指标；历史报告导入不等于当时可用的原始历史序列；不用于回测",
    }
    safe_public_data(payload)
    key = digest({k: v for k, v in payload.items() if k != "recorded_at"})
    directory = target / "snapshots"
    directory.mkdir(parents=True, exist_ok=True)
    output = directory / (key + ".json")
    if output.is_symlink():
        raise ValueError("历史快照不允许符号链接")
    if not output.exists():
        with output.open("x") as stream:
            stream.write(json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    return output


def history_view(root):
    """只读取明确授权的指标子目录，生成本地趋势比较；不回流公共报告。"""
    directory = root / "sensitive/market-indicators"
    if directory.is_symlink() or (root / "sensitive").is_symlink():
        raise ValueError("指标目录不允许符号链接")
    snapshots = directory / "snapshots"
    if snapshots.is_symlink():
        raise ValueError("快照目录不允许符号链接")
    data = []
    for path in snapshots.glob("*.json"):
        if path.is_symlink():
            raise ValueError("快照不允许符号链接")
        data.append(json.loads(path.read_text()))
    data.sort(key=lambda d: d["generated_at"])
    if not data:
        raise ValueError("没有指标历史")
    latest = data[-1]
    comparison = compare_history(latest["indicators"], data[:-1], latest["generated_at"])
    series = {}
    for snapshot in data:
        for row in snapshot["indicators"]:
            if row["session"] != "completed" or row["quality"] not in ("ok", "lagged"):
                continue
            key = " | ".join(signature(row))
            day = observation_day(row)
            series.setdefault(key, {})[day] = row["value"]
    view = {"latest": latest, "comparisons": comparison, "runs": len(data), "series": series}
    text = json.dumps(view, ensure_ascii=False, indent=2, allow_nan=False)
    for name in ("index.json", "index.html", "index.md"):
        if (directory / name).is_symlink():
            raise ValueError("历史索引不允许符号链接")
    (directory / "index.json").write_text(text + "\n")
    table = ""
    latest_rows = {r["id"]: r for r in latest["indicators"]}
    for item in comparison:
        row = latest_rows[item["id"]]
        values = [
            item["id"],
            str(row["value"]) + " " + row["unit"],
            row.get("observation_date", row.get("observed_at", "")),
            json.dumps(item["changes"], ensure_ascii=False)
            if item["changes"]
            else "首次基线：无更早的可比观测",
        ]
        table += "<tr>" + "".join("<td>" + html.escape(v) + "</td>" for v in values) + "</tr>"
    encoded = json.dumps(series, ensure_ascii=False).replace("<", "\\u003c")
    page = (
        '<!doctype html><html lang="zh-CN"><meta charset="utf-8">'
        "<title>本地指标历史</title><style>body{font:16px/1.6 system-ui;margin:32px}"
        "td{padding:10px;border-bottom:1px solid #ccc}pre{white-space:pre-wrap}"
        "</style><h1>本地指标历史</h1><p>比较 1/5/20/60 次不同日期观测，"
        "不等于交易日跨度。样本不足不推断长期趋势。未完成日线不参与收盘比较。</p>"
        '<label>历史序列 <select id="metric"></select></label>'
        '<p id="range"></p><svg id="chart" viewBox="0 0 900 220" '
        'style="width:100%;max-height:250px" aria-label="指标历史趋势"></svg>'
        '<input id="q" placeholder="筛选指标"><table>' + table + "</table>"
        "<details><summary>完整数据与评估记录</summary><pre>"
        + html.escape(text)
        + '</pre></details><script type="application/json" id="series">'
        + encoded
        + '</script><script>const data=JSON.parse(document.getElementById("series").textContent);'
        'const select=document.getElementById("metric");Object.keys(data).forEach(k=>{'
        'const o=document.createElement("option");o.value=k;'
        'o.textContent=k.split(" | ").slice(0,2).join(" · ");o.title=k;select.append(o)});'
        "function plot(){const points=Object.entries(data[select.value]||{}).sort();"
        'const svg=document.getElementById("chart");svg.replaceChildren();'
        'document.getElementById("range").textContent=points.length?'
        'points[0][0]+" → "+points.at(-1)[0]+"；"+points.length'
        '+"个观测日期（非等距时间轴）；最新值 "+points.at(-1)[1]:'
        '"无可用数据";if(!points.length)return;const v=points.map(p=>p[1]);'
        "const lo=Math.min(...v),hi=Math.max(...v);"
        'const line=document.createElementNS("http://www.w3.org/2000/svg","polyline");'
        'line.setAttribute("points",v.map((y,i)=>[10+i*880/Math.max(1,v.length-1),'
        '210-(y-lo)*200/(hi-lo||1)].join(",")).join(" "));'
        'line.setAttribute("fill","none");line.setAttribute("stroke","#08776f");'
        'line.setAttribute("stroke-width","3");svg.append(line);'
        'if(v.length===1){const dot=document.createElementNS("http://www.w3.org/2000/svg","circle");'
        'dot.setAttribute("cx","10");dot.setAttribute("cy","210");'
        'dot.setAttribute("r","5");dot.setAttribute("fill","#08776f");svg.append(dot)}}'
        "select.onchange=plot;plot();"
        'document.getElementById("q").oninput=function(){'
        'document.querySelectorAll("tr").forEach(r=>r.hidden=!r.textContent.toLowerCase()'
        ".includes(this.value.toLowerCase()))}</script></html>"
    )
    (directory / "index.html").write_text(page)
    (directory / "index.md").write_text(
        "# 本地指标历史\n\n比较单位为不同日期观测次数，非交易日。\n\n```json\n" + text + "\n```\n"
    )
    return directory / "index.html"
