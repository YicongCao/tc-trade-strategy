"""公共数据缺口与 Codex 补查交接；不调用模型，不读取账户数据。"""

from copy import deepcopy
from datetime import date
from urllib.parse import urlsplit

import pandas as pd

from .calendar import aware, closing
from .evidence import digest, safe_public_data
from .intelligence import FRED_SERIES, PROXIES, SECTORS, price_metrics, summarize_series


def comparable_prices(left, right):
    def provider(row):
        return urlsplit(row.get("source", "https://finance.yahoo.com")).hostname

    return provider(left) == provider(right) and left.get("price_basis") == right.get("price_basis")


def inspect(snapshot, window, tc):
    """重新检测实际数据；请求成功不等于数据完整。阈值为工程规则。"""
    gaps = []

    def add(key, reason, requirement, alternatives, core=False):
        gaps.append(
            dict(
                id=key,
                reason=reason,
                requirement=requirement,
                alternatives=alternatives,
                core=core,
                impact="阻止完整报告" if core else "降低相关判断可信度；保留缺口",
            )
        )

    end = window["end_date"]
    for symbol in {**PROXIES, **SECTORS}:
        row = snapshot.get("prices", {}).get(symbol, {})
        if not row or row.get("observation_date") != end:
            add(
                "prices." + symbol,
                "missing_or_stale",
                f"{end} 已完成常规交易日价格；指标需同源复权历史",
                ["tc 日线（核验复权口径）", "交易所/发行人公开历史"],
                symbol in ("SPY", "QQQ"),
            )
        elif any(row.get(k) is None for k in ("sma200", "atr14_sma")):
            add(
                "history." + symbol,
                "insufficient_history",
                "连续完整交易日 OHLC；SMA200 至少200条，ATR14至少15条",
                ["同源完整历史", "缺失指标保留空值"],
            )
    for symbol in [
        *FRED_SERIES,
        "CBOE_VIX",
        "GPRD",
        "GPRD_ACT",
        "GPRD_THREAT",
        "GPRD_MA7",
        "GPRD_MA30",
    ]:
        row = snapshot.get("macro", {}).get(symbol, {})
        lag = (
            (date.fromisoformat(end) - date.fromisoformat(row["observation_date"])).days
            if row
            else None
        )
        tolerance = 14 if symbol == "STLFSI4" else 7
        if lag is None or lag < 0 or lag > tolerance:
            add(
                "macro." + symbol,
                "missing_or_stale",
                f"原始序列与单位，允许发布滞后；检查最近公告（提示阈值{tolerance}天）",
                ["FRED 官方序列", "Cboe / GPR 官方页面"],
            )
    poly = snapshot.get("polymarket", {})
    if not poly.get("markets"):
        add(
            "polymarket",
            "empty",
            "主动搜索五类领域、合约结算条件与当前报价",
            ["Gamma 重试", "Polymarket 事件页"],
        )
    for row in poly.get("coverage", []):
        if row.get("truncated"):
            add(
                "polymarket.query." + row["query"],
                "truncated",
                "按主题或事件ID补查；不能声称全市场覆盖",
                ["事件页", "细分搜索"],
            )
    add(
        "cnn",
        "requires_verification" if snapshot.get("cnn") else "missing",
        "核验 CNN Fear & Greed 原值及更新时间",
        ["CNN 官方页面；不可用则缺失"],
    )
    if tc.get("news", {}).get("has_more"):
        add("news", "truncated", "按事件/时间分批核验新闻线索", ["公司IR", "政府公告", "财经原文"])
    if window["market_phase"] in ("盘前", "盘中", "盘后"):
        from .evidence import quote_quality

        quotes = [q for b in tc.get("quotes", []) for q in b.get("quotes", [])]
        if not any(
            q.get("symbol", "").removesuffix(".US") == "SPY"
            and quote_quality(q, aware(window["cutoff"]), window)[0] == "ok"
            for q in quotes
        ):
            add(
                "tc.SPY",
                "missing_or_stale",
                "20分钟内有效成交时戳；重新获取 tc 包",
                ["tc get_symbol_quotes"],
                True,
            )
    for error in snapshot.get("errors", []):
        # 异常正文可能含URL参数，仅保存在原始快照，不进入公共报告。
        add(
            "request." + digest(error)[:12],
            "request_failed",
            "核验该来源失败影响，见本地原始错误",
            ["重试一次", "公开官方替代来源"],
        )
    return {
        "snapshot_digest": digest(snapshot),
        "window": window,
        "gaps": gaps,
        "policy": "每个缺口最多两次补查；核心未解决停止；无缺口仍执行五类主动研究",
    }


