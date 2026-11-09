# 每日交易总结 · 2026-11-06

## 一分钟读懂 · Agent 摘要

### 当前判断

恐慌有所降温，当前是宽基改善、芯片分化的盘前修复，仍未确认趋势反转。今晚北京时间22:30开盘，明晚CPI将检验反弹能否延续。

### 与上次相比

相对早报，已有真实盘前价格：SPY/QQQ上涨而SMH偏弱、NVDA显著下跌；油价回落，CNN从22升至25。NVIDIA韩国合作是经营利好，但不能抵消治理调查的不确定性。

### 最重要的信号

- 约20:01北京：SPY+0.62%、QQQ+0.49%、SMH-0.30%、NVDA-5.15%，市场并未把整个AI板块同等抛售。
- WTI88.10、Brent94.79，较供应商前收分别约跌3.01%和3.59%；VIX23.38低于周五25.64，但缺少同刻三个月VIX。
- 周五19个ETF仅7个上涨，等权与收盘承接偏弱；今天尚无完整现货广度，不能由期货上涨认定反转。

### 接下来观察

- 开盘后先看SPY734.58、QQQ654附近承接，再看742.21/664.52突破回踩和收盘保持；等权与更多行业须跟随。
- NVDA已在盘前跌破185.22旧低点，半导体确认门槛提高；观察SMH456.44与周五高点476.25，避免只凭低价抢反弹。
- 明晚21:30 CPI、今晚RKLB盘后、随后CoreWeave/Nebius业绩：同时看指引、融资与现金回收。

### 不要忽略

盘前成交与常规时段分开；当前广度、净申赎、同步信用数据和四家完整估值缺失。预测合约不是客观概率，情景价也不是目标价。

## 研究结论

11月9日晚间：油价与波动回落、宽基盘前修复，但NVDA治理风险压制半导体；等待开盘承接与明晚CPI，尚不确认趋势反转。

## 时点与口径

| 项目 | 内容 |
| --- | --- |
| 模式 | 每日交易总结 |
| 常规交易窗口 | 2026-11-06 → 2026-11-06（纽约交易日） |
| 截止·纽约 | 2026-11-09T07:07:32.565388-05:00 |
| 截止·北京 | 2026-11-09T20:07:32.565388+08:00 |
| 实际生成时间 | 2026-11-09T12:07:32.980942+00:00 |
| 市场阶段 | 盘前 |
| 下一交易日 | 2026-11-09 |
| 运行重点 | 全市场 |
| 上一版本 | reports/daily/2026-11-06/20261108T232226.117273Z/evidence.json |
| 质量 | partial |
| Daily 北京时间计划时段 | 2026-11-09T20:00:00+08:00 |

## 采集、补查与剩余缺口

| 目标 | 补查结果 | 来源 | 观测 / 抓取时间 | 说明 |
| --- | --- | --- | --- | --- |
| 1219847 | 已校验接入 | https://gamma-api.polymarket.com/events/1219847 | 2026-11-09T12:01:01.689393+00:00 / 2026-11-09T12:01:01.689393+00:00 | Gamma observation, not last trade; each contract and rule retained |
| 1147445 | 已校验接入 | https://gamma-api.polymarket.com/events/1147445 | 2026-11-09T12:01:01.581187+00:00 / 2026-11-09T12:01:01.581187+00:00 | Gamma observation, not last trade; each contract and rule retained |
| 549019 | 已校验接入 | https://gamma-api.polymarket.com/events/549019 | 2026-11-09T12:01:04.307019+00:00 / 2026-11-09T12:01:04.307019+00:00 | Gamma observation, not last trade; each contract and rule retained |
| 652109 | 已校验接入 | https://gamma-api.polymarket.com/events/652109 | 2026-11-09T12:01:04.938061+00:00 / 2026-11-09T12:01:04.938061+00:00 | Gamma observation, not last trade; each contract and rule retained |
| 1103684 | 已校验接入 | https://gamma-api.polymarket.com/events/1103684 | 2026-11-09T12:01:05.595244+00:00 / 2026-11-09T12:01:05.595244+00:00 | Gamma observation, not last trade; each contract and rule retained |
| 1189688 | 冲突，保留原值 | 缺失 |  /  | 已有合约不可静默覆盖；重新采集统一时点快照 |
| 1308738 | 已校验接入 | https://gamma-api.polymarket.com/events/1308738 | 2026-11-09T12:02:55.253363+00:00 / 2026-11-09T12:02:55.253363+00:00 | Gamma observation, not last trade; each contract and rule retained |
| 1343940 | 冲突，保留原值 | 缺失 |  /  | 已有合约不可静默覆盖；重新采集统一时点快照 |
| 1262853 | 已校验接入 | https://gamma-api.polymarket.com/events/1262853 | 2026-11-09T12:01:08.527141+00:00 / 2026-11-09T12:01:08.527141+00:00 | Gamma observation, not last trade; each contract and rule retained |

## 仍需核验的数据与影响

| 数据 | 状态 | 需要核验 | 影响 |
| --- | --- | --- | --- |
| history.DRAM | insufficient_history | 连续完整交易日 OHLC；SMA200 至少200条，ATR14至少15条 | 降低相关判断可信度；保留缺口 |
| polymarket.query.AI bubble | truncated | 按主题或事件ID补查；不能声称全市场覆盖 | 降低相关判断可信度；保留缺口 |
| polymarket.query.AI spending | truncated | 按主题或事件ID补查；不能声称全市场覆盖 | 降低相关判断可信度；保留缺口 |
| polymarket.query.CPI | truncated | 按主题或事件ID补查；不能声称全市场覆盖 | 降低相关判断可信度；保留缺口 |
| polymarket.query.Fed rate | truncated | 按主题或事件ID补查；不能声称全市场覆盖 | 降低相关判断可信度；保留缺口 |
| polymarket.query.Hormuz | truncated | 按主题或事件ID补查；不能声称全市场覆盖 | 降低相关判断可信度；保留缺口 |
| polymarket.query.Iran | truncated | 按主题或事件ID补查；不能声称全市场覆盖 | 降低相关判断可信度；保留缺口 |
| polymarket.query.Microsoft | truncated | 按主题或事件ID补查；不能声称全市场覆盖 | 降低相关判断可信度；保留缺口 |
| polymarket.query.Nvidia | truncated | 按主题或事件ID补查；不能声称全市场覆盖 | 降低相关判断可信度；保留缺口 |
| polymarket.query.SpaceX | truncated | 按主题或事件ID补查；不能声称全市场覆盖 | 降低相关判断可信度；保留缺口 |
| polymarket.query.bank | truncated | 按主题或事件ID补查；不能声称全市场覆盖 | 降低相关判断可信度；保留缺口 |
| polymarket.query.ceasefire | truncated | 按主题或事件ID补查；不能声称全市场覆盖 | 降低相关判断可信度；保留缺口 |
| polymarket.query.inflation | truncated | 按主题或事件ID补查；不能声称全市场覆盖 | 降低相关判断可信度；保留缺口 |
| cnn | missing | 核验 CNN Fear & Greed 原值及更新时间 | 降低相关判断可信度；保留缺口 |
| news | truncated | 按事件/时间分批核验新闻线索 | 降低相关判断可信度；保留缺口 |
| request.38906ddc2d63 | request_failed | 核验该来源失败影响，见本地原始错误 | 降低相关判断可信度；保留缺口 |

## 决策指标：趋势、相对强弱、波动与宏观

