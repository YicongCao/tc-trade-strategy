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