def _provenance(row, cutoff):
    required = {
        "gap_id",
        "kind",
        "target",
        "source",
        "observed_at",
        "published_at",
        "retrieved_at",
        "method",
        "unit",
        "definition",
        "data",
    }
    if set(row) != required:
        raise ValueError("补查字段必须符合契约")
    url = urlsplit(row["source"])
    if url.scheme != "https" or not url.hostname or url.username or url.query or url.fragment:
        raise ValueError("来源须为无凭证/查询参数的公开 HTTPS 页面")
    if row["method"] not in ("web", "browser", "tc_mcp", "public_api"):
        raise ValueError("未知采集方法")
    for key in ("observed_at", "retrieved_at"):
        if aware(row[key]) > cutoff:
            raise ValueError("补查时间晚于截止时点")
    if aware(row["observed_at"]) > aware(row["retrieved_at"]):
        raise ValueError("观测晚于抓取")
    if (cutoff - aware(row["retrieved_at"])).total_seconds() > 21600:
        raise ValueError("补查抓取超过6小时")
    if row["published_at"] and aware(row["published_at"]) > aware(row["retrieved_at"]):
        raise ValueError("发布时间晚于抓取")
    if not row["unit"] or not row["definition"]:
        raise ValueError("缺少单位/定义")


def merge(snapshot, supplements, window, tc):
    """原快照不变；每条补查独立校验，冲突不覆盖有效数据。"""
    safe_public_data(supplements)
    if set(supplements) != {"snapshot_digest", "items"} or supplements["snapshot_digest"] != digest(
        snapshot
    ):
        raise ValueError("补查不属于当前原始快照")
    if not isinstance(supplements["items"], list):
        raise ValueError("items 必须为数组")
    result = deepcopy(snapshot)
    manifest = inspect(snapshot, window, tc)
    gap_ids = {g["id"] for g in manifest["gaps"]}
    audit, seen = [], set()
    cutoff = aware(window["cutoff"])
    for row in supplements["items"]:
        if not isinstance(row, dict):
            raise ValueError("补查条目必须为对象")
        entry = {"gap_id": row.get("gap_id"), "target": row.get("target"), "status": "rejected"}
        try:
            _provenance(row, cutoff)
            if row["gap_id"] not in gap_ids:
                raise ValueError("未知缺口ID")
            key = (row["kind"], row["target"])
            if key in seen:
                raise ValueError("重复补查目标；合并前请明确唯一已核验输入")
            seen.add(key)
            metadata = {
                k: row[k]
                for k in (
                    "source",
                    "observed_at",
                    "published_at",
                    "retrieved_at",
                    "method",
                    "definition",
                )
            }
            if row["kind"] in ("price_history", "macro_series"):
                group = "prices" if row["kind"] == "price_history" else "macro"
                symbol = row["target"]
                if row["gap_id"] not in (group + "." + symbol, "history." + symbol):
                    raise ValueError("补查目标与缺口不匹配")
                if not row["data"]:
                    raise ValueError("空序列")
                frame = pd.DataFrame(row["data"])
                dates = pd.DatetimeIndex(pd.to_datetime(frame.pop("date"), format="%Y-%m-%d"))
                if dates.duplicated().any() or not dates.is_monotonic_increasing:
                    raise ValueError("日期必须唯一且升序")
                frame.index = dates
                if dates[-1].date().isoformat() > window["end_date"]:
                    raise ValueError("包含未完成交易日")
                old = result.get(group, {}).get(symbol, {})
                if group == "prices":
                    if symbol not in {**PROXIES, **SECTORS}:
                        raise ValueError("未知标的")
                    if row["unit"] != (
                        "index"
                        if symbol.startswith("^")
                        else "USD_per_troy_ounce"
                        if symbol == "GC=F"
                        else "USD_per_barrel"
                        if symbol in ("CL=F", "BZ=F")
                        else "USD_per_share"
                    ):
                        raise ValueError("价格单位不匹配")
                    if (
                        set(frame.columns) - {"Close", "High", "Low", "Volume"}
                        or "Close" not in frame
                    ):
                        raise ValueError("历史列不符合契约")
                    last_session = next(
                        d
                        for d in tc["calendar"]["trading_days"]
                        if d["trade_date"] == window["end_date"]
                    )
                    if aware(row["observed_at"]) < closing(last_session):
                        raise ValueError("收盘证据时间早于该交易日收盘")
                    known = {d["trade_date"] for d in tc["calendar"]["trading_days"]}
                    supplied = {d.date().isoformat() for d in dates}
                    if known:
                        expected = {
                            d for d in known if str(dates[0].date()) <= d <= window["end_date"]
                        }
                        within = {d for d in supplied if min(known) <= d <= max(known)}
                        if expected != within:
                            raise ValueError("历史与交易日历不一致或存在缺口")
                    if dates[-1].date().isoformat() != window["end_date"]:
                        raise ValueError("仍缺最新完整交易日")
                    for column in frame:
                        frame[column] = pd.to_numeric(frame[column], errors="raise")
                        if frame[column].isna().any() or (frame[column] < 0).any():
                            raise ValueError("无效历史数值")
                    if (frame.Close <= 0).any():
                        raise ValueError("收盘价必须为正")
                    if (
                        "High" in frame
                        and "Low" in frame
                        and (
                            (frame.High < frame.Low)
                            | (frame.Close > frame.High)
                            | (frame.Close < frame.Low)
                        ).any()
                    ):
                        raise ValueError("OHLC 不一致")
                    if "Volume" not in frame:
                        frame["Volume"] = float("nan")
                    # 完整替换历史，不与另一来源拼接。相对收益暂留空，由下方同口径端点重算。
                    value = price_metrics(
                        frame, pd.Series(dtype=float), date.fromisoformat(window["end_date"])
                    )
                    value.update(
                        unit=row["unit"],
                        name=SECTORS.get(symbol, PROXIES.get(symbol)),
                        kind="sector_etf" if symbol in SECTORS else "risk_or_theme_proxy",
                        price_basis=row["definition"],
                        **metadata,
                    )
                    value["recent_closes"] = {
                        str(d.date()): float(v) for d, v in frame.Close.tail(61).items()
                    }
                    if len(frame) < 63:
                        value["drawdown_from_63d_high_pct"] = None
                else:
                    expected_unit = FRED_SERIES.get(symbol, (None, "index"))[1]
                    if (
                        symbol
                        not in [
                            *FRED_SERIES,
                            "CBOE_VIX",
                            "GPRD",
                            "GPRD_ACT",
                            "GPRD_THREAT",
                            "GPRD_MA7",
                            "GPRD_MA30",
                        ]
                        or row["unit"] != expected_unit
                        or list(frame.columns) != ["value"]
                    ):
                        raise ValueError("宏观序列或单位不匹配")
                    frame["value"] = pd.to_numeric(frame["value"], errors="raise")
                    if frame.value.isna().any():
                        raise ValueError("宏观观测不能为空")
                    value = {
                        **summarize_series(frame.value, date.fromisoformat(window["end_date"])),
                        "unit": row["unit"],
                        **metadata,
                    }
                if (
                    old
                    and old.get("observation_date") == value["observation_date"]
                    and (
                        old.get("value") != value["value"]
                        or old.get("price_basis", row["definition"]) != row["definition"]
                    )
                ):
                    entry["status"] = "conflict"
                    raise ValueError("同日有效数据数值或定义冲突；保留原值并单列核验")
                result.setdefault(group, {})[symbol] = value
                entry["status"] = "accepted"
            elif row["kind"] == "polymarket_event":
                from .intelligence import normalize_market

                if urlsplit(row["source"]).hostname not in (
                    "polymarket.com",
                    "gamma-api.polymarket.com",
                    "www.polymarket.com",
                ):
                    raise ValueError("预测市场补查必须来自 Polymarket")
                if row["unit"] != "probability" or row["target"] != str(row["data"].get("id")):
                    raise ValueError("事件ID或单位不匹配")
                event = row["data"]
                markets = [
                    normalize_market(event, m, aware(row["retrieved_at"]))
                    for m in event.get("markets", [])
                ]
                markets = [m for m in markets if m is not None]
                if not markets:
                    raise ValueError("没有可核验的活跃Yes合约")
                poly = result.setdefault("polymarket", {"markets": [], "coverage": []})
                existing = {str(m["id"]): m for m in poly["markets"]}
                if any(str(m["id"]) in existing for m in markets):
                    entry["status"] = "conflict"
                    raise ValueError("已有合约不可静默覆盖；重新采集统一时点快照")
                for m in markets:
                    m["retrieved_at"] = row["retrieved_at"]
                poly["markets"].extend(markets)
                poly.setdefault("retrieved_at", row["retrieved_at"])
                entry.update(status="accepted", market_ids=[m["id"] for m in markets])
            elif row["kind"] == "evidence":
                if not isinstance(row["data"], str) or not row["data"].strip():
                    raise ValueError("证据须为自行撰写的简短事实摘要")
                # 新闻/披露/预测合约仍须经各自分析输入契约，不用摘要伪装成可计算序列。
                entry.update(status="context_only", fact=row["data"])
            else:
                raise ValueError("不支持的补查类型")
            entry.update(metadata, unit=row["unit"])
        except (ValueError, KeyError, TypeError) as exc:
            entry["reason"] = str(exc)
        audit.append(entry)
    # SPY 更换后旧相对收益也失效；只在同来源/口径且端点完整时重算。
    if any(e["status"] == "accepted" and e["target"] in result.get("prices", {}) for e in audit):
        base = result.get("prices", {}).get("SPY", {})
        for value in result.get("prices", {}).values():
            for period in (1, 5, 20, 60):
                field = f"relative_spy_{period}d_pp"
                value[field] = None
                endpoints = value.get(f"window_{period}d", [])
                closes = base.get("recent_closes", {})
                if (
                    len(endpoints) == 2
                    and all(d in closes for d in endpoints)
                    and comparable_prices(value, base)
                ):
                    value[field] = (
                        value[f"return_{period}d_pct"]
                        - (closes[endpoints[1]] / closes[endpoints[0]] - 1) * 100
                    )
    result["recovery"] = {
        "base_digest": digest(snapshot),
        "attempts": audit,
        "remaining": inspect(result, window, tc)["gaps"],
    }
    return result