| ID | 数值 | 单位 | 观测日/时间 | 质量 | 定义 | 来源 |
| --- | --- | --- | --- | --- | --- | --- |
| prices.SPY.value | 735.29 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_1d_pct | 0.31 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_5d_pct | -2.70 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_20d_pct | -5.56 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_60d_pct | -5.24 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_1d_pp | 0.00 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_5d_pp | 0.00 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_20d_pp | 0.00 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_60d_pp | 0.00 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma20 | 763.36 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma50 | 765.15 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma200 | 727.65 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma20_pct | -3.68 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma50_pct | -3.90 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma200_pct | 1.05 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_sma | 11.12 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_pct | 1.51 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.drawdown_from_63d_high_pct | -5.62 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.volume_vs_previous20_ratio | 1.30 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SPY/history/ |
| prices.QQQ.value | 656.10 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_1d_pct | 1.40 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_5d_pct | -4.98 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_20d_pct | -12.67 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_60d_pct | -10.28 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_1d_pp | 1.09 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_5d_pp | -2.28 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_20d_pp | -7.11 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_60d_pp | -5.04 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma20 | 707.64 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma50 | 720.75 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma200 | 679.79 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma20_pct | -7.28 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma50_pct | -8.97 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma200_pct | -3.49 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_sma | 16.61 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_pct | 2.53 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.drawdown_from_63d_high_pct | -13.63 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.volume_vs_previous20_ratio | 1.50 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.IWM.value | 273.67 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_1d_pct | 0.99 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_5d_pct | -2.03 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_20d_pct | -1.89 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_60d_pct | -9.59 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_1d_pp | 0.68 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_5d_pp | 0.68 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_20d_pp | 3.67 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_60d_pp | -4.35 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma20 | 276.84 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma50 | 281.94 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma200 | 278.02 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma20_pct | -1.15 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma50_pct | -2.93 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma200_pct | -1.57 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_sma | 4.73 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_pct | 1.73 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.drawdown_from_63d_high_pct | -10.06 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.volume_vs_previous20_ratio | 1.02 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IWM/history/ |
| prices.RSP.value | 216.05 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_1d_pct | -0.38 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_5d_pct | -1.04 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_20d_pct | 1.41 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_60d_pct | -2.63 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_1d_pp | -0.69 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_5d_pp | 1.67 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_20d_pp | 6.97 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_60d_pp | 2.61 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma20 | 216.72 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma50 | 214.54 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma200 | 207.09 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma20_pct | -0.31 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma50_pct | 0.70 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma200_pct | 4.33 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_sma | 2.75 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_pct | 1.27 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.drawdown_from_63d_high_pct | -3.26 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.volume_vs_previous20_ratio | 1.29 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/RSP/history/ |
| prices.GLD.value | 372.52 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_1d_pct | -0.79 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_5d_pct | 4.71 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_20d_pct | -3.14 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_60d_pct | -6.63 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_1d_pp | -1.10 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_5d_pp | 7.41 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_20d_pp | 2.42 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_60d_pp | -1.39 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma20 | 372.79 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma50 | 384.96 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma200 | 411.24 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma20_pct | -0.07 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma50_pct | -3.23 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma200_pct | -9.42 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_sma | 6.68 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_pct | 1.79 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.drawdown_from_63d_high_pct | -12.98 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.volume_vs_previous20_ratio | 0.84 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GC=F.value | 4,074.90 | USD_per_troy_ounce | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_1d_pct | -0.94 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_5d_pct | 4.51 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_20d_pct | -3.35 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_60d_pct | -7.82 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_1d_pp | -1.25 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_5d_pp | 7.22 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_20d_pp | 2.21 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_60d_pp | -2.58 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma20 | 4,080.71 | USD_per_troy_ounce | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma50 | 4,230.42 | USD_per_troy_ounce | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma200 | 4,501.50 | USD_per_troy_ounce | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma20_pct | -0.14 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma50_pct | -3.68 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma200_pct | -9.48 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_sma | 84.98 | USD_per_troy_ounce | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_pct | 2.09 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.drawdown_from_63d_high_pct | -13.26 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.volume_vs_previous20_ratio | 1.32 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.CL=F.value | 90.83 | USD_per_barrel | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_1d_pct | 0.34 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_5d_pct | -12.76 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_20d_pct | -1.11 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_60d_pct | 11.79 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_1d_pp | 0.03 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_5d_pp | -10.06 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_20d_pp | 4.45 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_60d_pp | 17.03 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma20 | 98.01 | USD_per_barrel | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma50 | 95.47 | USD_per_barrel | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma200 | 87.16 | USD_per_barrel | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma20_pct | -7.33 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma50_pct | -4.86 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma200_pct | 4.21 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_sma | 5.12 | USD_per_barrel | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_pct | 5.64 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.drawdown_from_63d_high_pct | -14.17 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.volume_vs_previous20_ratio | 1.19 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.BZ=F.value | 98.32 | USD_per_barrel | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_1d_pct | 0.03 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_5d_pct | -16.42 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_20d_pct | -6.11 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_60d_pct | 12.92 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_1d_pp | -0.28 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_5d_pp | -13.72 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_20d_pp | -0.55 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_60d_pp | 18.16 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma20 | 108.42 | USD_per_barrel | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma50 | 104.20 | USD_per_barrel | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma200 | 93.34 | USD_per_barrel | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma20_pct | -9.31 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma50_pct | -5.65 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma200_pct | 5.33 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_sma | 5.56 | USD_per_barrel | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_pct | 5.65 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.drawdown_from_63d_high_pct | -16.42 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.volume_vs_previous20_ratio | 1.41 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.TLT.value | 81.92 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_1d_pct | -0.01 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_5d_pct | 0.10 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_20d_pct | 5.05 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_60d_pct | -0.03 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_1d_pp | -0.32 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_5d_pp | 2.80 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_20d_pp | 10.61 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_60d_pp | 5.21 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma20 | 80.72 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma50 | 80.22 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma200 | 83.15 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma20_pct | 1.49 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma50_pct | 2.12 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma200_pct | -1.48 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_sma | 0.77 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_pct | 0.94 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.drawdown_from_63d_high_pct | -1.08 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.volume_vs_previous20_ratio | 1.01 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/TLT/history/ |
| prices.UUP.value | 29.13 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_1d_pct | 0.73 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_5d_pct | 0.45 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_20d_pct | 0.38 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_60d_pct | 3.37 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_1d_pp | 0.41 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_5d_pp | 3.15 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_20d_pp | 5.94 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_60d_pp | 8.61 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma20 | 29.00 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma50 | 28.69 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma200 | 27.97 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma20_pct | 0.44 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma50_pct | 1.54 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma200_pct | 4.16 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_sma | 0.11 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_pct | 0.38 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.drawdown_from_63d_high_pct | 0.00 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.volume_vs_previous20_ratio | 1.23 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/UUP/history/ |
| prices.HYG.value | 77.23 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_1d_pct | -0.06 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_5d_pct | -0.26 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_20d_pct | 0.00 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_60d_pct | -2.24 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_1d_pp | -0.38 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_5d_pp | 2.45 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_20d_pp | 5.56 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_60d_pp | 3.00 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma20 | 77.16 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma50 | 77.63 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma200 | 77.88 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma20_pct | 0.09 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma50_pct | -0.51 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma200_pct | -0.84 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_sma | 0.33 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_pct | 0.42 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.drawdown_from_63d_high_pct | -2.40 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.volume_vs_previous20_ratio | 0.60 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/HYG/history/ |
| prices.LQD.value | 104.53 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_1d_pct | -0.12 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_5d_pct | 0.25 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_20d_pct | 2.07 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_60d_pct | -1.06 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_1d_pp | -0.44 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_5d_pp | 2.95 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_20d_pp | 7.63 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_60d_pp | 4.18 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma20 | 103.71 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma50 | 103.63 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma200 | 105.78 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma20_pct | 0.79 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma50_pct | 0.86 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma200_pct | -1.18 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_sma | 0.59 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_pct | 0.57 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.drawdown_from_63d_high_pct | -1.35 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.volume_vs_previous20_ratio | 0.81 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/LQD/history/ |
| prices.^VIX.value | 25.64 | index | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_1d_pct | -9.01 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_5d_pct | 32.03 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_20d_pct | 72.78 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_60d_pct | 79.93 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_1d_pp | -9.33 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_5d_pp | 34.73 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_20d_pp | 78.34 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_60d_pp | 84.98 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma20 | 18.83 | index | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma50 | 16.92 | index | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma200 | 18.40 | index | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma20_pct | 36.18 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma50_pct | 51.52 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma200_pct | 39.38 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_sma | 3.36 | index | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_pct | 13.11 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.drawdown_from_63d_high_pct | -9.01 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-06 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX3M.value | 24.60 | index | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_1d_pct | -3.72 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_5d_pct | 18.38 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_20d_pct | 38.44 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_60d_pct | 32.19 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_1d_pp | -4.03 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_5d_pp | 21.09 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_20d_pp | 43.99 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_60d_pp | 37.43 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma20 | 20.11 | index | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma50 | 19.00 | index | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma200 | 20.58 | index | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma20_pct | 22.30 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma50_pct | 29.50 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma200_pct | 19.53 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_sma | 1.87 | index | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_pct | 7.60 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.drawdown_from_63d_high_pct | -3.72 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-06 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VVIX.value | 121.94 | index | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_1d_pct | -9.67 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_5d_pct | 14.57 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_20d_pct | 43.66 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_60d_pct | 36.37 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_1d_pp | -9.98 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_5d_pp | 17.28 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_20d_pp | 49.22 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_60d_pp | 41.61 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma20 | 102.58 | index | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma50 | 94.33 | index | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma200 | 99.04 | index | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma20_pct | 18.87 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma50_pct | 29.26 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma200_pct | 23.12 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_sma | 13.92 | index | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_pct | 11.42 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.drawdown_from_63d_high_pct | -9.67 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-06 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^MOVE.value | 92.77 | index | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_1d_pct | -5.26 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_5d_pct | -7.42 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_20d_pct | -7.87 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_60d_pct | 28.69 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_1d_pp | -5.57 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_5d_pp | -4.71 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_20d_pp | -2.88 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_60d_pp | 33.27 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma20 | 99.23 | index | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma50 | 92.81 | index | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma200 | 78.47 | index | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma20_pct | -6.51 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma50_pct | -0.05 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma200_pct | 18.22 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_sma | 5.06 | index | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_pct | 5.45 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.drawdown_from_63d_high_pct | -18.34 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-06 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.NVDA.value | 186.64 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_1d_pct | 2.78 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_5d_pct | -8.80 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_20d_pct | -18.60 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_60d_pct | -17.07 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_1d_pp | 2.46 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_5d_pp | -6.09 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_20d_pp | -13.04 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_60d_pp | -11.83 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma20 | 211.55 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma50 | 219.77 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma200 | 204.39 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma20_pct | -11.77 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma50_pct | -15.08 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma200_pct | -8.68 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_sma | 8.02 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_pct | 4.30 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.drawdown_from_63d_high_pct | -21.99 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.volume_vs_previous20_ratio | 1.59 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.MSFT.value | 530.61 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_1d_pct | -0.99 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_5d_pct | 1.67 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_20d_pct | -0.83 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_60d_pct | 6.99 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_1d_pp | -1.31 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_5d_pp | 4.37 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_20d_pp | 4.73 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_60d_pp | 12.23 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma20 | 531.41 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma50 | 516.65 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma200 | 438.85 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma20_pct | -0.15 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma50_pct | 2.70 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma200_pct | 20.91 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_sma | 15.88 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_pct | 2.99 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.drawdown_from_63d_high_pct | -4.53 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.volume_vs_previous20_ratio | 1.07 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.AMZN.value | 259.30 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_1d_pct | -0.35 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_5d_pct | 7.88 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_20d_pct | -1.19 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_60d_pct | -2.20 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_1d_pp | -0.66 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_5d_pp | 10.59 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_20d_pp | 4.37 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_60d_pp | 3.04 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma20 | 254.28 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma50 | 253.95 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma200 | 243.94 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma20_pct | 1.97 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma50_pct | 2.11 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma200_pct | 6.30 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_sma | 9.76 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_pct | 3.77 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.drawdown_from_63d_high_pct | -4.76 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.volume_vs_previous20_ratio | 0.88 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.GOOGL.value | 284.78 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_1d_pct | 0.78 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_5d_pct | 1.77 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_20d_pct | -19.02 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_60d_pct | -17.73 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_1d_pp | 0.47 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_5d_pp | 4.47 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_20d_pp | -13.46 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_60d_pp | -12.49 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma20 | 317.44 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma50 | 332.91 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma200 | 339.22 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma20_pct | -10.29 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma50_pct | -14.46 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma200_pct | -16.05 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_sma | 11.30 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_pct | 3.97 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.drawdown_from_63d_high_pct | -19.77 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.volume_vs_previous20_ratio | 0.96 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.META.value | 610.15 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_1d_pct | 0.84 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_5d_pct | -0.79 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_20d_pct | -15.10 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_60d_pct | 2.63 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_1d_pp | 0.53 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_5d_pp | 1.92 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_20d_pp | -9.54 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_60d_pp | 7.87 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma20 | 662.67 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma50 | 674.77 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma200 | 631.15 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma20_pct | -7.93 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma50_pct | -9.58 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma200_pct | -3.33 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_sma | 23.83 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_pct | 3.91 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.drawdown_from_63d_high_pct | -21.53 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.volume_vs_previous20_ratio | 0.63 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/META/history/ |
| prices.CRWV.value | 46.40 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_1d_pct | 6.28 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_5d_pct | -15.44 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_20d_pct | -43.47 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_60d_pct | -56.35 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_1d_pp | 5.96 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_5d_pp | -12.73 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_20d_pp | -37.91 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_60d_pp | -51.11 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma20 | 59.33 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma50 | 75.56 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma200 | 90.17 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma20_pct | -21.79 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma50_pct | -38.59 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma200_pct | -48.54 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_sma | 5.67 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_pct | 12.22 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.drawdown_from_63d_high_pct | -56.93 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.volume_vs_previous20_ratio | 0.89 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.MU.value | 690.00 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_1d_pct | 5.12 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_5d_pct | -22.01 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_20d_pct | -32.93 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_60d_pct | -27.34 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_1d_pp | 4.81 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_5d_pp | -19.31 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_20d_pp | -27.38 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_60d_pp | -22.10 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma20 | 878.99 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma50 | 961.53 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma200 | 756.53 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma20_pct | -21.50 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma50_pct | -28.24 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma200_pct | -8.79 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_sma | 58.85 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_pct | 8.53 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.drawdown_from_63d_high_pct | -37.11 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.volume_vs_previous20_ratio | 1.53 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MU/history/ |
| prices.DRAM.value | 39.29 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_1d_pct | 6.16 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_5d_pct | -18.16 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_20d_pct | -31.30 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_60d_pct | -30.99 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_1d_pp | 5.85 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_5d_pp | -15.46 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_20d_pp | -25.74 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_60d_pp | -25.74 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma20 | 47.98 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma50 | 54.65 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma200 | 缺失 | USD_per_share | 2026-11-06 | unavailable | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma20_pct | -18.11 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma50_pct | -28.10 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma200_pct | 缺失 | percent | 2026-11-06 | unavailable | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_sma | 3.25 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_pct | 8.26 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.drawdown_from_63d_high_pct | -38.24 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.volume_vs_previous20_ratio | 1.42 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.VRT.value | 182.86 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_1d_pct | 3.47 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_5d_pct | -21.35 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_20d_pct | -24.68 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_60d_pct | -36.29 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_1d_pp | 3.16 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_5d_pp | -18.65 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_20d_pp | -19.12 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_60d_pp | -31.05 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma20 | 214.37 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma50 | 236.98 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma200 | 271.13 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma20_pct | -14.70 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma50_pct | -22.84 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma200_pct | -32.56 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_sma | 18.81 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_pct | 10.29 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.drawdown_from_63d_high_pct | -37.75 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.volume_vs_previous20_ratio | 1.15 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/VRT/history/ |
| prices.XLK.value | 164.74 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_1d_pct | 1.45 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_5d_pct | -8.23 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_20d_pct | -17.12 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_60d_pct | -13.54 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_1d_pp | 1.14 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_5d_pp | -5.52 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_20d_pp | -11.57 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_60d_pp | -8.30 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma20 | 183.53 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma50 | 188.38 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma200 | 169.91 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma20_pct | -10.24 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma50_pct | -12.55 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma200_pct | -3.04 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_sma | 5.53 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_pct | 3.36 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.drawdown_from_63d_high_pct | -18.45 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.volume_vs_previous20_ratio | 1.75 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLE.value | 61.62 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_1d_pct | -0.02 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_5d_pct | -12.00 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_20d_pct | -5.32 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_60d_pct | 1.52 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_1d_pp | -0.33 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_5d_pp | -9.29 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_20d_pp | 0.24 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_60d_pp | 6.76 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma20 | 67.11 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma50 | 64.96 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma200 | 58.58 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma20_pct | -8.18 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma50_pct | -5.14 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma200_pct | 5.20 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_sma | 1.84 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_pct | 2.98 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.drawdown_from_63d_high_pct | -12.00 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.volume_vs_previous20_ratio | 1.16 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLF.value | 57.16 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_1d_pct | -0.59 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_5d_pct | 1.15 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_20d_pct | 4.44 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_60d_pct | -1.54 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_1d_pp | -0.90 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_5d_pp | 3.85 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_20d_pp | 10.00 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_60d_pp | 3.70 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma20 | 56.23 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma50 | 55.85 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma200 | 53.52 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma20_pct | 1.65 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma50_pct | 2.34 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma200_pct | 6.80 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_sma | 1.00 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_pct | 1.74 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.drawdown_from_63d_high_pct | -3.45 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.volume_vs_previous20_ratio | 0.97 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLI.value | 162.67 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_1d_pct | 0.12 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_5d_pct | -2.83 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_20d_pct | -3.89 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_60d_pct | -12.21 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_1d_pp | -0.19 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_5d_pp | -0.12 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_20d_pp | 1.67 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_60d_pp | -6.97 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma20 | 167.51 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma50 | 169.33 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma200 | 172.65 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma20_pct | -2.89 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma50_pct | -3.93 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma200_pct | -5.78 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_sma | 3.21 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_pct | 1.97 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.drawdown_from_63d_high_pct | -12.55 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.volume_vs_previous20_ratio | 0.92 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLV.value | 184.80 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_1d_pct | -0.06 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_5d_pct | -0.04 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_20d_pct | 8.19 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_60d_pct | 10.17 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_1d_pp | -0.37 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_5d_pp | 2.67 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_20d_pp | 13.75 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_60d_pp | 15.41 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma20 | 179.98 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma50 | 173.19 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma200 | 158.43 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma20_pct | 2.68 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma50_pct | 6.71 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma200_pct | 16.64 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_sma | 3.79 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_pct | 2.05 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.drawdown_from_63d_high_pct | -2.56 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.volume_vs_previous20_ratio | 1.37 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLP.value | 90.08 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_1d_pct | -1.28 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_5d_pct | 0.74 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_20d_pct | 7.97 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_60d_pct | 5.43 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_1d_pp | -1.59 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_5d_pp | 3.44 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_20d_pp | 13.53 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_60d_pp | 10.67 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma20 | 88.09 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma50 | 84.88 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma200 | 83.82 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma20_pct | 2.25 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma50_pct | 6.13 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma200_pct | 7.46 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_sma | 1.78 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_pct | 1.98 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.drawdown_from_63d_high_pct | -2.02 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.volume_vs_previous20_ratio | 1.35 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLY.value | 117.58 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_1d_pct | -0.05 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_5d_pct | 1.91 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_20d_pct | 4.19 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_60d_pct | -0.52 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_1d_pp | -0.36 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_5d_pp | 4.61 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_20d_pp | 9.75 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_60d_pp | 4.72 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma20 | 115.26 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma50 | 113.28 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma200 | 115.10 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma20_pct | 2.01 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma50_pct | 3.80 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma200_pct | 2.15 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_sma | 2.46 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_pct | 2.09 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.drawdown_from_63d_high_pct | -3.88 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.volume_vs_previous20_ratio | 1.21 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLC.value | 104.79 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_1d_pct | 0.43 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_5d_pct | 4.89 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_20d_pct | -5.06 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_60d_pct | -6.59 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_1d_pp | 0.12 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_5d_pp | 7.60 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_20d_pp | 0.49 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_60d_pp | -1.35 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma20 | 106.35 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma50 | 109.70 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma200 | 112.07 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma20_pct | -1.47 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma50_pct | -4.47 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma200_pct | -6.50 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_sma | 2.16 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_pct | 2.07 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.drawdown_from_63d_high_pct | -8.68 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.volume_vs_previous20_ratio | 0.84 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLU.value | 43.13 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_1d_pct | -0.39 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_5d_pct | -0.69 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_20d_pct | 4.15 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_60d_pct | -1.35 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_1d_pp | -0.71 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_5d_pp | 2.01 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_20d_pp | 9.71 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_60d_pp | 3.89 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma20 | 42.57 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma50 | 41.68 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma200 | 43.83 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma20_pct | 1.32 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma50_pct | 3.48 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma200_pct | -1.60 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_sma | 0.62 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_pct | 1.44 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.drawdown_from_63d_high_pct | -1.95 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.volume_vs_previous20_ratio | 1.00 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLRE.value | 44.00 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_1d_pct | -0.68 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_5d_pct | 1.92 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_20d_pct | 5.74 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_60d_pct | -1.66 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_1d_pp | -0.99 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_5d_pp | 4.63 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_20d_pp | 11.30 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_60d_pp | 3.58 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma20 | 42.75 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma50 | 42.45 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma200 | 42.86 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma20_pct | 2.93 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma50_pct | 3.66 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma200_pct | 2.66 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_sma | 0.75 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_pct | 1.70 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.drawdown_from_63d_high_pct | -2.48 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.volume_vs_previous20_ratio | 1.03 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLB.value | 51.95 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_1d_pct | -0.73 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_5d_pct | -1.50 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_20d_pct | 5.10 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_60d_pct | -0.23 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_1d_pp | -1.04 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_5d_pp | 1.21 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_20d_pp | 10.66 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_60d_pp | 5.01 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma20 | 51.58 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma50 | 50.86 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma200 | 50.84 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma20_pct | 0.72 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma50_pct | 2.15 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma200_pct | 2.18 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_sma | 0.96 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_pct | 1.85 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.drawdown_from_63d_high_pct | -3.62 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.volume_vs_previous20_ratio | 1.30 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLB/history/ |
| prices.SMH.value | 463.96 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_1d_pct | 3.62 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_5d_pct | -11.20 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_20d_pct | -23.10 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_60d_pct | -21.25 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_1d_pp | 3.31 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_5d_pp | -8.50 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_20d_pp | -17.54 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_60d_pp | -16.00 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma20 | 536.94 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma50 | 565.64 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma200 | 521.76 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma20_pct | -13.59 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma50_pct | -17.98 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma200_pct | -11.08 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_sma | 24.64 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_pct | 5.31 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.drawdown_from_63d_high_pct | -26.81 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.volume_vs_previous20_ratio | 1.53 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SMH/history/ |
| prices.IGV.value | 98.88 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_1d_pct | -0.13 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_5d_pct | -5.19 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_20d_pct | -12.24 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_60d_pct | -6.96 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_1d_pp | -0.44 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_5d_pp | -2.48 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_20d_pp | -6.68 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_60d_pp | -1.72 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma20 | 106.91 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma50 | 106.70 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma200 | 94.05 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma20_pct | -7.51 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma50_pct | -7.33 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma200_pct | 5.13 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_sma | 3.00 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_pct | 3.04 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.drawdown_from_63d_high_pct | -12.24 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.volume_vs_previous20_ratio | 0.89 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IGV/history/ |
| prices.XOP.value | 173.77 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_1d_pct | -0.19 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_5d_pct | -14.72 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_20d_pct | -9.27 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_60d_pct | -2.63 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_1d_pp | -0.50 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_5d_pp | -12.01 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_20d_pp | -3.71 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_60d_pp | 2.61 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma20 | 195.25 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma50 | 191.13 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma200 | 170.87 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma20_pct | -11.00 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma50_pct | -9.09 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma200_pct | 1.70 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_sma | 6.26 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_pct | 3.60 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.drawdown_from_63d_high_pct | -15.18 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.volume_vs_previous20_ratio | 1.23 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XOP/history/ |
| prices.OIH.value | 356.15 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_1d_pct | 2.44 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_5d_pct | -13.47 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_20d_pct | -8.36 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_60d_pct | -13.25 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_1d_pp | 2.13 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_5d_pp | -10.76 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_20d_pp | -2.80 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_60d_pp | -8.01 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma20 | 387.10 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma50 | 397.04 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma200 | 398.57 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma20_pct | -8.00 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma50_pct | -10.30 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma200_pct | -10.64 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_sma | 14.97 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_pct | 4.20 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.drawdown_from_63d_high_pct | -18.42 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.volume_vs_previous20_ratio | 0.91 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/OIH/history/ |
| prices.ITA.value | 68.98 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_1d_pct | 1.28 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_5d_pct | -1.33 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_20d_pct | 0.14 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_60d_pct | -17.03 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_1d_pp | 0.96 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_5d_pp | 1.37 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_20d_pp | 5.70 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_60d_pp | -11.78 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma20 | 69.28 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma50 | 70.75 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma200 | 75.96 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma20_pct | -0.43 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma50_pct | -2.50 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma200_pct | -9.19 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_sma | 2.01 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_pct | 2.91 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.drawdown_from_63d_high_pct | -18.18 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.volume_vs_previous20_ratio | 0.71 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ARKX.value | 28.42 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_1d_pct | 5.08 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_5d_pct | -4.60 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_20d_pct | -11.74 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_60d_pct | -18.45 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_1d_pp | 4.77 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_5d_pp | -1.90 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_20d_pp | -6.18 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_60d_pp | -13.21 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma20 | 30.04 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma50 | 31.37 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma200 | 32.35 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma20_pct | -5.38 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma50_pct | -9.40 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma200_pct | -12.14 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_sma | 1.00 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_pct | 3.52 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.drawdown_from_63d_high_pct | -18.47 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.volume_vs_previous20_ratio | 1.29 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.KRE.value | 72.20 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_1d_pct | -0.15 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_5d_pct | 0.26 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_20d_pct | 4.62 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_60d_pct | -6.61 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_1d_pp | -0.46 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_5d_pp | 2.97 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_20d_pp | 10.18 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_60d_pp | -1.37 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma20 | 71.48 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma50 | 71.69 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma200 | 70.49 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma20_pct | 1.01 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma50_pct | 0.71 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma200_pct | 2.43 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_sma | 1.64 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_pct | 2.27 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.drawdown_from_63d_high_pct | -6.83 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.volume_vs_previous20_ratio | 0.63 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/KRE/history/ |
| prices.SKYY.value | 146.45 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_1d_pct | -0.49 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_5d_pct | -8.34 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_20d_pct | -16.26 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_60d_pct | -13.30 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_1d_pp | -0.80 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_5d_pp | -5.63 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_20d_pp | -10.70 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_60d_pp | -8.06 | pp | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma20 | 162.88 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma50 | 163.91 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma200 | 137.25 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma20_pct | -10.09 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma50_pct | -10.65 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma200_pct | 6.71 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_sma | 5.06 | USD_per_share | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_pct | 3.46 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.drawdown_from_63d_high_pct | -16.26 | percent | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.volume_vs_previous20_ratio | 0.79 | ratio | 2026-11-06 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SKYY/history/ |
| macro.DGS2.value | 4.46 | percent | 2026-11-05 | lagged | source_series_v1:DGS2 | https://fred.stlouisfed.org/series/DGS2 |
| macro.BAMLH0A0HYM2.value | 3.48 | percentage_points | 2026-11-05 | lagged | source_series_v1:BAMLH0A0HYM2 | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| macro.BAMLC0A0CM.value | 0.93 | percentage_points | 2026-11-05 | lagged | source_series_v1:BAMLC0A0CM | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| macro.DGS10.value | 4.84 | percent | 2026-11-05 | lagged | source_series_v1:DGS10 | https://fred.stlouisfed.org/series/DGS10 |
| macro.DFII10.value | 2.60 | percent | 2026-11-05 | lagged | source_series_v1:DFII10 | https://fred.stlouisfed.org/series/DFII10 |
| macro.T10YIE.value | 2.23 | percent | 2026-11-06 | ok | source_series_v1:T10YIE | https://fred.stlouisfed.org/series/T10YIE |
| macro.STLFSI4.value | -0.52 | index | 2026-10-30 | lagged | source_series_v1:STLFSI4 | https://fred.stlouisfed.org/series/STLFSI4 |
| macro.CBOE_VIX.value | 25.64 | index | 2026-11-06 | ok | source_series_v1:CBOE_VIX | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| macro.GPRD.value | 97.67 | index | 2026-11-02 | lagged | source_series_v1:GPRD | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_ACT.value | 113.60 | index | 2026-11-02 | lagged | source_series_v1:GPRD_ACT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_THREAT.value | 94.75 | index | 2026-11-02 | lagged | source_series_v1:GPRD_THREAT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA7.value | 137.64 | index | 2026-11-02 | lagged | source_series_v1:GPRD_MA7 | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA30.value | 164.04 | index | 2026-11-02 | lagged | source_series_v1:GPRD_MA30 | https://www.matteoiacoviello.com/gpr.htm |
| quotes.MU.value | 684.84 | USD_per_share | 2026-11-09T12:01:05+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/MU |
| quotes.XLV.value | 187.06 | USD_per_share | 2026-11-09T12:00:13+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLV |
| quotes.BABA.value | 107.66 | USD_per_share | 2026-11-09T12:01:02+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/BABA |
| quotes.SNDK.value | 820.46 | USD_per_share | 2026-11-09T12:01:05+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SNDK |
| quotes.GOOGL.value | 290.01 | USD_per_share | 2026-11-09T12:01:01+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GOOGL |
| quotes.RSP.value | 218.25 | USD_per_share | 2026-11-09T11:17:00+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/RSP |
| quotes.DRAM.value | 39.02 | USD_per_share | 2026-11-09T12:01:06+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/DRAM |
| quotes.CVX.value | 213.19 | USD_per_share | 2026-11-09T11:20:00+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/CVX |
| quotes.ARM.value | 173.00 | USD_per_share | 2026-11-09T12:00:00+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/ARM |
| quotes.IWM.value | 276.97 | USD_per_share | 2026-11-09T12:01:00+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/IWM |
| quotes.QCOM.value | 163.90 | USD_per_share | 2026-11-09T12:00:37+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/QCOM |
| quotes.STX.value | 461.20 | USD_per_share | 2026-11-09T12:00:03+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/STX |
| quotes.SPY.value | 739.85 | USD_per_share | 2026-11-09T12:00:59+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SPY |
| quotes.CI.value | 294.00 | USD_per_share | 2026-11-09T09:01:25+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/CI |
| quotes.GEV.value | 783.55 | USD_per_share | 2026-11-09T11:42:00+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GEV |
| quotes.XLE.value | 61.75 | USD_per_share | 2026-11-09T12:00:41+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLE |
| quotes.NOW.value | 103.30 | USD_per_share | 2026-11-09T11:42:00+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NOW |
| quotes.AVGO.value | 300.51 | USD_per_share | 2026-11-09T12:00:51+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AVGO |
| quotes.IGV.value | 99.55 | USD_per_share | 2026-11-09T11:20:00+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/IGV |
| quotes.META.value | 623.52 | USD_per_share | 2026-11-09T12:00:51+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/META |
| quotes.ORCL.value | 115.92 | USD_per_share | 2026-11-09T12:00:55+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/ORCL |
| quotes.NVDA.value | 177.04 | USD_per_share | 2026-11-09T12:01:01+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| quotes.COIN.value | 131.60 | USD_per_share | 2026-11-09T12:00:13+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/COIN |
| quotes.NXPI.value | 246.36 | USD_per_share | 2026-11-09T09:01:27+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NXPI |
| quotes.VRT.value | 185.26 | USD_per_share | 2026-11-09T12:00:27+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/VRT |
| quotes.XOM.value | 166.00 | USD_per_share | 2026-11-09T11:25:03+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XOM |
| quotes.SO.value | 92.33 | USD_per_share | 2026-11-09T09:01:00+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SO |
| quotes.COHR.value | 191.25 | USD_per_share | 2026-11-09T11:44:00+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/COHR |
| quotes.TAN.value | 46.45 | USD_per_share | 2026-11-09T12:00:07+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/TAN |
| quotes.ILMN.value | 214.50 | USD_per_share | 2026-11-09T09:01:22+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/ILMN |
| quotes.INTC.value | 56.03 | USD_per_share | 2026-11-09T12:01:06+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/INTC |
| quotes.COP.value | 136.58 | USD_per_share | 2026-11-09T12:00:06+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/COP |
| quotes.QQQ.value | 659.34 | USD_per_share | 2026-11-09T12:01:00+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| quotes.AMD.value | 465.98 | USD_per_share | 2026-11-09T12:01:09+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AMD |
| quotes.CEG.value | 261.00 | USD_per_share | 2026-11-09T12:00:55+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/CEG |
| quotes.XLF.value | 57.91 | USD_per_share | 2026-11-09T11:17:00+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLF |
| quotes.GLD.value | 376.45 | USD_per_share | 2026-11-09T12:00:35+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GLD |
| quotes.CRWV.value | 44.85 | USD_per_share | 2026-11-09T12:00:51+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/CRWV |
| quotes.MSFT.value | 540.70 | USD_per_share | 2026-11-09T12:01:02+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/MSFT |
| quotes.GDX.value | 89.56 | USD_per_share | 2026-11-09T12:00:55+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GDX |
| quotes.LITE.value | 532.67 | USD_per_share | 2026-11-09T12:00:52+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/LITE |
| quotes.CAT.value | 565.95 | USD_per_share | 2026-11-09T12:00:26+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/CAT |
| quotes.TLT.value | 81.97 | USD_per_share | 2026-11-09T12:00:35+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/TLT |
| quotes.AMZN.value | 266.74 | USD_per_share | 2026-11-09T12:00:42+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AMZN |
| quotes.GLW.value | 106.62 | USD_per_share | 2026-11-09T12:00:38+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GLW |
| quotes.PLTR.value | 160.70 | USD_per_share | 2026-11-09T11:58:57+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/PLTR |
| quotes.SMH.value | 462.58 | USD_per_share | 2026-11-09T12:00:55+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SMH |
| quotes.AAPL.value | 344.43 | USD_per_share | 2026-11-09T12:00:35+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AAPL |
| quotes.MRVL.value | 140.36 | USD_per_share | 2026-11-09T12:00:48+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/MRVL |
| quotes.LLY.value | 1,382.10 | USD_per_share | 2026-11-09T12:01:04+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/LLY |
| premarket.SPY.price | 739.85 | USD | 2026-11-09T12:00:59+00:00 | ok | 最后非空分钟close；股票与周五常规收盘比较，期货前收为供应商口径。TNX直接为百分数，旧观测仅背景。 | https://query1.finance.yahoo.com/v8/finance/chart/SPY |
| premarket.QQQ.price | 659.34 | USD | 2026-11-09T12:01:00+00:00 | ok | 最后非空分钟close；股票与周五常规收盘比较，期货前收为供应商口径。TNX直接为百分数，旧观测仅背景。 | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| premarket.SMH.price | 462.58 | USD | 2026-11-09T12:00:55+00:00 | ok | 最后非空分钟close；股票与周五常规收盘比较，期货前收为供应商口径。TNX直接为百分数，旧观测仅背景。 | https://query1.finance.yahoo.com/v8/finance/chart/SMH |
| premarket.NVDA.price | 177.04 | USD | 2026-11-09T12:01:01+00:00 | ok | 最后非空分钟close；股票与周五常规收盘比较，期货前收为供应商口径。TNX直接为百分数，旧观测仅背景。 | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| premarket.MSFT.price | 540.70 | USD | 2026-11-09T12:01:02+00:00 | ok | 最后非空分钟close；股票与周五常规收盘比较，期货前收为供应商口径。TNX直接为百分数，旧观测仅背景。 | https://query1.finance.yahoo.com/v8/finance/chart/MSFT |
| premarket.AMZN.price | 266.74 | USD | 2026-11-09T12:00:42+00:00 | ok | 最后非空分钟close；股票与周五常规收盘比较，期货前收为供应商口径。TNX直接为百分数，旧观测仅背景。 | https://query1.finance.yahoo.com/v8/finance/chart/AMZN |
| premarket.GOOGL.price | 290.01 | USD | 2026-11-09T12:01:01+00:00 | ok | 最后非空分钟close；股票与周五常规收盘比较，期货前收为供应商口径。TNX直接为百分数，旧观测仅背景。 | https://query1.finance.yahoo.com/v8/finance/chart/GOOGL |
| premarket.META.price | 623.52 | USD | 2026-11-09T12:00:51+00:00 | ok | 最后非空分钟close；股票与周五常规收盘比较，期货前收为供应商口径。TNX直接为百分数，旧观测仅背景。 | https://query1.finance.yahoo.com/v8/finance/chart/META |
| premarket.CL_F.price | 88.10 | USD | 2026-11-09T11:51:03+00:00 | ok | 最后非空分钟close；股票与周五常规收盘比较，期货前收为供应商口径。TNX直接为百分数，旧观测仅背景。 | https://query1.finance.yahoo.com/v8/finance/chart/CL=F |
| premarket.BZ_F.price | 94.79 | USD | 2026-11-09T11:51:04+00:00 | ok | 最后非空分钟close；股票与周五常规收盘比较，期货前收为供应商口径。TNX直接为百分数，旧观测仅背景。 | https://query1.finance.yahoo.com/v8/finance/chart/BZ=F |
| premarket.GC_F.price | 4,120.30 | USD | 2026-11-09T11:51:08+00:00 | ok | 最后非空分钟close；股票与周五常规收盘比较，期货前收为供应商口径。TNX直接为百分数，旧观测仅背景。 | https://query1.finance.yahoo.com/v8/finance/chart/GC=F |
| premarket.VIX.price | 23.38 | index points | 2026-11-09T11:46:01+00:00 | ok | 最后非空分钟close；股票与周五常规收盘比较，期货前收为供应商口径。TNX直接为百分数，旧观测仅背景。 | https://query1.finance.yahoo.com/v8/finance/chart/^VIX |
| premarket.TNX.price | 4.86 | percent | 2026-11-06T19:59:00+00:00 | stale | 最后非空分钟close；股票与周五常规收盘比较，期货前收为供应商口径。TNX直接为百分数，旧观测仅背景。 | https://query1.finance.yahoo.com/v8/finance/chart/^TNX |
| premarket.DX-Y.NYB.price | 101.84 | index points | 2026-11-09T11:51:08+00:00 | ok | 最后非空分钟close；股票与周五常规收盘比较，期货前收为供应商口径。TNX直接为百分数，旧观测仅背景。 | https://query1.finance.yahoo.com/v8/finance/chart/DX-Y.NYB |

## 指标历史比较（不同日期观测，非连续交易日）

