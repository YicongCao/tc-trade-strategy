# Trade Copilot MCP 工具参考

> 最后核对：2026-07-30 · 服务器 ID `user-trade-copilot` · 状态 `ready`（已通过 OAuth 认证）
> 当前连接可见 **23 个功能工具 + 1 个认证工具**，其中 **18 个只读 + 5 个可写**。

## 关键结论（先看这个）

1. **写工具走两段式提案。** `create_strategy` / `update_strategy` / `archive_strategy` / `unarchive_strategy` 都只生成草案，返回 `proposal_id` 与字段级 diff，**必须把 diff 展示给用户并取得同意后**再调 `confirm_proposal` 才落库。草案 15 分钟过期，期间若策略被别处改动会返回 `stale`。详见「写工具」一节。
2. **工具清单只在配置指纹变化时才刷新。** 换新对话没用、重新 OAuth 也没用——踩过两次，排查过程和唯一有效的刷新办法见「工具清单刷新」一节。
3. **手机上用这套工具走 Cursor Cloud Agent。** 云端请求从 Cursor 服务器发出、不带本地 IP，绕开了大陆 IP 的前沿模型过滤，且笔记本关机也能跑。授权服务器支持动态客户端注册，接入不需要平台侧配合。见「从云端 / 手机接入」。
4. **MCP 不能当回测数据源。** K 线一次只能查一个标的、最多 120 根、且不开放分钟级；实时行情一次最多 20 个标的。这个量级只够做归因和抽查，撑不起参数网格搜索。本仓库的回测数据必须另找来源。
5. **MCP 的行情缺口不代表平台的缺口。** `get_symbol_kline` 对 `DRAM` 返回旧主体历史、对中概 ADR 与 ETF 只返回 1 根，但**平台喂给 AI 策略的 K 线是完整正确的**——见下文"策略引擎的真实行为"。两条数据管道是分开的，不要用 MCP 的缺陷推断平台的缺陷。
6. **MCP 的真正价值在"对标口径"和"实盘校准"**：`list_transactions` 有真实手续费和已实现盈亏，`get_decision_detail` 能看到 LLM 的完整输入输出，`get_retro_overview` + `list_retro_cases` 有决策的事后价格路径与超额收益。这些是校准本地假设最可靠的输入。
7. **字段口径要抄平台的**，这样本地策略能平移回站内。见文末"平台字段口径"。

## 工具清单刷新

服务端更新工具后，Cursor 侧的清单会长期停在旧版本。这个坑踩过两次，2026-07-30 排查清楚了。

### 现象

平台的 MCP 接入页写着 23 个工具，而 `GetMcpTools` 只返回 17 个，且两边是**错位**的：客户端有个服务端已经删掉的 `list_signal_performance`，缺了服务端新增的 `get_retro_overview` / `list_retro_cases` 和 5 个写工具。

调用 `list_signal_performance`，服务端回 `Unknown tool: list_signal_performance`——客户端在请求一个不存在的工具，证明它拿的是旧快照。

### 无效的办法（都试过）

- **开新对话**：无效。工具清单跟对话无关，一个全新对话看到的还是同一份旧清单。
- **重新 OAuth**：无效。完整走一遍清凭证 + 浏览器授权 + 拿新 token，清单纹丝不动。
- **调 `mcp_auth`**：无效，同上。
- 顺带排除：不是权限问题（接入页「允许 MCP 写操作」开关是开启状态，页面小字的"当前默认关闭"说的是默认值不是当前值）；不是端点问题（只有 `https://tc.zkd.me/api/mcp` 一个端点，没有只读版与完整版之分）。

### 清单存在哪

不在磁盘上。`state.vscdb` 里跟本服务器相关的键只有 OAuth 凭证（`mcpOAuth.secret.*` / `mcpOAuth.global.*`），没有任何 tool schema；`storage.json` 里也搜不到工具名。所以清单是每次建连时从服务端 `tools/list` 拿的，然后**由 MCP 宿主进程按配置指纹在内存里长期持有**。

日志里能看到这个指纹：

```
[McpProxyFetch] Built VS Code proxy-aware MCP fetch for
user-trade-copilot::mcpScope:profile:ZGVmYXVsdA:cfg:NTQ3MmVmZTA
```

末尾的 `cfg:<hash>` 是 `~/.cursor/mcp.json` 里该服务器配置块的哈希。**只要哈希不变，无论连接断开重连多少次、token 换几茬，进程都复用同一份清单。**

### 有效的办法：改配置指纹

给 `~/.cursor/mcp.json` 的服务器配置块加一个无害字段，让哈希变掉：

