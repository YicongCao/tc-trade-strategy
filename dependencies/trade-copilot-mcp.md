# Trade Copilot MCP 工具参考

> Codex 接入核对：2026-10-18。当前会话可发现 22 个 tc 功能工具，已验证只读查询。下文业务细节包含 7–8 月历史样本，以当前工具 schema 为准。

## Codex 接入

端点为 `https://tc.zkd.me/api/mcp`，使用 Streamable HTTP。当前已在用户级 `~/.codex/config.toml` 配置并授权；无需重复添加。新环境按 Codex 的 MCP 设置或 CLI 接入：

```bash
codex mcp add trade-copilot --url https://tc.zkd.me/api/mcp
codex mcp login trade-copilot
codex mcp list
```

对应配置（不含凭证）：

```toml
[mcp_servers.trade-copilot]
url = "https://tc.zkd.me/api/mcp"
```

也可按官方规范使用受信任项目的 `.codex/config.toml`。本仓库不重复提交已有用户级连接，不复制 OAuth token 或硬编码回调地址。

来源：[Codex MCP 官方说明](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)。仅验证本地 Codex；其他客户端或云端是否支持相同连接须单独验证，不能推断自动继承认证。

## 发现与诊断

先检查连接状态和当前工具清单，再执行 `get_market_overview` 等只读查询。鉴权失败按当前客户端提示重新登录；缺工具时区分服务未连接、权限不足、客户端清单过期和服务端已下线。必要时重连或重启后再次检查，不通过修改无关配置字段强制刷新。

旧 IDE 的配置指纹、专用认证工具与云端接入说明已退出当前操作指南；历史内容保存在迁移前的 Git 提交中。

## 关键边界

- tc 写操作走两段式：生成 proposal 与 diff，取得用户对具体操作的授权后才 `confirm_proposal`，随后回读。已有明确授权不重复询问。
- 当前 `risk_config` 为顶层浅合并，`market_data` 为整体替换。参数以调用时的 schema 为准，历史案例不是接口契约。
- tc K 线适合抽查，不能满足本地大批量回测。历史上 MCP 行情和平台策略输入存在管道差异，须分别验证。
- 真实成交、费用、完整决策输入输出可用于校准执行假设。数据时间和样本限制必须保留。

## 工具清单

### 策略元信息

| 工具 | 参数 | 返回要点 |
| --- | --- | --- |
| `list_user_strategies` | `include_archived?`（默认 false） | 策略精简列表：`id`、`name`、`market`、`status`、`tag_name`，**另含各策略当前的 AI 供应商 id / 名称 / 模型**。不含 `system_prompt` / `risk_config` / 现金 / api_key。用它拿 `strategy_ids` 再调其他工具 |
| `get_strategy_profile` | `strategy_ids[]`（必填，可多个） | 完整属性：描述、标的池、`finviz_url`、`system_prompt`、`market_data`、`risk_config`、资金与盈亏、当前 AI 供应商 |
| `get_strategy_screener_pool` | `strategy_ids[]`（必填） | 最近一轮 finviz 筛选命中的候选池 `symbols[]` + `total_count` + `updated_at`。**是候选清单，不是持仓**；超 100 个截断 |
| `preview_finviz_screener` | `finviz_url`（必填）、`limit?`（默认 30，上限 50） | 干跑一个 finviz URL，返回命中 ticker 与 `total`。改选股条件前先用它验证 URL 合法性 |
| `list_ai_providers` | 无 | 全部 AI 供应商：`id`、`name`、`model`、`protocol`、`api_base_url`、`temperature`、`enable_thinking`、限速、单价、`disabled`、被几个策略引用（总数 / active 数）。**不返回 api_key，也不返回最大输出长度** |

`list_ai_providers` 的主要用途是把供应商名称映射成 uuid——`update_strategy` 的 `ai_provider_id` 只认 uuid 不认名称。改策略模型前必须先调它。

### ⚠️ 供应商参数没有写工具，只能走 UI

写工具白名单全部作用于策略（`create_strategy` / `update_strategy` / `archive_strategy` / `unarchive_strategy` / `confirm_proposal`），**没有任何修改 AI 供应商的 MCP 工具**。

以下参数只能在平台「AI 供应商」页上改：**最大输出长度、`enable_thinking`、`temperature`、api_base_url、限速、单价**。

MCP 能做的只有「把某个策略换到另一个已存在的供应商」，用 `update_strategy` 改 `ai_provider_id`。

