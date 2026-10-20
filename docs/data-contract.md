# 数据契约 v1

所有 JSON 使用 UTF-8；金额与百分比必须保留单位，时间用带时区 ISO8601。最终 `evidence.json` 是报告唯一数据源；不要直接编辑生成的 HTML 或 Markdown。

## tc 输入（本地、忽略入库）

```json
{"retrieved_at":"2026-10-18T03:45:12Z","calendar":{"range":{"from":"2026-09-01","to":"2026-11-15"},"trading_days":[{"trade_date":"2026-10-16","session_type":"full"}]},"overview":{},"quotes":[{"quotes":[{"symbol":"SPY.US","last":763.25,"change_pct":-1.1,"ts":1792295112031}]}],"news":{"count":50,"has_more":true}}
```

示例日历仅说明结构；实际需连续覆盖研究窗口、截止日和下一交易日。原始 tc 工具返回若有 content/structuredContent 包装，取实际 JSON payload，不能把包装对象放 calendar。每批 quote 最多20个，ts 单位毫秒；overview 的缓存时间不是报价时间。休市时晚于最近交易日的 ts 标为 unverified_trade_timestamp，observed_at 留空，另存 provider_timestamp。

## Codex 研究输入 analysis.json

必填键：`summary`、`themes`、`risk_analysis`、`rotation_analysis`、`ai_analysis`、`trade_scenarios`、`comparison_analysis`、`catalysts`、`news`、`sources`、`gaps`、`paid_sources`、`flows`、`event_reviews`。可空数组意味着该域缺少证据，需 gaps 解释。可选 `fear_greed` 为经核验的 CNN 数值、观测时间、来源说明，否则报告明确缺失。

- themes：对象含 title、status（新增/强化/减弱/失效/首次基线/待核验）、event、reaction、interpretation、beneficiaries、adverse、counterevidence、next_catalyst、sources。
- trade_scenarios：title、catalyst、symbols、confirmation、invalidation、horizon、counterevidence、status。horizon 是观察期限，不是保证持仓期。
- event_reviews：以 snapshot 合约 id 为键，每项包含相同 rule_hash 和人工 `resolution_summary`。只发布已核验的重点合约，完整搜索覆盖统计保留；摘要不要复制整个结算条款。
- flows：symbol、value_million、start、end、quality（issuer_verified/public_report/estimate）、source；发行人优先，公开报告需保留窗口。
- news：event_key、summary（简短自行归纳）、event_at、published_at、retrieved_at、source。event_at/published_at 未知为 null；同事件多个来源合并保存。
- sources：url、checked_at、note；可补 observed_at/published_at。来源应支持相邻关键判断，不用搜索页链接代替原始来源。
- comparison_analysis：复核前期剧本，说明哪些条件已触发/未触发/无法核验。首次基线明确无上期；不从当天数据重造“上周预测”。
- polymarket_watch：weekly/daily 构建必填，realtime可选。含非空 search_summary（搜索主题/词、检查时点、失败/截断及空栏目原因），以及 risk_signals、reference_events、upcoming_events 三个数组。每项仅含 market_id、reason、transmission、confirmation、invalidation、event_at、event_time_source；引用本次 event_reviews 已核验且已采集的合约，不另手填概率。事件时间与官方来源未知时均为null，时间已过不能留在 upcoming_events。报告三栏使用同一 events 对象生成概率、规则、质量和跨期比较。没有合格合约保留空栏目并说明，不伪造信号。
- catalysts：带时间和来源的已确认事件，未知日期注明未定；daily 盘后、weekly 周末增量单列。
- paid_sources：产品、补足缺口、官方链接、checked_at；没有实际增益可留空。

## 决策指标扩展

新增构建必填 `indicator_assessments`，非空数组，每项 question、evidence_ids（指标ID数组）、interpretation、counterevidence、confirmation、invalidation、horizon、guidance、confidence（low/medium/high）、change_reason 均需填写。引用需存在且质量可用。它记录判断依据、反证与结论变化摘要。

可选 `indicator_observations` 为外部指标数组，每项仅含 id、value（有限数值）、unit、source、observed_at、retrieved_at、quality（ok/stale/lagged/unverified）、definition、universe、session（completed/intraday/premarket/afterhours）。时间带时区，观测≤抓取≤截止；ID不得重复。definition记录统计窗口、成分/覆盖率和口径版本。不可得写 gaps，不造数。

最终对象增加 indicators、indicator_assessments、indicator_comparisons，三种输出同源。固定ID如 `prices.SPY.sma20`、`macro.DGS2.value`；每项保留数值、单位、来源、观测/抓取时点、质量、定义、交易阶段。旧报告不补写新字段。

`sensitive/market-indicators/` 是忽略入Git的公开指标本地副本，保留原生成/截止时点及 recorded_at，同内容导入幂等。公共报告只读 reports，绝不从此目录取材。历史比较是同定义、来源、单位、阶段的不同日期观测之差，非连续交易日收益；percent指标之差解释为百分点。

## 财务底稿

`financials.json` 按五家公司 symbol 索引，包含 symbol、status、fiscal_period、filing_date、sources、observations、accounting_policy、disclosure_check。观测值与 `scenarios` 分离。未核验输入 status=unavailable 并填 reason。

`disclosure_check`：checked_at、status=verified/unavailable、source、latest_filing_date；“verified”表示本次核验最新披露列表，而非仅打开一份旧财报。每24小时重新检查；最新披露日期与底稿不同则拒绝估值。无法验证最新列表时保留 unavailable。

