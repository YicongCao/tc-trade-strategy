# 市场研究数据来源

| 层 | 来源 | 注意事项 |
| --- | --- | --- |
| 市场状态 | tc 报价/概览/交易日历，Yahoo 日线 | 时戳缺失拒绝称实时；仅完整日线参与历史收益 |
| 事件预期 | Polymarket Gamma public-search + event ID | 规则指纹一致才比较；价格为合约定价，非客观概率 |
| 宏观风险 | FRED、Cboe、GPR、Yahoo | 观测时滞/修订/连续期货换月单列 |
| 情绪 | CNN Fear & Greed | 无法核验则缺失，无替代冒充 |
| ETF | 19ETF同端点价格量能；发行人份额/NAV；公开流量报告 | 申赎、量价、滞后持仓三层分开；拆分处理后仍只能估算 |
| 财务 | SEC submissions/companyfacts + 最新公司 IR | 财年、filed、累计转单季、TTM；融资租赁和优先股单独核验 |
| 新闻 | tc 社交线索 + 政府/公司/公开财经原文 | 事件/发布/抓取三个时间；事件去重，标查询上限 |

采集器 `intelligence.py` 可单独使用；日常研究经 `research prepare`，由真实交易日历决定截止日。原始响应和全文留在 results，不入库。

[SEC 官方 API 说明](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) · [Polymarket 搜索 API](https://docs.polymarket.com/api-reference/search/search-markets-events-and-profiles) · [GPR 方法与数据](https://www.matteoiacoviello.com/gpr.htm)

方法见统一技能的 `references/methodology.md`；输入契约见 [data-contract.md](../docs/data-contract.md)。