```json
[
  {
    "id": "prices.SPY.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.28997802734375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -20.42999267578125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 4.721587107841397,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.0853158265071947,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.022622876311742,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.1441487178347485,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.27032189781024396,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -3.7502695128991625,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.3640091403464547,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -3.8139296706872328,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.16400146484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -7.1045043945312045,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.6779992675781159,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.6247436523436818,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.2582467651366187,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.6615884399413972,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.5714224601963358,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.7634430200896944,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.3840964125155666,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.4607816912426306,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.2789459653218307,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -3.045387983097414,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.14285714285714235,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.819292340959821,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.014766807670061999,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.41392610429523735,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.29392983460286803,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.622289077199458,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.7607238962303615,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.7592442466392675,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 9.04998779296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -34.3900146484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 7.8875651479585756,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 4.87253112910524,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 4.565991183359886,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -3.005788220365735,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.7795059513832197,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -4.784803310819796,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.21420621274660334,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -7.004037972173084,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 3.165978040117179,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.787215302598045,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.543368307048144,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.8616395025309864,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.0498278491934627,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.0345337979206333,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.578215353093058,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -3.1901083014858505,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -4.758502197265557,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -20.548498535156227,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.2851879882812227,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -3.955623779296843,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.18723602294926422,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.41905914306642,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.8896636956689523,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.1063410138440153,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.4154330910235888,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -4.248521022354634,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.30505949879145,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -5.271360788740753,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.1942879813058056,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.238573346819196,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.005391080795028369,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.45032145553417546,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.1913208689286687,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -4.527027336465251,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.4954978255407219,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.8245115012995732,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.69000244140625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -5.65997314453125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 5.583912459688278,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.6405314599096785,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.5615983904791144,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -3.3245402020448123,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.48488326777291757,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.1113704726155582,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.6550235969056235,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -3.4940790943063345,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.8623253518468816,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.5552156334024838,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.5389755141673724,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.1803914842100638,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.7552051655831615,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.6388990402836043,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.0190327372520782,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.3198505763808983,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.2634994506835824,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.566499328613304,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.5071795654296807,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.088063964843741,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.028489227294926422,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.32570564270019986,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.0647486143570806,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.838428319811447,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.126684436326963,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.279151750951546,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.9575585786811613,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.1536333975100352,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.14999825613839235,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.7057124546595981,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.03819926238645044,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.2876606171750571,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.8840106358877335,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.8600267351388968,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.0710001686743251,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.05109473564725742,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.8199920654296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.2599945068359375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.514480419110654,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.4081157197588614,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.4054237329538579,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.8526255744111042,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.9470529132772798,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.6780902272057316,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.098967888934299,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.886423277438721,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.2071066887307427,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.6772001067483333,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.617199143357884,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.29152314342364427,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.6767310154670358,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.072179285693431,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.7349587485878444,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.9275063932485117,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.15050048828126705,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.8264999389648438,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.09141357421873408,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.18574310302733466,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.09374938964842272,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.567425537109358,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.44790457749005474,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.8990030513945988,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.3391569842170261,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.9653947313572386,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.44338681496540744,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.380942658079598,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.07999965122767883,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.5671419416155135,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.041694745751682305,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.27294718790975636,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.36716610339259104,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.6260570470321478,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.451144796444301,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.09256905765384582,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.970001220703125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 16.739990234375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.5963575860058032,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.6792039223187736,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.8276301593093356,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 7.659241502908721,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.309200288706459,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 3.272281363951179,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.6408762741042295,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.0698745821537523,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -6.3179446938472,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.5938880958115789,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.805007282997594,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 9.80339022074347,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.0388783908962145,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 7.0225508768503415,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.0048854144506842,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 5.883804252840985,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.602999877929733,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.9744995117187614,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.001600341796859,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -5.61260070800779,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.39635009765623863,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.6791502380370957,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.6340338726036454,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 5.24592807065749,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.5183857150277249,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 5.676608140298912,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.63428890958237,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 4.4224137683740885,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.23856898716517794,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.8092782156808029,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.07772650561813199,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.14304844881441392,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.6938120330522661,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 3.910573024962293,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.5693679705282219,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.1934073454781262,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -38.60009765625,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 176.0,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.9327290785029705,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.3483234674630538,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.477577990038271,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 7.233722631324413,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.307221432546458,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.9745807930216746,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.1078598750872457,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.5034409889933862,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -6.654316186344367,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.26300764095585905,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.4549551137265295,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 9.377871349159161,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.0368995347362144,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 6.724850305920837,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.4718690154337004,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 5.317370659680619,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -7.069995117187773,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -34.32500000000027,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -11.782001953124563,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -64.37599609374956,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -4.192500000000109,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -17.821999511718786,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.7715713403401492,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 5.109940287175208,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.6423838874782151,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 5.541805612036076,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.7724660592625892,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 4.251373196365117,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.8214285714285694,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 10.028564453125,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.0638483143819073,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.1630776878547604,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.8216633160428533,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 3.7464346570150955,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.13382846670956283,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.36160635812956476,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.31000518798828125,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -13.290000915527344,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.381080274777103,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.7359625678341484,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.5092136157093492,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -13.587209921295585,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.05027610363257384,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -15.389947305093253,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 3.084154104435811,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -22.922647474408596,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -7.1026673826185,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -3.821278394341343,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -3.5318364920210907,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -11.443061203460836,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.22004579417767012,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -11.639677792194089,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 3.4481632447822665,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -19.108717803721362,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.050999832153323155,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.5764999389648438,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.14600006103515284,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.8365998840331912,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.15735000610351335,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.8153499984741188,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.36431858214903645,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -14.187884080786727,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.1794953259037113,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -14.885310054708278,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.16784451651321586,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -16.376406549228694,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.10571452549525695,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.865714481898717,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.13610677377288827,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.551561739706905,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.29292750885817576,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -12.557876486427066,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.41776925464640313,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.20792798765741294,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.029998779296875,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -19.31999969482422,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -3.848149854630911,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.371988198068764,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.9818320585635032,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -17.211194731408963,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.3673885260705223,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -21.162881055518156,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.4576163514969487,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -29.690589944417397,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -8.569736962472309,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -4.457304024575959,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -4.004454934875245,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -15.067046013574213,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.09706662826027834,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -17.412611542618993,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.8216254918434043,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -25.876660273730163,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.3200000762939368,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.5249999999999915,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.1724000549316429,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.9384001159668003,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.17130001068115064,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.887450046539314,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.29446394484641303,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -17.29702505084666,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.12752465616919828,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -19.5664105698484,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.16145962862912366,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -21.907561724352377,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.028570992606026913,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.8628561837332587,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.027342332104455913,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.5121238794688665,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.02550049256420195,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -16.42298520491513,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.3024444203227703,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.2213989156611331,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.01000213623046875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.0800018310546875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.2201315396821002,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.44170683965554236,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.44219260908033853,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.5169497880975316,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.16124386898246357,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.574678630899994,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.19327195708955802,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.012912796270037052,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -4.941718647523497,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.527022666162737,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.4648154853920805,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.627198929737217,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.10907802882778128,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 3.1755908819991685,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.17073718325689669,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 3.82684246695727,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.19699974060058878,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.0529998779296932,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.16718551635743495,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.0564260864257875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.30724323272704623,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.07277427673339787,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.2607340128556457,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.2411095509038406,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.1999595389597486,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.17144862533984284,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.3506847993627882,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.18227036591469403,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -5.449567522797238e-07,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.08214351109095985,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.00011419099749221395,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.10129054786663794,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.3847577475050934,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.09659977275193743,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.31918030931229024,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.032941394106376976,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.20999908447265625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.12999916076660156,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.6569321740786949,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.8638821063304047,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.8614989855512012,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.310148255481435,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.5860819543662577,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.0017122506096312051,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.8179921548071789,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.4978237418226783,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -4.064654933762702,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.22143372017679,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.1611238907605412,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.4542969733161835,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.8564038521765021,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 3.7485572622895313,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.1820012951536327,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 4.31175341250991,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.0054999351501479055,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.0005001068115220164,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.022199974060061578,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.10159996032714957,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.009899997711183772,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.04214999198913816,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.7051945479005006,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.44998186971973997,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.6539638797459668,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.09385809077417928,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.7142515186688181,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.3083118351555836,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.010714258466448107,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.00357137407575335,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.03428809485117701,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.014018829583639036,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.7209031600505234,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.44627244940566024,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.035213354518376594,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.17829070185650076,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.04999542236328125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.1999969482421875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.2449009103716815,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.12865689298005023,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.12840765198579573,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.7514765335443929,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.18148741347698838,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.676110542590691,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.14981503004611874,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.6601854819375808,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -4.476686197469715,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.9566589335271445,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.8942152243259467,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.3926721842903556,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.08883448433325558,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 3.0741589703084715,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.5138241703925734,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 3.153744188749652,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.0,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.004999923706051845,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.20412734985350767,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.18335098266601335,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.30404170989989154,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.009104003906244884,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.06479154324523506,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.2656883964647694,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.19669265134701908,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.022598016241093255,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.32166246724093517,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.24517208099634757,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.0021433149065289703,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.019999367850167427,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.002498802635633124,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.026925472795265026,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.369398893099393,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.2527373613964934,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.7767641791846325,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.5623391270798979,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.1300048828125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.26000213623046875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.27732994654744436,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.17218743802186465,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.17283148052289476,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.15507300938937263,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.06710774923386342,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.3260398101270434,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.09712069262118872,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.06979344810490451,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -4.998917054388841,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.2575032645290594,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.1954543568346367,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.9890757084453758,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.20321414857638054,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 3.424229702772119,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.266888447725266,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 3.8837231187921373,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.10599975585937216,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.5084999084472628,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.24156600952147755,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.1369189453124875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.41059814453124943,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.062131347656247726,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.22861506080031901,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.24470977985702191,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.1094102886496362,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.3836394700743373,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.2596450495271685,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.3036471090845816,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.015714372907366103,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.04500034877232151,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.014308478253808876,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.044575184596744144,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.30168518230708763,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.24538667789180124,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.8504070590838885,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.40443968009322895,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.5400009155273438,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 6.219999313354492,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -78.67031672827304,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -21.920460071741477,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -31.80837121959228,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 32.183077759198206,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -10.091996715923301,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 45.93107819609713,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -12.688088708382423,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 49.59424595954536,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -83.39190383611444,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -24.00577589824867,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -33.830994095904025,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 34.32722647703295,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -9.821674818113053,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 49.6813477089963,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -13.1711792543651,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 52.62105776986959,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.5399999618530273,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.8274999618530288,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.224199981689452,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.7391999816894526,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.04744999885559409,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.13769999980926784,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -17.90996097335691,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 21.948219363866862,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -17.24601961613039,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 31.51477415177033,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -14.203576784297844,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 33.01571117914906,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.15071432931082596,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.8792856761387413,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.7165041479543763,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.32872208045868767,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -9.013487892194327,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -6.162063673331841,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.9499988555908203,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 3.8199996948242188,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -39.62245201675306,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -10.997492020726607,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -13.521939531008908,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 16.91820918850342,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.8808039174718516,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 23.055217541023246,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -5.6975084229946376,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 21.00454294788461,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -44.34403912459446,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -13.082807847233802,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -15.544562407320651,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 19.062357906338168,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.6104820196616103,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 26.805487053922405,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -5.333499282648184,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 24.81847261857184,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.341499996185302,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.1305000305175774,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.14080001831054645,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.4200000381469735,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.029250001907350054,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.07269999504089242,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -6.916996674492481,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 12.839390268664765,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -6.005579764106031,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 17.636491973362368,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -4.79257596917391,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 18.20284540007477,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.07857145581926628,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.49000004359654037,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.5902716438650533,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.9600915660896208,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -3.7181952405416774,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -3.7181952405416774,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -13.050003051757812,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 15.510002136230469,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -58.9760894537213,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -18.25834268705697,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -23.157885676544844,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 17.553814622842445,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -10.331051410501658,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 21.356425227002823,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -16.16337115589444,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 16.406032617326314,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -63.6976765615627,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -20.343658513564165,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -25.180508552856583,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 19.697963340677195,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -10.060729512691417,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 25.106694739901982,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -15.799362015547985,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 20.219962288013544,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.8530002593994226,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 7.072000885009771,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.7808000183105435,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.729800415039051,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.12909999847411768,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.23260002136230185,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -15.142205302777882,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 7.437404289411575,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -15.028165137331158,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 13.079497149170319,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -13.354478215776133,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 15.407460471286186,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.5742857796805243,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.5614291599818646,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.5294001240697952,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.7425132178277352,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -9.667384636426778,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -6.5011547747374046,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -5.150001525878906,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -7.430000305175781,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -9.562764181734739,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -12.37934145557249,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -12.097655983847533,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -4.404812351722953,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -3.3506959308048696,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.5411110295048589,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 3.019014414932485,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -7.491935639363966,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -14.284351289576136,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -14.464657282079685,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -14.120278860159274,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.2606636338882042,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -4.047499599682869,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 3.369113036813065,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.960084546070295,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -4.496693755765868,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.39650001525878054,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.2224998474121094,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.46659988403320085,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.4595997619628918,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.16604997634887297,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.9318499755859335,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -4.7973428786517776,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -5.275639029331702,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -6.081952604675767,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -10.944384670853857,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -6.827382230440904,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -11.002729117756417,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.1385710580008368,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.03000041416713195,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.42817796883129144,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.37422327127912425,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -4.533452108322088,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -6.540493314239248,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 5.0399932861328125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -18.0,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 12.034307432196687,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 6.9969891156632436,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 6.209212616792813,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -5.800102380317973,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.6105617566887886,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -6.069030916789719,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.8037957452255426,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -10.618400639342441,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 7.312720324355292,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 4.911673289156049,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 4.186589740481072,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -3.655953662483225,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.8808836544990317,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.318761403890557,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.1678048855719982,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -6.804470968655208,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.131999969482422,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -9.912499237060558,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.8217034912109398,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.911393737792963,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.011157760620136514,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.298783340454122,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 3.2389598204837657,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -4.178900883685322,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.601064338536686,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -7.3874182493609775,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.4610087112237,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -8.953226701098437,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.5578569684709818,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.4800000871930798,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.1879329730215531,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.1011863914104447,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.1066682705275355,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -7.523825274495877,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.3361021245544669,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.09881941398999405,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -5.32000732421875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 8.70001220703125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.582357855146744,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.5597595684263101,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.5747963381489862,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.162664219235677,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -3.382287085659641,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.679856745287167,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.049238016791066,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.381594149890609,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.1392292526946526,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.5255562580808846,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.4478265381627553,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 4.306812937070426,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -3.111965187849397,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.0704127676119954,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.6852288764446115,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 6.195523820577842,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.22300109863283524,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.4264984130859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.5109997558594159,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 3.7351995849610375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.4115707397461392,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.9922358703613554,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.9588127232711963,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.5582768164121408,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.1324209583725597,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.9482852564420163,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.326911317865843,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.4401140271773443,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.4535740443638385,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 4.137858799525668,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.11433347192754839,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.742955059847394,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.9571801801119166,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.5686331639546576,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.6900673175845937,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.6164362498854381,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.910003662109375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 18.949981689453125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.8380069976201896,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.0613263208991364,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.1490231157858632,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 10.96900248404803,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -3.6133865466724147,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 3.248297024950752,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.4462411810519318,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 9.521487545295216,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.883580110221207,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.0239895056080583,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.8735997605258792,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 13.113151201882777,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -3.343064648862171,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 6.998566537849914,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.8102503213983865,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 13.335417215982448,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.15650024414063068,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.11200103759765057,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.060799560546854536,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.3288006591797057,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.12479995727539972,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.5395500183105355,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.29493302958547574,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 7.494066985174131,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.38287697070269466,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 7.584467824598851,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.4276440032844775,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 7.5498822034928414,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.5764290945870538,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.0478570120675226,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.2083573841717361,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.5551799737066538,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.6659206336359542,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 8.807488332256742,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.984323909247033,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.864446277923062,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.209991455078125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 4.94000244140625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.9833242404018745,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.1844051095654127,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.2057153226362702,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 14.372645586684985,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.14903829232293475,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.48561904912458687,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.03163972617112876,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 4.001160863409158,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.7382628674395222,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.09908928305821796,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.1830924463245287,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 16.516794304519735,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.12128360548730832,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 3.2646504637745775,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.33236941417532684,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 7.815090534096392,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -3.3440002441406023,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -16.4650009155273,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.113023681640641,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -6.121671142578123,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.22559112548827898,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.1260441589355423,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.624115835583483,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 5.90312625464767,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.9466858556096192,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 3.0017306313407808,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.7068601608728784,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.7292412570990123,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.13785661969866148,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.45499747140067015,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.017760858153771597,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.0925632211361549,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.139555392769065,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 6.078510584846839,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.4983841162728645,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.1646851874969864,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 5.07000732421875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -4.8399658203125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 4.79345976114428,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.3638835080965537,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.325791795297938,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 3.512587740549844,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.9647535248090815,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.4325270253570981,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.9815731182887042,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.7031967321688102,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.07187265330288417,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.27856768158935896,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.3031689189861959,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 5.656736458384593,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.2350754226193246,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 4.182796538256261,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.6175639779422495,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.1107329385184226,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -5.425997924804619,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -28.432998657226562,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.790008544921875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 4.9801745605469705,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.1790841674804824,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.1239749145507858,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.5066529554328856,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 3.0877201140074764,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.6462596269503411,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.3949498023641969,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.8304894196395578,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.7477111611208231,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.3607090541294653,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.2228524344308056,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.02689112688136408,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.16810678493912778,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.6520154771945244,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.622431571027871,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.5426429731551907,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.49595917432442804,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.740001678466797,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -8.46999740600586,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 16.10641655669458,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 15.939917659502434,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 12.683375544540642,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -16.60730934960578,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 3.0121972887931037,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -4.694954861392951,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 3.1269121584040036,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -20.649135675860578,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 11.384829448853184,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 13.85460183299524,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 10.660752668228898,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -14.463160631771032,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 3.282519186603345,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.9446853484937918,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 3.4909212987504574,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -16.835206005173347,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.7840000152587905,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -9.442499923706059,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.8080000305175759,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -3.8916000366210994,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.22694999694823537,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.174650039672855,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 6.767093218746368,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.577402055133124,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 4.237567197258443,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -7.6527171310714515,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 3.1600975607871646,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -8.610431590224358,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.1482140677315842,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.1465715680803568,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.1063423737286726,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.20335096322736668,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.5433970046288366,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -7.862245560266878,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.4200644841353528,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.011296519645471181,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 33.6099853515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -194.739990234375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 22.579525118645236,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 10.421897445017258,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 7.732022393140838,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -22.830312241328674,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 3.68807418424133,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -15.25683016902778,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.6160111692050556,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -27.73076203356223,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 17.857938010803842,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 8.336581618510063,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 5.709399516829098,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -20.686163523493924,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 3.9583960820515713,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -11.506560656128618,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.9800203095515094,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -23.916832362874995,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -16.941906738281205,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -71.561099243164,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -4.904855957031259,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -17.058460693359393,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.4635530090332622,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 9.902968139648465,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 5.235795447780578,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -14.577334102076446,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 3.8419129233668414,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -18.64911523369296,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 4.274488182731117,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -27.292433886404744,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.4600001743861597,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 7.8671015110688245,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.21431834066983413,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.766626701780642,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 3.063202321568987,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -17.748534667556108,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.324585640471901,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.3407734612350557,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.2800025939941406,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -8.71999740600586,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 24.116616575410887,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 13.38756083472975,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 10.320217066130244,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -20.181570953503012,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 3.6911673821561664,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -9.010407154964607,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.478086318400063,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -24.317456007629538,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 19.39502946756949,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 11.302245008222556,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 8.297594189818504,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -18.037422235668267,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 3.9614892799664077,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -5.260137642065445,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.8420954587465204,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -20.5035263369423,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.8949998855590877,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -3.997499847412115,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.35080001831054375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.321000061035157,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 6.165057617031344,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -10.47884401086192,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 4.604331329226309,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -13.883599371357326,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.05000005449567535,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.2921428680419922,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.3740393553579793,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.1095848275097184,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 3.583782823440856,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -13.706377793784604,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.5118260771630718,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.02255857357634561,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 6.1300048828125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -49.63999938964844,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 17.489493557988045,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 8.92562922091804,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 6.784629737971795,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -40.998536155711705,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.8086551885998965,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -16.876833441710737,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.4113665055707756,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -20.799565288047017,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 12.767906450146649,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 6.840313394410846,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 4.762006861660051,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -38.85438743787695,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 3.0789770864101413,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -13.12656392881157,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.775375645917233,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -16.985635617359783,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.99599990844726,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -10.720499420165993,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.7270797729492244,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -5.601799011230469,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.00932479858397528,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.6936153411865575,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 3.9958531854045525,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -17.990672186357493,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 3.126219565458264,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -18.68103203246111,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.2586760064359055,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -18.528564209708694,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.4385713849748889,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 3.751000540597099,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.10869711864856235,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 3.8099356979085464,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.0866824867037153,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -16.897689210132892,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.3580303195103638,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.053810719157601605,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.3600006103515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -14.769989013671875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 9.453378523955024,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 6.343712284218961,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 5.738354761341192,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -6.197712068999173,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.7742163914905227,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -6.964802608198529,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.3767032538482642,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -10.516608872472533,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 4.731791416113628,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 4.258396457711767,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 3.7157318850294505,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -4.053563351164424,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.0445382893007658,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -3.214533095299366,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.740712394194718,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -6.702679201785301,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.7019996643066406,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -7.326499176025408,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.4730029296874818,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.2226330566406034,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.10190387725828032,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.6766678237914903,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.098813634357377,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -4.293050967019141,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.4686732269459384,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -7.2260264154382465,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.3316027284235528,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -9.115140997637283,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.08428519112723176,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.6628559657505582,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.0031063745969337475,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.6455259667313649,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.1683171338374159,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -7.311875749342512,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.5321475836544347,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.45432054225835294,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.01000213623046875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -8.39999771118164,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.9592104937570918,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.9227896211140072,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.692395488207321,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -12.99180236067915,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.2168725499012929,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -16.777851051744086,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.06639548368196913,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -19.59064966876447,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.762376614084305,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -4.008105447621202,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -3.7150183645190626,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -10.847653642844401,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.48719444771153686,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -13.027581538844924,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.2976136566644856,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -15.776719998077237,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.17300014495849325,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.009000015258791905,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.006038742065427982,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.1804522705078142,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.06830247879028661,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.42407444000244254,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.2212231307595509,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -12.502769695914207,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.006578564757253602,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -13.231765948276841,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.13990434157511444,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -15.212144679040929,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.022142682756696397,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.4114276341029577,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.03641227756976129,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.9452523692659316,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.01428468538988703,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -11.996569714222394,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.8024711659305468,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.15478613735298885,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.3400001525878906,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.6500015258789062,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.2803182601663585,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.16387683314476043,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.1667478001363465,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.05901304514863703,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.589894990246088,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.2059300024227504,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.1670683435474505,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.3619421229494435,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.441268847675038,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.9214389933624343,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.8558750761753955,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.2031617629833855,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.319573092435844,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.544339510476412,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.8030592032009958,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 4.175871793636676,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.12150001525878906,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.9005001068115206,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.010317535400396594,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.010334701538091906,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.02000104904174549,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.11291900634765284,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.826058020983389,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.4795813917539249,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.5897095533190067,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.1824523532861564,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.6754499386224522,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.9912677532896375,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.03714261736188618,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.2457147325788226,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.07491102658157711,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.4147506907884091,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.5743245746725356,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.28678841216064344,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.1006260150643576,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.17365094125354474,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.1999969482421875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -4.7299957275390625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 4.247968073339181,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.7277594450647138,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.676876280666562,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -4.5143020612671725,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.3663676608663291,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.387297982516523,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.15040218463411392,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -3.0563734194178007,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.47361903450221554,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.3575563814424809,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.34574659564517995,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.370153343432424,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.09604576305608514,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.3629715303826395,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.5144113249805686,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.757556251269432,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.3290000915527287,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.5769989013671761,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.31301483154294374,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.1751242065429608,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.00759971618651889,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.07057449340820199,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.3095204203378832,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.4806737098166165,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.2951490966301211,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.1120122069759883,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.11998366383357784,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.7793413056542042,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.010713849748884119,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.4621440342494423,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.0041663236136944,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.33180434579844365,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.10751941944927523,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.542870774241546,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.4305094887896106,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.5313124972240995,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.1100006103515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.0699920654296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.4449929270792814,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.5104786554918417,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.5105891304675647,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -3.155885799087843,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.7703611354592077,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -3.05645242718915,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.0263128527064449,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.675596729585772,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.2765941807621153,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.5957944819990364,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.5332120067793067,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.0117370812530946,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.5000392376489646,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.6938170857100125,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.3376962876400107,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.1383329411014618,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.6995002746581918,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 4.287501525878895,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.27748321533204034,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.2315185546875114,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.1422432708740473,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.7647493743896518,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.46198144195772617,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.545564585346516,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.23485712181603446,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.8049115189749712,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.1743077284600325,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.6101412901264176,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.1914280482700894,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.4435708182198663,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.10474501605732511,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.2407130812013305,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.05799884436760161,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.5624805001111084,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.0159081905234022,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.7637473186610453,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.1699981689453125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.660003662109375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.5316976890401559,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.688401907865623,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.743420701365351,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.5762001129439698,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.4154849879409293,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -3.068607896291664,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.5242997085553442,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.3219490555750104,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -5.253284796881553,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -4.773717734372818,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -4.7660435776770935,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.5679486048907787,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.1451630901306835,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.6816616166074994,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.1602905682088895,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 3.4919806151122215,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.33250007629395384,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.0830001831054688,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.11111785888672898,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.49116210937499716,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.04682491302490632,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.24639495849609716,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.7205655822840837,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.7090324761538822,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.519408734256178,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.1643992138787409,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.4566162671902259,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.47287668955859896,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.1135711669921875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.30857086181640625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.14978771671981805,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.3305013359823983,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.2725670414148182,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.3896557391236186,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.8279007565936278,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.6189843886038717,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.05999755859375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.2000045776367188,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 3.7828928848998578,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.6546786330814625,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.6675021306072892,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.10916711803037327,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.1169805558708612,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.6613698879911922,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.5235735142807285,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.572107030038239,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.9386942229415389,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.4306371934257323,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.3551207457044532,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.0349815998043748,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.8466586580606155,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 3.088899624907971,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.15956437393427336,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 5.386036700725472,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.23650016784667116,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.7490005493164062,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.03909332275389943,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.1404139709472645,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.021412086486805038,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.056713409423821304,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.2618977557203417,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.36633882171859256,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.08881869145105359,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.8157379039288823,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.033116007532418834,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.960692072142911,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.009999956403460075,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.7171429225376675,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.009566582447122496,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.5816906715499264,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.0490456614858914,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.3572551390777945,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.3263619410350278,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.22018469324778622,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.45000457763671875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 4.8899993896484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.0219905899980564,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.7256228521344008,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.8023171103319857,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 10.211926240981972,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.8331577514615454,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 4.380928492400971,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.5220031251326542,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 3.261708671609121,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -3.6995965178433403,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.3596929743727939,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.2203057659797567,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 12.35607495881672,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.1034796492717893,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 8.131198005300133,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.1579939847861995,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 7.075638342296354,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.2794998168945284,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.059000015258789,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.12508056640625398,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.8657482910156347,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.05204914093017976,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.27369560241699276,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.6803214194882945,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 6.382277011983029,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.5185471771408157,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 5.170746737270804,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.4447413973409198,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 4.5803407799312685,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.09928567068917404,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.26964242117745507,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.08624830591113808,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.1688153934518588,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.3921608519710009,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 4.261437376599952,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.9606791296445263,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.38190920718353416,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.1699981689453125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.2999992370605469,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.31824379736326014,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.0648375586608694,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.0616501301777492,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.7349353462310932,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.2761639506876366,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -4.884819956381303,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.8406914125086651,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.1976102315655166,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -4.403343310478137,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -3.150153385168064,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -3.084273006489491,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.5907866283963448,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.0058420528773926,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.1345504434821407,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.47668227216220993,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.6163194391217162,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.08600006103515767,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.618499755859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.005303649902344887,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.0543311309814456,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.006466560363769247,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.02925039291381637,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.6052957490396915,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.209088308863305,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.42107852130415235,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.8557540408947961,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.40241018270196216,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.7505825020035273,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.013571602957589302,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.006429127284458658,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.025686431879387905,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.00485070153402023,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.386477418423814,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.682024585250518,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.8132722618611208,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.013587016283276299,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.2999992370605469,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.8300018310546875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.1401760607959832,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.9326492438174627,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.9570619073892006,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.5131960844641181,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.70172458620641,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.0390782698081793,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.0725030730326166,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.187547083874363,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -3.5814110470454135,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -3.0179650703246574,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.979684783700943,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.657344802298866,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.431402688396167,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 3.7111912430909832,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.708493932686162,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 5.001476754561596,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.11949996948242614,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.7965000152587933,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.005744400024418894,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.05815162658691975,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.01913900375366495,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.08811536788940799,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.9923518653074392,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.024161497296182333,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.6926587730983425,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.0945869878424617,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.7461631145948555,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.729108434253268,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.015356881277901802,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.1015712193080357,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.04619672448095913,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.20254408846973226,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.6648919418491994,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.5446930162171353,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.44807840113869646,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.07633229830857036,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.3800010681152344,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.7900009155273438,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.1866379179074746,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.1259400051478297,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.1171869673091028,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -4.284897600282688,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.1125591511448985,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.8429387193699585,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.2137174743038095,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.788990933996315,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.534949189933922,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -3.2112558316550244,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -3.139809843620845,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.1407488824479404,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.8422372533346536,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.9073307935292032,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.1502916660426452,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.0249387366909177,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.12600002288818501,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.876500129699707,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.020723114013669885,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.03868293762207031,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.015289478302001669,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.11475679397582894,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.9852331593402042,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -3.299454298196336,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.7052848727646444,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.4745597571713231,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.7784134442886836,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.7885931937933197,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.03928593226841526,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.2878573281424387,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.08848243894647334,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.5734643948697267,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.7050112381402962,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.3372313478601248,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.7607307905817104,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.2849348042099118,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 16.22998046875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -58.529998779296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 14.837191381228598,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 10.6005732527784,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 9.08380039357085,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -10.308725009493491,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 3.1715442153729363,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -5.956143027823913,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.1974622599048352,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -12.672770884915252,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 10.115604273387202,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 8.515257426271205,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 7.061177517259109,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -8.164576291658744,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 3.4418661131831776,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.205873514924752,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.5614714002512926,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -8.858841214228018,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -6.968501281738327,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -32.96200408935556,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.180800170898465,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -6.980399780273501,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.3056999206543196,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.2542498779297375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 4.091021329948873,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -5.272509273027149,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 3.173347179771202,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -9.221605919838584,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 3.0603429749210154,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -11.652441382171597,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.6964263916015625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 3.6321454729352673,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.03696224291331607,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.2900665919264078,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.560337568018234,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -9.23331700979162,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.3170176485047669,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.46019796431020477,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.1300048828125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -5.410003662109375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 4.262279143814796,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 3.2770496190665077,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 3.1111390060022615,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.5092521393288418,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.585123315213867,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -8.421152933161002,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -3.014352213826254,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -11.861155083302265,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.4593079640266007,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.191733792559313,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.0885161296905195,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.6534008571635908,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.314801417403623,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -4.6708834202618394,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.6503430734797995,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -8.047225412615033,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.68950004577637,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.3484996795654354,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.22880004882811988,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.28739990234375057,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.009790840148923508,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.09870590209960994,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.47182389707707273,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.963500638899963,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.07669844456644803,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -4.8075187348974975,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.14918795227145676,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -5.868688343052786,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.02857153756277908,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.17357145036969834,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.02486682171307608,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.008782646650482562,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.11538553734381551,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -4.801636416108967,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.9236977548182811,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.9635112079188232,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.3300018310546875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -29.989990234375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.7051971964413224,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.314642583386939,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.977715443458182,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -15.744615224516933,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.7532277617811829,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -19.45019387172252,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.5072360142734822,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -25.088990013241574,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.0163899114000743,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -4.399958409894134,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -4.000338319769924,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -13.600466506682183,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.0235496595914269,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -15.699924358823358,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.1432268739270275,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -21.27506034255434,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.8874999999999886,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.8455009460449219,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.21926818847654772,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.2502548217773324,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.20480804443360512,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.3059477996826274,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.23444586836031078,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -14.382355856526564,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.06827884317234378,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -15.551104174687891,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.315397647297444,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -18.469468893114424,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.054999215262276024,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.3249991280691962,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.038418182019021696,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.180435138313515,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.1610865127753094,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -14.639261029495287,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.18667010021642683,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.46170422901453345,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 8.5,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -55.420013427734375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 7.474219032785578,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.5452541865450753,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.3052642295620966,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -17.0416210792255,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.6871386201304794,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -15.906046265370865,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.6173854663244853,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -18.225676203756446,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.7526319249441817,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.5400616399621194,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.7173586467496449,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -14.89747236139075,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.9574605179407234,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -12.155776752471704,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.981394606670941,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -14.411746533069213,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -4.9420013427734375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.1760003662109284,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -4.111200561523447,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.07304992675778976,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.9255497741698946,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.57120785802345,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -12.976301654706667,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.399391171678989,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -12.895795676869248,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.1166529090910657,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -14.145187163543183,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.5335715157645087,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 3.297143118722099,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.05068027243896278,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.367269553268363,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.9469513631937936,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -12.69412596368773,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.7266890661911857,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.11361105950022099,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.8700027465820312,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -140.76000213623047,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 5.275662450691998,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 3.4052064649251923,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 3.3173802350488506,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -5.048575118533694,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.40879303637716413,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.7981116470693994,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.674923264833538,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.0217651709607978,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.5540753428506013,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.3198906384179976,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.2947573587371086,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.9044264006989446,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.6791149341874085,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.952157865829763,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.0389324051799935,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.792164499726436,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.004833602905264911,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -137.3301662445068,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.18032501220703523,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -143.88281677246096,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.04714859008788608,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -152.62886154174805,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.2489210575415965,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.9477156647545346,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.4744807877632549,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.22013104847243836,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.2009328202347245,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.9448151236548838,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.09476198468889518,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.760476793561663,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.10199845022874277,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.6347829435888008,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.0319224218906946,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.1070329036602438,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.34407268342048625,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.7536320162964297,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.3700008392333984,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 11.56752151900492,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 8.95633222639065,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 8.131050631146351,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -4.431303589146484,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 3.9297160624900833,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.8958049859542996,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 3.587549642785504,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -8.695885912614765,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 6.8459344111635225,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 6.871016399883456,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 6.10842775483461,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -2.2871548713117362,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 4.200037960300326,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.854464526944863,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 3.9515587831319614,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -4.881956241927531,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.18900003433227397,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.9582499504089341,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.08799999237060518,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.39190006256103516,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.02765000343322299,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.1370749950408907,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 5.1409289458736795,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.4948028782436729,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 4.624757785827594,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -3.1956852202076114,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 4.322269475814112,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -3.8467707959659805,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.0725000926426479,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.16578565325055805,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.08933312828901219,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.7181934964054935,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 3.944348754806672,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -3.930008075864988,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.5101052731821965,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.3402689795286927,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.1100006103515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.18999481201171875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 2.3030223899798585,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.0144951589887152,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.0187215705243169,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.8848731202593996,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.7139012963775615,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.8847270083903087,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.5895224546877076,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.2885985630954222,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.418564717861538,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.0708206675184795,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.003901305787425,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 3.029021838094148,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.9842231941878055,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 6.634996521289472,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.22551331434125288,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 2.5253311075918106,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.15949974060058025,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.8649997711181641,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.034578857421877274,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.11036621093749943,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.017346973419194,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.1403718185424765,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.38011211348971674,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.968186620152145,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.10480963947232524,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.41940029444424987,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.18131392962554838,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.06568928874430835,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.009999956403459853,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.3135724748883928,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.017289242304536323,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.42945584491751165,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.14195703795977188,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.24519046444113624,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.9481589276020622,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.571824828568034,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.720001220703125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -13.32000732421875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_1d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 5.586462509033474,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 4.080111980370527,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_5d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 3.7583404683160797,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -3.8018571378711234,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_20d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.7610043405404063,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -11.283659990408346,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_60d_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -3.829752380525541,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -19.39305349876772,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_1d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.8648754011920778,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 1.9947961538633323,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_5d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 1.7357175920043382,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -1.6577084200363745,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_20d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.4906824427301633,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -7.533390477509183,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_60d_pp",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -3.4657432401790853,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -15.579123828080487,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma20",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -1.4220001220703011,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -4.790999603271473,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma50",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.40300018310546193,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.8886001586914176,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma200",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.11430000305176691,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.735850028991706,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma20_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.3399690946344087,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -5.37500555580852,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma50_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.21905106855291123,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -7.600804755215262,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma200_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.6139866131160687,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -10.332759086191626,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_sma",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.0007138933454244878,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.38499886648995485,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.017398066566931547,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.04724363815745258,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.drawdown_from_63d_high_pct",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.41168804575211126,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -7.616220121621852,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.volume_vs_previous20_ratio",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.16097528209392264,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.2092719758422692,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS2.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.1200000000000001,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.15000000000000036,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLH0A0HYM2.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.16000000000000014,
        "unit": "percentage_points"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.2200000000000002,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLC0A0CM.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.020000000000000018,
        "unit": "percentage_points"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.040000000000000036,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS10.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.0600000000000005,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.14000000000000057,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DFII10.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.040000000000000036,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.029999999999999805,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.T10YIE.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.010000000000000231,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.10999999999999988,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.STLFSI4.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.06130000000000002,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.CBOE_VIX.value",
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.539999999999999,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 6.219999999999999,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.GPRD.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -67.5849609375,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.GPRD_ACT.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -36.172332763671875,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.GPRD_THREAT.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -92.63170623779297,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.GPRD_MA7.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -43.773468017578125,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.GPRD_MA30.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -11.395751953125,
        "unit": "index"
      }
    ],
    "status": "comparable"
  }
]
```