这条限制在 2026-08-12 撞上过一次实际问题：推理模型开着 `enable_thinking`、最大输出长度偏小，思维链把输出预算吃光，再平衡调用返回 `finish_reason: length` 且正文为空。**只能让用户去 UI 调，MCP 无解。** 详见 `reviews/2026-08-12-ai-truncation-and-recurring-warnings.md`。

改供应商参数时注意它是**共享设置**：`list_ai_providers` 的 `used_by_strategies` 会告诉你有几个策略在引用，改一次影响全部。

### 持仓与绩效

| 工具 | 参数 | 返回要点 |
| --- | --- | --- |
| `get_positions` | `strategy_ids[]`（必填） | 当前持仓：`current_price`、`unrealized_pnl`、`day_change_pct`，按 `market_value` 降序 + 汇总。分析涨跌**优先用它**，别从决策流水反推持仓 |
| `get_daily_snapshots` | `strategy_ids[]`（必填）、`date_from?`（默认 365 天前）、`date_to?`（默认昨天） | 每日 `total_assets`、`daily_pnl`、`daily_pnl_pct`、`cumulative_twr_pct`（TWR 链式连乘）。范围上限 366 天。**2026-08 新增 `per_strategy_summary`**：逐策略给出天数、总盈亏、期末资产、累计 TWR、最好/最差单日，比逐条 snapshot 好用得多；另新增 `currency` 计价币种 |
| `list_transactions` | `strategy_ids[]`（必填）、`symbol?`、`date_from?`/`date_to?`（默认近 30 天）、`limit?`（默认 50，上限 200，跨策略共享） | 真实成交流水，**含 `fees` 与 `realized_pnl`**，按 `executed_at` 倒序 + 窗口汇总。`truncated=true` 时汇总只覆盖返回窗口 |

### 决策与信号

| 工具 | 参数 | 返回要点 |
| --- | --- | --- |
| `list_decisions` | 全可选：`strategy_ids?`、`symbol?`、`date_from?`/`date_to?`（默认近 30 天）、`execution_status?`、`decision?`、`limit?`（默认 20，上限 200） | 决策流水。**反查"哪些策略买了某标的"时直接传 `symbol` 不传 `strategy_ids`**，一次跨全部策略；不传 `strategy_ids` 时**必须**传 `symbol`。`summary` 截断到 200 字符 |
| `get_decision_detail` | `decision_id`（必填）、`include_ai_text?`（默认 true） | 单条决策全文，含决策当时 LLM 的原始请求/响应。**单条返回很大**，仅在需要具体理由时调 |

### ⚠️ 复盘工具已下线（2026-08-12）

服务端的复盘工具链换过两轮，目前**一个都不剩**：

```
list_signal_performance  →  拆成 get_retro_overview + list_retro_cases  →  两个都下线
```

现在做决策质量分析只能手工组合 `list_decisions`（拿 confidence、decision、execution_status）+ `list_transactions`（拿成交价与已实现盈亏）+ `get_symbol_quotes`（拿事后价格），自己算事后表现。8/11 的组合复盘就是这么做的。

**下线前记下来的一条口径仍然有效**：`execution_status` 里 **`filled` 才是真实成交的决策，`skipped` 是被再平衡毙掉的信号**。两者混算得到的是"AI 嘴上说买的能力"，不是策略赚钱能力。这条在用 `list_decisions` 自己统计时同样要守。

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

### ⚠️ ETF 同样没有历史 K 线

第三种失败模式，2026-07-30 实测：

| 标的 | 类型 | 请求 | 实际返回 |
| --- | --- | --- | --- |
| `MU.US` | 个股 | 日线 10 根 | 10 根真实数据 |
| `SPY.US` | ETF | 日线 30 根 | **1 根** |
| `VOO.US` | ETF | 日线 10 根 | **1 根** |

和中概 ADR 是同一种「拿当前报价拼一根」的合成 bar。**后果：算不出大盘的均线位置。** 这直接卡住一类常见的策略门槛——比如「SPY 跌破 20 日均线时暂停开仓」，从 MCP 侧无法验证是否触发。

绕过办法：从 `get_decision_detail` 的 AI 请求原文里读，平台喂给 LLM 的 K 线是完整的，均线值直接写在里面。代价是必须等策略先产生一条决策。

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

`mcp_auth`（无参数）：认证该 MCP 服务器。仅在工具调用报认证/授权错误时调用，或按上面「工具清单刷新」改完配置后重新授权。

## 写工具（两段式提案）

四个写工具都**不直接落库**，只生成草案并返回 `proposal_id` + 字段级 diff；必须把 diff 展示给用户、拿到明确同意后再调 `confirm_proposal`。

