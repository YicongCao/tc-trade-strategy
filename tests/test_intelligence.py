from datetime import UTC, date, datetime

import numpy as np
import pandas as pd

from tc_trade_strategy.intelligence import normalize_market, price_metrics, summarize_series


def _market():
    return {
        "id": "example",
        "active": True,
        "closed": False,
        "acceptingOrders": True,
        "endDate": "2027-01-01T00:00:00Z",
        "updatedAt": "2026-10-18T00:00:00Z",
        "outcomes": '["Yes", "No"]',
        "outcomePrices": '["0.6", "0.4"]',
        "bestBid": 0.59,
        "bestAsk": 0.61,
        "volume24hr": 20000,
        "liquidityNum": 100000,
        "oneDayPriceChange": 0.02,
    }


NOW = datetime(2026, 10, 18, 1, tzinfo=UTC)
EVENT = {"slug": "example", "title": "Example event"}


def test_prediction_expired_or_closed_is_not_live():
    market = _market()
    market["endDate"] = "2026-10-17T00:00:00Z"
    assert normalize_market(EVENT, market, NOW) is None
    assert normalize_market({**EVENT, "closed": True}, _market(), NOW) is None


def test_probability_uses_outcome_label_and_change_is_percentage_points():
    result = normalize_market(EVENT, _market(), NOW)
    assert result["yes_probability"] == 0.6
    assert result["change_1d_pp"] == 2.0
    assert result["passes_snapshot_filter"]
    market = {**_market(), "outcomes": '["No", "Yes"]'}
    reversed_result = normalize_market(EVENT, market, NOW)
    assert reversed_result["yes_probability"] == 0.4
    assert reversed_result["change_1d_pp"] is None
    assert not reversed_result["passes_snapshot_filter"]


def test_missing_liquidity_and_stale_metadata_cannot_pass_filter():
    market = {**_market(), "liquidityNum": None, "updatedAt": "2026-10-15T00:00:00Z"}
    result = normalize_market(EVENT, market, NOW)
    assert not result["passes_snapshot_filter"]
    assert len(result["quality_flags"]) == 2


def test_macro_stops_at_as_of_and_preserves_percent_units():
    series = pd.Series(
        [3.1, 3.2, 8.0],
        index=pd.to_datetime(
            [
                "2026-10-14",
                "2026-10-15",
                "2026-10-19",
            ]
        ),
    )
    result = summarize_series(series, date(2026, 10, 16))
    assert result["value"] == 3.2
    assert result["observation_date"] == "2026-10-15"
    assert result["lag_calendar_days"] == 1


def test_relative_return_requires_benchmark_on_same_endpoints():
    dates = pd.bdate_range("2026-08-01", periods=30)
    close = pd.Series(np.arange(100, 130), index=dates)
    frame = pd.DataFrame({"Close": close, "Volume": 1000})
    result = price_metrics(frame, close.iloc[:-1], dates[-1].date())
    assert result["return_20d_pct"] is not None
    assert result["relative_spy_20d_pp"] is None
    aligned = price_metrics(frame, close, dates[-1].date())
    assert aligned["relative_spy_20d_pp"] == 0
    assert aligned["sma200"] is None
