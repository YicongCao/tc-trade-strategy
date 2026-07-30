# Trade Copilot MCP 工具参考

> 最后核对：2026-07-30 · 服务器 ID `user-trade-copilot` · 状态 `ready`（已通过 OAuth 认证）
> 当前连接可见 **17 个功能工具 + 1 个认证工具**，全部为**只读**。

## 关键结论（先看这个）

1. **写工具已开放，但会被客户端的工具清单缓存挡住。** 服务端现有 22 个工具，比只读时期多出 `create_strategy` / `update_strategy` / `archive_strategy` / `unarchive_strategy` / `confirm_proposal`，走**两段式提案**：先调用写工具拿到 `proposal_id` 与字段级 diff，再 `confirm_proposal` 才真正落库。
   **坑**：Cursor 的 MCP 客户端在建立连接时缓存工具清单，服务端新增工具不会同步到已有会话。实测在一个旧会话里 `GetMcpTools` 仍只返回 17 个，重新 `mcp_auth` 认证成功也刷不掉，直接调 `update_strategy` 报 "tool not found"。**解决办法是开一个新对话**（新连接会重新拉清单），或重启 Cursor。
   下面的工具清单是只读时期整理的，写工具的参数 schema 待在能调用的会话里用 `GetMcpTools` 补齐。
2. **MCP 不能当回测数据源。** K 线一次只能查一个标的、最多 120 根、且不开放分钟级；实时行情一次最多 20 个标的。这个量级只够做归因和抽查，撑不起参数网格搜索。本仓库的回测数据必须另找来源。
3. **MCP 的行情缺口不代表平台的缺口。** `get_symbol_kline` 对 `DRAM` 返回旧主体历史、对中概 ADR 只返回 1 根，但**平台喂给 AI 策略的 K 线是完整正确的**——见下文"策略引擎的真实行为"。两条数据管道是分开的，不要用 MCP 的缺陷推断平台的缺陷。
4. **MCP 的真正价值在"对标口径"和"实盘校准"**：`list_transactions` 有真实手续费和已实现盈亏，`get_decision_detail` 能看到 LLM 的完整输入输出，`list_signal_performance` 有决策的事后 1/3/5 日表现。这些是校准本地假设最可靠的输入。
5. **字段口径要抄平台的**，这样本地策略能平移回站内。见文末"平台字段口径"。

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

### ⚠️ 中概 ADR 没有历史 K 线

同一个数据源对中概 ADR 只返回 1 根合成 K 线。实测（2026-07-29）：

| 标的 | 请求 | 实际返回 |
| --- | --- | --- |
| `TSLA.US` | 日线 10 根 | 10 根真实数据 |
| `MU.US` | 日线 10 根 | 10 根真实数据 |
| `XPEV.US` | 日线 120 根 / 周线 60 根 | **各 1 根** |
| `NIO.US` | 日线 30 根 | **1 根** |

那唯一一根不是真实 K 线：它的开高低收与成交量和 `get_symbol_quotes` 的实时报价完全一致，且开盘价恰好等于最低价（XPEV 的 12.64、NIO 的 4.62 均如此），是拿当前报价拼出来的。

**这与 ticker 复用错配是两种不同的失败模式，但后果相同：无法计算 ATR、无法确认高低点、无法回测。** 涉及中概标的时不要依赖本接口取历史。

### 由此引出的连带风险

平台 AI 策略的 `market_data.klines` 会把 K 线喂给 LLM。**如果它用的是同一个行情源**，那么在 DRAM 或中概 ADR 上配 AI 策略时，LLM 可能拿到的是错的（旧主体）或空的历史数据，而 `system_prompt` 里那些"分析 20 日/50 日均线偏离"的要求就无从满足。

目前无法从 MCP 侧确认两者是否共用数据源。**验证方法**：策略产生第一条决策后调 `get_decision_detail`，查看决策当时 LLM 的原始输入里 K 线的条数与日期是否正常。这个检查成本很低，但能避免基于错误数据运行策略。

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

## 策略引擎的真实行为

以下全部来自 `get_decision_detail` 读到的一次真实决策（2026-07-29 XPEV 首次开仓），是**写策略提示词前必须知道的约束**。

### AI 的输出 schema 里没有数量字段

实际返回：

```json
[{"symbol":"XPEV","decision":"open","confidence":0.95,"intensity":"heavy",
  "summary":"策略首次运行，按当前价$13.005建立长期底仓1000股及网格初始持仓720股。"}]
```

只有 `symbol` / `decision` / `confidence` / `intensity` / `summary` 五个字段。**没有股数、没有价格、不能挂限价单。**

`decision` 取值 `open`/`buy`/`sell`/`close`/`hold`/`wait`，`intensity` 取值 `light`/`medium`/`heavy`。

**后果：提示词里写"每格买 30 股""在 11.28 挂买单"是无效的**，这些文字只会进入 `summary` 自由文本，执行引擎不解析。网格类策略无法用 AI 策略接口表达，必须用平台自带的网格引擎。

### 仓位大小由风控字段算出，不由提示词决定

实测那一单：`intensity=heavy` + `max_position_pct=100` + `cash_reserve_pct=10` + 可用现金 100,000 → 投入 90,000，成交 6,882 股，与"提示词里写的 1,720 股"无关。

推算关系：**投入金额 ≈ 可用现金 × (1 − cash_reserve_pct)，再受 max_position_pct 封顶**。

`target_cash_pct` 会反向施压：设为 0 时，平台在 AI 请求里主动写入"现金占比已超过目标 0%，应通过换仓 close 弱仓 → open 强仓消化"，等于催 AI 把现金用光。想让策略只用部分资金，**必须把 `target_cash_pct` 调高**，光靠提示词说"只买 1720 股"没用。

