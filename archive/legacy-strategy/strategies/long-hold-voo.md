---
strategy: 长持标普 500
strategy_id: f9f1d84d-6552-470f-9074-36363e1f3559
tag: 长持
market: US
symbols: [VOO]
analysis_interval: 240
allow_overnight: true
klines: [1d]
market_data:
  fundamentals: true
  include_news: false
  include_market_context: false
risk_config:
  trading_mode: open_only
  max_positions: 1
  max_position_pct: 20
  stop_loss_pct: 50
  take_profit_pct: 50
  target_cash_pct: 80
  cash_reserve_pct: 0.5
  daily_pnl_stop_pct: -50
  max_slippage_pct: 1
  trade_cooldown_minutes: 1440
  reverse_cooldown_minutes: 1440
  trailing_profit: disabled
synced: 2026-08-11
---

长期定投标普 500，只买入，永不卖出。

执行规则：
1. 标的固定为 VOO，不交易任何其他标的。
2. 每周一和每周四各买入一次。买入时必须使用 light（轻仓）强度，不要用 medium 或 heavy。本策略靠多次小额买入摊平成本，不做一次性重仓。
3. 若当天不是周一或周四，或本周已经买入过两次，输出 wait，不做任何操作。
4. 任何情况下都不卖出：不止损、不止盈、不因新闻或市场波动减仓。
5. 市场下跌不是卖出理由，而是继续按计划买入的机会。
6. 当 VOO 持仓市值已占策略总资产 95% 以上时，输出 wait，停止买入。
