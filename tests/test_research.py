import json
import subprocess
from datetime import UTC, date, timedelta

import pytest

from tc_trade_strategy.calendar import aware, closing, research_window
from tc_trade_strategy.evidence import (
    deduplicate_news,
    estimate_flow,
    probability_change,
    quote_quality,
    safe_public_data,
)
from tc_trade_strategy.fundamentals import verify_workpaper
from tc_trade_strategy.publishing import git, publish, published_period, run_lock, save_report
from tc_trade_strategy.reporting import render
from tc_trade_strategy.research import assemble, polymarket_watch
from tc_trade_strategy.valuation import (
    dcf,
    implied_growth,
    standalone_quarters,
    trailing_twelve_months,
)


def calendar():
    # Thanksgiving fixture: Thursday closed; Friday half-day.
    days = [
        "2026-11-19",
        "2026-11-20",
        "2026-11-23",
        "2026-11-24",
        "2026-11-25",
        "2026-11-27",
        "2026-11-30",
        "2026-12-01",
    ]
    return {
        "range": {"from": "2026-11-16", "to": "2026-12-02"},
        "trading_days": [
            {"trade_date": d, "session_type": "half" if d.endswith("27") else "full"} for d in days
        ],
    }


def test_half_day_and_incomplete_daily():
    c = calendar()
    w = research_window("daily", aware("2026-11-27T12:59:00-05:00"), c)
    assert w["end_date"] == "2026-11-25" and w["market_phase"] == "盘中"
    w = research_window("daily", aware("2026-11-27T13:00:00-05:00"), c)
    assert w["end_date"] == "2026-11-27" and w["market_phase"] == "盘后"


def test_week_and_closed_holiday():
    w = research_window("weekly", aware("2026-11-29T03:00:00Z"), calendar())
    assert (w["start_date"], w["end_date"], w["next_session"]) == (
        "2026-11-23",
        "2026-11-27",
        "2026-11-30",
    )
    assert (
        research_window("daily", aware("2026-11-26T15:00:00-05:00"), calendar())["market_phase"]
        == "休市"
    )
    assert (
        research_window("weekly", aware("2026-11-27T12:00:00-05:00"), calendar())["end_date"]
        == "2026-11-20"
    )


def test_dst_and_calendar_boundaries():
    summer = closing({"trade_date": "2026-10-30", "session_type": "full"})
    winter = closing({"trade_date": "2026-11-02", "session_type": "full"})
    assert summer.astimezone(UTC).hour == 20 and winter.astimezone(UTC).hour == 21
    with pytest.raises(ValueError):
        aware("2026-10-18T12:00:00")
    with pytest.raises(ValueError):
        research_window("daily", aware("2027-01-01T00:00:00Z"), calendar())


def test_quotes_missing_stale_future():
    assert quote_quality({"trade_timestamp_verified": False}, None, {}) == (
        "unverified_trade_timestamp",
        None,
    )
    now = aware("2026-11-27T17:00:00Z")
    w = research_window("realtime", now, calendar())
    assert quote_quality({}, now, w)[0] == "missing_timestamp"
    assert quote_quality({"ts": now.timestamp() * 1000 - 21 * 60 * 1000}, now, w)[0] == "stale"
    assert quote_quality({"ts": now.timestamp() * 1000 + 1}, now, w)[0] == "future_timestamp"
    assert quote_quality({"ts": now.timestamp() * 1000}, now, w)[0] == "ok"
    weekend = aware("2026-11-29T06:00:00Z")
    closed = research_window("realtime", weekend, calendar())
    assert quote_quality({"ts": weekend.timestamp() * 1000}, weekend, closed)[0] == (
        "unverified_trade_timestamp"
    )


def test_rule_change_and_percentage_points():
    a = {"id": "1", "rule_hash": "same", "yes_probability": 0.2}
    b = {**a, "yes_probability": 0.25}
    assert probability_change(b, a)["change_pp"] == pytest.approx(5)
    assert probability_change({**b, "rule_hash": "new"}, a)["change_pp"] is None


def test_split_adjusted_flow_is_not_trading_volume():
    result = estimate_flow(
        100, 200, 50, split_factor=2, start="2026-01-01", end="2026-01-02", source="issuer"
    )
    assert result["estimate_usd"] == 0
    assert (
        estimate_flow(100, 210, 50, split_factor=2, start="a", end="b", source="issuer")[
            "estimate_usd"
        ]
        == 500
    )
    with pytest.raises(ValueError):
        estimate_flow(100, 200, 50, split_factor=None, start="a", end="b", source="issuer")


def test_ytd_quarters_ttm_and_no_future_disclosures():
    facts = [
        {"start": "2025-01-01", "end": end, "filed": filed, "val": value}
        for end, filed, value in [
            ("2025-03-31", "2025-04-30", 10),
            ("2025-06-30", "2025-07-30", 25),
            ("2025-09-30", "2025-10-30", 45),
            ("2025-12-31", "2026-02-01", 70),
        ]
    ]
    facts += [{**facts[-1], "filed": "2027-01-01", "val": 700}]
    q = standalone_quarters(facts, date(2026, 3, 1))
    assert [r["value"] for r in q] == [10, 15, 20, 25]
    assert trailing_twelve_months(q) == 70
    with pytest.raises(ValueError):
        trailing_twelve_months(q[1:])


