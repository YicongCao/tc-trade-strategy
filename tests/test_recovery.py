from copy import deepcopy

import pytest
from test_research import research_data

from tc_trade_strategy.evidence import digest
from tc_trade_strategy.recovery import inspect, merge
from tc_trade_strategy.research import assemble


def fixture(tmp_path):
    tc, snapshot, analysis, cutoff = research_data(tmp_path)
    from tc_trade_strategy.calendar import research_window

    window = research_window("daily", cutoff, tc["calendar"])
    return tc, snapshot, analysis, cutoff, window


def item():
    return dict(
        gap_id="prices.SPY",
        kind="price_history",
        target="SPY",
        source="https://issuer.example/history",
        observed_at="2026-11-27T18:00:00Z",
        published_at=None,
        retrieved_at="2026-11-29T02:00:00Z",
        method="web",
        unit="USD_per_share",
        definition="issuer_adjusted_close_v1",
        data=[{"date": "2026-11-27", "Close": 112}],
    )


def apply(snap, row, window, tc):
    return merge(snap, {"snapshot_digest": digest(snap), "items": [row]}, window, tc)


def test_detect_partial_stale_empty_truncated(tmp_path):
    tc, snap, _, _, window = fixture(tmp_path)
    snap["prices"]["QQQ"]["observation_date"] = "2026-11-25"
    snap["errors"] = [{"source": "prices", "error": "timeout with secret local details"}]
    snap["polymarket"]["coverage"] = [{"query": "Fed", "truncated": True}]
    tc["news"] = {"has_more": True}
    manifest = inspect(snap, window, tc)
    gaps = {g["id"]: g for g in manifest["gaps"]}
    assert gaps["prices.QQQ"]["core"]
    assert gaps["polymarket"]["reason"] == "empty"
    assert gaps["news"]["reason"] == "truncated"
    assert "secret local details" not in str(manifest)


def test_missing_core_recovered_but_short_history_stays_missing(tmp_path):
    tc, snap, analysis, cutoff, window = fixture(tmp_path)
    del snap["prices"]["SPY"]
    original = deepcopy(snap)
    recovered = apply(snap, item(), window, tc)
    assert snap == original
    assert recovered["recovery"]["attempts"][0]["status"] == "accepted"
    assert recovered["prices"]["SPY"]["sma200"] is None
    assert recovered["prices"]["SPY"]["atr14_sma"] is None
    report = assemble(tmp_path, "daily", cutoff, tc, recovered, analysis, {})
    assert report["prices"]["SPY"]["source"] == item()["source"]
    assert report["prices"]["SPY"]["retrieved_at"] == item()["retrieved_at"]
    from tc_trade_strategy.reporting import render

    md, html = render(report)
    assert "采集、补查与剩余缺口" in md and "context_only" not in str(report["acquisition"])
    assert "issuer.example" in html


@pytest.mark.parametrize(
    "change",
    [
        {"unit": "CNY"},
        {"retrieved_at": "2026-11-29T05:00:00Z"},
        {"data": []},
        {"data": [{"date": "2026-11-30", "Close": 111}]},
        {
            "data": [
                {"date": "2026-11-25", "Close": 110},
                {"date": "2026-11-26", "Close": 111},
                {"date": "2026-11-27", "Close": 112},
            ]
        },
    ],
)
def test_invalid_fallback_cannot_restore_core(tmp_path, change):
    tc, snap, analysis, cutoff, window = fixture(tmp_path)
    del snap["prices"]["SPY"]
    result = apply(snap, {**item(), **change}, window, tc)
    assert result["recovery"]["attempts"][0]["status"] == "rejected"
    with pytest.raises(ValueError, match="核心"):
        assemble(tmp_path, "daily", cutoff, tc, result, analysis, {})


def test_conflict_no_overwrite_and_stale_digest(tmp_path):
    tc, snap, _, _, window = fixture(tmp_path)
    result = apply(snap, {**item(), "gap_id": "history.SPY"}, window, tc)
    assert result["recovery"]["attempts"][0]["status"] == "conflict"
    assert result["prices"]["SPY"]["value"] == 110
    with pytest.raises(ValueError, match="快照"):
        merge(snap, {"snapshot_digest": "old", "items": []}, window, tc)


def test_context_and_secrets(tmp_path):
    tc, snap, _, _, window = fixture(tmp_path)
    evidence = {
        **item(),
        "gap_id": "cnn",
        "kind": "evidence",
        "target": "CNN",
        "data": "页面不可访问，维持缺口",
    }
    result = apply(snap, evidence, window, tc)
    assert result["recovery"]["attempts"][0]["status"] == "context_only"
    assert any(g["id"] == "cnn" for g in result["recovery"]["remaining"])
    with pytest.raises(ValueError, match="禁止字段"):
        apply(snap, {**evidence, "cookie": "private"}, window, tc)


def test_macro_units_and_changes(tmp_path):
    tc, snap, _, _, window = fixture(tmp_path)
    row = {
        **item(),
        "gap_id": "macro.DGS2",
        "kind": "macro_series",
        "target": "DGS2",
        "unit": "percent",
        "definition": "FRED_DGS2_percent_v1",
        "data": [{"date": "2026-11-27", "value": 4.3}],
    }
    result = apply(snap, row, window, tc)
    assert result["macro"]["DGS2"]["value"] == 4.3
    assert result["macro"]["DGS2"]["change_20_observations"] is None
    assert not any(g["id"] == "macro.DGS2" for g in result["recovery"]["remaining"])


def test_collector_timeout_preserves_partial_snapshot(tmp_path, monkeypatch):
    from datetime import date

    from tc_trade_strategy.intelligence import Collector

    collector = Collector(tmp_path, date(2026, 11, 27))

    def timeout(*args):
        raise TimeoutError("public source timeout")

    monkeypatch.setattr(collector, "polymarket", timeout)
    monkeypatch.setattr(collector, "prices", lambda: {"SPY": {"value": 1}})
    monkeypatch.setattr(collector, "macro", lambda: {})
    result = collector.run()
    assert result["prices"]["SPY"]["value"] == 1
    assert result["errors"][0]["source"] == "polymarket"
    assert result["retrieved_at"] >= result["collection_started_at"]


def test_polymarket_recovery_still_requires_rule_review(tmp_path):
    tc, snap, analysis, cutoff, window = fixture(tmp_path)
    row = {
        **item(),
        "gap_id": "polymarket",
        "kind": "polymarket_event",
        "target": "event1",
        "source": "https://polymarket.com/event/test",
        "unit": "probability",
        "data": {
            "id": "event1",
            "slug": "test",
            "title": "test",
            "markets": [
                {
                    "id": "m1",
                    "active": True,
                    "endDate": "2026-12-31T00:00:00Z",
                    "outcomes": ["Yes", "No"],
                    "outcomePrices": [0.4, 0.6],
                    "question": "test?",
                    "description": "resolution definition",
                }
            ],
        },
    }
    recovered = apply(snap, row, window, tc)
    market = recovered["polymarket"]["markets"][0]
    assert market["yes_probability"] == 0.4
    analysis["event_reviews"] = {"m1": {"rule_hash": "wrong", "resolution_summary": "review"}}
    with pytest.raises(ValueError, match="结算规则"):
        assemble(tmp_path, "daily", cutoff, tc, recovered, analysis, {})
    analysis["event_reviews"]["m1"]["rule_hash"] = market["rule_hash"]
    data = assemble(tmp_path, "daily", cutoff, tc, recovered, analysis, {})
    assert data["events"][0]["retrieved_at"] == row["retrieved_at"]
    assert "description" not in data["events"][0]
