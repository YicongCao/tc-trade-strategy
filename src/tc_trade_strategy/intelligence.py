"""只读市场情报采集：预测市场、跨资产风险、板块轮动。"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import logging
import math
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import UTC, date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd
import requests
import yfinance as yf

LOGGER = logging.getLogger(__name__)
GAMMA_URL = "https://gamma-api.polymarket.com/public-search"
GPR_URL = "https://www.matteoiacoviello.com/gpr_files/data_gpr_daily_recent.dta"
CBOE_URL = "https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv"
CNN_URL = "https://production.dataviz.cnn.io/index/fearandgreed/graphdata"

# 查询标签只表示发现入口，不表示合约与板块存在已验证的因果关系。
QUERIES = {
    "美联储": ["Fed decision", "Fed rate"],
    "宏观政策": ["inflation", "recession", "tariff", "government shutdown", "CPI", "unemployment"],
    "科技与半导体": [
        "Nvidia",
        "semiconductor",
        "AI bubble",
        "Micron",
        "chip export",
        "AI spending",
    ],
    "地缘催化剂": ["ceasefire", "Iran"],
    "软件": ["Microsoft", "software"],
    "能源与油气": ["crude oil", "Hormuz"],
    "金融": ["bank", "stablecoin"],
    "工业": ["manufacturing"],
    "航天": ["SpaceX", "Starship"],
}
SECTORS = {
    "XLK": "科技",
    "XLE": "能源",
    "XLF": "金融",
    "XLI": "工业",
    "XLV": "医疗",
    "XLP": "必需消费",
    "XLY": "可选消费",
    "XLC": "通信",
    "XLU": "公用事业",
    "XLRE": "房地产",
    "XLB": "材料",
    "SMH": "半导体",
    "IGV": "软件",
    "XOP": "油气开采",
    "OIH": "油服",
    "ITA": "航空与国防",
    "ARKX": "航天主题",
    "KRE": "区域银行",
    "SKYY": "云计算",
}
PROXIES = {
    "SPY": "标普500 ETF",
    "QQQ": "纳指100 ETF",
    "IWM": "罗素2000 ETF",
    "RSP": "标普等权 ETF",
    "GLD": "黄金 ETF",
    "GC=F": "COMEX 黄金近月连续报价",
    "CL=F": "WTI 原油近月连续报价",
    "BZ=F": "Brent 原油近月连续报价",
    "TLT": "长期美债 ETF",
    "UUP": "美元 ETF",
    "HYG": "高收益债 ETF",
    "LQD": "投资级债 ETF",
    "^VIX": "VIX",
    "^VIX3M": "VIX3M",
    "^VVIX": "VVIX",
    "^MOVE": "美债波动 MOVE",
    "NVDA": "Nvidia",
    "MSFT": "Microsoft",
    "AMZN": "Amazon",
    "GOOGL": "Alphabet",
    "META": "Meta",
    "CRWV": "CoreWeave",
    "MU": "Micron",
    "DRAM": "存储 ETF",
    "VRT": "Vertiv",
}
FRED_SERIES = {
    "DGS2": ("2 年美债名义收益率", "percent"),
    "BAMLH0A0HYM2": ("美国高收益债 OAS", "percentage_points"),
    "BAMLC0A0CM": ("美国投资级债 OAS", "percentage_points"),
    "DGS10": ("10 年美债名义收益率", "percent"),
    "DFII10": ("10 年美债实际收益率", "percent"),
    "T10YIE": ("10 年盈亏平衡通胀率", "percent"),
    "STLFSI4": ("圣路易斯联储金融压力", "index"),
}


def number(value: object) -> float | None:
    try:
        result = float(value)
        return result if math.isfinite(result) else None
    except (TypeError, ValueError):
        return None


def array(value: object) -> list:
    if isinstance(value, str):
        try:
            value = json.loads(value)
        except (TypeError, ValueError):
            return []
    return value if isinstance(value, list) else []


def parse_time(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return result.replace(tzinfo=UTC) if result.tzinfo is None else result
    except ValueError:
        return None


def normalize_market(event: dict, market: dict, now: datetime) -> dict | None:
    """排除已结束合约；按 outcome 标签找 Yes，不假定 Yes 永远排第一。"""
    if event.get("closed") or event.get("archived"):
        return None
    if market.get("active") is not True or market.get("closed") or market.get("archived"):
        return None
    end = parse_time(market.get("endDate") or event.get("endDate"))
    if end is None or end <= now:
        return None
    outcomes, prices = array(market.get("outcomes")), array(market.get("outcomePrices"))
    if len(outcomes) != len(prices) or "Yes" not in outcomes:
        return None
    yes_index = outcomes.index("Yes")
    probability = number(prices[yes_index])
    if probability is None or not 0 <= probability <= 1:
        return None
    bid, ask = number(market.get("bestBid")), number(market.get("bestAsk"))
    # Gamma 的 bestBid/bestAsk 对应第一个 outcome；不把倒序 outcome 的价差用于质量筛选。
    spread = ask - bid if outcomes[0] == "Yes" and bid is not None and ask is not None else None
    liquidity = number(market.get("liquidityNum", market.get("liquidity")))
    volume = number(market.get("volume24hr"))
    updated = parse_time(market.get("updatedAt"))
    fresh = updated is not None and 0 <= (now - updated).total_seconds() <= 86400
    flags = []
    if not fresh:
        flags.append("metadata_update_older_than_24h_or_unknown")
    if liquidity is None or liquidity < 10000:
        flags.append("liquidity_under_10000_or_unknown")
    if volume is None or volume < 1000:
        flags.append("volume24h_under_1000_or_unknown")
    if spread is None or not 0 <= spread <= 0.05:
        flags.append("spread_over_5pp_or_invalid")
    if market.get("acceptingOrders") is not True:
        flags.append("not_accepting_orders_or_unknown")
    return {
        "id": market.get("id"),
        "event_id": str(event.get("id", "")),
        "rule_hash": hashlib.sha256(
            json.dumps(
                [
                    market.get("question"),
                    market.get("description") or event.get("description"),
                    market.get("resolutionSource") or event.get("resolutionSource"),
                    end.isoformat(),
                    outcomes,
                ],
                ensure_ascii=False,
            ).encode()
        ).hexdigest(),
        "event": event.get("title"),
        "question": market.get("question"),
        "yes_probability": probability,
        "best_bid_first_outcome": bid,
        "best_ask_first_outcome": ask,
        "spread": spread,
        "liquidity_usd": liquidity,
        "volume24h_usd": volume,
        "change_1d_pp": scale(market.get("oneDayPriceChange"), 100) if yes_index == 0 else None,
        "change_1w_pp": scale(market.get("oneWeekPriceChange"), 100) if yes_index == 0 else None,
        "outcomes": outcomes,
        "end_at": end.isoformat(),
        "updated_at": market.get("updatedAt"),
        "url": "https://polymarket.com/event/" + event["slug"],
        "resolution_source": market.get("resolutionSource") or event.get("resolutionSource"),
        "description": market.get("description") or event.get("description"),
        "quality_flags": flags,
        "passes_snapshot_filter": not flags,
    }


def scale(value: object, factor: float) -> float | None:
    parsed = number(value)
    return None if parsed is None else round(parsed * factor, 6)


def summarize_series(series: pd.Series, as_of: date) -> dict:
    series = pd.to_numeric(series, errors="coerce").dropna().sort_index()
    series = series[series.index.date <= as_of]
    if series.empty:
        raise ValueError("没有截止日期以内的有效观测")
    return {
        "value": float(series.iloc[-1]),
        "observation_date": str(series.index[-1].date()),
        "lag_calendar_days": (as_of - series.index[-1].date()).days,
        "change_20_observations": float(series.iloc[-1] - series.iloc[-21])
        if len(series) > 20
        else None,
    }


def price_metrics(frame: pd.DataFrame, benchmark: pd.Series, as_of: date) -> dict:
    """价格变化只用同一日期端点；不把收益或成交额冒充资金净流入。"""
    close = frame["Close"].dropna().sort_index()
    close = close[close.index.date <= as_of]
    if close.empty:
        raise ValueError("没有有效收盘价")
    last_day = close.index[-1]
    result = summarize_series(close, as_of)
    result.pop("change_20_observations")
    result["recent_closes"] = {str(t.date()): float(v) for t, v in close.tail(15).items()}
    for period in [1, 5, 20, 60]:
        result[f"return_{period}d_pct"] = None
        result[f"relative_spy_{period}d_pp"] = None
        if len(close) <= period:
            continue
        start = close.index[-period - 1]
        result[f"window_{period}d"] = [str(start.date()), str(last_day.date())]
        change = (close.iloc[-1] / close.loc[start] - 1) * 100
        result[f"return_{period}d_pct"] = float(change)
        if start in benchmark.index and last_day in benchmark.index:
            base = (benchmark.loc[last_day] / benchmark.loc[start] - 1) * 100
            result[f"relative_spy_{period}d_pp"] = float(change - base)
    result["drawdown_from_63d_high_pct"] = float((close.iloc[-1] / close.tail(63).max() - 1) * 100)
    for period in (20, 50, 200):
        ma = float(close.tail(period).mean()) if len(close) >= period else None
        result[f"sma{period}"] = ma
        result[f"distance_sma{period}_pct"] = (
            float((close.iloc[-1] / ma - 1) * 100) if ma and ma > 0 else None
        )
    # 简单移动平均真实波幅（不是 Wilder 平滑）；要求完整 14 个有效 TR。
    result["atr14_sma"] = None
    result["atr14_pct"] = None
    if {"High", "Low"} <= set(frame.columns):
        high, low = frame["High"].reindex(close.index), frame["Low"].reindex(close.index)
        valid = high.notna() & low.notna() & close.shift().notna() & (high >= low)
        tr = (
            pd.concat(
                [high - low, (high - close.shift()).abs(), (low - close.shift()).abs()], axis=1
            )
            .max(axis=1)
            .where(valid)
        )
        if len(tr) >= 14 and tr.tail(14).notna().all():
            result["atr14_sma"] = float(tr.tail(14).mean())
            result["atr14_pct"] = float(result["atr14_sma"] / close.iloc[-1] * 100)
    result["price_basis"] = "yahoo_auto_adjust_ohlc_v1"
    volume = frame["Volume"].reindex(close.index)
    average = volume.iloc[-21:-1].mean()
    result["volume_vs_previous20_ratio"] = (
        number(volume.iloc[-1] / average)
        if len(volume) >= 21 and volume.iloc[-21:].notna().all() and average > 0
        else None
    )
    result["last_close_times_volume_usd_proxy"] = number(close.iloc[-1] * volume.iloc[-1])
    return result


class Collector:
    def __init__(self, output: Path, as_of: date, watchlist: Path | None = None):
        self.output = output
        self.raw = output / "raw"
        self.raw.mkdir(parents=True, exist_ok=True)
        self.as_of = as_of
        self.now = datetime.now(UTC)
        self.errors: list[dict] = []
        self.watchlist = watchlist

    def fetch(self, name: str, url: str, *, params: dict | None = None) -> bytes:
        response = requests.get(url, params=params, timeout=25)
        response.raise_for_status()
        (self.raw / name).write_bytes(response.content)
        (self.raw / (name + ".meta.json")).write_text(
            json.dumps(
                {
                    "url": response.url,
                    "retrieved_at": datetime.now(UTC).isoformat(),
                    "content_type": response.headers.get("Content-Type"),
                },
                indent=2,
            )
        )
        return response.content

    def record_error(self, source: str, error: Exception) -> None:
        self.errors.append({"source": source, "error": str(error)[:500]})
        LOGGER.warning("%s: %s", source, error)

    def polymarket(self, max_pages: int = 2) -> dict:
        def search(topic: str, query: str) -> tuple[list, dict]:
            rows = []
            has_more = False
            for page in range(1, max_pages + 1):
                name = "poly-" + query.replace(" ", "-") + f"-{page}.json"
                payload = json.loads(
                    self.fetch(
                        name,
                        GAMMA_URL,
                        params={
                            "q": query,
                            "events_status": "active",
                            "limit_per_type": 10,
                            "page": page,
                            "keep_closed_markets": 0,
                            "search_tags": "false",
                            "search_profiles": "false",
                        },
                    )
                )
                for event in payload.get("events") or []:
                    for market in event.get("markets") or []:
                        item = normalize_market(event, market, datetime.now(UTC))
                        if item is not None:
                            item["discovery_topics"] = [topic]
                            rows.append(item)
                has_more = bool(payload.get("pagination", {}).get("hasMore"))
                if not has_more:
                    break
            return rows, {
                "query": query,
                "topic": topic,
                "pages": page,
                "truncated": has_more,
                "active_markets_found": len(rows),
            }

        unique, coverage = {}, []
        with ThreadPoolExecutor(max_workers=4) as pool:
            futures = {
                pool.submit(search, topic, query): query
                for topic, queries in QUERIES.items()
                for query in queries
            }
            for future in as_completed(futures):
                try:
                    rows, meta = future.result()
                    coverage.append(meta)
                    for row in rows:
                        if row["id"] in unique:
                            topics = set(unique[row["id"]]["discovery_topics"])
                            topics.update(row["discovery_topics"])
                            unique[row["id"]]["discovery_topics"] = sorted(topics)
                        else:
                            unique[row["id"]] = row
                except Exception as exc:
                    self.record_error("polymarket:" + futures[future], exc)
        if self.watchlist and self.watchlist.exists():
            for watched in json.loads(self.watchlist.read_text())["events"]:
                event_id = str(watched["event_id"])
                try:
                    event = json.loads(
                        self.fetch(
                            f"poly-event-{event_id}.json",
                            f"https://gamma-api.polymarket.com/events/{event_id}",
                        )
                    )
                    for market in event.get("markets", []):
                        row = normalize_market(event, market, datetime.now(UTC))
                        if row:
                            row["discovery_topics"] = unique.get(row["id"], {}).get(
                                "discovery_topics", ["跟踪清单"]
                            )
                            row["watched"] = True
                            unique[row["id"]] = row
                    coverage.append(
                        {
                            "event_id": event_id,
                            "status": "queried",
                            "closed": event.get("closed", False),
                        }
                    )
                except Exception as exc:
                    self.record_error("polymarket:event:" + event_id, exc)
        return {
            "retrieved_at": datetime.now(UTC).isoformat(),
            "note": "当前价格隐含概率，不是客观概率；关键词发现可能误匹配，需审阅结算规则。"
            "质量门槛为工程启发式，未做预测校准。updated_at 为元数据更新时间。",
            "coverage": sorted(coverage, key=lambda x: x.get("query", x.get("event_id", ""))),
            "markets": sorted(unique.values(), key=lambda x: x["volume24h_usd"] or 0, reverse=True),
        }

    def prices(self) -> dict:
        symbols = list(dict.fromkeys([*PROXIES, *SECTORS]))
        yf.set_tz_cache_location(str(self.raw / "yahoo-timezone"))
        downloaded = yf.download(
            symbols,
            start=str(self.as_of - timedelta(days=420)),
            end=str(self.as_of + timedelta(days=1)),
            auto_adjust=True,
            group_by="ticker",
            threads=False,
            progress=False,
            timeout=25,
        )
        frames = {}
        for symbol in symbols:
            if symbol not in downloaded.columns.get_level_values(0):
                self.record_error(symbol, ValueError("行情缺失"))
                continue
            frame = downloaded[symbol].dropna(subset=["Close"]).copy()
            frame.index = pd.to_datetime(frame.index).tz_localize(None)
            if frame.empty:
                self.record_error(symbol, ValueError("行情为空"))
                continue
            frame.to_csv(self.raw / (symbol.replace("^", "_").replace("=", "_") + ".csv"))
            frames[symbol] = frame
        benchmark = frames.get("SPY", pd.DataFrame(columns=["Close"]))["Close"]
        result = {}
        for symbol, frame in frames.items():
            try:
                metrics = price_metrics(frame, benchmark, self.as_of)
            except (ValueError, KeyError, TypeError) as exc:
                self.record_error(symbol, exc)
                continue
            metrics["name"] = SECTORS.get(symbol, PROXIES.get(symbol))
            metrics["kind"] = "sector_etf" if symbol in SECTORS else "risk_or_theme_proxy"
            metrics["unit"] = (
                "index"
                if symbol.startswith("^")
                else "USD_per_troy_ounce"
                if symbol == "GC=F"
                else "USD_per_barrel"
                if symbol in {"CL=F", "BZ=F"}
                else "USD_per_share"
            )
            if symbol.startswith("^") or symbol.endswith("=F"):
                metrics.pop("last_close_times_volume_usd_proxy")
            result[symbol] = metrics
        return result

    def macro(self) -> dict:
        result = {}
        for symbol, (name, unit) in FRED_SERIES.items():
            try:
                url = "https://fred.stlouisfed.org/graph/fredgraph.csv"
                content = self.fetch(
                    symbol + ".csv",
                    url,
                    params={
                        "id": symbol,
                        "cosd": str(self.as_of - timedelta(days=730)),
                        "coed": str(self.as_of),
                    },
                )
                data = pd.read_csv(io.BytesIO(content), index_col=0, parse_dates=True)
                result[symbol] = {
                    **summarize_series(data[symbol], self.as_of),
                    "name": name,
                    "unit": unit,
                    "source": "https://fred.stlouisfed.org/series/" + symbol,
                }
            except Exception as exc:
                self.record_error("FRED:" + symbol, exc)
        try:
            data = pd.read_csv(io.BytesIO(self.fetch("VIX_History.csv", CBOE_URL)))
            series = pd.Series(data.CLOSE.values, index=pd.to_datetime(data.DATE))
            result["CBOE_VIX"] = {
                **summarize_series(series, self.as_of),
                "unit": "index",
                "source": CBOE_URL,
            }
        except Exception as exc:
            self.record_error("CBOE_VIX", exc)
        try:
            data = pd.read_stata(io.BytesIO(self.fetch("gpr.dta", GPR_URL))).set_index("date")
            for column in ["GPRD", "GPRD_ACT", "GPRD_THREAT", "GPRD_MA7", "GPRD_MA30"]:
                result[column] = {
                    **summarize_series(data[column], self.as_of),
                    "unit": "index",
                    "source": "https://www.matteoiacoviello.com/gpr.htm",
                }
        except Exception as exc:
            self.record_error("GPR", exc)
        return result

    def run(self, include_cnn: bool = False, max_pages: int = 2) -> dict:
        result = {
            "retrieved_at": self.now.isoformat(),
            "price_as_of": str(self.as_of),
            "live_predictions_not_historical": True,
        }
        for name, function in [
            ("polymarket", lambda: self.polymarket(max_pages)),
            ("prices", self.prices),
            ("macro", self.macro),
        ]:
            try:
                result[name] = function()
                if name in ("prices", "macro"):
                    for row in result[name].values():
                        row.setdefault("retrieved_at", datetime.now(UTC).isoformat())
            except Exception as exc:
                self.record_error(name, exc)
        if include_cnn:
            try:
                result["cnn"] = json.loads(self.fetch("cnn.json", CNN_URL))
            except Exception as exc:
                self.record_error("CNN fear and greed", exc)
        result["limitations"] = [
            "板块价格和成交量只表示轮动代理；本采集器未获取 ETF 净申赎或机构仓位。",
            "黄金和原油期货连续报价非可投资总收益指数；换月可能影响变化率。",
            "金融压力、VIX、地缘新闻风险测量不同概念，不合并为官方避险或战争指数。",
            "Polymarket 为抓取时的活跃合约，不能用于 --as-of 日期的历史回测。",
            "--as-of 只限制观测日期，不复原历史发布版本；FRED/GPR 数据可能修订。",
            "新闻主题与 AI 泡沫风险需要独立证据分析；不自动输出破裂概率。",
        ]
        result["collection_started_at"] = self.now.isoformat()
        result["retrieved_at"] = datetime.now(UTC).isoformat()
        result["errors"] = self.errors
        (self.output / "snapshot.json").write_text(
            json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False), encoding="utf-8"
        )
        return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--as-of",
        type=date.fromisoformat,
        default=datetime.now(ZoneInfo("America/New_York")).date() - timedelta(days=1),
    )
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--include-cnn", action="store_true")
    parser.add_argument("--polymarket-pages", type=int, default=2)
    args = parser.parse_args()
    if args.polymarket_pages < 1:
        parser.error("--polymarket-pages 至少为 1")
    if args.as_of >= datetime.now(ZoneInfo("America/New_York")).date():
        parser.error("--as-of 必须早于纽约当天，避免使用未完成日线")
    output = args.output_dir or Path("results/intelligence") / datetime.now(UTC).strftime(
        "%Y%m%dT%H%M%SZ"
    )
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    result = Collector(output, args.as_of).run(args.include_cnn, args.polymarket_pages)
    print(
        json.dumps(
            {
                "output": str(output / "snapshot.json"),
                "prices": len(result.get("prices", {})),
                "prediction_markets": len(result.get("polymarket", {}).get("markets", [])),
                "errors": len(result["errors"]),
            },
            ensure_ascii=False,
        )
    )
    return (
        0
        if (
            result.get("prices")
            and result.get("macro")
            and result.get("polymarket", {}).get("markets")
        )
        else 1
    )


if __name__ == "__main__":
    raise SystemExit(main())