## 判断依据 · 周五反弹是否足以支持重新提高风险

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 周五反弹是否足以支持重新提高风险 |
| 事实指标引用 | ["prices.SPY.distance_sma20_pct", "prices.QQQ.distance_sma20_pct", "prices.RSP.return_1d_pct"] |
| 推断与解释 | 盘前宽基上涨是改善，行业分化与缺乏常规广度使修复仍脆弱。 |
| 反证与缺口 | 周五芯片量价反弹是真实积极证据，但区间收盘偏低、等权未扩散。 |
| 确认条件 | 先看SPY734.58、QQQ654.00、SMH456.44周五低点附近回踩承接；再看742.21/664.52/476.25周五高点突破并回踩守住，RSP同步改善且至少两个收盘保留进展。实测常规VWAP可辅助，当前未取得不得声称已达成。 |
| 失效条件 | 跌破周五低点且反抽失败即下调；进一步跌破周四收盘733/647.05/447.73加强失效证据，后三个是历史收盘而非盘中低点。 |
| 观察期限 | 11月9–13日，盘中、收盘及下一交易日分层确认 |
| 条件式指导 | 条件未满足先观察；不以单次越线或涨跌幅指定最佳仓位。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相对早报盘前宽基/油价/VIX改善而NVDA独立走弱，尚无新完整常规日，保留双向确认。 |

## 判断依据 · 如何看板块轮动

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 如何看板块轮动 |
| 事实指标引用 | ["prices.XLF.return_5d_pct", "prices.XLV.return_20d_pct", "prices.OIH.return_5d_pct"] |
| 推断与解释 | 能源旧主线失败，金融医疗仅取得观察资格，不证明净流入。 |
| 反证与缺口 | XLF/RSP盘前有报价但较旧；不可把较早一笔成交当持续突破。 |
| 确认条件 | XLF先收复57.50，再看59.20及回踩；XLV守184附近再试189.66，RSP收复216.72附近动态20日线。当前低于这些参照不称已守住。 |
| 失效条件 | 金融或医疗持续失守回踩低点且相对SPY优势消失；RSP不跟随则仅局部强势。 |
| 观察期限 | 11月9–13日，盘中、收盘及下一交易日分层确认 |
| 条件式指导 | 条件未满足先观察；不以单次越线或涨跌幅指定最佳仓位。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相对早报盘前宽基/油价/VIX改善而NVDA独立走弱，尚无新完整常规日，保留双向确认。 |

## 判断依据 · AI供应链压力改善了吗

| 要素 | 记录 |
| --- | --- |
| 评估问题 | AI供应链压力改善了吗 |
| 事实指标引用 | ["prices.SMH.return_5d_pct", "prices.SMH.volume_vs_previous20_ratio"] |
| 推断与解释 | 交付、融资压力未证实解除；本次另有NVIDIA调查，不等于订单损失。H100指数8日3.00较7日3.04小降，尚远高于专门泡沫阈值。 |
| 反证与缺口 | H100截至8日3.00仍有韧性，韩国合作与云端股上涨反对整个需求消失；不等于项目现金流已改善。 |
| 确认条件 | 指引、投产、客户预付款和融资进展可核验且没有新增延期；价格在消息后守低点、跑赢QQQ，至少次日不回吐。SMH先收复476.25再谈进一步修复。 |
| 失效条件 | 新增延期/融资缺口扩大同时价格创新低；收入增长但现金回收或指引转弱；EPS过固定门槛并不足够。 |
| 观察期限 | 11月10–17日财报后1–3个交易日 |
| 条件式指导 | 条件未满足先观察；不以单次越线或涨跌幅指定最佳仓位。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相对早报盘前宽基/油价/VIX改善而NVDA独立走弱，尚无新完整常规日，保留双向确认。 |

## 判断依据 · 风险是在升还是降

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 风险是在升还是降 |
| 事实指标引用 | ["macro.CBOE_VIX.value", "macro.BAMLH0A0HYM2.value", "prices.^VIX3M.value"] |
| 推断与解释 | VIX23.38与CNN25显示恐慌缓解；同步期限结构和信用尚缺，不能宣布解除。 |
| 反证与缺口 | 本周油价和能源股大跌，发生风险消息也未必恢复上周趋势。 |
| 确认条件 | VIX持续回落且VIX/VIX3M回到1以下，HY/IG最新同口径利差收窄，同时宽基守低点并有更多行业参与；不能只看油价或单日波动回落。 |
| 失效条件 | VIX重返28.18附近、期限倒挂加深、信用继续走阔且指数失守周五低点；周末新供应冲击需另外确认。 |
| 观察期限 | 11月9–13日，盘中、收盘及下一交易日分层确认 |
| 条件式指导 | 条件未满足先观察；不以单次越线或涨跌幅指定最佳仓位。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相对早报盘前宽基/油价/VIX改善而NVDA独立走弱，尚无新完整常规日，保留双向确认。 |

## AI建设从订单增长转向交付与融资 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | NVIDIA独立调查仍在；新NVLink Fusion韩国合作及已公开国会简报请求分别核验。 |
| 事实：市场反应 | NVDA盘前-5.15%、SMH-0.30%，云端巨头上涨，与宽基反弹分化。 |
| 推断：解释 | 推断：治理/政策风险溢价压制单股，不等同全AI需求塌陷；合作计划也不是已兑现收入。 |
| 受益篮子 | ["资产负债表较强、现金回收可见的应用与买方观察篮子"] |
| 受损篮子 | ["NVDA", "MU", "VRT", "CRWV", "NBIS"] |
| 反证 | IREN订单租价与H100指数仍强，不能说需求崩溃。 合作姿态不能确认监管放行，抗议不能确认政府禁令。 |
| 下一催化剂 | 11日国会信函回复期限、17日财报；18日简报仅请求未确认 |
| 证据 | ["https://www.sec.gov/Archives/edgar/data/1878848/000187884826000065/irenreportsq1-fy27result.htm", "https://www.investing.com/news/stock-market-news/microsoft-is-winding-down-oracle-deal-to-rent-ai-cloud-capacity-bloomberg-news-reports-5008946", "https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/default.aspx", "https://au.investing.com/news/stock-market-news/coreweave-seeks-truce-with-texas-governorelect-hinojosa-4753439", "https://stopdirtydatacentres.eu/", "https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors"] |

## 选后政策预期与相对防御轮动 · 新增

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | AP周末回顾将本周AI建设担忧与州级政策变化联系；法案落地尚需独立核验。 |
| 事实：市场反应 | 周五XLF-0.59%、XLV-0.06%，相对周线优势尚不足支持追高；伯克希尔周末披露待周一消化。 |
| 推断：解释 | 监管预期会先压估值；州选举结果不等于全州数据中心禁令已生效。 |
| 受益篮子 | ["XLF", "XLV", "XLC"] |
| 受损篮子 | ["XLK", "SMH", "SKYY"] |
| 反证 | 市场整体仍跌，周五金融医疗未跟随芯片上涨，不能追相对强度。 伯克希尔Q3经营利润127.05亿美元低于上年134.85亿，同时回购96亿美元；回购不是全市场见底信号。 |
| 下一催化剂 | 正式政策文本、项目许可与CPI。 |
| 证据 | ["https://apnews.com/article/4ac9a6a3c35aeec37374fc8083bf9395", "https://www.bls.gov/schedule/2026/11_sched.htm", "https://berkshirehathaway.com/news/nov0726.pdf"] |

## 能源溢价消退后面对周末航运冲击 · 减弱

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 特朗普有条件降低新增打击预期，谈判未有突破；海峡与地区设施风险仍在。 |
| 事实：市场反应 | WTI/Brent盘前约跌3.01%/3.59%，不支持把新增冲突消息等同油价必涨。 |
| 推断：解释 | 推断：外交缓和溢价暂时超过新增供应恐惧；持续性需运输与库存/真实供应验证。 |
| 受益篮子 | ["供应受限时的能源观察篮子"] |
| 受损篮子 | ["航空运输及高能源成本行业"] |
| 反证 | 沙特警报解除、具体油轮身份未核验，且谈判可逆转价格。 |
| 下一催化剂 | 周日晚期货与周一现货/股票实际反应。 |
| 证据 | ["https://apnews.com/article/f7b507b55634985d6013d36265b3fbc0", "https://uk.marketscreener.com/news/oil-falls-as-trump-says-new-iran-attacks-unlikely-ce785fd3d988f42d"] |

## 强就业下的通胀与贴现率检验 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 10月新增就业16.5万；密歇根通胀预期下降但调查较早。 |
| 事实：市场反应 | 信用利差周际走阔，VIX期限倒挂；国债收益率周际回落并未阻止科技下跌。 |
| 推断：解释 | 下周CPI要结合收益率、信用和市场反应，不只看一个数据是否超预期。 |
| 受益篮子 | ["通胀回落时现金回报可见的成长观察篮子"] |
| 受损篮子 | ["高杠杆融资和高估值长久期资产"] |
| 反证 | H100与订单仍支持部分需求；利率下行本身不是见底保证。 |
| 下一催化剂 | 11/10 CPI、11/13 PPI、11/25 PCE。 |
| 证据 | ["https://www.bls.gov/news.release/empsit.nr0.htm", "https://www.sca.isr.umich.edu/", "https://www.bls.gov/schedule/2026/11_sched.htm", "https://www.bea.gov/news/schedule"] |

## 月球运输框架与航天业绩验证 · 新增

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | NASA官方7日选择八家公司参与CLPS2，十年框架合计上限100亿美元；未来任务仍需竞争。 |
| 事实：市场反应 | ARKX周五上涨5.08%，早于该公告，不将其归因为周末新消息。 |
| 推断：解释 | 推断：订单可见性主题有催化，但框架上限不是各公司收入或利润保证。 |
| 受益篮子 | ["FLY", "LUNR", "LMT", "NOC", "VOYG"] |
| 受损篮子 | ["缺现金或交付能力的高估值承包商"] |
| 反证 | 任务未分配、延期/成本超支；RKLB属相邻财报观察，不是该八家直接中标者。 |
| 下一催化剂 | RKLB周一盘后及未来具体任务授予 |
| 证据 | ["https://www.nasa.gov/news-release/nasa-awards-moon-base-transportation-technology-science-projects/"] |

## tc 报价（供应商时戳不等于成交时戳）

