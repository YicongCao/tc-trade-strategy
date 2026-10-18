import numpy as np
import pandas as pd

from tc_trade_strategy.screening import score_symbol, screen_universe


def _frame(start: float, end: float, *, latest_volume: float = 2_000) -> pd.DataFrame:
    index = pd.bdate_range("2025-01-01", periods=220)
    close = np.linspace(start, end, len(index))
    volume = np.full(len(index), 1_000.0)
    volume[-10:-1] = 700
    volume[-1] = latest_volume
    return pd.DataFrame(
        {
            "Open": close * 0.995,
            "High": close * 1.005,
            "Low": close * 0.99,
            "Close": close,
            "Volume": volume,
        },
        index=index,
    )


def test_score_symbol_rewards_uptrend_near_pivot_with_volume() -> None:
    result = score_symbol("TEST", _frame(100, 150), spy_return63_pct=3)

    assert result is not None
    assert result.score >= 80
    assert result.state in {"放量突破", "临近枢轴"}
    assert result.volume_ratio50 > 1.4


def test_screen_universe_limits_and_sorts_results() -> None:
    bars = {
        "SPY": _frame(100, 110, latest_volume=1_000),
        "FAST": _frame(80, 160),
        "SLOW": _frame(100, 120, latest_volume=900),
    }

    results = screen_universe(bars, limit=2)

    assert len(results) == 2
    assert results[0].score >= results[1].score