| 工具 | 参数 | 说明 |
| --- | --- | --- |
| `create_strategy` | 必填 `name`、`market`（`US`/`HK`）、`risk_config`；可选 `symbols[]`、`finviz_url`、`system_prompt`、`description`、`market_data`、`analysis_interval`、`allow_overnight`、`close_before_minutes`、`tag_name` | 新建策略。`symbols` 与 `finviz_url` **至少填一个** |
| `update_strategy` | `strategy_id` + `updates{}` | 只填要改的字段，白名单见下 |
| `archive_strategy` | `strategy_id` | **仅【已暂停】的策略可归档** |
| `unarchive_strategy` | `strategy_id` | 解除后回到暂停状态 |
| `confirm_proposal` | `proposal_id` + `decision?`（`confirm` 默认 / `reject`） | 幂等，同一 id 重复调只执行一次 |

### 硬约束

- **新建策略一律以「暂停」状态创建、初始资金固定 100000、AI 供应商留空**，这三项调用方指定不了，建完要去 UI 或用 `update_strategy` 补 `ai_provider_id` 再启动。
- **本系统不提供删除策略的能力**，最多只能归档，数据保留。
- **未配置任何 K 线的策略无法被启动。**
- 归档中的策略拒绝修改，要先 `unarchive_strategy`。
- 草案 **15 分钟过期**；期间策略若被别处（比如 UI）改动，`confirm_proposal` 会返回 `stale`，需要重新读取现状再重新发起提案。

### `update_strategy` 的字段白名单

可改：`name`、`description`、`system_prompt`、`symbols`、`finviz_url`、`analysis_interval`、`allow_overnight`、`close_before_minutes`、`risk_config`、`market_data`、`tag_name`、`ai_provider_id`、`status`（只能 `active` / `paused`，用于启停）。

**禁止且无法**改动：一切资金字段、分享链接、归档状态。

`market_data` 是**整体替换，不做深合并**——只想改一个指标也得把整个结构完整传一遍，否则没传的部分会丢。

### `market_data` 结构

这是写工具里唯一复杂的参数，决定 AI 分析时能拿到哪些数据：

```json
{
  "klines": [
    { "period": "1d", "count": 200,
      "indicators": { "sma": [20,50,200], "ema": [12,26], "rsi": [14],
                      "atr": null, "macd": null, "kdj": null } }
  ],
  "realtime": { "enabled": true, "change_pct": true, "volume": true, "high_low": true },
  "include_market_context": true,
  "include_news": true,
  "fundamentals": false
}
```

- `period` 可选 `1m`/`5m`/`15m`/`30m`/`1h`/`1d`/`1w`/`1M`，`count` 为拉取根数（1~1000）
- `indicators` 各项填参数数组或 `null`（关闭）；`macd` 填 `{fast,slow,signal}`，`kdj` 填 `{period,k_smooth,d_smooth}`，`amv` 填 `{half_life}`（**仅日线生效**）
- 不传 `market_data` 时默认「日线 200 根 + SMA/EMA/RSI」
- 工具描述自带的经验之谈：**数据维度多不等于决策好，分钟线易诱发过度交易，低频策略建议只配日线**。这与下文实测「配了 15m/1h 的策略当天零决策」互相印证

> `preview_finviz_screener` 的描述里提到的 `propose_strategy_update` 是服务端遗留的旧名字，实际工具叫 `update_strategy`。

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

### 风控参数同时是 LLM 的"软参考"和引擎的硬触发

AI 请求原文里逐条标注成软参考：

```
- 止损（软参考）: 50% — 浮亏接近此值时综合趋势/动能/位置判断,
  不要因单日波动伪触发就提前 close;高 Beta(>1.5) 标的可参考 ATR(14)/价格 放宽幅度
- 止盈（软）: 50% — 浮盈达此值时考虑落袋，结合行情判断
- 当日熔断线（软）: ≤-50% — 触及此线时停止 open/buy/加仓，仅允许 hold/sell/close
```

> **2026-08-14 更正。** 本节此前写「所以 `stop_loss_pct` 不会机械平仓，只是提示词里的一句建议，硬止损可能只在网格引擎等非 AI 路径上生效」——**这个结论是错的**，它只看到了 AI 请求里的措辞，没看到引擎侧。
>
> 两次实测证明引擎会机械执行：8/04 赌狗 AXTI 浮亏 −8.85% 触发 `system:hard-stop-loss`（该策略 `stop_loss_pct: 8`）；8/13 均值回归 COHR 浮亏 −5.39% 触发 `system:hard-stop-loss`（`stop_loss_pct: 5`）。

正确的理解是**两个作用面并存**：这些字段既以「软参考」的措辞进入 AI 请求让 LLM 参考，**也被引擎当硬触发机械执行**。

