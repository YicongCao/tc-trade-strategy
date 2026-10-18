"""证据质量、概率比较、新闻去重及申赎估算。"""

import hashlib
import json
import math
from datetime import UTC, datetime
from urllib.parse import urlsplit

from .calendar import NY, aware


def quote_quality(quote, cutoff, window):
    stamp = quote.get("ts")
    if not isinstance(stamp, (int, float)) or not math.isfinite(stamp):
        return "missing_timestamp", None
    observed = datetime.fromtimestamp(stamp / 1000, UTC)
    if observed > cutoff:
        return "future_timestamp", observed.isoformat()
    if window["market_phase"] in ("盘中", "盘前", "盘后"):
        status = "ok" if (cutoff - observed).total_seconds() <= 1200 else "stale"
    else:
        observed_date = str(observed.astimezone(NY).date())
        status = "last_session" if observed_date == window["end_date"] else "stale"
        if observed_date > window["end_date"]:
            status = "unverified_trade_timestamp"
    return status, observed.isoformat()


def probability_change(current, previous):
    if current.get("id") != previous.get("id"):
        return {"status": "different_contract"}
    if not current.get("rule_hash") or current["rule_hash"] != previous.get("rule_hash"):
        return {"status": "definition_changed_or_unknown", "change_pp": None}
    return {
        "status": "comparable",
        "change_pp": 100 * (current["yes_probability"] - previous["yes_probability"]),
    }


def estimate_flow(previous_shares, current_shares, nav, *, split_factor, start, end, source):
    # 同一 ETF、同一份额口径；NAV 是期末每份，拆分倍数为新份额/旧份额。
    if not start < end or not source or split_factor is None:
        raise ValueError("必须核验窗口、来源及拆分倍数；无拆分时显式填 1")
    if any(
        not math.isfinite(v) or v <= 0 for v in (previous_shares, current_shares, nav, split_factor)
    ):
        raise ValueError("份额、NAV 和拆分倍数必须为正")
    return {
        "estimate_usd": (current_shares - previous_shares * split_factor) * nav,
        "start": start,
        "end": end,
        "source": source,
        "quality": "estimate",
        "note": "期末 NAV 近似，非发行人公布净申赎；不代表最终机构身份",
    }


def deduplicate_news(items):
    """经研究者给出 event_key 后按事件去重，保留每个来源的时间。"""
    groups = {}
    for item in items:
        if not all(item.get(k) for k in ("event_key", "summary", "source", "retrieved_at")):
            raise ValueError("新闻缺少事件键、摘要、来源或抓取时间")
        aware(item["retrieved_at"])
        for field in ("published_at", "event_at"):
            if item.get(field):
                aware(item[field])
        key = item["event_key"]
        group = groups.setdefault(
            key,
            {
                "event_key": key,
                "summary": item["summary"],
                "event_at": item.get("event_at"),
                "sources": [],
            },
        )
        entry = {k: item.get(k) for k in ("source", "published_at", "retrieved_at")}
        if entry not in group["sources"]:
            group["sources"].append(entry)
    return list(groups.values())


def safe_public_data(value):
    forbidden = {
        "api_key",
        "authorization",
        "access_token",
        "refresh_token",
        "user_id",
        "account_id",
        "positions",
        "holdings",
        "trades",
        "raw_response",
        "full_text",
    }
    if isinstance(value, dict):
        for key, item in value.items():
            if key.lower() in forbidden:
                raise ValueError("公开数据含禁止字段: " + key)
            safe_public_data(item)
    elif isinstance(value, list):
        for item in value:
            safe_public_data(item)
    elif isinstance(value, float) and not math.isfinite(value):
        raise ValueError("公开数据包含非有限数值")
    elif isinstance(value, str):
        if any(
            marker in value
            for marker in ("Bearer ", "sk-proj-", "-----BEGIN", "ghp_", "github_pat_")
        ):
            raise ValueError("公开数据疑似包含凭证")
        if value.startswith(("https://", "http://")):
            url = urlsplit(value)
            if url.username or any(k in url.query.lower() for k in ("token=", "key=", "secret=")):
                raise ValueError("来源链接包含疑似凭证")


def digest(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, ensure_ascii=False, allow_nan=False).encode()
    ).hexdigest()
