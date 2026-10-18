"""SEC 披露检查；只缓存公开财务数据，拒绝静默使用过期底稿。"""

import json
from datetime import UTC, datetime
from pathlib import Path

import requests

CIKS = {
    "NVDA": "0001045810",
    "MSFT": "0000789019",
    "AMZN": "0001018724",
    "GOOGL": "0001652044",
    "META": "0001326801",
}


def check_filings(output: Path, user_agent: str):
    output.mkdir(parents=True, exist_ok=True)
    results = {}
    for symbol, cik in CIKS.items():
        url = f"https://data.sec.gov/submissions/CIK{cik}.json"
        row = {"symbol": symbol, "source": url, "checked_at": datetime.now(UTC).isoformat()}
        try:
            response = requests.get(url, headers={"User-Agent": user_agent}, timeout=20)
            response.raise_for_status()
            raw = response.json()
            (output / f"{symbol}-submissions.json").write_text(json.dumps(raw))
            recent = raw["filings"]["recent"]
            filings = [
                {
                    k: recent[k][i]
                    for k in (
                        "form",
                        "filingDate",
                        "reportDate",
                        "accessionNumber",
                        "primaryDocument",
                    )
                }
                for i, form in enumerate(recent["form"])
                if form in ("10-K", "10-Q", "10-K/A", "10-Q/A")
            ]
            row.update(status="ok", filings=filings[:8])
            facts = requests.get(
                f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json",
                headers={"User-Agent": user_agent},
                timeout=20,
            )
            facts.raise_for_status()
            (output / f"{symbol}-companyfacts.json").write_text(facts.text)
        except (requests.RequestException, ValueError, KeyError) as exc:
            row.update(status="unavailable", reason=str(exc)[:300])
        results[symbol] = row
    (output / "checks.json").write_text(json.dumps(results, indent=2))
    return results


def verify_workpaper(workpaper, cutoff):
    """每次研究必须有新披露检查；不可将失败检查伪装成没有新披露。"""
    check = workpaper.get("disclosure_check", {})
    from .calendar import aware

    if not check.get("checked_at") or not check.get("source"):
        return "缺少本次披露检查"
    checked = aware(check["checked_at"])
    if checked > cutoff or (cutoff - checked).total_seconds() > 86400:
        return "披露检查超过 24 小时或晚于截止时点"
    if check.get("status") != "verified":
        return "最新披露状态未核验"
    if workpaper.get("status") == "reviewed":
        if not workpaper.get("sources") or not workpaper.get("fiscal_period"):
            return "缺少财报来源或财年口径"
        if workpaper.get("filing_date", "9999") > str(cutoff.date()):
            return "财报晚于研究截止日"
        if check.get("latest_filing_date") != workpaper.get("filing_date"):
            return "检测到更新披露，需重新核验财务底稿"
        if not workpaper.get("accounting_policy"):
            return "缺少租赁、净债务和股权稀释处理"
    return None
