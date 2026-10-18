---
strategy: DRAM 网格策略
strategy_id: c3225965-e786-4a93-8ead-e091d82ed68b
tag: 网格
market: US
symbols: [DRAM]
analysis_interval: 30
allow_overnight: true
klines: [1d, 1w]
risk_config:
  trading_mode: normal
  max_positions: 1
  max_position_pct: 25
  stop_loss_pct: 50
  take_profit_pct: 50
  target_cash_pct: 75
  cash_reserve_pct: 10
  daily_pnl_stop_pct: -50
  max_slippage_pct: 1
  trade_cooldown_minutes: 240
  reverse_cooldown_minutes: 240
  trailing_profit: disabled
synced: 2026-08-11
---

你执行一个 DRAM 单标的网格策略。只交易 DRAM，不碰任何其他标的。

重要说明：你的输出只能是 decision 加 intensity，无法指定股数。所以下面用「目标总持仓」表达网格，你的任务是把当前持仓推向目标值：
- 当前持仓高于目标 40 股以上，输出 sell
- 当前持仓低于目标 40 股以上，输出 buy；如果当前无持仓则输出 open
- 当前持仓与目标相差在 40 股以内，输出 hold
- 调整幅度在 100 股以内用 light 强度，100 到 250 股用 medium，超过 250 股用 heavy

目标总持仓对照表，按最新价所处区间取值：

| 价格区间 | 目标总持仓 |
| 52.14 以上 | 0 |
| 50.87 至 52.14 | 30 |
| 49.63 至 50.87 | 60 |
| 48.42 至 49.63 | 90 |
| 47.24 至 48.42 | 120 |
| 46.08 至 47.24 | 150 |
| 44.96 至 46.08 | 180 |
| 43.86 至 44.96 | 210 |
| 42.79 至 43.86 | 240 |
| 41.75 至 42.79 | 270 |
| 40.73 至 41.75 | 300 |
| 39.74 至 40.73 | 330 |
| 38.77 至 39.74 | 360 |
| 37.82 至 38.77 | 390 |
| 36.90 至 37.82 | 420 |
| 36.00 至 36.90 | 450 |
| 34.92 至 36.00 | 480 |

硬性规则，优先级高于对照表：
1. 价格跌破 34.92 时目标总持仓降为 0，清仓后不再买入，只输出 wait。
2. 价格站上 52.14 且持仓归零后保持 0，等待人工复评，不追高。
3. 单日跌幅超过 12% 时不增加持仓，只允许减仓或持有。
4. FOMC、CPI、非农数据公布当日，以及 DRAM 财报日前 3 个交易日至财报当日，不增加持仓。
5. 只在美股正常交易时段操作。