已核验底稿还需要：base.revenue（基期年/TTM收入，百万美元）、base.net_debt（含融资租赁、优先权益调整后的净债务，百万美元）、base.diluted_shares（百万股）；可选 base.non_operating_assets（经税项和流动性调整后额外非经营资产，百万美元，不与现金重复）。

三情景键为 bear/base/bull；各项 growth、start_margin、operating_margin、tax_rate、da_ratio、capex_ratio、working_capital_ratio、wacc、terminal_growth、dilution 均为小数。终值第六年以稳定增长率计算营运资本增量；不要延续高速增长期再投资增量。资本开支包括融资租赁资产新增，租赁本金不再重复扣除。

最终对象另含：schema_version、window、generated_at、focus、quality、prices、quotes、macro、events、valuations、comparisons、previous_version、coverage、methodology、gaps。观察值保留 source / observation_date或observed_at / retrieved_at / quality。原始接口响应、新闻全文、账户字段、凭证与缓存禁止入库。

## 关联输出与Daily时段

公共证据可有 delivery_slot（最近已到的北京时间07:15或20:00，带时区ISO时间），定时日报按它而非单一交易日判断是否已发布。旧报告无该字段不回写。私人附录独立写入敏感目录，持仓及其数量、金额、建议不得进入公共证据；字段与失败输入见 ibkr-position-review/references/linked-review.md。关联为私人→公共目录+hash，不生成公共→私人链接。


## 公共采集恢复契约

`prepare` 返回 snapshot 与 gaps 路径；`gaps --mode ... --tc ... --snapshot ...` 可重查。
缺口包含 id、reason、core、requirement、alternatives、impact。宏观超过7天（STLFSI4为14天）仅是补查提示，非统一发布频率判断；请求错误正文留在本地。缺口并非全部研究工作清单。

`build --supplements results/RUN/supplements.json`：顶层严格为 `snapshot_digest`（gaps输出的原快照SHA256）与 `items` 数组。每项严格包含：

|字段|含义|
|---|---|
|gap_id / target|缺口ID / 标的或序列、事件ID|
|kind|price_history、macro_series、polymarket_event 或 evidence|
|source|不含查询参数/凭证的公开HTTPS来源页|
|observed_at / retrieved_at|实际观测/采集时间，必须含时区|
|published_at|发布时间，未知为null|
|method|web、browser、tc_mcp、public_api|
|unit / definition|单位与明确口径；价格复权定义作为比较基线|
|data|下述类型之一|

price_history：`[{"date":"2026-10-16","Close":100,"High":102,"Low":99,"Volume":1000}]`。High/Low/Volume可省略，相关指标为null。日期唯一升序、最后日为窗口收盘日；已知交易日历范围内不能漏日/混入休市日；更早历史须人工核验完整性。仅支持既有标的与对应单位。不能混合不同来源历史，调整后价格需一致复权。数值与已有同日值或复权定义冲突拒绝覆盖。相对收益仅在同口径且端点齐全时重算。

macro_series：`[{"date":"2026-10-16","value":4.2}]`，只支持既有FRED/Cboe/GPR序列及原单位，Python计算变化。polymarket_event：Gamma事件结构（id/slug/title/markets，每个market包含原结算条件与报价字段）；经现有normalize_market过滤和生成rule_hash，已有market ID不覆盖；最终仍须event_reviews核验。完整补查输入仅在results中保存，公开报告不含合约原始description。

evidence：自行撰写的简短事实字符串；只记录context_only，不能替代可计算数据。新闻、外部指标、财务底稿仍写入已有分析契约。发布时间未知不得猜测。禁止账户资料、密钥、完整新闻正文。

合并不改变原快照，报告 acquisition 同源记录 accepted/context_only/rejected/conflict 及remaining缺口；原始错误保留，不能将context_only视为数值恢复。抓取距截止超过6小时、未来取证、错误单位、历史缺日、重复目标均拒绝。无法核验核心市场状态时仍停止。结构校验不能证明网页真实性，Codex必须保留事实、判断依据、反证与条件式建议。

备用当前报价可在独立的规范化输入包中使用相同 quote 字段，并显式提供公开 `source` URL；不得覆盖原始 tc 包。已确认服务端时间并非成交时间的报价设置 `trade_timestamp_verified: false`，不能满足当前行情门槛。备用报价 ts 必须取实际成交/分钟行情时间，不能取请求时间。

## Agent 阅读摘要

新研究在分析输入中提供 `agent_brief`：`verdict`（当前判断）、`changes`（相对上次的实质变化）、`signals`（1–3条信号）、`watch`（1–3条下一步观察与条件）、`caveat`（关键限制）。由执行研究的 agent 基于本次证据综合撰写，建议300–500中文字，硬上限900字符；不调用额外模型服务，不用机械截断正文冒充摘要。与正文同源保存；不增加正文没有的事实或更强的确定性。旧报告无此字段时显示原 summary，不虚构摘要。HTML 首屏展示摘要，其余章节默认折叠，搜索/分类可展开详情。

私人 HTML 使用仓位条形图、逐标的条件卡片和折叠证据；Markdown 保留可读列表。图只读取显式 `positions[].weight_pct`（占净值百分比），不从不同步账户值重算、不推断现金、不将市值比例称为杠杆敞口；缺失值不画，负值标色，不强行归一化。原始 JSON 仅保留独立证据文件。重排旧快照时保留 observed_at/public_cutoff，不能称为新持仓查询。
