# tc 市场数据接入

沿用当前 Codex 已授权的 Trade Copilot MCP，无需另建服务或申请模型 API Key。配置中的令牌留在本机，不写仓库。2026-10-18 已实际读取下列市场数据接口。

| 只读工具 | 用途与边界 |
| --- | --- |
| get_trading_calendar | US 交易日；full/half，覆盖前45日至后35日；非交易日不出现 |
| get_market_overview | 最新概览缓存，约每小时刷新；updated_at 不是每条报价时间；不支持历史概览 |
| get_symbol_quotes | 单批最多20标的；内部格式 SPY.US；ts 为供应商毫秒时间戳；本次休市返回抓取时刻，成交时间未核验，不能视为新成交 |
| get_symbol_kline | 历史价格抽查；以当前 schema 的周期和数量上限为准；不使用未完成日线 |
| list_news_for_period | Twitter/Truth Social 线索；最多50条，分日/主题补查；不是公告/研报/财经新闻全集 |

tc 接入仍禁止账户/持仓/交易记录及所有平台写工具。关联私人附录通过单独的 ibkr-position-review 只读浏览器流程获取已授权持仓，不调用tc账户接口。实际工具 schema 优先于文档；若不可见先核对 Codex MCP 连接状态并重连现有授权，不把其他编辑器配置复制为 Codex API。

其他公开源：Polymarket Gamma（无需 Key）、Yahoo 复权日线、FRED CSV、Cboe、GPR、SEC submissions/companyfacts 与公司 IR。CNN 恐贪不可访问时留空；有价值的付费源仅建议，不订阅。

现有 MCP 授权与用户配置没有迁移到仓库。完整旧平台文档归档为 `archive/legacy-strategy/dependencies/trade-copilot-mcp.md`，不属于当前可调用范围。