BASE = {"revenue": 100, "net_debt": 10, "diluted_shares": 10}
SCENARIO = {
    "growth": 0.1,
    "operating_margin": 0.3,
    "tax_rate": 0.2,
    "da_ratio": 0.03,
    "capex_ratio": 0.06,
    "working_capital_ratio": 0.1,
    "wacc": 0.1,
    "terminal_growth": 0.02,
    "dilution": 0,
}


def test_fcff_terminal_reverse_and_no_solution():
    result = dcf(BASE, SCENARIO)
    assert result["years"][0]["fcff"] == pytest.approx(
        110 * 0.3 * 0.8 + 110 * 0.03 - 110 * 0.06 - 1
    )
    revenue = 100 * 1.1**5
    assert result["terminal_fcff"] == pytest.approx(
        revenue * 1.02 * (0.3 * 0.8 + 0.03 - 0.06) - revenue * 0.02 * 0.1
    )
    assert implied_growth(BASE, SCENARIO, result["per_share"])["growth"] == pytest.approx(0.1)
    assert implied_growth(BASE, SCENARIO, 100000)["status"] == "no_solution"
    with pytest.raises(ValueError):
        dcf(BASE, {**SCENARIO, "wacc": 0.02})
    with pytest.raises(ValueError):
        dcf(BASE, {**SCENARIO, "capex_ratio": 0.9})
    with pytest.raises(ValueError):
        dcf(BASE, {**SCENARIO, "growth": float("nan")})


def test_new_filing_invalidates_workpaper():
    paper = {
        "status": "reviewed",
        "filing_date": "2026-07-30",
        "sources": ["SEC"],
        "fiscal_period": "FY",
        "accounting_policy": "reviewed",
        "disclosure_check": {
            "source": "SEC",
            "checked_at": "2026-10-18T02:00:00Z",
            "status": "verified",
            "latest_filing_date": "2026-10-17",
        },
    }
    assert "更新披露" in verify_workpaper(paper, aware("2026-10-18T03:00:00Z"))


def test_news_dedup_preserves_distinct_times():
    item = {
        "event_key": "earnings",
        "summary": "own summary",
        "source": "https://example.com",
        "event_at": None,
        "published_at": None,
        "retrieved_at": "2026-10-18T00:00:00Z",
    }
    news = deduplicate_news([item, item, {**item, "source": "https://issuer.example"}])
    assert len(news) == 1 and len(news[0]["sources"]) == 2 and news[0]["event_at"] is None


@pytest.mark.parametrize(
    "data",
    [
        {"nested": {"user_id": "x"}},
        {"url": "https://a/?token=secret"},
        {"x": "Bearer secret"},
        {"x": float("nan")},
    ],
)
def test_public_data_rejects_secrets(data):
    with pytest.raises(ValueError):
        safe_public_data(data)


def research_data(tmp_path):
    cutoff = aware("2026-11-29T03:00:00Z")
    tc = {"calendar": calendar(), "retrieved_at": cutoff.isoformat(), "quotes": []}

    def price(v):
        return {
            "value": v,
            "observation_date": "2026-11-27",
            "unit": "USD_per_share",
            "kind": "risk_or_theme_proxy",
            "name": "test",
            "recent_closes": {"2026-11-20": 100, "2026-11-27": v},
        }

    snapshot = {
        "retrieved_at": cutoff.isoformat(),
        "prices": {"SPY": price(110), "QQQ": price(120)},
        "macro": {},
        "polymarket": {"markets": [], "coverage": []},
    }
    theme = dict.fromkeys(
        (
            "title",
            "event",
            "reaction",
            "interpretation",
            "beneficiaries",
            "adverse",
            "counterevidence",
            "next_catalyst",
            "sources",
        ),
        "test",
    )
    theme["status"] = "首次基线"
    analysis = {
        k: []
        for k in (
            "trade_scenarios",
            "catalysts",
            "news",
            "sources",
            "gaps",
            "paid_sources",
            "flows",
        )
    }
    analysis.update(
        summary="Research <script>unsafe</script>",
        themes=[theme],
        risk_analysis="risk",
        rotation_analysis="rotation",
        ai_analysis="ai",
        comparison_analysis="none",
        event_reviews={},
        polymarket_watch={
            "search_summary": "fixture: searched, no eligible markets",
            "risk_signals": [],
            "reference_events": [],
            "upcoming_events": [],
        },
        indicator_assessments=[
            {
                "question": "market",
                "evidence_ids": ["prices.SPY.value"],
                "interpretation": "test inference",
                "counterevidence": "test contrary",
                "confirmation": "higher close",
                "invalidation": "lower close",
                "horizon": "next session",
                "guidance": "observe",
                "confidence": "low",
                "change_reason": "first baseline",
            }
        ],
    )
    return tc, snapshot, analysis, cutoff


