# Trade Copilot MCP 工具参考

> 探索时间：2026-07-29 · 服务器 ID `user-trade-copilot` · 状态 `ready`（已通过 OAuth 认证）
> 共 **17 个功能工具 + 1 个认证工具**，全部为**只读**。

## 关键结论（先看这个）

1. **当前接入的 MCP 只有读能力。** 多个工具描述里引用了 `propose_strategy_update` / 提案类写工具，但它们**没有出现在实际工具列表中**——按服务器名和 `propose|create|update|write|order|rebalance` 检索均无结果。也就是说通过 MCP 只能"看"，创建/修改策略、下单、调参都得回站内 UI 操作。
2. **MCP 不能当回测数据源。** K 线一次只能查一个标的、最多 120 根、且不开放分钟级；实时行情一次最多 20 个标的。这个量级只够做归因和抽查，撑不起参数网格搜索。本仓库的回测数据必须另找来源。
3. **MCP 的真正价值在"对标口径"和"实盘校准"**：平台已经跑了实盘，`list_transactions` 有真实手续费和已实现盈亏，`list_signal_performance` 有决策的事后 1/3/5 日表现。这些是校准本地回测假设（滑点、费率、信号胜率）最可靠的输入。
4. **字段口径要抄平台的**，这样本地策略能平移回站内。见文末"平台字段口径"。

## 工具清单

### 策略元信息

| 工具 | 参数 | 返回要点 |
| --- | --- | --- |
| `list_user_strategies` | `include_archived?`（默认 false） | 策略精简列表：`id`、`name`、`market`、`status`、`tag_name`。**不含** `system_prompt` / `risk_config` / 现金。用它拿 `strategy_ids` 再调其他工具 |
| `get_strategy_profile` | `strategy_ids[]`（必填，可多个） | 完整属性：描述、标的池、`finviz_url`、`system_prompt`、`market_data`、`risk_config`、资金与盈亏 |
| `get_strategy_screener_pool` | `strategy_ids[]`（必填） | 最近一轮 finviz 筛选命中的候选池 `symbols[]` + `total_count` + `updated_at`。**是候选清单，不是持仓**；超 100 个截断 |
| `preview_finviz_screener` | `finviz_url`（必填）、`limit?`（默认 30，上限 50） | 干跑一个 finviz URL，返回命中 ticker 与 `total`。改选股条件前先用它验证 URL 合法性 |

### 持仓与绩效

| 工具 | 参数 | 返回要点 |
| --- | --- | --- |
| `get_positions` | `strategy_ids[]`（必填） | 当前持仓：`current_price`、`unrealized_pnl`、`day_change_pct`，按 `market_value` 降序 + 汇总。分析涨跌**优先用它**，别从决策流水反推持仓 |
| `get_daily_snapshots` | `strategy_ids[]`（必填）、`date_from?`（默认 365 天前）、`date_to?`（默认昨天） | 每日 `total_assets`、`daily_pnl`、`daily_pnl_pct`、`cumulative_twr_pct`（TWR 链式连乘）。范围上限 366 天 |
| `list_transactions` | `strategy_ids[]`（必填）、`symbol?`、`date_from?`/`date_to?`（默认近 30 天）、`limit?`（默认 50，上限 200，跨策略共享） | 真实成交流水，**含 `fees` 与 `realized_pnl`**，按 `executed_at` 倒序 + 窗口汇总。`truncated=true` 时汇总只覆盖返回窗口 |

### 决策与信号

| 工具 | 参数 | 返回要点 |
| --- | --- | --- |
| `list_decisions` | 全可选：`strategy_ids?`、`symbol?`、`date_from?`/`date_to?`（默认近 30 天）、`execution_status?`、`decision?`、`limit?`（默认 20，上限 200） | 决策流水。**反查"哪些策略买了某标的"时直接传 `symbol` 不传 `strategy_ids`**，一次跨全部策略；不传 `strategy_ids` 时**必须**传 `symbol`。`summary` 截断到 200 字符 |
| `get_decision_detail` | `decision_id`（必填）、`include_ai_text?`（默认 true） | 单条决策全文，含决策当时 LLM 的原始请求/响应。**单条返回很大**，仅在需要具体理由时调 |
| `list_signal_performance` | `strategy_ids[]`（必填）、`date_from?`/`date_to?`、`symbol?`、`decision?`、`limit?`（默认 50，上限 200） | 决策事后表现：`return_1d/3d/5d`（决策后 1/3/5 个交易日**对数收益**）、`correct_1d/3d/5d`（按方向判定，buy/open 涨为对，sell/close 跌为对） |

