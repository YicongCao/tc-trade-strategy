"""Yahoo Finance 日线下载、代码映射与本地缓存。"""

from __future__ import annotations

import logging
import re
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd
import yfinance as yf

LOGGER = logging.getLogger(__name__)

YAHOO_SYMBOL_OVERRIDES = {
    ".KOSPI": "^KS11",
    ".VVIX": "^VVIX",
    "BRK.B": "BRK-B",
    "SQ": "XYZ",
    "XAUUSD": "GC=F",
}

REQUIRED_COLUMNS = ("Open", "High", "Low", "Close", "Volume")


@dataclass(frozen=True)
class FetchFailure:
    symbol: str
    yahoo_symbol: str
    reason: str


def load_symbols(path: Path) -> list[str]:
    """读取标的清单，保留顺序并去重。"""
    seen: set[str] = set()
    symbols: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        symbol = line.strip().upper()
        if symbol and not symbol.startswith("#") and symbol not in seen:
            seen.add(symbol)
            symbols.append(symbol)
    return symbols


def to_yahoo_symbol(symbol: str) -> str:
    """把平台代码转换成 Yahoo Finance 代码。"""
    return YAHOO_SYMBOL_OVERRIDES.get(symbol, symbol)


def _cache_path(cache_dir: Path, symbol: str) -> Path:
    safe_name = re.sub(r"[^A-Z0-9._-]+", "_", symbol.upper())
    return cache_dir / f"{safe_name}.csv"


def _normalize_frame(frame: pd.DataFrame) -> pd.DataFrame:
    normalized = frame.copy()
    normalized.columns = [str(column).title() for column in normalized.columns]
    if "Adj Close" in normalized.columns and "Close" not in normalized.columns:
        normalized["Close"] = normalized["Adj Close"]
    missing = [column for column in REQUIRED_COLUMNS if column not in normalized.columns]
    if missing:
        raise ValueError(f"缺少字段: {', '.join(missing)}")

    normalized = normalized.loc[:, list(REQUIRED_COLUMNS)]
    normalized.index = pd.to_datetime(normalized.index, errors="coerce")
    if getattr(normalized.index, "tz", None) is not None:
        normalized.index = normalized.index.tz_localize(None)
    normalized = normalized[~normalized.index.isna()]
    normalized = normalized.apply(pd.to_numeric, errors="coerce")
    normalized = normalized.dropna(subset=["Open", "High", "Low", "Close"])
    normalized = normalized[normalized["Close"] > 0]
    normalized = normalized[~normalized.index.duplicated(keep="last")].sort_index()

    # 盘中日线尚未收盘，盘前筛选只使用上一交易日及更早的数据。
    new_york_today = datetime.now(ZoneInfo("America/New_York")).date()
    normalized = normalized[normalized.index.date < new_york_today]
    return normalized


def _extract_symbol_frame(
    downloaded: pd.DataFrame, yahoo_symbol: str, batch_size: int
) -> pd.DataFrame:
    if downloaded.empty:
        return pd.DataFrame()
    if not isinstance(downloaded.columns, pd.MultiIndex):
        if batch_size != 1:
            return pd.DataFrame()
        return downloaded

    level_zero = downloaded.columns.get_level_values(0)
    level_one = downloaded.columns.get_level_values(1)
    if yahoo_symbol in level_zero:
        return downloaded[yahoo_symbol]
    if yahoo_symbol in level_one:
        return downloaded.xs(yahoo_symbol, axis=1, level=1)
    return pd.DataFrame()


def _download_batch(yahoo_symbols: list[str], period: str) -> pd.DataFrame:
    return yf.download(
        tickers=yahoo_symbols,
        period=period,
        interval="1d",
        group_by="ticker",
        auto_adjust=True,
        repair=False,
        actions=False,
        threads=False,
        progress=False,
        timeout=30,
        multi_level_index=True,
    )


def _load_cache(cache_dir: Path, symbol: str) -> pd.DataFrame:
    path = _cache_path(cache_dir, symbol)
    if not path.exists():
        return pd.DataFrame()
    try:
        cached = pd.read_csv(path, index_col="Date", parse_dates=["Date"])
        return _normalize_frame(cached)
    except (OSError, ValueError, pd.errors.ParserError) as exc:
        LOGGER.warning("忽略损坏缓存 %s: %s", path, exc)
        return pd.DataFrame()


def _save_cache(cache_dir: Path, symbol: str, frame: pd.DataFrame) -> None:
    cache_dir.mkdir(parents=True, exist_ok=True)
    output = frame.tail(500).copy()
    output.index.name = "Date"
    output.to_csv(_cache_path(cache_dir, symbol))


def download_daily_bars(
    symbols: list[str],
    cache_dir: Path,
    *,
    min_bars: int = 200,
    period: str = "2y",
    batch_size: int = 25,
    retries: int = 2,
    pause_seconds: float = 1.0,
) -> tuple[dict[str, pd.DataFrame], list[FetchFailure]]:
    """批量下载完整日线；下载失败时回退到有效缓存。"""
    bars: dict[str, pd.DataFrame] = {}
    failures: list[FetchFailure] = []
    symbol_map = {symbol: to_yahoo_symbol(symbol) for symbol in symbols}
    timezone_cache = cache_dir / "_timezone"
    timezone_cache.mkdir(parents=True, exist_ok=True)
    yf.set_tz_cache_location(str(timezone_cache))

    for start in range(0, len(symbols), batch_size):
        batch = symbols[start : start + batch_size]
        yahoo_batch = [symbol_map[symbol] for symbol in batch]
        downloaded = pd.DataFrame()
        last_error = ""

        for attempt in range(retries + 1):
            try:
                downloaded = _download_batch(yahoo_batch, period)
                if not downloaded.empty:
                    break
                last_error = "返回空数据"
            except Exception as exc:  # yfinance 会抛出多种网络层异常
                last_error = str(exc)
            if attempt < retries:
                time.sleep(pause_seconds * (attempt + 1))

        for symbol in batch:
            yahoo_symbol = symbol_map[symbol]
            frame = pd.DataFrame()
            try:
                extracted = _extract_symbol_frame(downloaded, yahoo_symbol, len(batch))
                if not extracted.empty:
                    frame = _normalize_frame(extracted)
            except ValueError as exc:
                last_error = str(exc)

            cached = _load_cache(cache_dir, symbol)
            if frame.empty:
                try:
                    single_download = _download_batch([yahoo_symbol], period)
                    single_frame = _extract_symbol_frame(single_download, yahoo_symbol, 1)
                    if not single_frame.empty:
                        frame = _normalize_frame(single_frame)
                except Exception as exc:  # 单标的回退仍可能遇到网络或代码错误
                    last_error = str(exc)
            if not frame.empty and not cached.empty:
                frame = _normalize_frame(pd.concat([cached, frame]))
            elif frame.empty:
                frame = cached

            if not frame.empty:
                _save_cache(cache_dir, symbol, frame)

            if len(frame) >= min_bars:
                bars[symbol] = frame.tail(min_bars).copy()
            else:
                reason = f"仅有 {len(frame)} 根完整日 K"
                if last_error and frame.empty:
                    reason = f"{reason}；{last_error}"
                failures.append(FetchFailure(symbol, yahoo_symbol, reason))

        if start + batch_size < len(symbols):
            time.sleep(pause_seconds)

    return bars, failures
