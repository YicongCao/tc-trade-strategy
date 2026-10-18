# 市场情报数据层

本层覆盖事件预期、跨资产风险、板块轮动、AI 预期差和交易主题。Trade Copilot 以下简称 **tc**。
行情、预测概率、新闻观点、ETF 申赎和公司财报分别保存，分析时通过日期与标的关联。

## 已接通的采集

安装项目后运行 `market-intelligence`，或者使用模块入口：

```bash
.venv/bin/python -m pip install -e '.[dev]'
.venv/bin/python -m tc_trade_strategy.intelligence --as-of 2026-10-16
```

默认输出为带 UTC 时间的 `results/intelligence/<抓取时间>/`，包括 `snapshot.json`、原始响应、请求 URL 和抓取时间。
所有产物被 git 忽略。`--output-dir` 可以指定目录，重复使用同一目录会覆盖该目录的同名产物。
不安装定时任务、不调用交易工具。部分数据源失败会写入 `errors` 并继续获取其余数据。
行情、宏观数据或 Polymarket 合约列表整项缺失时退出码为 1；个别标的或可选源失败时仍可产生部分报告。

`--as-of` 只控制价格和宏观数据的观测日期，不代表历史时点可获得的信息：Polymarket 始终是抓取时的活跃市场；FRED/GPR 可能包含事后修订。研究回测需要另行保存发布版本和首次可见时间。

### 事件预测：Polymarket