所以把 `stop_loss_pct` 设成 50 的效果不是「关掉了硬止损」，而是「把触发线设到了实际到不了的位置」。对网格与 `open_only` 策略这是有意为之；对需要止损的策略要设成真实可达的值。

引擎侧还有另外两个同类的自动触发，`model` 字段可以区分来源：`system:trailing-stop`（移动止盈，由 `trailing_profit_activation_pct` 与 `trailing_profit_lock_drawdown_pct` 控制）、`system:rebalance`（二阶段再平衡改写）。完整的七段流程与各段的控制旋钮见 `strategy-pipeline.md`。

### AI 请求里实际包含什么

`风控参数` / `当前持仓` / `当前时间`（含距收盘分钟数、报价快照时延）/ `即将到来的关键事件`（FOMC、CPI 等，带影响级别与天数）/ `当前账户状态`（现金占比与调仓建议）/ 每个标的的实时行情 + 各周期 K 线 + 技术指标 / `相关新闻`（近 30 天，带发布与采集时间、影响、情感、中文摘要）。

`prompt_version` 字段标明模板版本，实测为 `v6`。

### 平台的 K 线数据完整可用

同一次请求里 XPEV 的 1d / 1w / 1M 都是真实完整数据：30 根 K 线、20 根支撑 12.32 阻力 14.46、周线 20 根 -25.21%、月线支撑 11.14 阻力 28.23，指标齐全。

而 MCP 的 `get_symbol_kline` 查同一个 `XPEV.US` 只返回 1 根合成 bar。**两条数据管道不同源，不要在提示词里写"本标的历史数据不可靠"之类的话去误导 AI 忽略好数据。**

### 已确认：`market_data` 里配置 1h 周期会导致策略完全不运行

2026-07-29 有四个策略全天零决策，7/30 用对照实验定位到了原因。**元凶是 1h，不是分钟级**：

| 策略 | K 线配置 | 7/29 决策 | 7/30 决策 |
| --- | --- | --- | --- |
| 价格行为日内 | **保留 15m，删掉 1h** | 0 | **186** |
| DRAM 网格 | 15m 和 1h 都删掉 | 0 | 13 |
| 主题动量赌狗 | 从建立起只配 1d + 1w | — | 23 |
| 标普500动量 | 删掉 1h，剩 1d/1w/1M | 0 | **仍为 0** |

价格行为策略是关键证据：它**保留了 15m**、只删掉 1h，决策数从 0 涨到 186。所以分钟级本身没问题。

**规则：不要在 `market_data.klines` 里配置 `1h`。** 已知可用的周期有 `15m`、`1d`、`1w`、`1M`。

注意标普500动量删掉 1h 后仍然零决策，说明它另有原因。它的候选池是正常的（finviz 命中 21 只，缓存有刷新），与能正常运行的策略相比有两处独有差异：`include_positions` 为 true，以及市场数据请求体最重（21 只标的 × 3 周期 × 30 根 × 全套指标）。怀疑是请求体过大，待验证。

### 调度频率远低于配置值

XPEV 的 `analysis_interval` 是 30 分钟，6.5 小时的交易时段本应运行约 13 次，实际只有 2 次（09:32 与 13:30 美东）。原因不明，**不要假设策略会严格按 `analysis_interval` 执行**。

### 真实交易成本

基于 2026-07-30 的 50 笔成交样本还原：

| 项 | 公式 / 实测值 | 验证 |
| --- | --- | --- |
| 买入佣金 | **max($0.35, 股数 × $0.0035)** | AMZN 买 86 股：86×0.0035=0.30 低于下限，实收 0.35；PLTR 买 164 股：0.574，实收 0.57 |
| 卖出费用 | 同上佣金 **+ 约 0.00278% 证监会规费** | XPEV 卖 4,966 股 @12.7536：佣金 17.38 + 规费 1.76 = 19.14，实收 19.28 |
| 滑点 | 市价单曾出现 **+0.55%**（分析报价 13.005，成交 13.0765，间隔约 2.5 分钟） | |
| 订单类型 | 一律 `market` | |

**存在每笔 $0.35 的最低收费**——早前根据单笔大额样本得出的"按股计费、无固定部分"是错的。但下限很低，按 0.35 反推，每格名义金额低于约 100 美元时固定费才开始显著侵蚀收益，因此**"每格名义不低于 1,000 美元""网格资金下限 22,000 美元"这两条结论作废**。成本从来不是网格的瓶颈，下单粒度才是（见下一节）。

### 下单粒度：AI 策略接口做不了网格

