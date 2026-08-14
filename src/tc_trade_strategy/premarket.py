"""每日盘前行情下载与候选池预筛入口。"""

from __future__ import annotations

import argparse
import json
import logging
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from tc_trade_strategy.market_data import download_daily_bars, load_symbols
from tc_trade_strategy.screening import ScreenResult, screen_universe

LOGGER = logging.getLogger(__name__)
REPO_ROOT = Path(__file__).resolve().parents[2]


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="下载股票清单的完整日 K，并输出供 us-mushroom 使用的盘前候选池。"
    )
    parser.add_argument(
        "--symbols",
        type=Path,
        default=REPO_ROOT / "data" / "symbols.txt",
        help="每行一个代码的标的清单",
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=REPO_ROOT / "data" / "cache" / "yahoo",
        help="Yahoo 日 K 缓存目录",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=REPO_ROOT / "results" / "premarket",
        help="筛选报告输出目录",
    )
    parser.add_argument("--limit", type=int, default=20, help="输出候选数量")
    parser.add_argument("--batch-size", type=int, default=25, help="单次下载的代码数量")
    parser.add_argument("--min-bars", type=int, default=200, help="最低完整日 K 数")
    parser.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    return parser


def _markdown_report(
    generated_at: datetime,
    data_date: str,
    requested: int,
    available: int,
    candidates: list[ScreenResult],
    failures: list[dict[str, str]],
) -> str:
    lines = [
        f"# {data_date} 盘前预筛",
        "",
        f"- 生成时间：{generated_at.isoformat()}",
        f"- 请求标的：{requested}",
        f"- 满足 200 根完整日 K：{available}",
        f"- 数据不足或下载失败：{len(failures)}",
        "",
        "## 前置候选",
        "",
        "| 排名 | 代码 | 预筛分 | 状态 | 收盘价 | 距 60 日枢轴 | 量比 | 63 日相对 SPY |",
        "| ---: | --- | ---: | --- | ---: | ---: | ---: | ---: |",
    ]
    for rank, item in enumerate(candidates, start=1):
        lines.append(
            f"| {rank} | {item.symbol} | {item.score:.2f} | {item.state} | "
            f"{item.close:.4f} | {item.pivot_distance_pct:+.2f}% | "
            f"{item.volume_ratio50:.2f} | {item.relative_strength63_pct:+.2f}% |"
        )

    if failures:
        lines.extend(
            [
                "",
                "## 数据不足或下载失败",
                "",
                "| 原代码 | Yahoo 代码 | 原因 |",
                "| --- | --- | --- |",
            ]
        )
        for failure in failures:
            lines.append(
                f"| {failure['symbol']} | {failure['yahoo_symbol']} | {failure['reason']} |"
            )

    lines.extend(
        [
            "",
            "> 该结果只做机械预筛，不是最终买入名单；杯柄、双底、平底及 "
            "MACD/KDJ 的 50/50 综合评分仍由 us-mushroom 完成。",
            "",
        ]
    )
    return "\n".join(lines)


def run(args: argparse.Namespace) -> int:
    symbols = load_symbols(args.symbols)
    if not symbols:
        raise ValueError(f"标的清单为空：{args.symbols}")
    LOGGER.info("开始下载 %d 个标的的完整日 K", len(symbols))

    bars, fetch_failures = download_daily_bars(
        symbols,
        args.cache_dir,
        min_bars=args.min_bars,
        batch_size=args.batch_size,
    )
    candidates = screen_universe(bars, limit=args.limit)
    generated_at = datetime.now(ZoneInfo("Asia/Shanghai"))
    data_date = max(frame.index[-1] for frame in bars.values()).date().isoformat()
    failures = [
        {
            "symbol": failure.symbol,
            "yahoo_symbol": failure.yahoo_symbol,
            "reason": failure.reason,
        }
        for failure in fetch_failures
    ]

    payload = {
        "generated_at": generated_at.isoformat(),
        "data_date": data_date,
        "requested_count": len(symbols),
        "available_count": len(bars),
        "failure_count": len(failures),
        "candidates": [candidate.to_dict() for candidate in candidates],
        "failures": failures,
    }

    args.output_dir.mkdir(parents=True, exist_ok=True)
    stem = generated_at.date().isoformat()
    (args.output_dir / f"{stem}.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (args.output_dir / f"{stem}.md").write_text(
        _markdown_report(
            generated_at,
            data_date,
            len(symbols),
            len(bars),
            candidates,
            failures,
        ),
        encoding="utf-8",
    )
    (args.output_dir / "latest-candidates.txt").write_text(
        "\n".join(candidate.symbol for candidate in candidates) + "\n",
        encoding="utf-8",
    )

    LOGGER.info(
        "完成：%d/%d 个标的可用，输出前 %d，%d 个失败",
        len(bars),
        len(symbols),
        len(candidates),
        len(failures),
    )
    print("候选：" + ",".join(candidate.symbol for candidate in candidates))
    return 0


def main() -> int:
    args = _parser().parse_args()
    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format="%(asctime)s %(levelname)s %(message)s",
    )
    return run(args)


if __name__ == "__main__":
    raise SystemExit(main())