```json
{
  "mcpServers": {
    "trade-copilot": {
      "url": "https://tc.zkd.me/api/mcp",
      "headers": {}
    }
  }
}
```

保存后 Cursor 立刻重连并重新拉取 `tools/list`。**代价是本地凭证会被一并清掉**（日志：`MCP OAuth credentials cleared (local housekeeping)`），连接进入 `needsAuth`，调一次 `mcp_auth` 重新授权即可，几秒钟。

保留服务器名不变很重要——OAuth token 是按 `[<server-id>::mcpScope:profile:<profile>]` 存的，改名会连带丢掉更多状态。下次再要刷新，把 `"headers": {}` 删掉（或改成别的无害字段）即可，哈希变了就会重拉。

### 诊断方法

两种"工具不存在"的报错要分清，它们指向完全不同的问题：

| 报错 | 来源 | 含义 |
| --- | --- | --- |
| `Unknown tool: xxx` | 服务端 | 客户端清单过期，请求了服务端已删除的工具 |
| `Tool user-trade-copilot-xxx was not found. Use GetMcpTools to...` | 客户端 | 该工具不在客户端清单里，请求**根本没发出去** |

后者意味着**没法绕过清单去调服务端新增的工具**，客户端是硬闸门，只能先刷新清单。

## 从云端 / 手机接入

本地桌面端不是唯一入口。把这个 MCP 挂到 Cursor Cloud Agent 上，就能在手机上跑同一套工具，笔记本合盖也不影响。

### 为什么云端这条路对国内用户更顺

Cursor 桌面端会按**你的本地 IP** 做模型过滤：从大陆 IP 连过去，Claude / GPT / Gemini 会被服务端从模型列表里隐藏，只剩 Composer、Grok、Kimi、GLM，要恢复得开 TUN 模式全局代理（只配 HTTP 代理不行，3.8+ 拉模型列表的进程走独立 HTTP/2 栈，不吃代理设置）。

**Cloud Agent 和网页端的请求从 Cursor 自己的服务器发出，不带你的本地 IP，地区过滤不生效。** 所以走云端这条路，前沿模型全都能用，而且不需要梯子。

### 配置