| 标的 | 价格 USD | 变化% | 观测时间 | 供应商时间 | 抓取时间 | 质量 |
| --- | --- | --- | --- | --- | --- | --- |
| MU | 684.84 | -0.75 | 2026-11-09T12:01:05+00:00 | 2026-11-09T12:01:05+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| XLV | 187.06 | 1.22 | 2026-11-09T12:00:13+00:00 | 2026-11-09T12:00:13+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| BABA | 107.66 | -1.63 | 2026-11-09T12:01:02+00:00 | 2026-11-09T12:01:02+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| SNDK | 820.46 | -1.75 | 2026-11-09T12:01:05+00:00 | 2026-11-09T12:01:05+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| GOOGL | 290.01 | 1.84 | 2026-11-09T12:01:01+00:00 | 2026-11-09T12:01:01+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| RSP | 218.25 | 1.02 | 2026-11-09T11:17:00+00:00 | 2026-11-09T11:17:00+00:00 | 2026-11-09T12:02:05.243626+00:00 | stale |
| DRAM | 39.02 | -0.69 | 2026-11-09T12:01:06+00:00 | 2026-11-09T12:01:06+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| CVX | 213.19 | 0.27 | 2026-11-09T11:20:00+00:00 | 2026-11-09T11:20:00+00:00 | 2026-11-09T12:02:05.243626+00:00 | stale |
| ARM | 173.00 | -0.93 | 2026-11-09T12:00:00+00:00 | 2026-11-09T12:00:00+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| IWM | 276.97 | 1.21 | 2026-11-09T12:01:00+00:00 | 2026-11-09T12:01:00+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| QCOM | 163.90 | -0.91 | 2026-11-09T12:00:37+00:00 | 2026-11-09T12:00:37+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| STX | 461.20 | 0.05 | 2026-11-09T12:00:03+00:00 | 2026-11-09T12:00:03+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| SPY | 739.85 | 0.62 | 2026-11-09T12:00:59+00:00 | 2026-11-09T12:00:59+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| CI | 294.00 | 0.14 | 2026-11-09T09:01:25+00:00 | 2026-11-09T09:01:25+00:00 | 2026-11-09T12:02:05.243626+00:00 | stale |
| GEV | 783.55 | 1.22 | 2026-11-09T11:42:00+00:00 | 2026-11-09T11:42:00+00:00 | 2026-11-09T12:02:05.243626+00:00 | stale |
| XLE | 61.75 | 0.21 | 2026-11-09T12:00:41+00:00 | 2026-11-09T12:00:41+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| NOW | 103.30 | 1.30 | 2026-11-09T11:42:00+00:00 | 2026-11-09T11:42:00+00:00 | 2026-11-09T12:02:05.243626+00:00 | stale |
| AVGO | 300.51 | 2.32 | 2026-11-09T12:00:51+00:00 | 2026-11-09T12:00:51+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| IGV | 99.55 | 0.68 | 2026-11-09T11:20:00+00:00 | 2026-11-09T11:20:00+00:00 | 2026-11-09T12:02:05.243626+00:00 | stale |
| META | 623.52 | 2.19 | 2026-11-09T12:00:51+00:00 | 2026-11-09T12:00:51+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| ORCL | 115.92 | -0.16 | 2026-11-09T12:00:55+00:00 | 2026-11-09T12:00:55+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| NVDA | 177.04 | -5.15 | 2026-11-09T12:01:01+00:00 | 2026-11-09T12:01:01+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| COIN | 131.60 | -2.34 | 2026-11-09T12:00:13+00:00 | 2026-11-09T12:00:13+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| NXPI | 246.36 | -0.78 | 2026-11-09T09:01:27+00:00 | 2026-11-09T09:01:27+00:00 | 2026-11-09T12:02:05.243626+00:00 | stale |
| VRT | 185.26 | 1.31 | 2026-11-09T12:00:27+00:00 | 2026-11-09T12:00:27+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| XOM | 166.00 | 0.08 | 2026-11-09T11:25:03+00:00 | 2026-11-09T11:25:03+00:00 | 2026-11-09T12:02:05.243626+00:00 | stale |
| SO | 92.33 | -0.01 | 2026-11-09T09:01:00+00:00 | 2026-11-09T09:01:00+00:00 | 2026-11-09T12:02:05.243626+00:00 | stale |
| COHR | 191.25 | -0.81 | 2026-11-09T11:44:00+00:00 | 2026-11-09T11:44:00+00:00 | 2026-11-09T12:02:05.243626+00:00 | stale |
| TAN | 46.45 | 1.91 | 2026-11-09T12:00:07+00:00 | 2026-11-09T12:00:07+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| ILMN | 214.50 | 0.64 | 2026-11-09T09:01:22+00:00 | 2026-11-09T09:01:22+00:00 | 2026-11-09T12:02:05.243626+00:00 | stale |
| INTC | 56.03 | -0.44 | 2026-11-09T12:01:06+00:00 | 2026-11-09T12:01:06+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| COP | 136.58 | 0.23 | 2026-11-09T12:00:06+00:00 | 2026-11-09T12:00:06+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| QQQ | 659.34 | 0.49 | 2026-11-09T12:01:00+00:00 | 2026-11-09T12:01:00+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| AMD | 465.98 | 3.77 | 2026-11-09T12:01:09+00:00 | 2026-11-09T12:01:09+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| CEG | 261.00 | 4.42 | 2026-11-09T12:00:55+00:00 | 2026-11-09T12:00:55+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| XLF | 57.91 | 1.31 | 2026-11-09T11:17:00+00:00 | 2026-11-09T11:17:00+00:00 | 2026-11-09T12:02:05.243626+00:00 | stale |
| GLD | 376.45 | 1.05 | 2026-11-09T12:00:35+00:00 | 2026-11-09T12:00:35+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| CRWV | 44.85 | -3.34 | 2026-11-09T12:00:51+00:00 | 2026-11-09T12:00:51+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| MSFT | 540.70 | 1.90 | 2026-11-09T12:01:02+00:00 | 2026-11-09T12:01:02+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| GDX | 89.56 | 2.24 | 2026-11-09T12:00:55+00:00 | 2026-11-09T12:00:55+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| LITE | 532.67 | -1.10 | 2026-11-09T12:00:52+00:00 | 2026-11-09T12:00:52+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| CAT | 565.95 | 1.31 | 2026-11-09T12:00:26+00:00 | 2026-11-09T12:00:26+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| TLT | 81.97 | 0.06 | 2026-11-09T12:00:35+00:00 | 2026-11-09T12:00:35+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| AMZN | 266.74 | 2.87 | 2026-11-09T12:00:42+00:00 | 2026-11-09T12:00:42+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| GLW | 106.62 | 0.46 | 2026-11-09T12:00:38+00:00 | 2026-11-09T12:00:38+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| PLTR | 160.70 | 0.20 | 2026-11-09T11:58:57+00:00 | 2026-11-09T11:58:57+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| SMH | 462.58 | -0.30 | 2026-11-09T12:00:55+00:00 | 2026-11-09T12:00:55+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| AAPL | 344.43 | 0.60 | 2026-11-09T12:00:35+00:00 | 2026-11-09T12:00:35+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| MRVL | 140.36 | -0.60 | 2026-11-09T12:00:48+00:00 | 2026-11-09T12:00:48+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |
| LLY | 1,382.10 | 2.08 | 2026-11-09T12:01:04+00:00 | 2026-11-09T12:01:04+00:00 | 2026-11-09T12:02:05.243626+00:00 | ok |

## 核心行情与风险代理

| 标的 | 价格/指数 | 单位 | 观测日 | 1日% | 5日% | 20日% | 质量 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 735.29 | USD_per_share | 2026-11-06 | 0.31 | -2.70 | -5.56 | ok |
| QQQ | 656.10 | USD_per_share | 2026-11-06 | 1.40 | -4.98 | -12.67 | ok |
| IWM | 273.67 | USD_per_share | 2026-11-06 | 0.99 | -2.03 | -1.89 | ok |
| RSP | 216.05 | USD_per_share | 2026-11-06 | -0.38 | -1.04 | 1.41 | ok |
| GLD | 372.52 | USD_per_share | 2026-11-06 | -0.79 | 4.71 | -3.14 | ok |
| GC=F | 4,074.90 | USD_per_troy_ounce | 2026-11-06 | -0.94 | 4.51 | -3.35 | ok |
| CL=F | 90.83 | USD_per_barrel | 2026-11-06 | 0.34 | -12.76 | -1.11 | ok |
| BZ=F | 98.32 | USD_per_barrel | 2026-11-06 | 0.03 | -16.42 | -6.11 | ok |
| TLT | 81.92 | USD_per_share | 2026-11-06 | -0.01 | 0.10 | 5.05 | ok |
| UUP | 29.13 | USD_per_share | 2026-11-06 | 0.73 | 0.45 | 0.38 | ok |
| HYG | 77.23 | USD_per_share | 2026-11-06 | -0.06 | -0.26 | 0.00 | ok |
| LQD | 104.53 | USD_per_share | 2026-11-06 | -0.12 | 0.25 | 2.07 | ok |
| ^VIX | 25.64 | index | 2026-11-06 | -9.01 | 32.03 | 72.78 | ok |
| ^VIX3M | 24.60 | index | 2026-11-06 | -3.72 | 18.38 | 38.44 | ok |
| ^VVIX | 121.94 | index | 2026-11-06 | -9.67 | 14.57 | 43.66 | ok |
| ^MOVE | 92.77 | index | 2026-11-06 | -5.26 | -7.42 | -7.87 | ok |
| NVDA | 186.64 | USD_per_share | 2026-11-06 | 2.78 | -8.80 | -18.60 | ok |
| MSFT | 530.61 | USD_per_share | 2026-11-06 | -0.99 | 1.67 | -0.83 | ok |
| AMZN | 259.30 | USD_per_share | 2026-11-06 | -0.35 | 7.88 | -1.19 | ok |
| GOOGL | 284.78 | USD_per_share | 2026-11-06 | 0.78 | 1.77 | -19.02 | ok |
| META | 610.15 | USD_per_share | 2026-11-06 | 0.84 | -0.79 | -15.10 | ok |
| CRWV | 46.40 | USD_per_share | 2026-11-06 | 6.28 | -15.44 | -43.47 | ok |
| MU | 690.00 | USD_per_share | 2026-11-06 | 5.12 | -22.01 | -32.93 | ok |
| DRAM | 39.29 | USD_per_share | 2026-11-06 | 6.16 | -18.16 | -31.30 | ok |
| VRT | 182.86 | USD_per_share | 2026-11-06 | 3.47 | -21.35 | -24.68 | ok |

## 跨资产风险解释

风险边际缓解，但尚未解除。最新可核验分钟观测：WTI88.10、Brent94.79较供应商前收约-3.01%/-3.59%，黄金期货4120.30约+1.11%；油价回落与有条件外交缓和报道一致，不证明停火已完成或运输已恢复。VIX23.38（11:46UTC）较周五25.64回落；三个月VIX只取得周五24.60，不混时点计算当前期限比。CNN浏览器更新至9日06:45:01EST，25、前收22，页面仍标Extreme Fear。周五VIX期限比约1.042仍是历史背景。FRED2年4.46%、10年4.84%、实际10年2.60%、HY348bp、IG93bp截至5日；Yahoo10年4.859%是6日观测，不能称今日利率下跌。GPR截至2日、金融压力截至10月30日，不覆盖周末冲突。避险/战争风险以黄金、油、美元、波动、利率及信用并列；能源设施损害和谈判结果均有不确定性，不生成统一战争指数。

## 宏观与地缘风险指标

| 指标 | 数值 | 单位 | 观测日 | 20次观测变化 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- | --- |
| DGS2 | 4.46 | percent | 2026-11-05 | -0.31 | lagged | https://fred.stlouisfed.org/series/DGS2 |
| BAMLH0A0HYM2 | 3.48 | percentage_points | 2026-11-05 | 0.33 | lagged | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| BAMLC0A0CM | 0.93 | percentage_points | 2026-11-05 | 0.11 | lagged | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| DGS10 | 4.84 | percent | 2026-11-05 | -0.44 | lagged | https://fred.stlouisfed.org/series/DGS10 |
| DFII10 | 2.60 | percent | 2026-11-05 | -0.32 | lagged | https://fred.stlouisfed.org/series/DFII10 |
| T10YIE | 2.23 | percent | 2026-11-06 | -0.12 | ok | https://fred.stlouisfed.org/series/T10YIE |
| STLFSI4 | -0.52 | index | 2026-10-30 | 0.24 | lagged | https://fred.stlouisfed.org/series/STLFSI4 |
| CBOE_VIX | 25.64 | index | 2026-11-06 | 10.80 | ok | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| GPRD | 97.67 | index | 2026-11-02 | -213.94 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_ACT | 113.60 | index | 2026-11-02 | -291.60 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_THREAT | 94.75 | index | 2026-11-02 | -209.43 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_MA7 | 137.64 | index | 2026-11-02 | -46.66 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_MA30 | 164.04 | index | 2026-11-02 | -2.33 | lagged | https://www.matteoiacoviello.com/gpr.htm |

## CNN Fear & Greed

```json
{
  "value": 25,
  "rating": "Extreme Fear",
  "observed_at": "2026-11-09T06:45:01-05:00",
  "retrieved_at": "2026-11-09T12:04:00+00:00",
  "source": "https://www.cnn.com/markets/fear-and-greed",
  "quality": "verified_browser",
  "previous_close": 22,
  "one_week_ago": 19,
  "note": "浏览器加载完成后核验25；页面Extreme Fear，月前43、年前20。API418由浏览器补核。"
}
```

## 19 板块与主题 ETF：价格量能证据

| 标的 | 板块 | 1日% | 5日% | 20日% | 相对SPY 1日pp | 相对SPY 5日pp | 相对SPY 20日pp | 成交量/前20日 | 观测日 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLK | 科技 | 1.45 | -8.23 | -17.12 | 1.14 | -5.52 | -11.57 | 1.75 | 2026-11-06 |
| XLE | 能源 | -0.02 | -12.00 | -5.32 | -0.33 | -9.29 | 0.24 | 1.16 | 2026-11-06 |
| XLF | 金融 | -0.59 | 1.15 | 4.44 | -0.90 | 3.85 | 10.00 | 0.97 | 2026-11-06 |
| XLI | 工业 | 0.12 | -2.83 | -3.89 | -0.19 | -0.12 | 1.67 | 0.92 | 2026-11-06 |
| XLV | 医疗 | -0.06 | -0.04 | 8.19 | -0.37 | 2.67 | 13.75 | 1.37 | 2026-11-06 |
| XLP | 必需消费 | -1.28 | 0.74 | 7.97 | -1.59 | 3.44 | 13.53 | 1.35 | 2026-11-06 |
| XLY | 可选消费 | -0.05 | 1.91 | 4.19 | -0.36 | 4.61 | 9.75 | 1.21 | 2026-11-06 |
| XLC | 通信 | 0.43 | 4.89 | -5.06 | 0.12 | 7.60 | 0.49 | 0.84 | 2026-11-06 |
| XLU | 公用事业 | -0.39 | -0.69 | 4.15 | -0.71 | 2.01 | 9.71 | 1.00 | 2026-11-06 |
| XLRE | 房地产 | -0.68 | 1.92 | 5.74 | -0.99 | 4.63 | 11.30 | 1.03 | 2026-11-06 |
| XLB | 材料 | -0.73 | -1.50 | 5.10 | -1.04 | 1.21 | 10.66 | 1.30 | 2026-11-06 |
| SMH | 半导体 | 3.62 | -11.20 | -23.10 | 3.31 | -8.50 | -17.54 | 1.53 | 2026-11-06 |
| IGV | 软件 | -0.13 | -5.19 | -12.24 | -0.44 | -2.48 | -6.68 | 0.89 | 2026-11-06 |
| XOP | 油气开采 | -0.19 | -14.72 | -9.27 | -0.50 | -12.01 | -3.71 | 1.23 | 2026-11-06 |
| OIH | 油服 | 2.44 | -13.47 | -8.36 | 2.13 | -10.76 | -2.80 | 0.91 | 2026-11-06 |
| ITA | 航空与国防 | 1.28 | -1.33 | 0.14 | 0.96 | 1.37 | 5.70 | 0.71 | 2026-11-06 |
| ARKX | 航天主题 | 5.08 | -4.60 | -11.74 | 4.77 | -1.90 | -6.18 | 1.29 | 2026-11-06 |
| KRE | 区域银行 | -0.15 | 0.26 | 4.62 | -0.46 | 2.97 | 10.18 | 0.63 | 2026-11-06 |
| SKYY | 云计算 | -0.49 | -8.34 | -16.26 | -0.80 | -5.63 | -10.70 | 0.79 | 2026-11-06 |

## 资金证据分层

同端点11月6日：ARKX +5.08%（5日-4.60%）；SMH +3.62%（5日-11.20%）；OIH +2.44%（5日-13.47%）；XLK +1.45%（5日-8.23%）；ITA +1.28%（5日-1.33%）；XLC +0.43%（5日+4.89%）；XLI +0.12%（5日-2.83%）；XLE -0.02%（5日-12.00%）；XLY -0.05%（5日+1.91%）；XLV -0.06%（5日-0.04%）；IGV -0.13%（5日-5.19%）；KRE -0.15%（5日+0.26%）；XOP -0.19%（5日-14.72%）；XLU -0.39%（5日-0.69%）；SKYY -0.49%（5日-8.34%）；XLF -0.59%（5日+1.15%）；XLRE -0.68%（5日+1.92%）；XLB -0.73%（5日-1.50%）；XLP -1.28%（5日+0.74%）。7/19是ETF样本上涨数，不等于全市场广度。芯片、航天、油服有反弹，但周线仍弱；金融和医疗需要自身止跌，软件/云未跟上。 当前盘前宽基SPY+0.62%、QQQ+0.49%，SMH-0.30%，MSFT/AMZN/GOOGL/META均高于周五收盘，NVDA约-5.15%，可见云端巨头与芯片治理风险分化。XLF、RSP等分钟成交较早、部分ETF无有效新成交，因此不能计算当前19ETF广度或直接给出全行业轮动排名。优先观察宽基/云端的回踩承接，金融医疗需常规时段确认，半导体提高门槛，能源受油价下行压制。发行人SMH页面截至6日NAV464.02、NVDA权重20.75%，说明单股风险可传导ETF；没有多日份额与拆分桥，不能推净申赎。ICI重查仍是11月3日发布、截至10月28日一周净发行459.06亿美元，国内股票265.90亿、债券142.34亿、商品-18.89亿；这是滞后背景，不代表今天主力方向。

## 最近可核验 ETF 申赎窗口

| 标的 | 金额 USD million | 起始日 | 结束日 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- |

## Polymarket 搜索覆盖与限制

本轮重新采集配置和全板块关键词，另主动20组Gamma搜索AI泡沫/融资评级、银行/衰退、Fed/CPI、沙特/伊朗/Khor Mor、Texas数据中心、Apple/CXMT、Anthropic、NVIDIA治理及RKLB。每组10项，NVIDIA76项及Khor Mor21项等截断；后者含无关体育结果。16项旧规则hash核验一致，新增6831494有效停火合约；未找到高质量工业/软件新增合约不等于无风险。