`intensity` 只有 `light` / `medium` / `heavy` 三档，实测**最小档单笔成交就在 1,100 股以上、约 14,700 美元**（XPEV 案例，`max_position_pct` 30、总资金 10 万）。

XPEV 网格 7/30 一天六笔，始终无法收敛到目标位：

```
10:00 卖 4,966  6,882 → 1,916
10:30 卖 1,150  1,916 →   766
11:34 买 1,530    766 → 2,296
13:01 卖 1,149  2,296 → 1,147
14:01 买 1,133  1,147 → 2,280
15:33 卖 1,144  2,280 → 1,136   （收盘价对应的目标是 1,600）
```

网格设计的单格步长是 120 股约 1,570 美元，**引擎最小成交粒度比格距大了约 9 倍**，只能在目标位两侧反复跨越。DRAM 同样：网格表目标 120 股，首笔买了 516 股，超 4.3 倍。

**结论：用 AI 策略接口模拟网格不可行**，且这不是提示词能解决的问题。要么等平台的网格引擎，要么把格距放大到与成交粒度同量级——但那时已经不算网格了。

同一机制也让**定投无法实现**：长持 VOO 的提示词写明"使用 light 强度、多次小额买入"，实际一次就买到了 `max_position_pct` 20% 的上限（29 股、19,618 美元），之后再也买不进。

**推论：`max_position_pct` 是唯一能真正控制单策略敞口的字段**，提示词里的任何数量表述都无效。

### UI 编辑的两个陷阱

**一、UI 的保存成功提示不可信，必须用 `get_strategy_profile` 回读核对。** 实测有一整轮 4 个策略的编辑，界面全程没有报错、每步都显示保存成功，但接口读出来一项都没生效。改完立刻回读是唯一可靠的验证方式。

**二、止盈标签页的回显是假象。** 切到「固定止盈」标签页保存后，`trailing_profit_activation_pct` 与 `trailing_profit_lock_drawdown_pct` 会从 `risk_config` 里**彻底消失**，即移动止盈真的被禁用了。但重新打开编辑页时，止盈区域默认停在「移动止盈」标签并显示 8 / 5，看起来像是没保存上。**以接口返回为准，不要以 UI 回显为准**——这个假象曾导致误判两次，一次以为失败其实成功，一次以为成功其实失败。

`analysis_interval` 实测可以保存 15 和 30，没有发现区间限制；此前观察到的数值漂移是编辑过程本身造成的，不是平台归一化。

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

## 当前账户状态（2026-07-30 快照）

6 个策略，全部 `market=US`：

| 策略 | id | 状态 | 标签 |
| --- | --- | --- | --- |
| 标普500均值回归动量成长策略 | `cc66fb26-025f-4086-b301-e5092a7c0676` | active | 动量 |
| 价格行为日内策略 | `b2ec2383-543a-48c1-9f67-74a5fab74569` | active | 日内 |
| DRAM 网格策略 | `c3225965-e786-4a93-8ead-e091d82ed68b` | active | 网格 |
| XPEV 底仓+网格策略 | `87be32af-c040-4327-b928-6a5c96126b6d` | active | 网格 |
| 长持标普 500 | `f9f1d84d-6552-470f-9074-36363e1f3559` | active | 长持 |
| 美股动量轮动 | `85f67f09-6682-4a1b-8af5-55fe51086620` | paused | 动量 |

成交历史仍然很短（最早的策略 2026-04 建立，实际出单从 2026-07-29 才开始），`list_transactions` / `list_decisions` / `get_daily_snapshots` 的样本量还不足以校准回测假设。本地回测暂时仍用自己假设的费率和滑点，并在结论里注明。

平台上的「网格策略」是用 AI 策略接口配的，不是平台自带网格引擎；网格引擎相关的配置字段（分时段滑点、必亏配置警告等）没有 MCP 工具可读取，只能参照 UI。

## 调用注意事项

- 调用前先用 `GetMcpTools` 确认 schema，工具集会随平台版本变化；**如果清单看起来比接入页少，先按「工具清单刷新」处理，别在旧清单上瞎猜**。
- 所有 `strategy_ids` 必填的工具都接受多个 ID，能合并就合并，别循环单个调。
- 日期范围类工具的默认窗口都不长（决策 30 天、消息 7 天、快照 365 天），要长历史必须显式传 `date_from`。
- `get_decision_detail` 和 `include_ai_text=true` 的返回很占 token，按需调用。
- 写工具永远是两步：先拿 `proposal_id` 和 diff 给用户看，得到同意再 `confirm_proposal`。改完仍然建议用 `get_strategy_profile` 回读核对。
