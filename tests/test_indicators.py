import json
from datetime import date

import pandas as pd
import pytest

from tc_trade_strategy.indicators import (
    compare_history,
    history_view,
    panel,
    record_history,
    validate_assessments,
)
from tc_trade_strategy.intelligence import price_metrics
from tc_trade_strategy.publishing import git


def row(day="2026-10-15", value=10):
    return {
        "id": "test",
        "value": value,
        "unit": "percent",
        "source": "official",
        "definition": "v1",
        "session": "completed",
        "universe": "SP500",
        "quality": "ok",
        "observation_date": day,
        "retrieved_at": day + "T22:00:00Z",
    }


def test_atr_ma_full_windows_and_future_exclusion():
    dates = pd.bdate_range("2025-01-01", periods=202)
    frame = pd.DataFrame(
        {"Close": 100.0, "High": 102.0, "Low": 98.0, "Volume": 1000.0}, index=dates
    )
    frame.loc[dates[-1], "Close"] = 10000
    result = price_metrics(frame, frame.Close, dates[-2].date())
    assert result["sma200"] == 100
    assert result["distance_sma20_pct"] == 0
    assert result["atr14_sma"] == 4
    assert result["atr14_pct"] == 4
    small = price_metrics(frame.iloc[:14], frame.Close, date(2026, 1, 1))
    assert small["atr14_sma"] is None  # 缺少第一个 TR 的前收盘
    assert small["volume_vs_previous20_ratio"] is None
    assert small["sma20"] is None


def test_history_comparison_dedup_definition_and_time():
    previous = [
        {"generated_at": "2026-10-15T23:00:00Z", "indicators": [row()]},
        {"generated_at": "2026-10-15T23:30:00Z", "indicators": [row(value=11)]},
        {"generated_at": "2026-10-16T23:00:00Z", "indicators": [row("2026-10-16", 99)]},
    ]
    current = row("2026-10-16", 13)
    result = compare_history([current], previous, "2026-10-16T22:00:00Z")[0]
    assert result["available_prior_observations"] == 1
    assert result["changes"][0]["change"] == 2
    assert len(result["changes"]) == 1
    changed = {**current, "definition": "v2"}
    assert compare_history([changed], previous, "2026-10-16T22:00:00Z")[0]["changes"] == []
    assert (
        compare_history([{**current, "session": "intraday"}], previous, "2026-10-16T22:00:00Z")
        == []
    )


def test_external_rejects_future_incomplete_and_bad_evidence():
    data = {
        "prices": {},
        "macro": {},
        "window": {"cutoff": "2026-10-16T16:00:00Z", "end_date": "2026-10-15"},
    }
    external = row("2026-10-16")
    del external["observation_date"]
    external["observed_at"] = "2026-10-16T15:00:00Z"
    external["retrieved_at"] = "2026-10-16T15:30:00Z"
    with pytest.raises(ValueError, match="已完成"):
        panel(data, [external])
    external["session"] = "intraday"
    assert panel(data, [external])[0]["value"] == 10
    with pytest.raises(ValueError, match="截止"):
        panel(data, [{**external, "retrieved_at": "2026-10-17T00:00:00Z"}])
    with pytest.raises(ValueError):
        validate_assessments([], [])


def test_local_history_ignored_idempotent_and_no_private_copy(tmp_path):
    git(tmp_path, "init")
    (tmp_path / ".gitignore").write_text("/sensitive/\n")
    secret = tmp_path / "sensitive/account-keys.json"
    secret.parent.mkdir()
    secret.write_text("DO_NOT_READ_OR_COPY")
    data = {
        "generated_at": "2026-10-16T23:00:00Z",
        "window": {"mode": "daily", "period": "2026-10-16", "cutoff": "2026-10-16T22:00:00Z"},
        "indicators": [row()],
        "unrelated_private": "DO_NOT_COPY",
    }
    output = record_history(tmp_path, data)
    original = output.read_bytes()
    assert record_history(tmp_path, data) == output
    assert output.read_bytes() == original
    assert "DO_NOT" not in output.read_text()
    assert history_view(tmp_path).exists()
    index = json.loads((output.parent.parent / "index.json").read_text())
    assert index["runs"] == 1
    assert index["comparisons"][0]["status"] == "no_baseline"
    (tmp_path / ".gitignore").write_text("")
    with pytest.raises(ValueError, match="Git"):
        record_history(tmp_path, data)
    (tmp_path / ".gitignore").write_text("/sensitive/\n")
    output.unlink()
    output.symlink_to(secret)
    with pytest.raises(ValueError, match="符号链接"):
        record_history(tmp_path, data)
    assert secret.read_text() == "DO_NOT_READ_OR_COPY"
