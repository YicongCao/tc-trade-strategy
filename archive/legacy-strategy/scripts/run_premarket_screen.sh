#!/bin/zsh
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PYTHON="$ROOT_DIR/.venv/bin/python"
LOCK_DIR="/tmp/tc-trade-strategy-premarket.lock"

if [[ ! -x "$PYTHON" ]]; then
  echo "缺少虚拟环境：$PYTHON，请先执行 python3 -m venv .venv && .venv/bin/pip install -e ."
  exit 1
fi

if [[ "${1:-}" != "--force" ]]; then
  ny_weekday="$(TZ=America/New_York date +%u)"
  ny_hour_minute="$(TZ=America/New_York date +%H%M)"
  ny_time=$((10#$ny_hour_minute))
  if (( ny_weekday > 5 || ny_time < 830 || ny_time > 930 )); then
    echo "当前不是纽约工作日盘前 08:30–09:30，跳过。"
    exit 0
  fi
fi

if ! mkdir "$LOCK_DIR" 2>/dev/null; then
  echo "已有盘前筛选任务在运行，跳过。"
  exit 0
fi
trap 'rmdir "$LOCK_DIR"' EXIT

cd "$ROOT_DIR"
"$PYTHON" -m tc_trade_strategy.premarket