枚举值：

- `decision`：`open` 开仓 / `buy` 加仓 / `sell` 减仓 / `close` 平仓 / `hold` 持有 / `wait` 观望
- `execution_status`：`filled` 已成交 / `submitted` 已提交 / `failed` 失败 / `skipped` 未执行 / `pending` 待执行

### 行情与日历

| 工具 | 参数 | 返回要点 / 限制 |
| --- | --- | --- |
| `get_symbol_quotes` | `symbols[]`（必填） | 实时行情：`last`、`prevClose`、涨跌额/幅、当日高低、成交量。**一次最多 20 个**，超出截断 |
| `get_symbol_kline` | `symbol`（必填，单个）、`period?`（`day`/`week`/`month`，默认 day）、`count?`（默认 30，上限 120） | 历史 K 线。**不开放分钟级**，一次只能一个标的 |
| `get_trading_calendar` | `market`（必填，`US`/`HK`/`CN`/`SG`）、`date_from?`（默认 30 天前）、`date_to?`（默认 30 天后） | 只返回交易日；`session_type`：`full` 全日 / `half` 半日市。可用于算有效交易日数与节假日缺口 |
| `get_current_time` | `timezones?`（IANA 名数组，默认 上海/纽约/香港） | `utc_iso` + 各时区当前时刻、日期、周几。**只给日历日**，"最近一个交易日"要配合 `get_trading_calendar` 排除周末假期 |

标的代码格式：`AAPL.US`、`00700.HK`、`600519.SH`。

### ⚠️ K 线历史数据存在代码复用错配

`get_symbol_kline` 的数据源是 `tencent`，对**曾被复用的 ticker 会返回旧主体的历史**。

实测（2026-07-29）：查 `DRAM.US` 日线和周线，返回的都是已退市的 Dataram Corp 数据（2015-03 至 2017-06，价格 0.7–5.7 美元，2017-05-08 有反向拆股跳空），之后直接跳到 2026-07-28 一根当前 bar，中间九年空白。而同一时刻 `get_symbol_quotes` 查 `DRAM.US` 返回的是正确的当前行情（47.77、成交量 8878 万）——**两个接口的数据源不一致**。

对照：`MU.US` 的日线返回正常的 2026 年数据，说明接口本身没问题。

**使用前的自检**：拿到 K 线后先看最后几根的日期是否连续、价格量级是否与 `get_symbol_quotes` 的 `last` 相符。若出现"大段历史 + 孤立的当前 bar"，说明命中了这个问题，该标的的历史数据不可用，需换数据源。

### 市场环境与择时

| 工具 | 参数 | 返回要点 |
| --- | --- | --- |
| `get_market_overview` | 无 | 市场概览缓存。**只有最新一份（每小时刷新），不支持按日期回查** |
| `get_cn_market_timing` | `date_from?`/`date_to?`（默认近 60 天，上限 366 天） | A 股大盘 0AMV 择时序列。**仅适用 A 股大盘，个股与美股不要用** |

`get_market_overview` 实测返回结构（2026-07-29 抽样）：

```
overview.macro    → spy/qqq/gld/tlt/uup 的 price+changePct、vix、us10y、
                    temperature{value, sentiment, valuation, description}
overview.events   → 未来宏观事件数组 {date, type(fomc/cpi/nfp), impact, description}
overview.sector   → 23 个板块 {name, group(primary|sub), symbol, price, turnover, changePct}
```

抽样值：`vix=18.21`，`temperature.value=67`（"Temp Comfortable & Gradually Dropping"），11 个一级板块 + 12 个子板块（含半导体 SMH、软件 IGV、中概互联 KWEB 等）。板块 `turnover` 可直接用来做资金流强弱排序。