在 [cursor.com/agents](https://cursor.com/agents) 的 MCP 下拉里添加个人 MCP server，选 **HTTP** 传输：

```
https://tc.zkd.me/api/mcp
```

注意 Cloud Agent **不支持 SSE 和 `mcp-remote`**，只支持 HTTP 与 stdio。本服务器是 Streamable HTTP，正好匹配。

选 HTTP 而不是 stdio 还有个安全收益：HTTP 的服务器配置**永远不进 agent 的 VM**，agent 拿不到 refresh token 和请求头，工具调用由 Cursor 后端代理转发。stdio 则是在 VM 里起进程，agent 能读到全部环境变量。

### OAuth 不需要平台侧配合

已核实（2026-07-30）：

- 受保护资源声明的授权服务器是 **Supabase Auth**，从 `https://tc.zkd.me/.well-known/oauth-protected-resource` 可读到
- 该授权服务器的元数据里**有 `registration_endpoint`**，即支持动态客户端注册（DCR）
- `token_endpoint_auth_methods_supported` 含 `none`，`code_challenge_methods_supported` 含 `S256`，公共客户端 + PKCE 可用

**结论：Cursor 能自助注册 OAuth 客户端，不需要平台运营方把 Cursor 的回调地址加白名单。** 添加完 server 点一次授权就能用。

万一将来平台改成固定客户端、要求白名单，需要登记的回调地址是：

```
https://www.cursor.com/agents/mcp/oauth/callback   ← 网页与 Cloud Agent
http://localhost:8787/callback                      ← 桌面端
```

两个都要登记，因为桌面和云端各走各的。届时在 `mcp.json` 里用 `auth` 对象填 `CLIENT_ID` / `CLIENT_SECRET` / `scopes`。

OAuth 授权是**按用户**的，团队级共享的 server 也一样，每个人得自己授权一次。

### 云端的工具清单会不会也卡在旧快照

**未验证。** 本地那个坑的根因是 MCP 宿主进程按 `~/.cursor/mcp.json` 的配置指纹在内存里长期持有清单，而云端配置存在 Cursor 后端（加密存储，`headers` 与 `CLIENT_SECRET` 保存后不可回读），是另一套实现，不能直接套结论。

**接入后先做一次核对**：让 Cloud Agent 调 `GetMcpTools` 数一下工具数量。应该是 **23 个功能工具 + 1 个 `mcp_auth`**，并且能看到 `create_strategy` / `update_strategy` / `archive_strategy` / `unarchive_strategy` / `confirm_proposal` 和 `get_retro_overview` / `list_retro_cases`。若数量偏少或出现 `list_signal_performance`，说明云端同样有缓存问题。

云端没有「改配置指纹」这个旋钮，对应的做法是**在 MCP 下拉里把 server 删掉重加**。

排查时还可以用内置的 Cursor Cloud MCP：`get-events` 会返回本次运行的事件，其中 `mcp_auth_error` 表示 MCP 认证失败、该 server 的工具被跳过而运行继续——这种情况下 agent 会表现得像"没有这些工具"，但根因是认证不是清单。

### 别忘了

- Cloud Agent 目前要绑一个仓库才能起，用本仓库即可，顺带让 agent 拿到 `strategies/` 下的策略设计与本文档
- Android 没有原生 app，在 Chrome 打开 cursor.com/agents 点 Install App 装 PWA；iOS 有原生应用
- 个人版与商业版账号在 Cursor 侧是独立实体，用另一个邮箱注册即可，互不干扰。注意**企业版不受地区模型限制，个人 Pro 受**，所以个人版的桌面端体验会比商业版差，但云端这条路不受影响
- `tc.zkd.me` 在 Cloudflare 后面，日志里见过 502 origin_bad_gateway。手机上依赖它时，工具调用失败先看是不是源站抖动，不要误判成配置问题

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

### 复盘（两步走）

旧版的 `list_signal_performance` 已被服务端删除，拆成了下面两个工具。**必须先 overview 选方向，再拉 cases**。

| 工具 | 参数 | 返回要点 |
| --- | --- | --- |
| `get_retro_overview` | `strategy_ids[]`（必填）、`date_from?`/`date_to?` | 按「决策类型 × 执行状态」的分层画像：样本数、平均/中位收益、超额收益、实际盈亏、各类问题标签计数 |
| `list_retro_cases` | `strategy_ids[]`（必填）、`date_from?`/`date_to?`、`decision?`（open/buy/sell/close）、`symbol?`、`flag?`、`execution_status?`（默认 filled，可选 skipped/any）、`sort?`（默认 `worst_excess`）、`limit?`（上限 100） | 具体案例：当时的 `summary` 理由 + 事后 d1/d3/d5 价格路径与窗口高低价 + 基准同期收益 + 实际成交与已实现盈亏 + 问题标签 |

`execution_status` 的口径是这里最容易算错的地方：**`filled` 才是真实成交的决策，`skipped` 是被再平衡毙掉的信号**（仅抽样评估，用来衡量过滤质量）。两者混算得到的是"AI 嘴上说买的能力"，不是策略赚钱能力。

`flag` 问题标签取值：

| 值 | 判定 |
| --- | --- |
| `sold_before_run_up` | 卖出后 5 日内最高价超卖价 5%（卖飞） |
| `stopped_at_bottom` | 卖出后几乎没再跌却收更高（割在地板） |
| `bought_the_top` | 买入后最高价没超买价 1%（买在山顶） |
| `underwater_exit` | 实际亏损离场 |
| `not_executed` | 未成交 |
| `corp_action` | 窗口内有拆股，收益失真 |

`list_retro_cases` 不给"对/错"判定，要自己结合当时的理由归因——**止盈平仓后继续上涨并不等于判断错误**，得看当时的理由说的是什么。`high_5d` / `low_5d` 用来区分"卖飞"和"躲过暴跌后反弹"。

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

成交历史仍然很短（最早的策略 2026-04 建立，实际出单从 2026-07-29 才开始），`list_transactions` / `get_retro_overview` / `get_daily_snapshots` 的样本量还不足以校准回测假设。本地回测暂时仍用自己假设的费率和滑点，并在结论里注明。

平台上的「网格策略」是用 AI 策略接口配的，不是平台自带网格引擎；网格引擎相关的配置字段（分时段滑点、必亏配置警告等）没有 MCP 工具可读取，只能参照 UI。

## 调用注意事项

- 调用前先用 `GetMcpTools` 确认 schema，工具集会随平台版本变化；**如果清单看起来比接入页少，先按「工具清单刷新」处理，别在旧清单上瞎猜**。
- 所有 `strategy_ids` 必填的工具都接受多个 ID，能合并就合并，别循环单个调。
- 日期范围类工具的默认窗口都不长（决策 30 天、消息 7 天、快照 365 天），要长历史必须显式传 `date_from`。
- `get_decision_detail` 和 `include_ai_text=true` 的返回很占 token，按需调用。
- 写工具永远是两步：先拿 `proposal_id` 和 diff 给用户看，得到同意再 `confirm_proposal`。改完仍然建议用 `get_strategy_profile` 回读核对。
