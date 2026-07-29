---
strategy: 长持标普 500
strategy_id: f9f1d84d-6552-470f-9074-36363e1f3559
tag: 长持
market: US
symbols: [VOO]
analysis_interval: 1440
allow_overnight: true
market_data:
  include_news: false
  include_market_context: false
risk_config:
  trading_mode: open_only
  max_positions: 1
  max_position_pct: 100
  stop_loss_pct: 50
  take_profit_pct: 50
  daily_pnl_stop_pct: -50
synced: 2026-07-29
---

长期定投标普 500，只买入，永不卖出。

执行规则：
1. 标的固定为 VOO，不交易任何其他标的。
2. 每周一和每周四各买入一次，每次买入金额为策略总资金的 2%，按当时价格取整股。
3. 累计投入达到策略总资金的 95% 后停止买入，之后只持有不操作。
4. 任何情况下都不卖出：不止损、不止盈、不因新闻或市场波动减仓。
5. 若当天不是周一或周四，或本周已完成两次买入，输出 wait，不做任何操作。
6. 市场下跌不是卖出理由，而是继续按计划买入的机会。