`get_cn_market_timing` 实测返回结构：

```json
{ "rows": [{ "date": "2026-07-28", "amv": 19275690475366.49, "regime": -1, "signal": null }],
  "latest": { ... }, "count": 7 }
```

- `amv`：换手衰减活跃市值（沪深两市合成）
- `regime`：`1` 多头 / `-1` 空头 / `null` 预热未定，由 ZigZag 判定
- `signal`：`to_long` 转多 / `to_short` 转空 / `null` 非反转日

### 消息面

| 工具 | 参数 | 返回要点 |
| --- | --- | --- |
| `list_news_for_period` | `date_from?`/`date_to?`（默认近 7 天）、`symbols?`、`sentiment?`（positive/negative/neutral）、`impact?`（high/medium/low）、`limit?`（默认 20，上限 50） | `posted_at`、`author_username`、`content`（截断 500 字）、`analysis`。**仅 Twitter / Truth Social**，不含传统财经新闻、研报、公告 |

### 认证

`mcp_auth`（无参数）：认证该 MCP 服务器。仅在工具调用报认证/授权错误时调用。

## 平台字段口径

从实盘策略 `get_strategy_profile` 提取的真实字段名，本地策略配置**建议直接沿用**，方便双向平移。

`risk_config`：

| 字段 | 实盘取值 | 含义 |
| --- | --- | --- |
| `max_positions` | 10 | 最大持仓标的数 |
| `max_position_pct` | 15 | 单标的最大仓位占比 % |
| `stop_loss_pct` | 5 | 独立硬止损 % |
| `take_profit_pct` | 15 | 止盈 % |
| `cash_reserve_pct` | 0.5 | 现金保留比例 % |
| `target_cash_pct` | 0 | 再平衡目标现金比例 % |
| `reverse_cooldown_minutes` | 60 | 反向开仓冷却分钟数，防反复打脸 |

平台文档另有 `daily_pnl_stop_pct`（每日亏损硬熔断）与 VIX 高波动开仓门控，当前这个策略未配置。

策略级其他字段：`market`、`symbols[]`、`finviz_url`、`include_positions`、`system_prompt`、`analysis_interval`（分钟，实盘 30）、`allow_overnight`、`close_before_minutes`（收盘前 N 分钟，实盘 15）、`ai_provider_id`、`initial_capital` / `current_cash` / `total_assets` / `unrealized_pnl` / `realized_pnl`。

`market_data.klines` 每个周期（`1d`/`1h`/`1w`/`1M`）各取 30 根，指标口径：

```
sma / ema : [5, 10, 20, 30, 60, 120, 250]
rsi       : [14]
atr       : [14]
macd      : fast 12, slow 26, signal 9
kdj       : period 9, k_smooth 3, d_smooth 3
```

本地实现指标时用同一套参数，回测结论才能和平台实盘对齐。

## 当前账户状态（探索时快照）

只有 1 个策略：「标普500均值回归动量成长策略」，`market=US`，`status=paused`，初始资金 100000，当前现金 100000，已实现/未实现盈亏均为 0——**等于还没有真实成交历史**。

这意味着短期内 `list_transactions` / `list_signal_performance` / `get_daily_snapshots` 拿不到有效样本，暂时无法用实盘数据校准回测假设。要么先在平台上把策略跑起来积累流水，要么本地回测先用自己假设的费率和滑点，并在结论里注明。

平台上**还没有网格策略**，网格相关的配置字段（分时段滑点、必亏配置警告等）也没有 MCP 工具可读取，只能参照 UI。

## 调用注意事项

- 调用前先用 `GetMcpTools` 确认 schema，工具集会随平台版本变化。
- 所有 `strategy_ids` 必填的工具都接受多个 ID，能合并就合并，别循环单个调。
- 日期范围类工具的默认窗口都不长（决策 30 天、消息 7 天、快照 365 天），要长历史必须显式传 `date_from`。
- `get_decision_detail` 和 `include_ai_text=true` 的返回很占 token，按需调用。