- [官方 Gamma 搜索接口](https://docs.polymarket.com/api-reference/search/search-markets-events-and-profiles)：公开只读，无需密钥。
- 已配置 18 个搜索词，覆盖美联储、通胀、衰退、关税、政府停摆、科技、半导体、软件、金融、工业、航天、油气。
- 每词默认最多两页；响应的 `truncated` 表示仍有结果未取。关键词是发现入口，不能据此认定每个结果都属于美股或相关板块。
- 保存问题、事件、Yes 价格、价差、流动性、24 小时成交额、1 日/1 周概率变化、截止时间、结算规则和来源。
- 排除已关闭、已归档、已过期和无有效 Yes 概率的合约。
- 第一版质量筛选要求：流动性至少 $10,000、24 小时成交额至少 $1,000、价差不超过 5 个百分点、元数据 24 小时内更新且接受订单。该门槛未经预测准确率校准；流动性金额也不等于可执行盘口深度。
- 价格是交易者对明确结算条件的定价，不是客观事件概率。不要把嵌套阈值概率相加、把多项相关事件当成独立证据，或把未加息误读成降息。
- 财报、GPU 租金、ISM 等细分合约常很薄，必须同时展示质量标记。人工审阅后才能加入生产信号白名单。
- 利率基准交叉验证用 [CME FedWatch](https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html)。官方 [FedWatch API](https://www.cmegroup.com/market-data/market-data-api/fedwatch-api.html) 提供授权服务，本轮未订阅、未接入。

### 风险与情绪指标

- **黄金**：GLD 为可交易 ETF 代理；GC=F 为黄金期货连续报价，单位美元/盎司。
- **原油**：CL=F、BZ=F 为 WTI/Brent 近月连续报价，单位美元/桶。需要长期总收益指数时应另接有明确换月规则的指数，不能把连续价格回报当成含展期成本的投资回报。
- **恐慌**：[Cboe VIX 官方日线](https://www.cboe.com/tradable-products/vix/vix-historical-data)；Yahoo 补 VIX3M、VVIX、MOVE。VIX 为隐含波动，不是下跌概率。
- **避险/信用**：GLD、TLT、UUP、HYG、LQD；[FRED](https://fred.stlouisfed.org/) 的 DGS10、DFII10、T10YIE、BAMLH0A0HYM2、BAMLC0A0CM、STLFSI4。FRED 的利差数值 3.23 表示 3.23 个百分点，即 323bp。
- **恐惧与贪婪**：[CNN 美股 Fear & Greed](https://www.cnn.com/markets/fear-and-greed) 是待补源。`--include-cnn` 可尝试一次公共前端接口；2026-10-18 实测返回 HTTP 418。它不是官方稳定 API，失败保留为空，不以加密货币指数或 tc 温度替代。
- **地缘/战争**：[Caldara–Iacoviello GPR](https://www.matteoiacoviello.com/gpr.htm) 官方 Stata 数据，包括总指数、行动、威胁、7 日和 30 日均值。引用 Caldara and Iacoviello (2022), “Measuring Geopolitical Risk”, AER，并标明下载日期。新闻覆盖风险不是实际战损或战争发生概率；最新值可能滞后和修订。
- 将 GPR、海峡通航事件概率、油价及信用利差并列展示。不存在本项目已接入的统一“官方战争影响指数”或“官方避险指数”；自建综合分必须先规定权重、标准化样本、缺失值处理并检验样本外效果。

### 板块轮动与资金

采集 11 个一级板块 ETF，以及 SMH、IGV、XOP、OIH、ITA、ARKX、KRE、SKYY，提供 1/5/20/60 个交易观测的收益、相对 SPY 超额收益、量比和 63 日高点回撤。相对收益必须使用完全相同的起止日期。

三类证据不可互换：

1. **价格/成交量**：判断相对强弱和交易活跃度；tc 的 `turnover` 也是成交额，不能命名为净流入。
2. **ETF 净申赎**：发行人份额变化 × NAV（需处理份额拆分）、或授权的 ETF.com/其他基金流数据库。核对窗口，排查 heartbeat 等技术性申赎。本轮只人工核对了 [ETF.com 周报](https://www.etf.com/sections/weekly-etf-flows/etf-inflows-top-41b-investors-pile-brazil-long-bonds)，未完成自动全板块资金流接入。
3. **机构持仓**：[SEC 13F](https://www.sec.gov/rules-regulations/staff-guidance/division-investment-management-frequently-asked-questions/frequently-asked-questions-about-form-13f) 按季度且有披露滞后，只能验证持仓变化；缺少即时、完整的多空敞口。单笔大单和期权成交也可能是对冲，不能自动认定为方向性主力。

### AI 泡沫：结算阈值与预警阈值

Polymarket 的 [AI bubble burst](https://polymarket.com/event/ai-bubble-burst-by) 合约有非常严格的专门定义：在截止日之前同一个 90 天窗口内，六类事件至少发生三类。
规则包括 NVDA 较历史高点跌 50%、SOXX 跌 40%、OpenAI 或 Anthropic 破产、OpenAI 被收购、指定 SiliconData H100 租金不高于 $1 持续五天、指定主要供应商之一较历史高点跌 50%。原始规则以每个合约保存的 `description` 为准。
这种合约的低概率不能推导为“AI 股票很安全”，也不能代替普通 20% 回撤概率。63 日回撤不是该规则中的历史最高点回撤。

本项目尚未训练“破裂概率”模型。建议先采用下列**待回测的观察门槛**，不自动交易、不输出伪精确概率：

- 市场压力：SMH 20 日相对 SPY 落后至少 10 个百分点；或 SMH 跌破 200 日均线且较 63 日高点回撤至少 20%。
- 信用压力：美国高收益债 OAS 20 个观测扩大至少 100bp，或绝对水平达到 500bp；这是广义市场压力，不能代替 AI 公司自身债券/CDS。
- 融资成本：10 年实际利率 20 个观测上升至少 50bp。
- 盈利兑现：至少两家主要云厂商的 AI/云增长指引下修，同时资本开支未同步降低；或连续两季资本开支增长快于经营现金流，且自由现金流率下滑。需读公司财报、租赁承诺、债务到期和现金流，不能用新闻数代替。
- 算力经济性：[SiliconData GPU 租金](https://www.silicondata.com/products/silicon-index)、GPU 利用率、融资与折旧成本；要区分 H100/B200 等代际替代和需求崩塌，监控租金与单位算力成本的差额。

若要估计“市场还能容忍多差的业绩”，应另做反向 DCF：以估值、折现率、利润率和资本开支路径反推出隐含增长，再比较实际指引。缺少可靠一致预期和现金流数据时，不给出统一估值阈值。

### 当前交易主题

每个主题保存：主题名 → 因果假设 → 受益/受损篮子 → 原始证据 → 反证 → 下一催化剂 → 失效条件。
价格证据、新闻观点和企业正式披露分别标记。重复转载按原始事件去重；只看最近标题频率容易把同一条消息误判为多重确认。

tc 提供已采集消息、AI 摘要、板块与宏观缓存；本地补公开市场数据及官方资料。当前工具调用结果可另存 `tc-overview.json`、`tc-news-high-impact.json`，采集器不读取或复制 tc OAuth 凭证。

## 下一步接入顺序

先积累每日快照和审阅后的 Polymarket 合约白名单，再补 ETF 净申赎历史、公司财报/一致预期、GPU 租金与公司信用数据。需要授权的数据源保持明确缺口；不在缺少观测时填零，也不把主观风险分展示成概率。