### 风控参数是喂给 LLM 的"软参考"，不是硬触发

AI 请求原文里逐条标注：

```
- 止损（软参考）: 50% — 浮亏接近此值时综合趋势/动能/位置判断,
  不要因单日波动伪触发就提前 close;高 Beta(>1.5) 标的可参考 ATR(14)/价格 放宽幅度
- 止盈（软）: 50% — 浮盈达此值时考虑落袋，结合行情判断
- 当日熔断线（软）: ≤-50% — 触及此线时停止 open/buy/加仓，仅允许 hold/sell/close
```

所以 `stop_loss_pct` 不会机械平仓，只是提示词里的一句建议。平台功能文档称其为"独立硬止损"，与 AI 策略路径的实际行为不符——**硬止损可能只在网格引擎等非 AI 路径上生效**。

### AI 请求里实际包含什么

`风控参数` / `当前持仓` / `当前时间`（含距收盘分钟数、报价快照时延）/ `即将到来的关键事件`（FOMC、CPI 等，带影响级别与天数）/ `当前账户状态`（现金占比与调仓建议）/ 每个标的的实时行情 + 各周期 K 线 + 技术指标 / `相关新闻`（近 30 天，带发布与采集时间、影响、情感、中文摘要）。

`prompt_version` 字段标明模板版本，实测为 `v6`。

### 平台的 K 线数据完整可用

同一次请求里 XPEV 的 1d / 1w / 1M 都是真实完整数据：30 根 K 线、20 根支撑 12.32 阻力 14.46、周线 20 根 -25.21%、月线支撑 11.14 阻力 28.23，指标齐全。

而 MCP 的 `get_symbol_kline` 查同一个 `XPEV.US` 只返回 1 根合成 bar。**两条数据管道不同源，不要在提示词里写"本标的历史数据不可靠"之类的话去误导 AI 忽略好数据。**

### 疑似：配置分钟级/小时级 K 线会导致策略不运行

2026-07-29 全天，五个 active 策略里只有 XPEV 产生了决策（2 条），另外三个日内型策略一条都没有：

| 策略 | K 线周期配置 | 当日决策数 |
| --- | --- | --- |
| XPEV | 1d / 1w / 1M | 2 |
| DRAM 网格 | **15m** / **1h** / 1d / 1w | 0 |
| 价格行为日内 | **15m** / **1h** / 1d / 1w | 0 |
| 标普500动量 | 1d / **1h** / 1w / 1M | 0 |

三个配了 15m 或 1h 的全部零决策，唯一没配的正常运行；`get_symbol_kline` 也明确"不开放分钟级"。**推测请求分钟级 K 线会导致取数失败、整次运行中断，连决策记录都写不进去。** 尚未验证，验证方法是把某个策略的 15m/1h 周期删掉再观察。

### 调度频率远低于配置值

XPEV 的 `analysis_interval` 是 30 分钟，6.5 小时的交易时段本应运行约 13 次，实际只有 2 次（09:32 与 13:30 美东）。原因不明，**不要假设策略会严格按 `analysis_interval` 执行**。

### 真实交易成本

| 项 | 实测值 |
| --- | --- |
| 手续费 | **$0.0035/股**（6,882 股收 24.09，无固定部分） |
| 滑点 | 分析时报价 13.005，实际成交 13.0765，**+0.55%** |
| 订单类型 | `market`（`suggested_order_type` 字段给出） |
| 分析到成交延迟 | 约 2.5 分钟 |

**佣金按股计费而非按笔固定**，所以"每格名义金额不能太小"这个约束不成立。真正的成本是滑点：市价单 0.55% 的单边滑点，对 2.5% 格距的网格会吃掉约 44% 的格子利润。

## 平台字段口径

从实盘策略 `get_strategy_profile` 提取的真实字段名，本地策略配置**建议直接沿用**，方便双向平移。

`risk_config`：

| 字段 | 实盘取值 | 含义 |
| --- | --- | --- |
| `max_positions` | 10 | 最大持仓标的数 |
| `max_position_pct` | 15 | 单标的最大仓位占比 % |
| `stop_loss_pct` | 5 | 止损 %。**在 AI 策略路径上是软参考，不会机械平仓**，见上一节 |
| `take_profit_pct` | 15 | 止盈 %，同样是软参考 |
| `cash_reserve_pct` | 0.5 | 现金保留比例 %。**直接决定单次开仓能投入多少资金** |
| `target_cash_pct` | 0 | 再平衡目标现金比例 %。设为 0 会催 AI 把现金用光 |
| `reverse_cooldown_minutes` | 60 | 反向开仓冷却分钟数，防反复打脸 |
| `daily_pnl_stop_pct` | -3 | 当日亏损熔断 %，软参考 |
| `trading_mode` | normal | `normal` 可开可平 / `open_only` 只买不卖 / `close_only` 只卖不开。**这个是真正的机制约束，比止损可靠** |
| `max_slippage_pct` | 1 | 最大滑点 % |
| `trade_cooldown_minutes` | 30 | 同向交易冷却 |
| `trailing_profit_activation_pct` | 8 | 移动止盈触发线。切到「固定止盈」标签页保存后，此字段与下一个会从配置中消失 |
| `trailing_profit_lock_drawdown_pct` | 5 | 移动止盈回撤锁定 |

服务端校验范围（UI 报错原文）：`stop_loss_pct` 0.5 ~ 50、`daily_pnl_stop_pct` -50 ~ -0.5。这几个字段**必填，没有关闭开关**，想禁用只能填到边界值；真要禁止卖出应该用 `trading_mode: open_only`。

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
