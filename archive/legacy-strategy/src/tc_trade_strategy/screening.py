"""盘前机械预筛：缩小 AI 形态识别的候选池。"""

from __future__ import annotations

from dataclasses import asdict, dataclass

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class ScreenResult:
    symbol: str
    score: float
    close: float
    sma50: float
    sma200: float
    pivot60: float
    pivot_distance_pct: float
    volume_ratio50: float
    volume_contraction: float
    return63_pct: float
    relative_strength63_pct: float
    state: str

    def to_dict(self) -> dict[str, float | str]:
        return asdict(self)


def _safe_ratio(numerator: float, denominator: float) -> float:
    if not np.isfinite(denominator) or denominator == 0:
        return float("nan")
    return numerator / denominator


def _proximity_score(distance_pct: float) -> float:
    if 0 <= distance_pct <= 5:
        return 25 - 2 * distance_pct
    if -3 <= distance_pct < 0:
        return 20 + 4 * distance_pct
    return 0


def _relative_strength_score(relative_return_pct: float) -> float:
    if relative_return_pct >= 10:
        return 15
    if relative_return_pct >= 5:
        return 12
    if relative_return_pct >= 0:
        return 9
    if relative_return_pct >= -5:
        return 5
    return 0


def _state(distance_pct: float, volume_ratio: float) -> str:
    if 0 <= distance_pct <= 5 and volume_ratio >= 1.4:
        return "放量突破"
    if -3 <= distance_pct < 0:
        return "临近枢轴"
    if 0 <= distance_pct <= 5:
        return "突破待量能确认"
    if distance_pct > 5:
        return "突破后延伸"
    return "远离枢轴"


def score_symbol(
    symbol: str,
    frame: pd.DataFrame,
    *,
    spy_return63_pct: float,
) -> ScreenResult | None:
    """按趋势、枢轴距离、量价和相对强度计算 100 分预筛分。"""
    if len(frame) < 200:
        return None

    close = frame["Close"].astype(float)
    high = frame["High"].astype(float)
    volume = frame["Volume"].astype(float)
    sma50_series = close.rolling(50).mean()
    sma200_series = close.rolling(200).mean()

    latest_close = float(close.iloc[-1])
    sma50 = float(sma50_series.iloc[-1])
    sma200 = float(sma200_series.iloc[-1])
    sma50_previous = float(sma50_series.iloc[-21])
    pivot60 = float(high.iloc[-61:-1].max())
    pivot_distance_pct = (_safe_ratio(latest_close, pivot60) - 1) * 100

    average_volume50 = float(volume.iloc[-50:].mean())
    volume_ratio50 = _safe_ratio(float(volume.iloc[-1]), average_volume50)
    contraction_base = float(volume.iloc[-50:-10].mean())
    contraction_recent = float(volume.iloc[-10:-1].mean())
    volume_contraction = _safe_ratio(contraction_recent, contraction_base)

    return63_pct = (_safe_ratio(latest_close, float(close.iloc[-64])) - 1) * 100
    relative_strength63_pct = return63_pct - spy_return63_pct

    required_values = (
        latest_close,
        sma50,
        sma200,
        sma50_previous,
        pivot60,
        pivot_distance_pct,
        volume_ratio50,
        volume_contraction,
        return63_pct,
        relative_strength63_pct,
    )
    if not all(np.isfinite(value) for value in required_values):
        return None

    trend_score = 0.0
    trend_score += 15 if latest_close > sma50 else 0
    trend_score += 15 if sma50 > sma200 else 0
    trend_score += 10 if sma50 > sma50_previous else 0

    volume_score = 0.0
    if volume_ratio50 >= 1.4:
        volume_score += 12
    elif volume_ratio50 >= 1.0:
        volume_score += 8
    elif volume_ratio50 >= 0.8:
        volume_score += 4

    if volume_contraction <= 0.8:
        volume_score += 8
    elif volume_contraction <= 1.0:
        volume_score += 4

    score = (
        trend_score
        + _proximity_score(pivot_distance_pct)
        + volume_score
        + _relative_strength_score(relative_strength63_pct)
    )

    return ScreenResult(
        symbol=symbol,
        score=round(score, 2),
        close=round(latest_close, 4),
        sma50=round(sma50, 4),
        sma200=round(sma200, 4),
        pivot60=round(pivot60, 4),
        pivot_distance_pct=round(pivot_distance_pct, 2),
        volume_ratio50=round(volume_ratio50, 2),
        volume_contraction=round(volume_contraction, 2),
        return63_pct=round(return63_pct, 2),
        relative_strength63_pct=round(relative_strength63_pct, 2),
        state=_state(pivot_distance_pct, volume_ratio50),
    )


def screen_universe(
    bars: dict[str, pd.DataFrame],
    *,
    limit: int = 20,
) -> list[ScreenResult]:
    """对完整数据标的排序并返回前 N 名。"""
    spy = bars.get("SPY")
    if spy is None or len(spy) < 200:
        raise ValueError("SPY 日 K 不足 200 根，无法计算相对强度")
    spy_close = spy["Close"].astype(float)
    spy_return63_pct = (
        _safe_ratio(float(spy_close.iloc[-1]), float(spy_close.iloc[-64])) - 1
    ) * 100

    results = [
        result
        for symbol, frame in bars.items()
        if (result := score_symbol(symbol, frame, spy_return63_pct=spy_return63_pct))
        is not None
    ]
    return sorted(
        results,
        key=lambda item: (
            item.score,
            item.relative_strength63_pct,
            -abs(item.pivot_distance_pct),
        ),
        reverse=True,
    )[:limit]