## Polymarket · 值得警惕的信号

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["AI bubble burst in 2026?", "期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。", "https://polymarket.com/event/ai-bubble-burst-by"] | [7.249999999999999, {"status": "comparable", "change_pp": -0.9500000000000008}] | {"spread": 0.0010000000000000009, "volume24h_usd": 40961.66970799999, "liquidity_usd": 192722.26013, "quality_flags": [], "retrieved_at": "2026-11-09T12:01:16.293007+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["AI专门阈值，不能解释为普通回调概率", "融资/资本开支/估值"] | ["三项规则证据逐项核验", "单只股大跌或主观泡沫报道不算"] | [null, null] |
| ["Oracle downgraded to junk by Moody's or S&P by December 31, 2026?", "2026年12月31日美东23:59前，Moody’s或S&P正式将Oracle长期主体或高级无担保债评级降至Ba1/BB+或更低才算Yes；负面展望或观察名单不算。低成交量与宽价差，仅作低置信度观察。", "https://polymarket.com/event/oracle-downgraded-to-junk-by-moodys-or-sp-by"] | [9.2, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.14200000000000002, "volume24h_usd": 20.0, "liquidity_usd": 631.50958, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"], "retrieved_at": "2026-11-09T12:01:01.689393+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["正式信用降级的专门事件；极宽价差与低成交，不把中间价波动当信用改善。", "信用融资成本"] | ["Moody’s/S&P正式降至非投资级", "负面观察/展望不是降级"] | [null, null] |
| ["Military action against Saudi Oil Pipeline (East-West) by November 30?", "11月30日23:59利雅得时间前，合格空袭或地对地导弹（含指定单向攻击无人机）直接命中沙特东西输油管或泵站则Yes；不要求已证明显著损害。拦截残骸、小型短程弹药、地面入侵、炮火、网络攻击或未执行威胁不算。官方沙特信息与可信报道共识，冲突可等待三完整日。不同期限不拼接。", "https://polymarket.com/event/military-action-against-saudi-oil-pipeline-east-west-byptptpt"] | [31.0, {"status": "comparable", "change_pp": -2.500000000000002}] | {"spread": 0.020000000000000018, "volume24h_usd": 2009.338856, "liquidity_usd": 30254.6311, "quality_flags": [], "retrieved_at": "2026-11-09T12:01:01.581187+00:00", "contract_end_at": "2026-11-30T20:59:00+00:00"} | ["仅指定东西管道/泵站命中；沙特阿美办公楼、其他油气田或油轮事件不自动触发。", "油价/通胀/利润率"] | ["专门地域和武器条件独立确认", "威胁、残骸或其它航道事故不算"] | [null, null] |
| ["Jensen Huang announced resignation or removal by December 31?", "年末23:59美东前，黄仁勋/NVIDIA或授权代表正式明确宣布辞任或被撤去CEO，且预定在宣布后18个月内实施则Yes；不要求年内实际离任。临时休假、停职、条件式考虑、未被接受辞呈和媒体单独传闻不算。以官方信息优先；不得把调查直接视为离任。", "https://polymarket.com/event/jensen-huang-announced-resignation-or-removal-by-december-31"] | [10.5, {"status": "comparable", "change_pp": -6.000000000000001}] | {"spread": 0.009999999999999995, "volume24h_usd": 203645.612051, "liquidity_usd": 33280.5329, "quality_flags": [], "retrieved_at": "2026-11-09T12:01:16.293007+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["同规则报价较早报下降6个百分点，但NVDA盘前更弱：离任概率与经营/估值风险不是同一变量。", "管理连续性、政策限制与NVDA/SMH风险溢价"] | ["公司正式更新及现货/行业相对走弱共同核验", "调查澄清且经营/价格保持，不凭盘口即认定离任"] | [null, null] |

## Polymarket · 有参考价值的事件

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Will the Fed increase interest rates by 25 bps after the December 2026 meeting?", "以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。", "https://polymarket.com/event/fed-decision-in-december-20260729232808632"] | [76.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.010000000000000009, "volume24h_usd": 30189.727356, "liquidity_usd": 742866.8769, "quality_flags": [], "retrieved_at": "2026-11-09T12:01:16.293007+00:00", "contract_end_at": "2026-12-09T23:59:00+00:00"} | ["12月单次加息25bp合约；CME动态概率未独立核验，不混为Fed承诺。", "贴现率"] | ["官方政策与经济数据核验", "报价变化不等于实际决策"] | [null, null] |
| ["Strait of Hormuz traffic returns to normal by December 31?", "期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。", "https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31"] | [8.5, {"status": "comparable", "change_pp": 2.0000000000000004}] | {"spread": 0.009999999999999995, "volume24h_usd": 140458.569745, "liquidity_usd": 353896.1167, "quality_flags": [], "retrieved_at": "2026-11-09T12:01:16.293007+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["海峡恢复按IMF船流阈值，不按谈判标题", "能源供应与运输"] | ["7日通行均值达60", "口头开放不算"] | [null, null] |
| ["Will Anthropic IPO by December 31, 2026?", "Anthropic股份在2026年12月31日23:59美东前于公开证券交易所挂牌并开始交易才为Yes；仅提交S-1不算。被已上市公司收购则No。官方文件/公司与交易所公告优先，可信报道共识可辅助。", "https://polymarket.com/event/anthropic-ipo-by"] | [87.2, {"status": "comparable", "change_pp": 0.14999999999999458}] | {"spread": 0.006000000000000005, "volume24h_usd": 7485.144066999999, "liquidity_usd": 51812.44741, "quality_flags": [], "retrieved_at": "2026-11-09T12:01:04.307019+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["正式上市交易与融资退出窗口；提交申请不等于IPO完成。", "融资退出渠道"] | ["交易所实际开始交易", "只提交文件不算"] | [null, null] |
| ["Will Apple purchase memory CXMT chips in 2026?", "2026年12月31日23:59ET前Apple官方宣布使用/购买/采购CXMT存储器即可Yes，不要求同期交付；经确认达成采购或供货协议也可。官方信息优先、可信报道共识辅助。不等同HBM已量产或全球利润率下降。", "https://polymarket.com/event/will-apple-purchase-memory-cxmt-chips-in-2026-20260630171913147"] | [18.0, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.01999999999999999, "volume24h_usd": 101.333734, "liquidity_usd": 1640.358, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"], "retrieved_at": "2026-11-09T12:01:04.938061+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["中国存储竞争的专门采购事件", "DRAM采购与议价"] | ["正式采购公告/可信报道证实", "不等于HBM或NAND利润已崩溃"] | [null, null] |
| ["Will Texas enact a data center moratorium by June 30, 2027?", "2027年6月30日23:59美东前，Texas以州法律或宪法条款强制暂停全州新数据中心（或覆盖所有单设施超100MW者）才算Yes；仅行政/机构命令、地方暂停、税惠撤销不算。以立法日期而非生效日判断，竞选承诺不算。", "https://polymarket.com/event/texas-enacts-data-center-moratorium-by-20260928"] | [17.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.009999999999999981, "volume24h_usd": 77.99, "liquidity_usd": 35491.7707, "quality_flags": ["volume24h_under_1000_or_unknown"], "retrieved_at": "2026-11-09T12:01:05.595244+00:00", "contract_end_at": "2027-07-01T03:59:00+00:00"} | ["Texas全州法定暂停，期限不同不能拼接；要求州级成文法制定，非仅行政令。", "建设许可、投产进度与贴现率"] | ["符合范围的州法律或宪法条款正式制定；不要求已经实施", "地方限制、提案或选举言论不算"] | [null, null] |
| ["US x Iran Effective Ceasefire by November 15?", "须完成连续14个伊朗标准时间日，美国未对伊朗陆地及内水实施命中目标的合资格空袭/地对地导弹攻击，且该14天首日在创建后至11月15日范围内；最后一次合资格行动次日为首日，无行动则创建日为首日。拦截碎片、威胁、海域/领空、地面入侵、网络、小型武器/部分小型袭击等不算。第14日后再留3个日历日报道窗口，按官方信息及可信报道综合裁定。不是双方全面停火，也不要求14天在15日前完成。", "https://polymarket.com/event/us-x-iran-effective-ceasefire-begins-by-2-week-pause-20261108"] | [42.5, {"status": "no_baseline"}] | {"spread": 0.010000000000000009, "volume24h_usd": 73140.62569300001, "liquidity_usd": 52878.8985, "quality_flags": [], "retrieved_at": "2026-11-09T12:01:16.293007+00:00", "contract_end_at": "2026-11-15T20:29:00+00:00"} | ["新观察42.5%；只衡量特定美国攻击的连续14日间隔，不代表全面和平或海峡恢复。", "能源风险溢价、通胀与风险偏好"] | ["逐日核验合资格行动与14日及额外3日报道窗口", "发生符合规则的命中行动重新计时；口头缓和不算完成"] | [null, null] |

## Polymarket · 将要发生的事件及概率

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Will Core CPI MoM be 0.2% in October?", "按BLS首次发布2026年10月季调核心CPI月环比一位小数恰为0.2%结算；不是超过此值，也非同比或总体CPI。计划11月10日08:30ET；若延期，按规则等至下一次计划发布，仍缺则用最近可用月。", "https://polymarket.com/event/core-cpi-mom-october-2026"] | [48.5, {"status": "comparable", "change_pp": 1.5000000000000013}] | {"spread": 0.04999999999999999, "volume24h_usd": 442.23, "liquidity_usd": 1924.5586, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"], "retrieved_at": "2026-11-09T12:01:16.293007+00:00", "contract_end_at": "2026-11-11T04:59:00+00:00"} | ["核心CPI环比恰0.2%；不是低于门槛累计概率", "利率与风险偏好"] | ["BLS首次值及股债汇反应", "低量/宽价差不能替代官方数据"] | ["2026-11-10T08:30:00-05:00", "https://www.bls.gov/schedule/2026/11_sched.htm"] |
| ["Will Nvidia (NVDA) beat quarterly earnings?", "NVDA下一次财报首次公布的non-GAAP EPS按美分取整须严格超过固定2.53美元，不是动态一致预期。若缺失依规则转SeekingAlpha，再经96小时转GAAP；预计日后45天未发布为No，后续修订通常不计。低成交、极端报价不等于股票上涨胜率。", "https://polymarket.com/event/nvda-quarterly-earnings-nongaap-eps-11-17-2026-2pt53"] | [93.7, {"status": "comparable", "change_pp": -0.09999999999998899}] | {"spread": 0.10399999999999998, "volume24h_usd": null, "liquidity_usd": 642.4275, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"], "retrieved_at": "2026-11-09T12:02:55.253363+00:00", "contract_end_at": "2026-11-17T22:00:00+00:00"} | ["固定EPS门槛，宽价差降低解释力；超预期不能排除治理/指引风险。", "需求与利润兑现"] | ["首次EPS/指引/现金流同时看", "业绩达标仍可能股价下跌"] | ["2026-11-17T16:20:00-05:00", "https://nvidianews.nvidia.com/news/nvidia-sets-conference-call-for-third-quarter-financial-results-6928873"] |
| ["Will Rocket Lab (RKLB) beat quarterly earnings?", "RKLB下一季度首次GAAP EPS按美分取整严格大于固定-0.07美元为Yes，非动态预期；首选官方稀释EPS，缺失按规则用基本EPS/SeekingAlpha。无EPS96小时或预计日45天仍未发布为No；后续修订通常不算。低流动性，不能等同股价上涨。", "https://polymarket.com/event/rklb-quarterly-earnings-gaap-eps-11-09-2026-neg0pt07"] | [24.0, {"status": "comparable", "change_pp": -4.0000000000000036}] | {"spread": 0.01999999999999999, "volume24h_usd": 525.378369, "liquidity_usd": 475.397, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"], "retrieved_at": "2026-11-09T12:01:08.527141+00:00", "contract_end_at": "2026-11-09T22:00:00+00:00"} | ["今晚盘后财报；GAAP固定EPS门槛，低流动性仅参考。", "航天交付、毛利与现金消耗"] | ["官方EPS与指引并看", "单项EPS达标但现金消耗/交付恶化"] | ["2026-11-09T17:00:00-05:00", "https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-announces-date-third-quarter-2026-financial-results"] |

## Jensen Huang announced resignation or removal by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1343940 / 6882826 |
| Yes 概率 % | 10.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -6.000000000000001} |
| 24h成交量 / 流动性 USD | [203645.612051, 33280.5329] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 年末23:59美东前，黄仁勋/NVIDIA或授权代表正式明确宣布辞任或被撤去CEO，且预定在宣布后18个月内实施则Yes；不要求年内实际离任。临时休假、停职、条件式考虑、未被接受辞呈和媒体单独传闻不算。以官方信息优先；不得把调查直接视为离任。 |
| 规则指纹 | df05f785aa4ae5976ef45bac70ab0440fbd316f96ed73e312f856beec7cea37e |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-09T11:59:25.167351Z |
| 抓取时间 | 2026-11-09T12:01:16.293007+00:00 |
| 来源 | https://polymarket.com/event/jensen-huang-announced-resignation-or-removal-by-december-31 |

## Strait of Hormuz traffic returns to normal by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 455875 / 2176270 |
| Yes 概率 % | 8.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, -3.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 2.0000000000000004} |
| 24h成交量 / 流动性 USD | [140458.569745, 353896.1167] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。 |
| 规则指纹 | b0c8ba27f4437b0d8ab819ae170bec118166232e39cdcaefb95bd352d29073d4 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-09T11:57:26.179687Z |
| 抓取时间 | 2026-11-09T12:01:16.293007+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31 |

## US x Iran Effective Ceasefire by November 15?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1337182 / 6831494 |
| Yes 概率 % | 42.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [1.0, null] |
| 与上一快照可比变化 | {"status": "no_baseline"} |
| 24h成交量 / 流动性 USD | [73140.62569300001, 52878.8985] |
| 价差 pp | 1.00 |
| 到期 | 2026-11-15T20:29:00+00:00 |
| 结算规则摘要 | 须完成连续14个伊朗标准时间日，美国未对伊朗陆地及内水实施命中目标的合资格空袭/地对地导弹攻击，且该14天首日在创建后至11月15日范围内；最后一次合资格行动次日为首日，无行动则创建日为首日。拦截碎片、威胁、海域/领空、地面入侵、网络、小型武器/部分小型袭击等不算。第14日后再留3个日历日报道窗口，按官方信息及可信报道综合裁定。不是双方全面停火，也不要求14天在15日前完成。 |
| 规则指纹 | c70e370d0e95bf9245a1a527f4f02bb307f13aa2766e1cc24004c7559bfb4b53 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-09T11:59:25.167351Z |
| 抓取时间 | 2026-11-09T12:01:16.293007+00:00 |
| 来源 | https://polymarket.com/event/us-x-iran-effective-ceasefire-begins-by-2-week-pause-20261108 |

## AI bubble burst in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 691340 |
| Yes 概率 % | 7.25 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.9, 0.7] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.9500000000000008} |
| 24h成交量 / 流动性 USD | [40961.66970799999, 192722.26013] |
| 价差 pp | 0.10 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | fc153b2136a8dfbadcd169dce1add40690acb1748566b99716fe7ae8fcb07330 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-09T11:55:26.49438Z |
| 抓取时间 | 2026-11-09T12:01:16.293007+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## Will the Fed increase interest rates by 25 bps after the December 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 770450 / 3215008 |
| Yes 概率 % | 76.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, 6.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [30189.727356, 742866.8769] |
| 价差 pp | 1.00 |
| 到期 | 2026-12-09T23:59:00+00:00 |
| 结算规则摘要 | 以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。 |
| 规则指纹 | 933a10a15eeec0ff1de30468fa20540301ed243f75cc3572d42946192f81a123 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-09T11:59:25.167351Z |
| 抓取时间 | 2026-11-09T12:01:16.293007+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-december-20260729232808632 |

## AI bubble burst by June 30, 2027?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 4838928 |
| Yes 概率 % | 25.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-1.0, 3.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 1.0000000000000009} |
| 24h成交量 / 流动性 USD | [2176.773509, 70859.2817] |
| 价差 pp | 1.00 |
| 到期 | 2027-07-01T03:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | bd0420587e08487fffa5050e7fd9b79ffff909a9f843d3f620207ee859462505 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-09T11:55:26.49438Z |
| 抓取时间 | 2026-11-09T12:01:16.293007+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## Tesla and SpaceX merger officially announced by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 192962 / 2252540 |
| Yes 概率 % | 8.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.5, -7.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.49999999999999906} |
| 24h成交量 / 流动性 USD | [903.456957, 22098.7564] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59纽约时间前，Tesla或SpaceX正式宣布双方合并或一方收购另一方的控制权即Yes；无需在期限内完成交易。控制权通常为过半权益或等效治理权；少数股权投资及仅讨论不算。以公司公告或可信报道共识核验；旧URL中的june-30不是本合约期限。 |
| 规则指纹 | 909906ae3b6db7e473468713ea6a1e1e4cf4c931fe247c7d3d576e7986513008 |
| 质量 | ["volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-09T11:51:26.010796Z |
| 抓取时间 | 2026-11-09T12:01:16.293007+00:00 |
| 来源 | https://polymarket.com/event/tesla-and-spacex-merger-officially-announced-by-june-30 |

## Will Core CPI MoM be 0.2% in October?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1189688 / 5699271 |
| Yes 概率 % | 48.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [1.5, 6.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 1.5000000000000013} |
| 24h成交量 / 流动性 USD | [442.23, 1924.5586] |
| 价差 pp | 5.00 |
| 到期 | 2026-11-11T04:59:00+00:00 |
| 结算规则摘要 | 按BLS首次发布2026年10月季调核心CPI月环比一位小数恰为0.2%结算；不是超过此值，也非同比或总体CPI。计划11月10日08:30ET；若延期，按规则等至下一次计划发布，仍缺则用最近可用月。 |
| 规则指纹 | 45dda9ee16dc73ce90be8c4ebccc0c3d9bb30b030af1c018876e6a0f462eb329 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-09T11:57:26.179687Z |
| 抓取时间 | 2026-11-09T12:01:16.293007+00:00 |
| 来源 | https://polymarket.com/event/core-cpi-mom-october-2026 |

## Will Core CPI MoM be 0.3% in October?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1189688 / 5699272 |
| Yes 概率 % | 32.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-1.5, -4.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -1.0000000000000009} |
| 24h成交量 / 流动性 USD | [383.474138, 1197.0113] |
| 价差 pp | 4.00 |
| 到期 | 2026-11-11T04:59:00+00:00 |
| 结算规则摘要 | 按BLS首次发布2026年10月季调核心CPI月环比一位小数恰为0.3%结算；不是超过此值，也非同比或总体CPI。计划11月10日08:30ET；若延期，按规则等至下一次计划发布，仍缺则用最近可用月。 |
| 规则指纹 | d590364746a9b5934e2a977dbef3e79e36f630c91f1b4964443a078174d83e57 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-09T11:59:25.167351Z |
| 抓取时间 | 2026-11-09T12:01:16.293007+00:00 |
| 来源 | https://polymarket.com/event/core-cpi-mom-october-2026 |

## Oracle downgraded to junk by Moody's or S&P by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1219847 / 5939428 |
| Yes 概率 % | 9.20 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [7.0, -8.3] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [20.0, 631.50958] |
| 价差 pp | 14.20 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日美东23:59前，Moody’s或S&P正式将Oracle长期主体或高级无担保债评级降至Ba1/BB+或更低才算Yes；负面展望或观察名单不算。低成交量与宽价差，仅作低置信度观察。 |
| 规则指纹 | cb29bc6ea2fb2a6cd1d97dc489f0163f0b47e0cb2d31a9cbb3fe5dda90eb10c4 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"] |
| 元数据更新（不是成交时间） | 2026-11-09T11:51:26.010796Z |
| 抓取时间 | 2026-11-09T12:01:01.689393+00:00 |
| 来源 | https://polymarket.com/event/oracle-downgraded-to-junk-by-moodys-or-sp-by |

## Military action against Saudi Oil Pipeline (East-West) by November 30?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1147445 / 5401796 |
| Yes 概率 % | 31.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-8.5, -5.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -2.500000000000002} |
| 24h成交量 / 流动性 USD | [2009.338856, 30254.6311] |
| 价差 pp | 2.00 |
| 到期 | 2026-11-30T20:59:00+00:00 |
| 结算规则摘要 | 11月30日23:59利雅得时间前，合格空袭或地对地导弹（含指定单向攻击无人机）直接命中沙特东西输油管或泵站则Yes；不要求已证明显著损害。拦截残骸、小型短程弹药、地面入侵、炮火、网络攻击或未执行威胁不算。官方沙特信息与可信报道共识，冲突可等待三完整日。不同期限不拼接。 |
| 规则指纹 | de6f019a1972387984a02c6a8e7cef39e331ff99c1895cf1bba902450d550441 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-09T11:59:25.167351Z |
| 抓取时间 | 2026-11-09T12:01:01.581187+00:00 |
| 来源 | https://polymarket.com/event/military-action-against-saudi-oil-pipeline-east-west-byptptpt |

## Will Anthropic IPO by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 549019 / 2413330 |
| Yes 概率 % | 87.20 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.7, -5.7] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.14999999999999458} |
| 24h成交量 / 流动性 USD | [7485.144066999999, 51812.44741] |
| 价差 pp | 0.60 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | Anthropic股份在2026年12月31日23:59美东前于公开证券交易所挂牌并开始交易才为Yes；仅提交S-1不算。被已上市公司收购则No。官方文件/公司与交易所公告优先，可信报道共识可辅助。 |
| 规则指纹 | 91cad6e5770d0b925976d3fbba5e8c61a7f0561a5ee40474d459b9851b8bf4e0 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-09T11:59:25.167351Z |
| 抓取时间 | 2026-11-09T12:01:04.307019+00:00 |
| 来源 | https://polymarket.com/event/anthropic-ipo-by |

## Will Apple purchase memory CXMT chips in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 652109 / 2745561 |
| Yes 概率 % | 18.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.5, 7.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [101.333734, 1640.358] |
| 价差 pp | 2.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59ET前Apple官方宣布使用/购买/采购CXMT存储器即可Yes，不要求同期交付；经确认达成采购或供货协议也可。官方信息优先、可信报道共识辅助。不等同HBM已量产或全球利润率下降。 |
| 规则指纹 | f9ba1bef2cbca87ceaec660e27ab85bc0edd5723bc3e5e58937caf9155b3e790 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-09T11:51:26.010796Z |
| 抓取时间 | 2026-11-09T12:01:04.938061+00:00 |
| 来源 | https://polymarket.com/event/will-apple-purchase-memory-cxmt-chips-in-2026-20260630171913147 |

## Will Texas enact a data center moratorium by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1103684 / 5123855 |
| Yes 概率 % | 1.90 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.1, -0.15] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [56.84, 52477.20469] |
| 价差 pp | 0.20 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年末23:59美东前，Texas以州法律或宪法条款强制暂停全州新数据中心（或覆盖所有单设施超100MW者）才算Yes；仅行政/机构命令、地方暂停、税惠撤销不算。以立法日期而非生效日判断，竞选承诺不算。 |
| 规则指纹 | b3e9528c7bb241316ba9beb5332075225a4976826229cd820fec02a115957e3a |
| 质量 | ["volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-09T11:57:26.179687Z |
| 抓取时间 | 2026-11-09T12:01:05.595244+00:00 |
| 来源 | https://polymarket.com/event/texas-enacts-data-center-moratorium-by-20260928 |

## Will Texas enact a data center moratorium by June 30, 2027?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1103684 / 5123856 |
| Yes 概率 % | 17.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, 3.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [77.99, 35491.7707] |
| 价差 pp | 1.00 |
| 到期 | 2027-07-01T03:59:00+00:00 |
| 结算规则摘要 | 2027年6月30日23:59美东前，Texas以州法律或宪法条款强制暂停全州新数据中心（或覆盖所有单设施超100MW者）才算Yes；仅行政/机构命令、地方暂停、税惠撤销不算。以立法日期而非生效日判断，竞选承诺不算。 |
| 规则指纹 | bad230b7f527696e74d48176c1f04e0fa6e22d9b444c004e912067120edc074f |
| 质量 | ["volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-09T11:59:25.167351Z |
| 抓取时间 | 2026-11-09T12:01:05.595244+00:00 |
| 来源 | https://polymarket.com/event/texas-enacts-data-center-moratorium-by-20260928 |

## Will Nvidia (NVDA) beat quarterly earnings?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1308738 / 6639362 |
| Yes 概率 % | 93.70 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-2.1, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.09999999999998899} |
| 24h成交量 / 流动性 USD | [null, 642.4275] |
| 价差 pp | 10.40 |
| 到期 | 2026-11-17T22:00:00+00:00 |
| 结算规则摘要 | NVDA下一次财报首次公布的non-GAAP EPS按美分取整须严格超过固定2.53美元，不是动态一致预期。若缺失依规则转SeekingAlpha，再经96小时转GAAP；预计日后45天未发布为No，后续修订通常不计。低成交、极端报价不等于股票上涨胜率。 |
| 规则指纹 | f9c0b1886ab273be18bc170b3841777783b7f9b2cd80b7ff77a9c0d7a9aa7918 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"] |
| 元数据更新（不是成交时间） | 2026-11-09T11:01:26.179567Z |
| 抓取时间 | 2026-11-09T12:02:55.253363+00:00 |
| 来源 | https://polymarket.com/event/nvda-quarterly-earnings-nongaap-eps-11-17-2026-2pt53 |

## Will Rocket Lab (RKLB) beat quarterly earnings?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1262853 / 6281226 |
| Yes 概率 % | 24.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-4.5, -10.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -4.0000000000000036} |
| 24h成交量 / 流动性 USD | [525.378369, 475.397] |
| 价差 pp | 2.00 |
| 到期 | 2026-11-09T22:00:00+00:00 |
| 结算规则摘要 | RKLB下一季度首次GAAP EPS按美分取整严格大于固定-0.07美元为Yes，非动态预期；首选官方稀释EPS，缺失按规则用基本EPS/SeekingAlpha。无EPS96小时或预计日45天仍未发布为No；后续修订通常不算。低流动性，不能等同股价上涨。 |
| 规则指纹 | 7b68875b4eb9e73a7e789ca3802aaa41896ebc77b9c7c16d7d07101af35911dd |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-09T11:51:26.010796Z |
| 抓取时间 | 2026-11-09T12:01:08.527141+00:00 |
| 来源 | https://polymarket.com/event/rklb-quarterly-earnings-gaap-eps-11-09-2026-neg0pt07 |

## AI 压力：合约、经营与估值分开

第一层：AI泡沫2026合约7.25%、2027年6月合约25.5%，专门多条件规则不等于普通回调概率；同定义差异见事件栏。H100指数截至11月8日3.00美元/GPU小时，7日3.04、6日2.99，远未满足≤1连续5日专门门槛；标准化neocloud报价不能代表所有芯片合同与利用率。第二层：NVIDIA官方8日独立董事调查且表示目前无理由认定安全/机密受损，支持管理层；调查不是定罪、离任或订单取消。9日与Rebellions/SK Telecom合作NVLink Fusion为计划部署，不能立即折算收入。国会11月4日信函请求18日闭门简报、11日前回复或提出替代日期，这是请求而非已确认出席/传票。盘前NVDA-5.15%，MSFT/AMZN/GOOGL/META上涨，显示治理折价和行业需求应分开。第三层：五家SEC最新定期财报仍为NVDA8月26、MSFT10月28、AMZN10月30、GOOGL10月29、META10月22日；没有新定期财报不等于没有公告。复用核验财务底稿更新价格，NVDA五年FCFF与敏感性是公司整体情景，不给客观概率；四家完整TTM/租赁/净债务/稀释桥缺失明确保留。新延期、融资收紧与现金回收恶化才加强需求/融资风险判断；韩国合作是反证线索，尚不足证明行业压力解除。