def test_same_object_render_and_week_endpoints(tmp_path):
    tc, snap, a, cut = research_data(tmp_path)
    data = assemble(tmp_path, "weekly", cut, tc, snap, a, {})
    assert data["prices"]["QQQ"]["return_week_pct"] == pytest.approx(20)
    assert data["prices"]["QQQ"]["relative_spy_week_pp"] == pytest.approx(10)
    md, page = render(data)
    payload = page.split('<script id="research-data" type="application/json">')[1].split(
        "</script>"
    )[0]
    assert json.loads(payload) == data
    assert "<script>unsafe</script>" not in page and "Research <script>unsafe</script>" in md


def test_core_failure_stops_report(tmp_path):
    tc, snap, a, cut = research_data(tmp_path)
    del snap["prices"]["SPY"]
    with pytest.raises(ValueError, match="核心"):
        assemble(tmp_path, "daily", cut, tc, snap, a, {})
    tc, snap, a, cut = research_data(tmp_path)
    tc["retrieved_at"] = (cut + timedelta(seconds=1)).isoformat()
    with pytest.raises(ValueError, match="伪造"):
        assemble(tmp_path, "daily", cut, tc, snap, a, {})


def test_polymarket_watch_required_and_references_verified_contracts(tmp_path):
    tc, snap, analysis, cutoff = research_data(tmp_path)
    watch = analysis.pop("polymarket_watch")
    for mode in ("weekly", "daily"):
        with pytest.raises(ValueError, match="Polymarket"):
            assemble(tmp_path, mode, cutoff, tc, snap, analysis, {})
    entry = {
        "market_id": "1",
        "reason": "risk repriced",
        "transmission": "rates to equities",
        "confirmation": "independent evidence",
        "invalidation": "reversal",
        "event_at": None,
        "event_time_source": None,
    }
    watch["risk_signals"] = [entry]
    analysis["polymarket_watch"] = watch
    with pytest.raises(ValueError, match="未经核验"):
        polymarket_watch(analysis, [], "daily", cutoff)
    assert polymarket_watch(analysis, [{"id": "1"}], "daily", cutoff) == watch
    watch["upcoming_events"] = [
        {
            **entry,
            "event_at": "2026-11-28T00:00:00Z",
            "event_time_source": "https://official.example",
        }
    ]
    with pytest.raises(ValueError, match="已过去"):
        polymarket_watch(analysis, [{"id": "1"}], "daily", cutoff)


def init_repo(tmp_path):
    root = tmp_path / "work"
    root.mkdir()
    remote = tmp_path / "remote.git"
    subprocess.run(["git", "init", "--bare", str(remote)], check=True, capture_output=True)
    git(root, "init", "-b", "main")
    git(root, "config", "user.email", "test@example.com")
    git(root, "config", "user.name", "Test")
    git(root, "remote", "add", "origin", str(remote))
    (root / ".gitignore").write_text("results/\n")
    git(root, "add", ".gitignore")
    git(root, "commit", "-m", "initial")
    git(root, "push", "-u", "origin", "main")
    return root, remote


def test_publication_scoped_immutable_duplicate_lock_and_failed_push(tmp_path):
    root, remote = init_repo(tmp_path)
    tc, snap, a, cut = research_data(root)
    data = assemble(root, "daily", cut, tc, snap, a, {})
    with run_lock(root):
        with pytest.raises(RuntimeError, match="其他报告"):
            with run_lock(root):
                pass
        report = save_report(root, data)
    original = (report / "evidence.json").read_bytes()
    (root / "unrelated.txt").write_text("user work")
    git(root, "add", "unrelated.txt")
    with pytest.raises(RuntimeError, match="暂存区"):
        publish(root, report)
    assert git(root, "diff", "--cached", "--name-only") == "unrelated.txt"
    git(root, "reset", "--", "unrelated.txt")
    hook = remote / "hooks/pre-receive"
    hook.write_text("#!/bin/sh\nexit 1\n")
    hook.chmod(0o755)
    with pytest.raises(RuntimeError):
        publish(root, report)
    assert (report / "evidence.json").read_bytes() == original
    assert not published_period(root, "daily", data["window"]["period"])
    assert not git(root, "ls-files", "unrelated.txt")
    hook.unlink()
    publish(root, report)
    assert published_period(root, "daily", data["window"]["period"])
    with run_lock(root):
        report2 = save_report(root, {**data, "summary": "Second version"})
    assert report2 != report and (report / "evidence.json").read_bytes() == original


def test_alternative_quote_preserves_provenance(tmp_path):
    tc, snap, analysis, cutoff = research_data(tmp_path)
    tc["quotes"] = [
        {
            "quotes": [
                {
                    "symbol": "SPY.US",
                    "last": 110,
                    "ts": cutoff.timestamp() * 1000,
                    "source": "https://finance.yahoo.com/quote/SPY/",
                }
            ]
        }
    ]
    data = assemble(tmp_path, "daily", cutoff, tc, snap, analysis, {})
    assert data["quotes"][0]["source"] == "https://finance.yahoo.com/quote/SPY/"