## NVDA · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | scenario_analysis |
| 财务底稿 | TTM 至 2026-07-26；最新 10-Q / filed 2026-08-26 |
| 披露检查 | {"checked_at": "2026-11-09T12:02:27.410686+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001045810.json", "latest_filing_date": "2026-08-26"} |
| 观测财务数据 | {"ttm_revenue_million": 302970, "revenue_quarters": [{"end": "2025-10-26", "value": 57006000000, "filed": "2025-11-19", "duration_days": 91}, {"end": "2026-01-25", "value": 68127000000, "filed": "2026-02-25", "duration_days": 91}, {"end": "2026-04-26", "value": 81615000000, "filed": "2026-05-20", "duration_days": 91}, {"end": "2026-07-26", "value": 96221000000, "filed": "2026-08-26", "duration_days": 91}], "cash_million": 22443.0, "liquid_investments_million": 34143.0, "debt_million": 33366.0, "finance_lease_million": 0, "diluted_shares_million": 24285.0, "latest_operating_income_million": 63734.0, "observed_end": "2026-07-26", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "Revenues", "latest_reported_revenue_million": 96221.0, "income_statement_window": "最近单季度", "ttm_bridge_note": "采用同版 FY2026全年 + FY2027半年 - FY2026半年；与四季逐项求和差1百万为披露舍入差。"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json", "https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。10-Q Note14 表明融资租赁费用不重大；模型按不重大近似零，不将其称为精确零负债。未确认担保仅作为压力情景，非已到期净债务。市场化股权42783和非市场化股权51157不作为类现金；非经营资产加回为0的保守假设。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | 无 |
| 价格 USD | 186.64 |
| 基期输入 USD million / million shares | {"revenue": 302970, "net_debt": -23220.0, "diluted_shares": 24285.0, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.2524832336442925, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## NVDA · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 98.77 | -47.08 | 14.00 | 60.00 | 12.00 | 68.42 |
| 基准 | 154.12 | -17.43 | 20.00 | 65.00 | 11.00 | 74.20 |
| 乐观 | 242.58 | 29.97 | 26.00 | 70.00 | 10.00 | 79.05 |

## NVDA · 可复算假设

| 情景 | 假设（比例以小数表示） |
| --- | --- |
| 悲观 | {"growth": 0.14, "start_margin": 0.6623710000935347, "operating_margin": 0.6, "tax_rate": 0.17, "da_ratio": 0.015, "capex_ratio": 0.055, "working_capital_ratio": 0.12, "wacc": 0.12, "terminal_growth": 0.025, "dilution": 0, "start_capex_ratio": 0.04} |
| 基准 | {"growth": 0.2, "start_margin": 0.6623710000935347, "operating_margin": 0.65, "tax_rate": 0.17, "da_ratio": 0.015, "capex_ratio": 0.04, "working_capital_ratio": 0.12, "wacc": 0.11, "terminal_growth": 0.025, "dilution": 0, "start_capex_ratio": 0.04} |
| 乐观 | {"growth": 0.26, "start_margin": 0.6623710000935347, "operating_margin": 0.7000000000000001, "tax_rate": 0.17, "da_ratio": 0.015, "capex_ratio": 0.025, "working_capital_ratio": 0.12, "wacc": 0.1, "terminal_growth": 0.025, "dilution": 0, "start_capex_ratio": 0.04} |

## NVDA · 折现率与经营下修敏感性

| WACC% | 收入CAGR% | 每股 USD |
| --- | --- | --- |
| 9.00 | 20.00 | 205.57 |
| 9.00 | 15.00 | 169.45 |
| 11.00 | 20.00 | 154.12 |
| 11.00 | 15.00 | 127.74 |
| 13.00 | 20.00 | 122.46 |
| 13.00 | 15.00 | 102.04 |

## MSFT · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | unavailable |
| 财务底稿 | FY2027Q1 ended 2026-09-30 |
| 披露检查 | {"checked_at": "2026-11-09T12:02:31.294290+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0000789019.json", "latest_filing_date": "2026-10-28"} |
| 观测财务数据 | {"revenue_million": 92279, "operating_income_million": 45915, "operating_cashflow_million": 58000, "cash_capex_million": 39367, "cfo_less_cash_capex_million": 18633, "diluted_shares_million": 7446, "unit": "USD million; shares million", "observed_end": "2026-09-30", "published_at": null} |
| 来源 | ["https://www.microsoft.com/en-us/Investor/earnings/FY-2027-Q1/press-release-webcast", "https://www.sec.gov/Archives/edgar/data/789019/000119312526439794/d799291dfwp.htm"] |
| 口径 | 单季CFO减现金capex不等于FCFF；融资租赁新增/负债、优先权益、TTM及稀释桥须完整后重算；不假设缺失项为零。 |
| 主观假设说明 | 缺失 |
| 权益桥额外假设 | 无 |
| 缺失原因 | 沿用底稿的历史核验说明（其中“本次”指原核验日）；本轮最新定期财报列表检查见disclosure_check。本次新增30日FWP，29日已定价250亿美元债券、11月4日预定结算；新财报完整TTM/租赁/净债务桥仍缺，不沿用旧精确DCF。 |

## AMZN · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | unavailable |
| 财务底稿 | FY2026 Q3 ended 2026-09-30 |
| 披露检查 | {"checked_at": "2026-11-09T12:02:33.641261+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001018724.json", "latest_filing_date": "2026-10-30"} |
| 观测财务数据 | {"revenue_quarter_million": 201900, "aws_revenue_quarter_million": 45980, "cfo_ttm_million": 168300, "net_cash_capex_ttm_million": 210657, "company_cash_fcf_ttm_million": -42357, "gaap_eps": 1.89} |
| 来源 | ["https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Third-Quarter-Results/default.aspx", "https://data.sec.gov/submissions/CIK0001018724.json", "https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm"] |
| 口径 | TTM公司现金FCF=CFO减净现金资本支出；不等于FCFF；不能当单季。融资租赁和债务股数桥待补。 |
| 主观假设说明 | 缺失 |
| 权益桥额外假设 | 无 |
| 缺失原因 | 沿用底稿的历史核验说明（其中“本次”指原核验日）；本轮最新定期财报列表检查见disclosure_check。30日新增Q3 10-Q已核验；最新TTM、融资租赁/净债务与稀释桥尚未完整，不沿用旧估值。 |

## GOOGL · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | unavailable |
| 财务底稿 | 2026Q3 ended 2026-09-30 |
| 披露检查 | {"checked_at": "2026-11-09T12:02:36.041047+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001652044.json", "latest_filing_date": "2026-10-29"} |
| 观测财务数据 | {"revenue_million": 127577, "operating_income_million": 40576, "net_income_million": 26468, "net_income_to_common_million": 26170, "operating_cashflow_million": 42290, "cash_capex_million": 51355, "cfo_less_cash_capex_million": -9065, "diluted_shares_million": 12368, "common_stock_net_proceeds_million": 12371, "unit": "USD million; shares million", "observed_end": "2026-09-30", "published_at": null, "finance_lease_liabilities_million": 3705} |
| 来源 | ["https://www.sec.gov/Archives/edgar/data/1652044/000165204426000080/googexhibit991q32026.htm", "https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm"] |
| 口径 | 单季CFO减现金capex不等于FCFF；融资租赁新增/负债、优先权益、TTM及稀释桥须完整后重算；不假设缺失项为零。 |
| 主观假设说明 | 缺失 |
| 权益桥额外假设 | 无 |
| 缺失原因 | 沿用底稿的历史核验说明（其中“本次”指原核验日）；本轮最新定期财报列表检查见disclosure_check。已发现新季度披露；必要TTM、融资租赁及优先权益/稀释桥未完成，暂停旧底稿估值和价格反推。 |

## META · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | unavailable |
| 财务底稿 | 2026Q3 ended 2026-09-30 |
| 披露检查 | {"checked_at": "2026-11-09T12:02:38.231152+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001326801.json", "latest_filing_date": "2026-10-22"} |
| 观测财务数据 | {"revenue_million": 64601, "operating_cashflow_million": 32790, "reported_capex_including_finance_lease_principal_million": 34910, "company_defined_fcf_million": -2120, "diluted_shares_million": 2573, "reported_operating_income_million": 12988, "legal_charge_million": 9900, "observed_end": "2026-09-30", "published_at": "2026-10-21T16:01:00-04:00", "unit": "USD million; shares million", "noncancelable_commitments_million": 454520, "leases_not_commenced_million": 355730, "contingent_cloud_capacity_max_million": 14720, "restricted_cash_reclassified_million": 10800, "commitments_due_2026_million": 45850, "commitments_due_2027_million": 121410} |
| 来源 | ["https://www.prnewswire.com/news-releases/meta-reports-third-quarter-2026-results-302915964.html", "https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm", "https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Announces-Launch-of-Offering-of-Depositary-Shares-Representing-Series-A-Mandatory-Convertible-Preferred-Stock-and-Offering-of-Class-A-Common-Stock-in-Connection-with-Forward-Sale-Agreements/default.aspx", "https://www.prnewswire.com/news-releases/meta-announces-pricing-of-offering-of-depositary-shares-representing-series-a-mandatory-convertible-preferred-stock-and-offering-of-class-a-common-stock-in-connection-with-forward-sale-agreements-302920247.html"] |
| 口径 | 公司FCF扣除融资租赁本金，不能直接代替模型FCFF；融资租赁负债/新增资产未齐，不假设零。法律费用不全归AI经营。 |
| 主观假设说明 | 缺失 |
| 权益桥额外假设 | 无 |
| 缺失原因 | 沿用底稿的历史核验说明（其中“本次”指原核验日）；本轮最新定期财报列表检查见disclosure_check。22日10-Q已核验，本次无新增定期财报。27日普通股625美元定价、优先票息6.5%已核验；完整融资租赁负债/新增资产、优先权益/远期发行与现金到账桥未齐，不用不同承诺简单充当现有债务，暂停精确FCFF反推。 |

## 宽基修复的第二次验证

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 盘前油价/波动回落，周二CPI |
| 关联标的 | ["SPY", "QQQ", "RSP"] |
| 确认条件 | 先守周五SPY734.58/QQQ654.00附近且低点抬高；再突破742.21/664.52并回踩承接，RSP收复216.87并同步走强；收盘保持、次日不吞没才逐步升级。常规VWAP需届时另行获取。 |
| 失效条件 | 跌破周五低点且反抽失败为转弱；SPY733/QQQ647.05重新失守则本轮修复大部分被吞没，VIX重返28.18附近强化风险。 |
| 观察期限 | 周一至周二CPI后首个收盘 |
| 反证 | 盘前指数上涨但半导体偏弱；RSP报价较旧，当前广度不明。突破未守到收盘不升级。 |
| 状态 | 盘前改善，常规时段待验证 |

## 半导体治理冲击与行业需求分开

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | NVIDIA独立调查、周二CPI与17日财报 |
| 关联标的 | ["SMH", "NVDA", "MU", "SNDK"] |
| 确认条件 | SMH守456.44后收复476.25并回踩不破；NVDA重返194.90、MU重返724.80需有收盘承接，且不能只一只存储独涨。 |
| 失效条件 | NVDA已在盘前跌破185.22，常规时段无法收复且再破开盘低点则加强转弱；SMH456.44失守反抽失败下调，进一步447.73/445.59失守则修复失败。MU676为自身预警。 |
| 观察期限 | 未来1–3交易日；17日财报前重评 |
| 反证 | NVDA韩国合作及其他云巨头上涨反对全行业需求消失；但SMH周跌11.20%，盘前弱于宽基。 |
| 状态 | 盘前预警已触发，等待现货验证 |

## 防御与顺周期分开

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | CPI、利率、能源供应 |
| 关联标的 | ["XLV", "XLP", "XLU", "XLE", "OIH"] |
| 确认条件 | 医疗等防御自身止跌并维持相对SPY强势；油服若受消息驱动，须独立供应证据、油价及个股同步承接，至少一个完整收盘。 |
| 失效条件 | 仅跌得少、利率上升压防御估值，或地缘消息否认后能源跳空回落；不以OIH单日反弹推净流入。 |
| 观察期限 | 周一至周五PPI |
| 反证 | 油价盘前下跌反对消息一出就买能源；医疗自身强弱仍需完整现货确认。 |
| 状态 | 观察 |

## AI融资缓解须看现实兑现

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 融资交付、项目进度及公司披露 |
| 关联标的 | ["MSFT", "AMZN", "GOOGL", "META", "NVDA", "ORCL", "CRWV"] |
| 确认条件 | 融资按条款交付、延期不扩大、利用率/现金回收改善，配合信用与价格止跌；逐公司核验。 |
| 失效条件 | 新延期、评级行动或融资收紧与价格新低共振；单一低量合约不触发。 |
| 观察期限 | 未来一周及NVDA财报 |
| 反证 | H100租金保持，META能融资；强者融资不证明全产业链健康。 企业寻求监管合作不等于许可获批；抗议也不是禁令。 |
| 状态 | 维持审慎 |

## 航天订单质量而非框架金额

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | NASA CLPS2与RKLB盘后财报 |
| 关联标的 | ["ARKX", "FLY", "LUNR", "LMT", "NOC", "VOYG", "RKLB"] |
| 确认条件 | 先核验具体订单/交付/毛利与现金，再看开盘30分钟区间突破后回踩、相对SPY保持至收盘 |
| 失效条件 | 把框架上限当收入、跳空回吐开盘区间、财报指引或现金消耗恶化 |
| 观察期限 | 周一开盘至RKLB财报后两个交易日 |
| 反证 | RKLB不是所列CLPS2八家之一；不得把全篮子称同一直接受益者；高波动与融资需求可能吞没新闻利好 |
| 状态 | 新增观察，不预先押注方向 |

## 跨期比较与上期剧本复核

对照11月9日早报：没有新完整现货交易日，周五量价背景不变；新增盘前宽基回升、油价/VIX回落和NVDA独立走弱。早报NVDA185.22预警已在盘前触发，不能继续写成尚未发生；但薄盘成交不是常规收盘失效，今晚需看能否收复与回踩。CNN22升25是同指数新观测。宽基剧本尚未获得常规开盘区间、VWAP、广度和收盘确认；原能源供应紧张主线遇到油价下跌反证。 同规则合约与早报观测差：2176270: +2.00个百分点；3215008: +0.00个百分点；691340: -0.95个百分点；4838928: +1.00个百分点；2252540: -0.50个百分点；2413330: +0.15个百分点；2745561: +0.00个百分点；5401796: -2.50个百分点；5939428: +0.00个百分点；5123855: +0.00个百分点；5123856: +0.00个百分点；6639362: -0.10个百分点；5699271: +1.50个百分点；5699272: -1.00个百分点；6882826: -6.00个百分点；6281226: -4.00个百分点。低成交或宽价差变化仅作观察。

## 可计算的跨期变化

```json
[
  {
    "mode": "daily",
    "baseline": "reports/daily/2026-11-06/20261108T232226.117273Z/evidence.json",
    "baseline_cutoff": "2026-11-08T23:22:07.851787+00:00",
    "close_change_pct": {
      "SPY": 0.0,
      "QQQ": 0.0,
      "IWM": 0.0,
      "RSP": 0.0,
      "GLD": 0.0,
      "GC=F": 0.0,
      "CL=F": 0.0,
      "BZ=F": 0.0,
      "TLT": 0.0,
      "UUP": 0.0,
      "HYG": 0.0,
      "LQD": 0.0,
      "^VIX": 0.0,
      "^VIX3M": 0.0,
      "^VVIX": 0.0,
      "^MOVE": 0.0,
      "NVDA": 0.0,
      "MSFT": 0.0,
      "AMZN": 0.0,
      "GOOGL": 0.0,
      "META": 0.0,
      "CRWV": 0.0,
      "MU": 0.0,
      "DRAM": 0.0,
      "VRT": 0.0,
      "XLK": 0.0,
      "XLE": 0.0,
      "XLF": 0.0,
      "XLI": 0.0,
      "XLV": 0.0,
      "XLP": 0.0,
      "XLY": 0.0,
      "XLC": 0.0,
      "XLU": 0.0,
      "XLRE": 0.0,
      "XLB": 0.0,
      "SMH": 0.0,
      "IGV": 0.0,
      "XOP": 0.0,
      "OIH": 0.0,
      "ITA": 0.0,
      "ARKX": 0.0,
      "KRE": 0.0,
      "SKYY": 0.0
    },
    "quote_change_pct": {
      "MU": {
        "change_pct": -0.7478260869565156,
        "from_observed_at": "2026-11-06T21:00:01+00:00",
        "to_observed_at": "2026-11-09T12:01:05+00:00"
      },
      "XLV": {
        "change_pct": 1.2229437229437146,
        "from_observed_at": "2026-11-06T21:00:00+00:00",
        "to_observed_at": "2026-11-09T12:00:13+00:00"
      },
      "BABA": {
        "change_pct": -1.6313385107354916,
        "from_observed_at": "2026-11-06T21:01:59+00:00",
        "to_observed_at": "2026-11-09T12:01:02+00:00"
      },
      "SNDK": {
        "change_pct": -1.748377362105702,
        "from_observed_at": "2026-11-06T21:00:00+00:00",
        "to_observed_at": "2026-11-09T12:01:05+00:00"
      },
      "GOOGL": {
        "change_pct": 1.8365053725682978,
        "from_observed_at": "2026-11-06T21:00:01+00:00",
        "to_observed_at": "2026-11-09T12:01:01+00:00"
      },
      "DRAM": {
        "change_pct": -0.6871977602443291,
        "from_observed_at": "2026-11-06T21:00:00+00:00",
        "to_observed_at": "2026-11-09T12:01:06+00:00"
      },
      "ARM": {
        "change_pct": -0.9277287824991487,
        "from_observed_at": "2026-11-06T21:00:01+00:00",
        "to_observed_at": "2026-11-09T12:00:00+00:00"
      },
      "IWM": {
        "change_pct": 1.2058318412686786,
        "from_observed_at": "2026-11-06T21:00:00+00:00",
        "to_observed_at": "2026-11-09T12:01:00+00:00"
      },
      "QCOM": {
        "change_pct": -0.9128831388670489,
        "from_observed_at": "2026-11-06T21:00:01+00:00",
        "to_observed_at": "2026-11-09T12:00:37+00:00"
      },
      "STX": {
        "change_pct": 0.0455541334952958,
        "from_observed_at": "2026-11-06T21:00:00+00:00",
        "to_observed_at": "2026-11-09T12:00:03+00:00"
      },
      "SPY": {
        "change_pct": 0.620163472915447,
        "from_observed_at": "2026-11-06T21:00:00+00:00",
        "to_observed_at": "2026-11-09T12:00:59+00:00"
      },
      "XLE": {
        "change_pct": 0.21097046413502962,
        "from_observed_at": "2026-11-06T21:00:00+00:00",
        "to_observed_at": "2026-11-09T12:00:41+00:00"
      },
      "AVGO": {
        "change_pct": 2.3221764445503723,
        "from_observed_at": "2026-11-06T21:00:01+00:00",
        "to_observed_at": "2026-11-09T12:00:51+00:00"
      },
      "META": {
        "change_pct": 2.191264443169705,
        "from_observed_at": "2026-11-06T21:00:01+00:00",
        "to_observed_at": "2026-11-09T12:00:51+00:00"
      },
      "ORCL": {
        "change_pct": -0.1579672695951717,
        "from_observed_at": "2026-11-06T21:03:15+00:00",
        "to_observed_at": "2026-11-09T12:00:55+00:00"
      },
      "NVDA": {
        "change_pct": -5.146163737676801,
        "from_observed_at": "2026-11-06T21:00:00+00:00",
        "to_observed_at": "2026-11-09T12:01:01+00:00"
      },
      "COIN": {
        "change_pct": -2.3449094686850636,
        "from_observed_at": "2026-11-06T21:00:01+00:00",
        "to_observed_at": "2026-11-09T12:00:13+00:00"
      },
      "VRT": {
        "change_pct": 1.312479492507923,
        "from_observed_at": "2026-11-06T21:00:03+00:00",
        "to_observed_at": "2026-11-09T12:00:27+00:00"
      },
      "TAN": {
        "change_pct": 1.9087318999561287,
        "from_observed_at": "2026-11-06T21:00:00+00:00",
        "to_observed_at": "2026-11-09T12:00:07+00:00"
      },
      "INTC": {
        "change_pct": -0.4442075337597773,
        "from_observed_at": "2026-11-06T21:00:01+00:00",
        "to_observed_at": "2026-11-09T12:01:06+00:00"
      },
      "COP": {
        "change_pct": 0.22748954281941458,
        "from_observed_at": "2026-11-06T21:00:02+00:00",
        "to_observed_at": "2026-11-09T12:00:06+00:00"
      },
      "QQQ": {
        "change_pct": 0.49382716049382047,
        "from_observed_at": "2026-11-06T21:00:00+00:00",
        "to_observed_at": "2026-11-09T12:01:00+00:00"
      },
      "AMD": {
        "change_pct": 3.772492428291474,
        "from_observed_at": "2026-11-06T21:00:01+00:00",
        "to_observed_at": "2026-11-09T12:01:09+00:00"
      },
      "CEG": {
        "change_pct": 4.420884176835371,
        "from_observed_at": "2026-11-06T21:00:01+00:00",
        "to_observed_at": "2026-11-09T12:00:55+00:00"
      },
      "GLD": {
        "change_pct": 1.0549769139911902,
        "from_observed_at": "2026-11-06T21:00:00+00:00",
        "to_observed_at": "2026-11-09T12:00:35+00:00"
      },
      "CRWV": {
        "change_pct": -3.340517241379304,
        "from_observed_at": "2026-11-06T21:00:01+00:00",
        "to_observed_at": "2026-11-09T12:00:51+00:00"
      },
      "MSFT": {
        "change_pct": 1.9018299692806329,
        "from_observed_at": "2026-11-06T21:00:01+00:00",
        "to_observed_at": "2026-11-09T12:01:02+00:00"
      },
      "GDX": {
        "change_pct": 2.237442922374444,
        "from_observed_at": "2026-11-06T21:00:00+00:00",
        "to_observed_at": "2026-11-09T12:00:55+00:00"
      },
      "LITE": {
        "change_pct": -1.0991663417441955,
        "from_observed_at": "2026-11-06T21:00:01+00:00",
        "to_observed_at": "2026-11-09T12:00:52+00:00"
      },
      "CAT": {
        "change_pct": 1.3103485312282004,
        "from_observed_at": "2026-11-06T21:00:03+00:00",
        "to_observed_at": "2026-11-09T12:00:26+00:00"
      },
      "TLT": {
        "change_pct": 0.06103515625,
        "from_observed_at": "2026-11-06T21:00:00+00:00",
        "to_observed_at": "2026-11-09T12:00:35+00:00"
      },
      "AMZN": {
        "change_pct": 2.869186270728874,
        "from_observed_at": "2026-11-06T21:00:01+00:00",
        "to_observed_at": "2026-11-09T12:00:42+00:00"
      },
      "GLW": {
        "change_pct": 0.46160369358334563,
        "from_observed_at": "2026-11-06T21:02:59+00:00",
        "to_observed_at": "2026-11-09T12:00:38+00:00"
      },
      "PLTR": {
        "change_pct": 0.19952612545204307,
        "from_observed_at": "2026-11-06T21:00:00+00:00",
        "to_observed_at": "2026-11-09T11:58:57+00:00"
      },
      "SMH": {
        "change_pct": -0.29743943443399923,
        "from_observed_at": "2026-11-06T21:00:00+00:00",
        "to_observed_at": "2026-11-09T12:00:55+00:00"
      },
      "AAPL": {
        "change_pct": 0.6007827788649722,
        "from_observed_at": "2026-11-06T21:00:01+00:00",
        "to_observed_at": "2026-11-09T12:00:35+00:00"
      },
      "MRVL": {
        "change_pct": -0.5968838526912101,
        "from_observed_at": "2026-11-06T21:00:01+00:00",
        "to_observed_at": "2026-11-09T12:00:48+00:00"
      },
      "LLY": {
        "change_pct": 2.0753323485967368,
        "from_observed_at": "2026-11-06T21:02:01+00:00",
        "to_observed_at": "2026-11-09T12:01:04+00:00"
      }
    },
    "macro_change": {
      "DGS2": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-11-05"
      },
      "BAMLH0A0HYM2": {
        "change": 0.0,
        "unit": "percentage_points",
        "observation_date": "2026-11-05"
      },
      "BAMLC0A0CM": {
        "change": 0.0,
        "unit": "percentage_points",
        "observation_date": "2026-11-05"
      },
      "DGS10": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-11-05"
      },
      "DFII10": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-11-05"
      },
      "T10YIE": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-11-06"
      },
      "STLFSI4": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-30"
      },
      "CBOE_VIX": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-11-06"
      },
      "GPRD": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-11-02"
      },
      "GPRD_ACT": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-11-02"
      },
      "GPRD_THREAT": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-11-02"
      },
      "GPRD_MA7": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-11-02"
      },
      "GPRD_MA30": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-11-02"
      }
    },
    "event_probability_change": {
      "6882826": {
        "status": "comparable",
        "change_pp": -6.000000000000001
      },
      "2176270": {
        "status": "comparable",
        "change_pp": 2.0000000000000004
      },
      "691340": {
        "status": "comparable",
        "change_pp": -0.9500000000000008
      },
      "3215008": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "4838928": {
        "status": "comparable",
        "change_pp": 1.0000000000000009
      },
      "2252540": {
        "status": "comparable",
        "change_pp": -0.49999999999999906
      },
      "5699271": {
        "status": "comparable",
        "change_pp": 1.5000000000000013
      },
      "5699272": {
        "status": "comparable",
        "change_pp": -1.0000000000000009
      },
      "5939428": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "5401796": {
        "status": "comparable",
        "change_pp": -2.500000000000002
      },
      "2413330": {
        "status": "comparable",
        "change_pp": 0.14999999999999458
      },
      "2745561": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "5123855": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "5123856": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "6639362": {
        "status": "comparable",
        "change_pp": -0.09999999999998899
      },
      "6281226": {
        "status": "comparable",
        "change_pp": -4.0000000000000036
      }
    },
    "note": "收盘价快照变化；同一收盘日为零，不代表盘中没有变化"
  }
]
```

## 后续催化剂与发布后增量

```json
[
  {
    "event": "10月CPI/实际工资；北京10日21:30，tc缓存12日错误",
    "date": "2026-11-10T08:30:00-05:00",
    "source": "https://www.bls.gov/schedule/2026/11_sched.htm"
  },
  {
    "event": "CoreWeave Q3电话会；北京11日06:00，tc缓存12日错误",
    "date": "2026-11-10T17:00:00-05:00",
    "source": "https://investors.coreweave.com/events-and-presentations/event-details/2026/CoreWeave-Third-Quarter-2026-Earnings-Call/default.aspx"
  },
  {
    "event": "Nebius Q3：官方11月12日美股开盘前，发布时间分钟未核验",
    "date": null,
    "source": "https://nebius.com/newsroom/nebius-group-announces-date-of-third-quarter-2026-results-and-conference-call"
  },
  {
    "event": "10月PPI；北京13日21:30",
    "date": "2026-11-13T08:30:00-05:00",
    "source": "https://www.bls.gov/schedule/2026/11_sched.htm"
  },
  {
    "event": "NVDA Q3预计业绩16:20ET、电话会17:00ET；北京时间次日",
    "date": "2026-11-17T16:20:00-05:00",
    "source": "https://nvidianews.nvidia.com/news/nvidia-sets-conference-call-for-third-quarter-financial-results-6928873"
  },
  {
    "event": "11月26日感恩节休市、27日股票13:00EST半日市；11日股票正常交易",
    "date": null,
    "source": "https://www.nyse.com/markets/hours-calendars"
  },
  {
    "event": "Nebius Q3电话会；北京12日21:00，业绩为此前盘前披露",
    "date": "2026-11-12T08:00:00-05:00",
    "source": "https://assets.nebius.com/assets/7a58f9de-6a9b-4124-b71e-db5185af68df/30102026%20Nebius%20Group%20announces%20date%20of%20third%20quarter%202026%20results%20and%20conference%20call.pdf"
  },
  {
    "event": "RKLB盘后业绩；电话会北京10日06:00",
    "date": "2026-11-09T17:00:00-05:00",
    "source": "https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-announces-date-third-quarter-2026-financial-results"
  }
]
```

## 新闻事件去重与时间

| 事件 | 摘要 | 发生时间（未知留空） | 各来源发布时间 / 抓取时间 |
| --- | --- | --- | --- |
| nvda-governance | 董事会独立调查、目前未认定安全或机密受损；不等于离任/订单取消。 | 缺失 | [{"source": "https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors", "published_at": null, "retrieved_at": "2026-11-09T12:07:25.694612+00:00"}] |
| nvda-korea | NVIDIA/Rebellions/SK Telecom宣布NVLink Fusion合作；计划部署不是已兑现收入。 | 缺失 | [{"source": "https://nvidianews.nvidia.com/news/nvidia-rebellions-and-sk-telecom-announce-collaboration-to-advance-sovereign-ai-infrastructure-with-nvidia-nvlink-fusion", "published_at": null, "retrieved_at": "2026-11-09T12:07:25.694612+00:00"}] |
| nvda-congress | 11月4日信函请求18日闭门简报，11日前回复或提出替代日期；非确认日程或传票。 | 缺失 | [{"source": "https://chinaselectcommittee.house.gov/sites/evo-subsites/selectcommitteeontheccp.house.gov/files/evo-media-document/nvidia-letter-pdf.pdf", "published_at": null, "retrieved_at": "2026-11-09T12:07:25.694612+00:00"}] |
| iran-diplomacy | AP报道外交接触尚无突破、特朗普有条件不新增打击；未宣布全面停火。 | 缺失 | [{"source": "https://apnews.com/article/f7b507b55634985d6013d36265b3fbc0", "published_at": "2026-11-09T00:06:33+00:00", "retrieved_at": "2026-11-09T12:07:25.694612+00:00"}] |
| china-denial | AP报道中方否认相关指控；否认与调查分别呈现，不直接认定任何一方指控已证实。 | 缺失 | [{"source": "https://apnews.com/article/3345b9f05c54d58909e88f6dcb9c1cd8", "published_at": "2026-11-09T08:27:25+00:00", "retrieved_at": "2026-11-09T12:07:25.694612+00:00"}] |

## 覆盖范围与数据缺口

```json
[
  "tc报价值仍与周五收盘相同且时戳不可信；独立分钟close和真实timestamp交叉核验，原包保留。",
  "基础新闻50条截断，主题补查48条未截断，但仍非全新闻覆盖。Apple中国AI获批快讯未找到足够正式证据，未作确定事实。",
  "盘前没有今天常规VWAP/开盘区间/广度；部分ETF分钟成交较旧，不拼接成实时轮动排名。",
  "VIX3M、信用、TNX均较旧，不与新VIX/股价计算同步结论。",
  "当期ETF净申赎、机构持仓和拆分桥缺失；ICI为滞后窗口。",
  "四家完整DCF底稿仍缺；NVDA情景假设不等于概率，未擅自将治理调查转换经营下修。",
  "Gamma部分搜索截断且有无关结果；Oracle/NVDA财报等宽价差降低参考价值。",
  "CME官方动态概率未核验，CNN API418但浏览器已核验。",
  "地区袭击损害/恢复量、调查结果和韩国合作收入贡献尚未确定。",
  "历史来源保留原核验时间，只有本次明确重查来源更新核验记录。",
  "DRAM历史不够SMA200；全市场成分广度和当前资金流缺失。",
  "原始采集存在请求失败，见采集质量记录",
  "MSFT 估值: 沿用底稿的历史核验说明（其中“本次”指原核验日）；本轮最新定期财报列表检查见disclosure_check。本次新增30日FWP，29日已定价250亿美元债券、11月4日预定结算；新财报完整TTM/租赁/净债务桥仍缺，不沿用旧精确DCF。",
  "AMZN 估值: 沿用底稿的历史核验说明（其中“本次”指原核验日）；本轮最新定期财报列表检查见disclosure_check。30日新增Q3 10-Q已核验；最新TTM、融资租赁/净债务与稀释桥尚未完整，不沿用旧估值。",
  "GOOGL 估值: 沿用底稿的历史核验说明（其中“本次”指原核验日）；本轮最新定期财报列表检查见disclosure_check。已发现新季度披露；必要TTM、融资租赁及优先权益/稀释桥未完成，暂停旧底稿估值和价格反推。",
  "META 估值: 沿用底稿的历史核验说明（其中“本次”指原核验日）；本轮最新定期财报列表检查见disclosure_check。22日10-Q已核验，本次无新增定期财报。27日普通股625美元定价、优先票息6.5%已核验；完整融资租赁负债/新增资产、优先权益/远期发行与现金到账桥未齐，不用不同承诺简单充当现有债务，暂停精确FCFF反推。",
  "Polymarket 查询 AI bubble 达到页数上限，存在遗漏",
  "Polymarket 查询 AI spending 达到页数上限，存在遗漏",
  "Polymarket 查询 CPI 达到页数上限，存在遗漏",
  "Polymarket 查询 Fed rate 达到页数上限，存在遗漏",
  "Polymarket 查询 Hormuz 达到页数上限，存在遗漏",
  "Polymarket 查询 Iran 达到页数上限，存在遗漏",
  "Polymarket 查询 Microsoft 达到页数上限，存在遗漏",
  "Polymarket 查询 Nvidia 达到页数上限，存在遗漏",
  "Polymarket 查询 SpaceX 达到页数上限，存在遗漏",
  "Polymarket 查询 bank 达到页数上限，存在遗漏",
  "Polymarket 查询 ceasefire 达到页数上限，存在遗漏",
  "Polymarket 查询 inflation 达到页数上限，存在遗漏",
  "tc 新闻达到查询条数上限；仅社交平台线索，非完整财经新闻",
  "tc 报价质量 stale: RSP, CVX, CI, GEV, NOW, IGV, NXPI, XOM, SO, COHR, ILMN, XLF；不作为新成交证据",
  "history.DRAM: insufficient_history",
  "polymarket.query.AI bubble: truncated",
  "polymarket.query.AI spending: truncated",
  "polymarket.query.CPI: truncated",
  "polymarket.query.Fed rate: truncated",
  "polymarket.query.Hormuz: truncated",
  "polymarket.query.Iran: truncated",
  "polymarket.query.Microsoft: truncated",
  "polymarket.query.Nvidia: truncated",
  "polymarket.query.SpaceX: truncated",
  "polymarket.query.bank: truncated",
  "polymarket.query.ceasefire: truncated",
  "polymarket.query.inflation: truncated",
  "cnn: missing",
  "news: truncated",
  "request.38906ddc2d63: request_failed",
  "指标缺失/历史不足: prices.^VIX.volume_vs_previous20_ratio, prices.^VIX3M.volume_vs_previous20_ratio, prices.^VVIX.volume_vs_previous20_ratio, prices.^MOVE.volume_vs_previous20_ratio, prices.DRAM.sma200, prices.DRAM.distance_sma200_pct, quotes.RSP.value, quotes.CVX.value, quotes.CI.value, quotes.GEV.value, quotes.NOW.value, quotes.IGV.value, quotes.NXPI.value, quotes.XOM.value, quotes.SO.value, quotes.COHR.value, quotes.ILMN.value, quotes.XLF.value, premarket.TNX.price"
]
```

## 来源、时间与核验记录

```json
[
  {
    "url": "https://www.bls.gov/news.release/empsit.nr0.htm",
    "checked_at": "2026-11-08T02:04:12.815853+00:00",
    "note": "历史底稿来源（保留原核验时间）；本次核验；新闻保留归属及限制，Nebius另核官方10月30日PDF"
  },
  {
    "url": "https://www.bls.gov/schedule/2026/11_sched.htm",
    "checked_at": "2026-11-08T02:04:12.815853+00:00",
    "note": "历史底稿来源（保留原核验时间）；本次核验；新闻保留归属及限制，Nebius另核官方10月30日PDF"
  },
  {
    "url": "https://www.sca.isr.umich.edu/",
    "checked_at": "2026-11-08T02:04:12.815853+00:00",
    "note": "历史底稿来源（保留原核验时间）；本次核验；新闻保留归属及限制，Nebius另核官方10月30日PDF"
  },
  {
    "url": "https://www.ici.org/research/stats/etf_flows",
    "checked_at": "2026-11-08T02:04:12.815853+00:00",
    "note": "历史底稿来源（保留原核验时间）；本次核验；新闻保留归属及限制，Nebius另核官方10月30日PDF"
  },
  {
    "url": "https://www.silicondata.com/products/silicon-index/h100",
    "checked_at": "2026-11-08T02:04:12.815853+00:00",
    "note": "历史底稿来源（保留原核验时间）；本次核验；新闻保留归属及限制，Nebius另核官方10月30日PDF"
  },
  {
    "url": "https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/default.aspx",
    "checked_at": "2026-11-08T02:04:12.815853+00:00",
    "note": "历史底稿来源（保留原核验时间）；本次核验；新闻保留归属及限制，Nebius另核官方10月30日PDF"
  },
  {
    "url": "https://www.sec.gov/Archives/edgar/data/1326801/000119312526450754/d44678d424b5.htm",
    "checked_at": "2026-11-08T02:04:12.815853+00:00",
    "note": "历史底稿来源（保留原核验时间）；本次核验；新闻保留归属及限制，Nebius另核官方10月30日PDF"
  },
  {
    "url": "https://www.sec.gov/Archives/edgar/data/1878848/000187884826000065/irenreportsq1-fy27result.htm",
    "checked_at": "2026-11-08T02:04:12.815853+00:00",
    "note": "历史底稿来源（保留原核验时间）；本次核验；新闻保留归属及限制，Nebius另核官方10月30日PDF"
  },
  {
    "url": "https://www.investing.com/news/stock-market-news/microsoft-is-winding-down-oracle-deal-to-rent-ai-cloud-capacity-bloomberg-news-reports-5008946",
    "checked_at": "2026-11-08T02:04:12.815853+00:00",
    "note": "历史底稿来源（保留原核验时间）；本次核验；新闻保留归属及限制，Nebius另核官方10月30日PDF"
  },
  {
    "url": "https://apnews.com/article/bc902d3400cb5d022f8bafd247ef975b",
    "checked_at": "2026-11-08T02:04:12.815853+00:00",
    "note": "历史底稿来源（保留原核验时间）；本次核验；新闻保留归属及限制，Nebius另核官方10月30日PDF"
  },
  {
    "url": "https://investors.coreweave.com/events-and-presentations/event-details/2026/CoreWeave-Third-Quarter-2026-Earnings-Call/default.aspx",
    "checked_at": "2026-11-08T02:04:12.815853+00:00",
    "note": "历史底稿来源（保留原核验时间）；本次核验；新闻保留归属及限制，Nebius另核官方10月30日PDF"
  },
  {
    "url": "https://nebius.com/newsroom/nebius-group-announces-date-of-third-quarter-2026-results-and-conference-call",
    "checked_at": "2026-11-08T02:04:12.815853+00:00",
    "note": "历史底稿来源（保留原核验时间）；本次核验；新闻保留归属及限制，Nebius另核官方10月30日PDF"
  },
  {
    "url": "https://www.bea.gov/news/schedule",
    "checked_at": "2026-11-08T02:04:12.815853+00:00",
    "note": "历史底稿来源（保留原核验时间）；本次核验；新闻保留归属及限制，Nebius另核官方10月30日PDF"
  },
  {
    "url": "https://www.nyse.com/markets/hours-calendars",
    "checked_at": "2026-11-08T02:04:12.815853+00:00",
    "note": "历史底稿来源（保留原核验时间）；本次核验；新闻保留归属及限制，Nebius另核官方10月30日PDF"
  },
  {
    "url": "https://apnews.com/article/4ac9a6a3c35aeec37374fc8083bf9395",
    "checked_at": "2026-11-08T02:04:12.815853+00:00",
    "note": "历史底稿来源（保留原核验时间）；本次核验；新闻保留归属及限制，Nebius另核官方10月30日PDF"
  },
  {
    "url": "https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/",
    "checked_at": "2026-11-08T02:04:12.815853+00:00",
    "note": "历史底稿来源（保留原核验时间）；本次核验；新闻保留归属及限制，Nebius另核官方10月30日PDF"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/MU",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLV",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/BABA",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SNDK",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GOOGL",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/RSP",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/DRAM",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CVX",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/ARM",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/IWM",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/QCOM",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/STX",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SPY",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CI",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GEV",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLE",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NOW",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AVGO",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLI",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/IGV",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/META",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/ORCL",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NVDA",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/COIN",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NXPI",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/VRT",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XOM",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SO",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/COHR",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/TAN",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/ILMN",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/INTC",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/COP",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/QQQ",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AMD",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CEG",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLF",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GLD",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CRWV",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/MSFT",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GDX",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/LITE",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CAT",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/TLT",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AMZN",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GLW",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/PLTR",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SMH",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AAPL",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/MRVL",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/LLY",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0001045810.json",
    "checked_at": "2026-11-08T02:00:50.879922+00:00",
    "note": "历史底稿来源（保留原核验时间）；最新定期财报列表；非全面8K检查"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0000789019.json",
    "checked_at": "2026-11-08T02:00:53.682582+00:00",
    "note": "历史底稿来源（保留原核验时间）；最新定期财报列表；非全面8K检查"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0001018724.json",
    "checked_at": "2026-11-08T02:00:56.065684+00:00",
    "note": "历史底稿来源（保留原核验时间）；最新定期财报列表；非全面8K检查"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0001652044.json",
    "checked_at": "2026-11-08T02:00:58.942985+00:00",
    "note": "历史底稿来源（保留原核验时间）；最新定期财报列表；非全面8K检查"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0001326801.json",
    "checked_at": "2026-11-08T02:01:01.304983+00:00",
    "note": "历史底稿来源（保留原核验时间）；最新定期财报列表；非全面8K检查"
  },
  {
    "url": "https://www.cnn.com/markets/fear-and-greed",
    "checked_at": "2026-11-08T02:05:37.724337+00:00",
    "note": "历史底稿来源（保留原核验时间）；浏览器只读官方页面22，更新11月6日18:59:54EST"
  },
  {
    "url": "https://assets.nebius.com/assets/7a58f9de-6a9b-4124-b71e-db5185af68df/30102026%20Nebius%20Group%20announces%20date%20of%20third%20quarter%202026%20results%20and%20conference%20call.pdf",
    "checked_at": "2026-11-08T02:05:37.724337+00:00",
    "note": "历史底稿来源（保留原核验时间）；公司10月30日PDF确认11月12日盘前业绩、08:00EST电话会；网页正文缺失，以PDF为准"
  },
  {
    "url": "https://au.investing.com/news/stock-market-news/coreweave-seeks-truce-with-texas-governorelect-hinojosa-4753439",
    "checked_at": "2026-11-08T02:17:05.773028+00:00",
    "note": "历史底稿来源（保留原核验时间）；媒体报道CoreWeave寻求与得州候任政府合作，尚无完整信件和监管回复，不能认定项目放行。"
  },
  {
    "url": "https://stopdirtydatacentres.eu/",
    "checked_at": "2026-11-08T02:17:05.773028+00:00",
    "note": "历史底稿来源（保留原核验时间）；行动组织官网列6–7日活动并要求暂停大规模数据中心；这是组织诉求，不是政府禁令。"
  },
  {
    "url": "https://www.ukmto.org/-/media/ukmto/products/20261107-ukmto_advisory-198-26.pdf",
    "checked_at": "2026-11-08T02:17:05.773028+00:00",
    "note": "历史底稿来源（保留原核验时间）；UKMTO198-26收到阿曼湾散货船与军队事件报告；船员、损害和环境影响未知，不能据此确认两艘油轮触雷。"
  },
  {
    "url": "https://berkshirehathaway.com/news/nov0726.pdf",
    "checked_at": "2026-11-08T02:17:05.773028+00:00",
    "note": "历史底稿来源（保留原核验时间）；7日官方Q3经营利润127.05亿美元低于上年134.85亿，同时本季回购约96亿美元；不把回购当全市场底部信号。"
  },
  {
    "url": "https://www.wam.ae/en/article/c2o8dle-uae-national-guard-rescues-people-after-oil-tanker",
    "checked_at": "2026-11-08T02:17:05.773028+00:00",
    "note": "历史底稿来源（保留原核验时间）；官方22人救援资料明确10月10日，不能核验11月8日新快讯；不认定为同一事件"
  },
  {
    "url": "https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "董事会宣布独立调查，未确认机密受损；不把调查当定罪、离任或订单取消。"
  },
  {
    "url": "https://www.rba.gov.au/speeches/2026/sp-ag-2026-11-09.html",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "Hunter官方讲话讨论AI投资回报不足的资产重估风险，短期需求推动通胀；这是条件风险框架，不是Fed政策或崩溃预测。"
  },
  {
    "url": "https://www.al-monitor.com/originals/2026/11/production-suspended-iraqs-khor-mor-gas-field-after-drone-attack-sources-say",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "Reuters据安全消息源报道Khor Mor气田遭无人机袭击后停产，运营方恢复时点/持续损失未确认。"
  },
  {
    "url": "https://www.nasa.gov/news-release/nasa-awards-moon-base-transportation-technology-science-projects/",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "NASA公告八家可竞争未来月球配送任务，十年总框架上限100亿美元，不等于已获全部订单。"
  },
  {
    "url": "https://www.forth.news/lists/centcom/Cgoet5KhSp6nWZnwnUeuR",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "CENTCOM新闻稿转载称设立Tampa协调小组，处理陆路/里海武器等运输；不是已证实所有能源陆路被物理封闭。"
  },
  {
    "url": "https://www.bls.gov/news.release/empsit.nr0.htm",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "BLS10月就业新增16.5万，失业率4.1%；民间预期分歧不采用单一未经核验值。"
  },
  {
    "url": "https://www.ici.org/research/stats/etf_flows",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "本次重查仍截至10月28日的净发行；不是本周资金"
  },
  {
    "url": "https://www.silicondata.com/products/silicon-index/h100",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "8日3.00、7日3.04、6日2.99美元/GPU小时"
  },
  {
    "url": "https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "本次查发行人，尚未取得完整份额/NAV/拆分桥"
  },
  {
    "url": "https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "本次官方页只有动态工具入口，无法核验78%快讯数值"
  },
  {
    "url": "https://www.cnn.com/markets/fear-and-greed",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "浏览器重新核验22，11月6日18:59:54EST"
  },
  {
    "url": "https://www.bls.gov/schedule/2026/11_sched.htm",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "本轮核验官方日历；交易休市以本轮tc日历为准"
  },
  {
    "url": "https://investors.coreweave.com/events-and-presentations/event-details/2026/CoreWeave-Third-Quarter-2026-Earnings-Call/default.aspx",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "本轮核验官方日历；交易休市以本轮tc日历为准"
  },
  {
    "url": "https://nebius.com/newsroom/nebius-group-announces-date-of-third-quarter-2026-results-and-conference-call",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "本轮核验官方日历；交易休市以本轮tc日历为准"
  },
  {
    "url": "https://www.bls.gov/schedule/2026/11_sched.htm",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "本轮核验官方日历；交易休市以本轮tc日历为准"
  },
  {
    "url": "https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/default.aspx",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "本轮核验官方日历；交易休市以本轮tc日历为准"
  },
  {
    "url": "https://www.nyse.com/markets/hours-calendars",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "本轮核验官方日历；交易休市以本轮tc日历为准"
  },
  {
    "url": "https://assets.nebius.com/assets/7a58f9de-6a9b-4124-b71e-db5185af68df/30102026%20Nebius%20Group%20announces%20date%20of%20third%20quarter%202026%20results%20and%20conference%20call.pdf",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "本轮核验官方日历；交易休市以本轮tc日历为准"
  },
  {
    "url": "https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-announces-date-third-quarter-2026-financial-results",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "本轮核验官方日历；交易休市以本轮tc日历为准"
  },
  {
    "url": "https://nvidianews.nvidia.com/news/nvidia-sets-conference-call-for-third-quarter-financial-results-6928873",
    "checked_at": "2026-11-08T23:22:07.360445+00:00",
    "note": "再次核对约13:20太平洋时间业绩公布、14:00电话会；换算16:20/17:00EST"
  },
  {
    "url": "https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors",
    "checked_at": "2026-11-09T12:07:25.694612+00:00",
    "note": "董事会独立调查、目前未认定安全或机密受损；不等于离任/订单取消。"
  },
  {
    "url": "https://nvidianews.nvidia.com/news/nvidia-rebellions-and-sk-telecom-announce-collaboration-to-advance-sovereign-ai-infrastructure-with-nvidia-nvlink-fusion",
    "checked_at": "2026-11-09T12:07:25.694612+00:00",
    "note": "NVIDIA/Rebellions/SK Telecom宣布NVLink Fusion合作；计划部署不是已兑现收入。"
  },
  {
    "url": "https://chinaselectcommittee.house.gov/sites/evo-subsites/selectcommitteeontheccp.house.gov/files/evo-media-document/nvidia-letter-pdf.pdf",
    "checked_at": "2026-11-09T12:07:25.694612+00:00",
    "note": "11月4日信函请求18日闭门简报，11日前回复或提出替代日期；非确认日程或传票。"
  },
  {
    "url": "https://apnews.com/article/f7b507b55634985d6013d36265b3fbc0",
    "checked_at": "2026-11-09T12:07:25.694612+00:00",
    "note": "AP报道外交接触尚无突破、特朗普有条件不新增打击；未宣布全面停火。"
  },
  {
    "url": "https://apnews.com/article/3345b9f05c54d58909e88f6dcb9c1cd8",
    "checked_at": "2026-11-09T12:07:25.694612+00:00",
    "note": "AP报道中方否认相关指控；否认与调查分别呈现，不直接认定任何一方指控已证实。"
  },
  {
    "url": "https://www.ici.org/research/stats/etf_flows",
    "checked_at": "2026-11-09T12:07:25.694612+00:00",
    "note": "本次核验仍截至10月28日"
  },
  {
    "url": "https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/",
    "checked_at": "2026-11-09T12:07:25.694612+00:00",
    "note": "截至6日NAV464.02，NVDA权重20.75%；缺份额桥"
  },
  {
    "url": "https://www.silicondata.com/products/silicon-index/h100",
    "checked_at": "2026-11-09T12:07:25.694612+00:00",
    "note": "截至8日3.00"
  },
  {
    "url": "https://www.cnn.com/markets/fear-and-greed",
    "checked_at": "2026-11-09T12:07:25.694612+00:00",
    "note": "9日06:45:01EST值25"
  },
  {
    "url": "https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool",
    "checked_at": "2026-11-09T12:07:25.694612+00:00",
    "note": "动态概率未获取，不引用快讯81%为官方核验"
  },
  {
    "url": "https://www.bls.gov/schedule/2026/11_sched.htm",
    "checked_at": "2026-11-09T12:07:25.694612+00:00",
    "note": "CPI10日、PPI13日08:30EST"
  },
  {
    "url": "https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-announces-date-third-quarter-2026-financial-results",
    "checked_at": "2026-11-09T12:07:25.694612+00:00",
    "note": "9日盘后，电话会17EST"
  },
  {
    "url": "https://investors.coreweave.com/events-and-presentations/event-details/2026/CoreWeave-Third-Quarter-2026-Earnings-Call/default.aspx",
    "checked_at": "2026-11-09T12:07:25.694612+00:00",
    "note": "10日17EST"
  },
  {
    "url": "https://nebius.com/newsroom/nebius-group-announces-date-of-third-quarter-2026-results-and-conference-call",
    "checked_at": "2026-11-09T12:07:25.694612+00:00",
    "note": "12日盘前，电话会08EST"
  }
]
```

## 付费信源建议（未订阅）

```json
[]
```
