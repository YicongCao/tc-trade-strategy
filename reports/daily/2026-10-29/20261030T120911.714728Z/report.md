# 每日交易总结 · 2026-10-29

## 一分钟读懂 · Agent 摘要

### 当前判断

反弹仍不可靠，盘前科技压力比早报更重；目前更像科技集中下修与非科技轮动，尚不能确认全市场极端恐慌。

### 与上次相比

北京时间20点附近，QQQ约697.75、SMH533.42，均低于早报警戒位；Amazon新10-Q已提交。XOM新业绩与ABBV上调指引给能源、医疗增加独立催化剂。

### 最重要的信号

- QQQ较昨收约−2.46%、SMH−5.03%，存储与AI基础设施同步承压。
- RSP约220.34、XLF57.36、XLV186.90仍相对强；盘前成交稀疏，需开盘确认。
- VIX盘前18.60高于昨收17.20；信用仅更新至28日，不能据其稳定排除风险。

### 接下来观察

- 先等30–60分钟高低点抬升并守常规VWAP；QQQ先收704.40、SMH先收546.67，随后再看前日低点。
- 金融、医疗优先观察承接，能源关注财报电话会；科技强业绩也须通过价格检验。
- 若等权与非科技一起跌破前日低点，且油价/信用风险共振，降低反弹评级。

### 不要忽略

尚未开盘，无今日常规VWAP。CNN、真实广度、当期ETF申赎缺失；四家公司最新估值桥未齐，不输出伪精确目标价。

## 研究结论

10月30日晚报：科技盘前继续下修，反弹尚不可靠；能源与医疗有新增业绩支撑，关注能否在常规开盘后承接。

## 时点与口径

| 项目 | 内容 |
| --- | --- |
| 模式 | 每日交易总结 |
| 常规交易窗口 | 2026-10-29 → 2026-10-29（纽约交易日） |
| 截止·纽约 | 2026-10-30T08:09:01.914944-04:00 |
| 截止·北京 | 2026-10-30T20:09:01.914944+08:00 |
| 实际生成时间 | 2026-10-30T12:09:02.150496+00:00 |
| 市场阶段 | 盘前 |
| 下一交易日 | 2026-10-30 |
| 运行重点 | 全市场 |
| 上一版本 | reports/daily/2026-10-29/20261030T002817.049748Z/evidence.json |
| 质量 | partial |
| Daily 北京时间计划时段 | 2026-10-30T20:00:00+08:00 |

## 采集、补查与剩余缺口

| 目标 | 补查结果 | 来源 | 观测 / 抓取时间 | 说明 |
| --- | --- | --- | --- | --- |
| 1147445 | 已校验接入 | https://gamma-api.polymarket.com/events/1147445 | 2026-10-30T12:01:58.852051+00:00 / 2026-10-30T12:01:58.852051+00:00 | Gamma current quote snapshot; same settlement definition, not last trade time |
| 549019 | 已校验接入 | https://gamma-api.polymarket.com/events/549019 | 2026-10-30T12:02:01.424076+00:00 / 2026-10-30T12:02:01.424076+00:00 | Gamma current quote snapshot; same settlement definition, not last trade time |
| 1262633 | 已校验接入 | https://gamma-api.polymarket.com/events/1262633 | 2026-10-30T12:01:58.547359+00:00 / 2026-10-30T12:01:58.547359+00:00 | Gamma current quote snapshot; same settlement definition, not last trade time |
| 1262630 | 已校验接入 | https://gamma-api.polymarket.com/events/1262630 | 2026-10-30T12:01:58.965935+00:00 / 2026-10-30T12:01:58.965935+00:00 | Gamma current quote snapshot; same settlement definition, not last trade time |

## 仍需核验的数据与影响

| 数据 | 状态 | 需要核验 | 影响 |
| --- | --- | --- | --- |
| history.DRAM | insufficient_history | 连续完整交易日 OHLC；SMA200 至少200条，ATR14至少15条 | 降低相关判断可信度；保留缺口 |
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
| prices.SPY.value | 769.36 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_1d_pct | -0.38 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_5d_pct | 0.71 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_20d_pct | 0.70 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_60d_pct | 0.19 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_1d_pp | 0.00 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_5d_pp | 0.00 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_20d_pp | 0.00 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_60d_pp | 0.00 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma20 | 771.16 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma50 | 766.87 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma200 | 725.63 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma20_pct | -0.23 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma50_pct | 0.32 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma200_pct | 6.03 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_sma | 7.11 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_pct | 0.92 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.drawdown_from_63d_high_pct | -1.25 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.volume_vs_previous20_ratio | 1.05 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SPY/history/ |
| prices.QQQ.value | 715.34 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_1d_pct | -1.42 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_5d_pct | 1.54 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_20d_pct | -3.60 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_60d_pct | -0.17 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_1d_pp | -1.03 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_5d_pp | 0.84 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_20d_pp | -4.30 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_60d_pp | -0.36 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma20 | 731.14 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma50 | 725.10 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma200 | 678.01 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma20_pct | -2.16 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma50_pct | -1.35 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma200_pct | 5.51 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_sma | 12.56 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_pct | 1.76 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.drawdown_from_63d_high_pct | -5.83 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.volume_vs_previous20_ratio | 1.03 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.IWM.value | 284.01 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_1d_pct | 0.97 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_5d_pct | 2.65 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_20d_pct | 1.79 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_60d_pct | -5.01 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_1d_pp | 1.35 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_5d_pp | 1.95 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_20d_pp | 1.09 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_60d_pp | -5.20 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma20 | 277.52 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma50 | 284.38 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma200 | 277.61 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma20_pct | 2.34 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma50_pct | -0.13 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma200_pct | 2.31 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_sma | 3.61 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_pct | 1.27 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.drawdown_from_63d_high_pct | -6.67 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.volume_vs_previous20_ratio | 0.87 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IWM/history/ |
| prices.RSP.value | 220.04 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_1d_pct | 1.20 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_5d_pct | 0.83 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_20d_pct | 5.28 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_60d_pct | 0.52 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_1d_pp | 1.58 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_5d_pp | 0.13 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_20d_pp | 4.58 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_60d_pp | 0.33 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma20 | 214.46 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma50 | 214.75 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma200 | 206.41 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma20_pct | 2.60 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma50_pct | 2.46 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma200_pct | 6.60 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_sma | 2.03 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_pct | 0.92 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.drawdown_from_63d_high_pct | -0.85 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.volume_vs_previous20_ratio | 0.98 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/RSP/history/ |
| prices.GLD.value | 368.57 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_1d_pct | -1.32 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_5d_pct | -0.12 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_20d_pct | -3.71 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_60d_pct | -5.41 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_1d_pp | -0.94 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_5d_pp | -0.82 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_20d_pp | -4.41 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_60d_pp | -5.60 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma20 | 376.98 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma50 | 391.76 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma200 | 413.27 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma20_pct | -2.23 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma50_pct | -5.92 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma200_pct | -10.82 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_sma | 5.13 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_pct | 1.39 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.drawdown_from_63d_high_pct | -13.90 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.volume_vs_previous20_ratio | 1.16 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GC=F.value | 4,031.40 | USD_per_troy_ounce | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_1d_pct | -0.50 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_5d_pct | -0.71 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_20d_pct | -4.07 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_60d_pct | -6.36 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_1d_pp | -0.12 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_5d_pp | -1.42 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_20d_pp | -4.77 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_60d_pp | -6.55 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma20 | 4,128.21 | USD_per_troy_ounce | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma50 | 4,308.25 | USD_per_troy_ounce | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma200 | 4,523.00 | USD_per_troy_ounce | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma20_pct | -2.35 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma50_pct | -6.43 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma200_pct | -10.87 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_sma | 68.19 | USD_per_troy_ounce | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_pct | 1.69 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.drawdown_from_63d_high_pct | -14.19 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.volume_vs_previous20_ratio | 1.03 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.CL=F.value | 102.00 | USD_per_barrel | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_1d_pct | -0.76 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_5d_pct | 2.54 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_20d_pct | 9.83 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_60d_pct | 35.60 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_1d_pp | -0.38 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_5d_pp | 1.84 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_20d_pp | 9.13 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_60d_pp | 35.41 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma20 | 96.79 | USD_per_barrel | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma50 | 94.30 | USD_per_barrel | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma200 | 86.13 | USD_per_barrel | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma20_pct | 5.39 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma50_pct | 8.16 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma200_pct | 18.42 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_sma | 4.38 | USD_per_barrel | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_pct | 4.30 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.drawdown_from_63d_high_pct | -3.62 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.volume_vs_previous20_ratio | 1.09 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.BZ=F.value | 114.88 | USD_per_barrel | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_1d_pct | -0.38 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_5d_pct | 1.51 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_20d_pct | 12.29 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_60d_pct | 44.59 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_1d_pp | 0.00 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_5d_pp | 0.80 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_20d_pp | 11.58 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_60d_pp | 44.40 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma20 | 108.17 | USD_per_barrel | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma50 | 102.79 | USD_per_barrel | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma200 | 92.20 | USD_per_barrel | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma20_pct | 6.20 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma50_pct | 11.76 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma200_pct | 24.60 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_sma | 3.83 | USD_per_barrel | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_pct | 3.33 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.drawdown_from_63d_high_pct | -1.58 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.volume_vs_previous20_ratio | 0.33 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.TLT.value | 81.49 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_1d_pct | 0.62 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_5d_pct | -0.31 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_20d_pct | 4.86 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_60d_pct | -1.05 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_1d_pp | 1.00 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_5d_pp | -1.01 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_20d_pp | 4.16 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_60d_pp | -1.24 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma20 | 79.45 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma50 | 80.27 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma200 | 83.24 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma20_pct | 2.57 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma50_pct | 1.52 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma200_pct | -2.11 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_sma | 0.82 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_pct | 1.01 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.drawdown_from_63d_high_pct | -1.60 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.volume_vs_previous20_ratio | 0.62 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/TLT/history/ |
| prices.UUP.value | 29.04 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_1d_pct | -0.07 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_5d_pct | 0.48 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_20d_pct | 0.28 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_60d_pct | 3.38 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_1d_pp | 0.31 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_5d_pp | -0.22 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_20d_pp | -0.43 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_60d_pp | 3.19 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma20 | 29.00 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma50 | 28.56 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma200 | 27.92 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma20_pct | 0.15 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma50_pct | 1.67 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma200_pct | 4.02 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_sma | 0.12 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_pct | 0.41 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.drawdown_from_63d_high_pct | -0.31 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.volume_vs_previous20_ratio | 0.78 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/UUP/history/ |
| prices.HYG.value | 77.58 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_1d_pct | -0.01 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_5d_pct | 0.62 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_20d_pct | 0.88 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_60d_pct | -1.47 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_1d_pp | 0.37 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_5d_pp | -0.08 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_20d_pp | 0.18 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_60d_pp | -1.66 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma20 | 77.13 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma50 | 77.84 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma200 | 77.89 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma20_pct | 0.58 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma50_pct | -0.33 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma200_pct | -0.40 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_sma | 0.30 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_pct | 0.39 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.drawdown_from_63d_high_pct | -1.96 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.volume_vs_previous20_ratio | 0.93 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/HYG/history/ |
| prices.LQD.value | 104.22 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_1d_pct | 0.14 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_5d_pct | -0.06 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_20d_pct | 2.15 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_60d_pct | -1.53 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_1d_pp | 0.53 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_5d_pp | -0.76 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_20d_pp | 1.44 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_60d_pp | -1.72 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma20 | 103.08 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma50 | 103.79 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma200 | 105.86 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma20_pct | 1.11 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma50_pct | 0.42 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma200_pct | -1.55 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_sma | 0.63 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_pct | 0.61 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.drawdown_from_63d_high_pct | -1.64 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.volume_vs_previous20_ratio | 1.61 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/LQD/history/ |
| prices.^VIX.value | 17.20 | index | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_1d_pct | 1.71 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_5d_pct | -9.62 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_20d_pct | 4.94 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_60d_pct | 13.53 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_1d_pp | 2.10 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_5d_pp | -10.32 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_20d_pp | 4.24 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_60d_pp | 13.18 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma20 | 16.80 | index | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma50 | 16.10 | index | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma200 | 18.24 | index | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma20_pct | 2.41 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma50_pct | 6.85 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma200_pct | -5.70 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_sma | 2.05 | index | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_pct | 11.92 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.drawdown_from_63d_high_pct | -13.96 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-29 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX3M.value | 19.37 | index | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_1d_pct | 0.78 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_5d_pct | -3.73 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_20d_pct | 4.25 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_60d_pct | 2.22 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_1d_pp | 1.16 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_5d_pp | -4.43 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_20d_pp | 3.55 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_60d_pp | 2.02 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma20 | 18.84 | index | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma50 | 18.54 | index | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma200 | 20.50 | index | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma20_pct | 2.79 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma50_pct | 4.47 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma200_pct | -5.52 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_sma | 1.13 | index | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_pct | 5.85 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.drawdown_from_63d_high_pct | -5.51 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-29 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VVIX.value | 98.01 | index | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_1d_pct | 1.45 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_5d_pct | -9.20 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_20d_pct | 6.52 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_60d_pct | 8.38 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_1d_pp | 1.83 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_5d_pp | -9.91 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_20d_pp | 5.82 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_60d_pp | 8.19 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma20 | 94.54 | index | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma50 | 91.27 | index | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma200 | 98.80 | index | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma20_pct | 3.67 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma50_pct | 7.38 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma200_pct | -0.80 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_sma | 9.70 | index | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_pct | 9.89 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.drawdown_from_63d_high_pct | -10.83 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-29 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^MOVE.value | 93.54 | index | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_1d_pct | -1.07 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_5d_pct | -12.45 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_20d_pct | -15.31 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_60d_pct | 20.60 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_1d_pp | -0.69 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_5d_pp | -13.16 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_20d_pp | -16.19 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_60d_pp | 20.61 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma20 | 101.85 | index | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma50 | 89.77 | index | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma200 | 77.34 | index | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma20_pct | -8.16 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma50_pct | 4.20 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma200_pct | 20.94 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_sma | 4.80 | index | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_pct | 5.13 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.drawdown_from_63d_high_pct | -17.66 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-29 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.NVDA.value | 213.66 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_1d_pct | -0.80 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_5d_pct | 0.68 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_20d_pct | -7.45 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_60d_pct | -2.43 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_1d_pp | -0.42 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_5d_pp | -0.02 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_20d_pp | -8.15 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_60d_pp | -2.62 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma20 | 222.93 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma50 | 221.92 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma200 | 203.98 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma20_pct | -4.16 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma50_pct | -3.72 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma200_pct | 4.74 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_sma | 5.94 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_pct | 2.78 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.drawdown_from_63d_high_pct | -10.69 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.volume_vs_previous20_ratio | 0.76 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.MSFT.value | 530.14 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_1d_pct | -0.16 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_5d_pct | 1.74 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_20d_pct | 3.38 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_60d_pct | 8.96 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_1d_pp | 0.22 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_5d_pp | 1.03 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_20d_pp | 2.68 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_60d_pp | 8.77 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma20 | 530.76 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma50 | 512.10 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma200 | 436.53 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma20_pct | -0.12 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma50_pct | 3.52 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma200_pct | 21.45 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_sma | 11.16 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_pct | 2.10 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.drawdown_from_63d_high_pct | -2.45 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.volume_vs_previous20_ratio | 1.95 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.AMZN.value | 243.79 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_1d_pct | -4.25 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_5d_pct | -2.63 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_20d_pct | -1.79 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_60d_pct | -10.58 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_1d_pp | -3.86 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_5d_pp | -3.34 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_20d_pp | -2.49 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_60d_pp | -10.78 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma20 | 254.95 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma50 | 254.67 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma200 | 243.38 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma20_pct | -4.38 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma50_pct | -4.27 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma200_pct | 0.17 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_sma | 7.00 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_pct | 2.87 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.drawdown_from_63d_high_pct | -14.16 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.volume_vs_previous20_ratio | 2.35 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.GOOGL.value | 283.82 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_1d_pct | -12.64 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_5d_pct | -12.46 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_20d_pct | -16.09 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_60d_pct | -21.64 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_1d_pp | -12.26 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_5d_pp | -13.17 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_20d_pp | -16.79 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_60d_pp | -21.83 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma20 | 337.09 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma50 | 340.24 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma200 | 340.62 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma20_pct | -15.80 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma50_pct | -16.58 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma200_pct | -16.68 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_sma | 10.78 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_pct | 3.80 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.drawdown_from_63d_high_pct | -24.80 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.volume_vs_previous20_ratio | 5.43 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.META.value | 624.52 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_1d_pct | 1.96 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_5d_pct | -3.75 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_20d_pct | -13.97 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_60d_pct | 6.16 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_1d_pp | 2.35 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_5d_pp | -4.46 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_20d_pp | -14.67 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_60d_pp | 5.96 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma20 | 696.76 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma50 | 668.40 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma200 | 631.27 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma20_pct | -10.37 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma50_pct | -6.56 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma200_pct | -1.07 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_sma | 26.29 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_pct | 4.21 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.drawdown_from_63d_high_pct | -19.69 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.volume_vs_previous20_ratio | 1.44 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/META/history/ |
| prices.CRWV.value | 60.74 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_1d_pct | -4.99 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_5d_pct | 9.24 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_20d_pct | -31.42 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_60d_pct | -32.43 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_1d_pp | -4.61 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_5d_pp | 8.54 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_20d_pp | -32.12 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_60d_pp | -32.62 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma20 | 70.51 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma50 | 80.15 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma200 | 91.52 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma20_pct | -13.85 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma50_pct | -24.22 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma200_pct | -33.63 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_sma | 6.52 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_pct | 10.73 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.drawdown_from_63d_high_pct | -43.62 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.volume_vs_previous20_ratio | 0.81 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.MU.value | 934.27 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_1d_pct | -4.98 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_5d_pct | 9.08 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_20d_pct | -14.85 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_60d_pct | 4.62 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_1d_pp | -4.60 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_5d_pp | 8.37 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_20d_pp | -15.55 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_60d_pp | 4.42 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma20 | 960.05 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma50 | 980.38 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma200 | 743.87 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma20_pct | -2.69 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma50_pct | -4.70 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma200_pct | 25.60 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_sma | 49.40 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_pct | 5.29 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.drawdown_from_63d_high_pct | -14.85 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.volume_vs_previous20_ratio | 0.81 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MU/history/ |
| prices.DRAM.value | 51.75 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_1d_pct | -4.38 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_5d_pct | 13.29 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_20d_pct | -16.57 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_60d_pct | -3.70 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_1d_pp | -4.00 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_5d_pp | 12.58 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_20d_pp | -17.28 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_60d_pp | -3.90 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma20 | 52.66 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma50 | 56.16 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma200 | 缺失 | USD_per_share | 2026-10-29 | unavailable | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma20_pct | -1.73 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma50_pct | -7.85 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma200_pct | 缺失 | percent | 2026-10-29 | unavailable | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_sma | 2.81 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_pct | 5.43 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.drawdown_from_63d_high_pct | -18.66 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.volume_vs_previous20_ratio | 0.95 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.VRT.value | 245.92 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_1d_pct | 1.23 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_5d_pct | 25.73 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_20d_pct | -0.08 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_60d_pct | -11.50 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_1d_pp | 1.61 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_5d_pp | 25.03 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_20d_pp | -0.78 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_60d_pp | -11.69 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma20 | 226.07 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma50 | 243.23 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma200 | 270.13 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma20_pct | 8.78 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma50_pct | 1.11 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma200_pct | -8.96 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_sma | 14.09 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_pct | 5.73 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.drawdown_from_63d_high_pct | -16.29 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.volume_vs_previous20_ratio | 1.45 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/VRT/history/ |
| prices.XLK.value | 188.74 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_1d_pct | -1.18 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_5d_pct | 3.51 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_20d_pct | -4.59 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_60d_pct | 1.64 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_1d_pp | -0.80 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_5d_pp | 2.80 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_20d_pp | -5.29 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_60d_pp | 1.45 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma20 | 191.87 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma50 | 189.67 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma200 | 169.06 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma20_pct | -1.63 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma50_pct | -0.49 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma200_pct | 11.64 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_sma | 4.24 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_pct | 2.24 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.drawdown_from_63d_high_pct | -6.56 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.volume_vs_previous20_ratio | 0.85 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLE.value | 68.71 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_1d_pct | 0.38 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_5d_pct | 1.69 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_20d_pct | 9.59 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_60d_pct | 20.60 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_1d_pp | 0.76 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_5d_pp | 0.98 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_20d_pp | 8.88 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_60d_pp | 20.41 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma20 | 66.76 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma50 | 64.64 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma200 | 58.04 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma20_pct | 2.92 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma50_pct | 6.29 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma200_pct | 18.39 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_sma | 1.42 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_pct | 2.06 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.drawdown_from_63d_high_pct | -1.34 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.volume_vs_previous20_ratio | 0.78 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLF.value | 56.94 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_1d_pct | 1.44 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_5d_pct | 0.51 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_20d_pct | 6.51 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_60d_pct | -1.48 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_1d_pp | 1.83 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_5d_pp | -0.19 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_20d_pp | 5.81 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_60d_pp | -1.67 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma20 | 55.18 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma50 | 55.87 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma200 | 53.39 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma20_pct | 3.19 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma50_pct | 1.92 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma200_pct | 6.65 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_sma | 0.72 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_pct | 1.27 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.drawdown_from_63d_high_pct | -2.42 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.volume_vs_previous20_ratio | 1.00 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLI.value | 170.13 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_1d_pct | 0.97 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_5d_pct | 2.04 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_20d_pct | 0.88 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_60d_pct | -8.46 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_1d_pp | 1.36 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_5d_pp | 1.33 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_20d_pp | 0.18 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_60d_pp | -8.65 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma20 | 168.21 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma50 | 170.74 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma200 | 172.55 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma20_pct | 1.14 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma50_pct | -0.36 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma200_pct | -1.41 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_sma | 2.58 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_pct | 1.52 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.drawdown_from_63d_high_pct | -8.54 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.volume_vs_previous20_ratio | 1.04 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLV.value | 184.04 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_1d_pct | 2.40 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_5d_pct | 1.51 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_20d_pct | 10.73 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_60d_pct | 12.54 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_1d_pp | 2.79 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_5d_pp | 0.80 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_20d_pp | 10.03 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_60d_pp | 12.35 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma20 | 174.76 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma50 | 171.69 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma200 | 157.52 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma20_pct | 5.31 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma50_pct | 7.19 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma200_pct | 16.83 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_sma | 3.15 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_pct | 1.71 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.drawdown_from_63d_high_pct | 0.00 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.volume_vs_previous20_ratio | 1.77 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLP.value | 88.18 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_1d_pct | 1.54 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_5d_pct | -2.01 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_20d_pct | 9.77 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_60d_pct | 4.02 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_1d_pp | 1.93 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_5d_pp | -2.72 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_20d_pp | 9.07 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_60d_pp | 3.83 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma20 | 85.57 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma50 | 84.29 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma200 | 83.53 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma20_pct | 3.05 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma50_pct | 4.61 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma200_pct | 5.56 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_sma | 1.39 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_pct | 1.57 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.drawdown_from_63d_high_pct | -2.01 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.volume_vs_previous20_ratio | 1.08 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLY.value | 116.20 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_1d_pct | 0.75 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_5d_pct | 1.03 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_20d_pct | 6.79 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_60d_pct | -1.84 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_1d_pp | 1.14 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_5d_pp | 0.33 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_20d_pp | 6.09 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_60d_pp | -2.03 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma20 | 113.25 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma50 | 113.16 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma200 | 115.19 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma20_pct | 2.61 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma50_pct | 2.69 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma200_pct | 0.88 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_sma | 1.67 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_pct | 1.44 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.drawdown_from_63d_high_pct | -2.84 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.volume_vs_previous20_ratio | 0.90 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLC.value | 101.21 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_1d_pct | -1.87 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_5d_pct | -5.78 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_20d_pct | -7.94 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_60d_pct | -8.41 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_1d_pp | -1.49 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_5d_pp | -6.49 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_20d_pp | -8.64 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_60d_pp | -8.60 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma20 | 108.93 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma50 | 110.77 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma200 | 112.43 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma20_pct | -7.09 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma50_pct | -8.63 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma200_pct | -9.98 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_sma | 1.87 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_pct | 1.84 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.drawdown_from_63d_high_pct | -11.80 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.volume_vs_previous20_ratio | 1.63 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLU.value | 43.14 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_1d_pct | 1.53 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_5d_pct | 0.63 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_20d_pct | 8.72 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_60d_pct | -0.46 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_1d_pp | 1.91 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_5d_pp | -0.08 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_20d_pp | 8.02 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_60d_pp | -0.66 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma20 | 41.77 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma50 | 41.63 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma200 | 43.80 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma20_pct | 3.28 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma50_pct | 3.64 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma200_pct | -1.50 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_sma | 0.62 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_pct | 1.44 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.drawdown_from_63d_high_pct | -2.04 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.volume_vs_previous20_ratio | 0.78 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLRE.value | 43.06 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_1d_pct | 2.21 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_5d_pct | 1.27 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_20d_pct | 5.85 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_60d_pct | -3.93 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_1d_pp | 2.59 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_5d_pp | 0.56 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_20d_pp | 5.15 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_60d_pp | -4.12 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma20 | 41.83 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma50 | 42.53 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma200 | 42.76 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma20_pct | 2.94 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma50_pct | 1.24 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma200_pct | 0.71 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_sma | 0.65 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_pct | 1.51 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.drawdown_from_63d_high_pct | -4.27 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.volume_vs_previous20_ratio | 0.83 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLB.value | 52.53 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_1d_pct | 1.29 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_5d_pct | 1.63 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_20d_pct | 8.22 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_60d_pct | 0.25 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_1d_pp | 1.67 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_5d_pp | 0.92 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_20d_pp | 7.52 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_60d_pp | 0.06 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma20 | 50.51 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma50 | 50.88 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma200 | 50.70 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma20_pct | 4.01 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma50_pct | 3.23 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma200_pct | 3.61 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_sma | 0.67 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_pct | 1.28 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.drawdown_from_63d_high_pct | -1.67 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.volume_vs_previous20_ratio | 1.32 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLB/history/ |
| prices.SMH.value | 561.67 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_1d_pct | -1.06 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_5d_pct | 7.32 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_20d_pct | -9.09 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_60d_pct | -1.41 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_1d_pp | -0.67 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_5d_pp | 6.62 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_20d_pp | -9.79 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_60d_pp | -1.60 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma20 | 575.31 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma50 | 573.42 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma200 | 518.83 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma20_pct | -2.37 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma50_pct | -2.05 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma200_pct | 8.26 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_sma | 18.44 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_pct | 3.28 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.drawdown_from_63d_high_pct | -11.39 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.volume_vs_previous20_ratio | 0.68 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SMH/history/ |
| prices.IGV.value | 107.97 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_1d_pct | -3.52 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_5d_pct | -0.69 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_20d_pct | -0.24 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_60d_pct | 6.57 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_1d_pp | -3.14 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_5d_pp | -1.40 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_20d_pp | -0.94 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_60d_pp | 6.38 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma20 | 109.47 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma50 | 106.94 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma200 | 93.94 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma20_pct | -1.37 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma50_pct | 0.96 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma200_pct | 14.94 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_sma | 3.05 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_pct | 2.82 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.drawdown_from_63d_high_pct | -4.17 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.volume_vs_previous20_ratio | 1.49 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IGV/history/ |
| prices.XOP.value | 199.52 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_1d_pct | -0.42 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_5d_pct | 1.35 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_20d_pct | 8.26 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_60d_pct | 21.26 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_1d_pp | -0.04 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_5d_pp | 0.64 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_20d_pp | 7.56 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_60d_pp | 21.07 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma20 | 196.16 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma50 | 191.04 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma200 | 169.20 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma20_pct | 1.71 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma50_pct | 4.44 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma200_pct | 17.92 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_sma | 4.92 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_pct | 2.47 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.drawdown_from_63d_high_pct | -2.61 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.volume_vs_previous20_ratio | 0.43 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XOP/history/ |
| prices.OIH.value | 407.90 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_1d_pct | -0.29 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_5d_pct | 8.20 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_20d_pct | 7.03 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_60d_pct | 5.93 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_1d_pp | 0.09 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_5d_pp | 7.49 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_20d_pp | 6.32 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_60d_pp | 5.74 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma20 | 390.60 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma50 | 401.25 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma200 | 397.21 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma20_pct | 4.43 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma50_pct | 1.66 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma200_pct | 2.69 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_sma | 11.64 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_pct | 2.85 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.drawdown_from_63d_high_pct | -6.57 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.volume_vs_previous20_ratio | 0.49 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/OIH/history/ |
| prices.ITA.value | 214.30 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_1d_pct | 3.16 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_5d_pct | 4.80 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_20d_pct | 3.01 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_60d_pct | -14.96 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_1d_pp | 3.54 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_5d_pp | 4.10 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_20d_pp | 2.31 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_60d_pp | -15.15 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma20 | 206.51 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma50 | 215.18 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma200 | 228.73 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma20_pct | 3.77 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma50_pct | -0.41 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma200_pct | -6.31 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_sma | 4.40 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_pct | 2.05 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.drawdown_from_63d_high_pct | -15.27 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.volume_vs_previous20_ratio | 1.31 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ARKX.value | 30.99 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_1d_pct | 0.62 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_5d_pct | 4.59 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_20d_pct | -3.07 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_60d_pct | -4.88 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_1d_pp | 1.00 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_5d_pp | 3.88 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_20d_pp | -3.77 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_60d_pp | -5.07 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma20 | 31.14 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma50 | 31.82 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma200 | 32.51 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma20_pct | -0.48 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma50_pct | -2.61 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma200_pct | -4.67 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_sma | 0.76 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_pct | 2.46 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.drawdown_from_63d_high_pct | -11.10 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.volume_vs_previous20_ratio | 0.77 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.KRE.value | 72.86 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_1d_pct | 1.04 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_5d_pct | 0.62 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_20d_pct | 4.16 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_60d_pct | -5.26 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_1d_pp | 1.42 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_5d_pp | -0.09 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_20d_pp | 3.46 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_60d_pp | -5.45 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma20 | 70.56 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma50 | 71.85 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma200 | 70.31 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma20_pct | 3.27 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma50_pct | 1.41 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma200_pct | 3.62 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_sma | 1.29 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_pct | 1.77 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.drawdown_from_63d_high_pct | -5.97 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.volume_vs_previous20_ratio | 0.61 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/KRE/history/ |
| prices.SKYY.value | 167.42 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_1d_pct | -2.84 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_5d_pct | 1.89 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_20d_pct | 0.28 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_60d_pct | 9.08 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_1d_pp | -2.46 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_5d_pp | 1.18 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_20d_pp | -0.43 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_60d_pp | 8.89 | pp | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma20 | 168.09 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma50 | 164.79 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma200 | 136.34 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma20_pct | -0.40 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma50_pct | 1.59 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma200_pct | 22.79 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_sma | 5.03 | USD_per_share | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_pct | 3.00 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.drawdown_from_63d_high_pct | -4.27 | percent | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.volume_vs_previous20_ratio | 1.73 | ratio | 2026-10-29 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SKYY/history/ |
| macro.DGS2.value | 4.67 | percent | 2026-10-28 | lagged | source_series_v1:DGS2 | https://fred.stlouisfed.org/series/DGS2 |
| macro.BAMLH0A0HYM2.value | 3.14 | percentage_points | 2026-10-28 | lagged | source_series_v1:BAMLH0A0HYM2 | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| macro.BAMLC0A0CM.value | 0.86 | percentage_points | 2026-10-28 | lagged | source_series_v1:BAMLC0A0CM | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| macro.DGS10.value | 5.05 | percent | 2026-10-28 | lagged | source_series_v1:DGS10 | https://fred.stlouisfed.org/series/DGS10 |
| macro.DFII10.value | 2.67 | percent | 2026-10-28 | lagged | source_series_v1:DFII10 | https://fred.stlouisfed.org/series/DFII10 |
| macro.T10YIE.value | 2.35 | percent | 2026-10-29 | ok | source_series_v1:T10YIE | https://fred.stlouisfed.org/series/T10YIE |
| macro.STLFSI4.value | -0.58 | index | 2026-10-23 | lagged | source_series_v1:STLFSI4 | https://fred.stlouisfed.org/series/STLFSI4 |
| macro.CBOE_VIX.value | 17.20 | index | 2026-10-29 | ok | source_series_v1:CBOE_VIX | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| macro.GPRD.value | 165.25 | index | 2026-10-26 | lagged | source_series_v1:GPRD | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_ACT.value | 149.77 | index | 2026-10-26 | lagged | source_series_v1:GPRD_ACT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_THREAT.value | 187.38 | index | 2026-10-26 | lagged | source_series_v1:GPRD_THREAT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA7.value | 181.42 | index | 2026-10-26 | lagged | source_series_v1:GPRD_MA7 | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA30.value | 175.44 | index | 2026-10-26 | lagged | source_series_v1:GPRD_MA30 | https://www.matteoiacoviello.com/gpr.htm |
| quotes.AMD.value | 520.75 | USD_per_share | 2026-10-30T12:01:50+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AMD |
| quotes.AMZN.value | 227.87 | USD_per_share | 2026-10-30T12:01:53+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AMZN |
| quotes.AVGO.value | 331.60 | USD_per_share | 2026-10-30T12:01:42+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AVGO |
| quotes.CAT.value | 634.00 | USD_per_share | 2026-10-30T12:00:40+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/CAT |
| quotes.CEG.value | 256.90 | USD_per_share | 2026-10-30T12:01:50+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/CEG |
| quotes.CVX.value | 235.00 | USD_per_share | 2026-10-30T12:01:08+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/CVX |
| quotes.DRAM.value | 48.51 | USD_per_share | 2026-10-30T12:01:38+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/DRAM |
| quotes.GEV.value | 854.00 | USD_per_share | 2026-10-30T12:01:33+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GEV |
| quotes.GLD.value | 363.51 | USD_per_share | 2026-10-30T12:01:15+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GLD |
| quotes.GLW.value | 119.76 | USD_per_share | 2026-10-30T12:00:53+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GLW |
| quotes.GOOGL.value | 281.00 | USD_per_share | 2026-10-30T12:01:50+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GOOGL |
| quotes.IGV.value | 106.81 | USD_per_share | 2026-10-30T11:45:34+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/IGV |
| quotes.ILMN.value | 253.00 | USD_per_share | 2026-10-30T11:21:00+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/ILMN |
| quotes.INTC.value | 69.08 | USD_per_share | 2026-10-30T12:02:01+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/INTC |
| quotes.IWM.value | 282.66 | USD_per_share | 2026-10-30T12:01:25+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/IWM |
| quotes.LLY.value | 1,410.01 | USD_per_share | 2026-10-30T12:00:30+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/LLY |
| quotes.META.value | 612.05 | USD_per_share | 2026-10-30T12:01:41+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/META |
| quotes.MSFT.value | 525.74 | USD_per_share | 2026-10-30T12:01:45+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/MSFT |
| quotes.MU.value | 882.00 | USD_per_share | 2026-10-30T12:02:01+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/MU |
| quotes.NOW.value | 109.11 | USD_per_share | 2026-10-30T12:00:35+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NOW |
| quotes.NVDA.value | 207.11 | USD_per_share | 2026-10-30T12:01:57+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| quotes.NXPI.value | 260.79 | USD_per_share | 2026-10-30T11:14:01+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NXPI |
| quotes.ORCL.value | 134.30 | USD_per_share | 2026-10-30T12:01:42+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/ORCL |
| quotes.PLTR.value | 193.41 | USD_per_share | 2026-10-30T12:02:01+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/PLTR |
| quotes.QQQ.value | 697.75 | USD_per_share | 2026-10-30T12:01:47+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| quotes.RSP.value | 220.34 | USD_per_share | 2026-10-30T11:55:16+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/RSP |
| quotes.SMH.value | 533.42 | USD_per_share | 2026-10-30T11:59:20+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SMH |
| quotes.SNDK.value | 1,211.69 | USD_per_share | 2026-10-30T12:01:57+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SNDK |
| quotes.SPY.value | 761.63 | USD_per_share | 2026-10-30T12:01:53+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SPY |
| quotes.STX.value | 649.48 | USD_per_share | 2026-10-30T12:01:22+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/STX |
| quotes.TLT.value | 81.95 | USD_per_share | 2026-10-30T12:01:43+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/TLT |
| quotes.VRT.value | 230.63 | USD_per_share | 2026-10-30T12:01:58+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/VRT |
| quotes.XLE.value | 69.75 | USD_per_share | 2026-10-30T12:01:04+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLE |
| quotes.XLF.value | 57.36 | USD_per_share | 2026-10-30T11:46:47+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLF |
| quotes.XLI.value | 169.41 | USD_per_share | 2026-10-30T11:40:37+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLI |
| quotes.XLV.value | 186.90 | USD_per_share | 2026-10-30T12:00:42+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLV |
| quotes.XOM.value | 186.64 | USD_per_share | 2026-10-30T12:01:56+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XOM |
| premarket.BZ_F.value | 113.54 | USD/barrel | 2026-10-30T11:51:56+00:00 | ok | 30日盘前实际分钟行情；期货具体交割月未对齐，不与连续日线或前次报告计算收益 | https://query1.finance.yahoo.com/v8/finance/chart/BZ=F |
| premarket.CL_F.value | 104.14 | USD/barrel | 2026-10-30T11:51:57+00:00 | ok | 30日盘前实际分钟行情；期货具体交割月未对齐，不与连续日线或前次报告计算收益 | https://query1.finance.yahoo.com/v8/finance/chart/CL=F |
| premarket.ES_F.value | 7,666.25 | index points | 2026-10-30T11:51:53+00:00 | ok | 30日盘前实际分钟行情；期货具体交割月未对齐，不与连续日线或前次报告计算收益 | https://query1.finance.yahoo.com/v8/finance/chart/ES=F |
| premarket.NQ_F.value | 28,781.25 | index points | 2026-10-30T11:51:56+00:00 | ok | 30日盘前实际分钟行情；期货具体交割月未对齐，不与连续日线或前次报告计算收益 | https://query1.finance.yahoo.com/v8/finance/chart/NQ=F |
| premarket.VIX.value | 18.60 | index points | 2026-10-30T11:46:46+00:00 | ok | 30日盘前实际分钟行情；期货具体交割月未对齐，不与连续日线或前次报告计算收益 | https://query1.finance.yahoo.com/v8/finance/chart/^VIX |

## 指标历史比较（不同日期观测，非连续交易日）

```json
[
  {
    "id": "prices.SPY.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -2.95001220703125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 5.39996337890625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.7262836122778449,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.7990030867549125,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.8077360781099663,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.7213574876448479,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.56640267322694,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.1226033071399022,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.18336735131130322,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -4.797264998149298,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.26849975585935226,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.44449768066408524,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.04410034179693412,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.34320556640625455,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.40483306884766534,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.007059020996053,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.41742154036138457,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.6431010947059224,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.3904715874267328,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.7487157763416463,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.4659572027260417,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.45216202696982677,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.01428658621651735,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.1964198521205356,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.005378059260294443,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.03223968301606106,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.37864843668169446,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.6931116036360208,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.2958904809519157,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.29023655194746323,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -10.26995849609375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 10.87005615234375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -2.0198592123736425,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.4431722845796302,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.4864795716251988,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 4.775158876896168,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.6827767917458658,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.3457638344394844,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.5169276821673674,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -6.739089478040173,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.2935756000957976,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.6441691978247177,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.6787434935152326,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 3.0538013892513205,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.1163741185189258,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.2231605272995818,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.3335603308560642,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.9418244798908746,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.334500122070267,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -6.0980010986327216,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.00010864257819775958,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.8804980468750045,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.45612762451173694,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.3242727661132676,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.223834559414816,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.283688180976884,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.4163698787809542,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.6169498092068135,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.5867664529780612,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.2458176291515244,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.621429443359375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.520721435546875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.11048620510068496,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.04683214168679428,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.351915180364494,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.430910741202851,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.21419042301767033,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.8006763783490247,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.720001220703125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 7.339996337890625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.5707944280901378,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.8982520454547505,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.9132515750842396,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.074955172429771,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.5649063301087942,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 3.5600458481626185,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.514667645736667,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.136537463678366,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.2970780403679827,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.09924895869983796,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.10551549697427332,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.35359768478492315,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.1313090033357343,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.4374425410227163,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.6980349970479702,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 3.660727534470931,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.24950103759766762,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.015499877929698869,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.3384802246093841,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -2.248690795898426,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.12210540771485512,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.5506406402587913,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.8889071754637268,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.6392989845789416,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.0740551026715672,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 3.344304009229715,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.9352126823001905,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.4459432223331468,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.1107134137834822,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.1399993896484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.02705839910083374,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.08434983047437616,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.8938690804578426,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.4121297178749774,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.11505740505942563,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.12932960260734705,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.6100006103515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.8199920654296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.2417674885846663,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.47106527336160386,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.46935990451784093,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.6636579140388177,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.7586956063771355,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.4965011231945935,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.4177880803951548,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.0169553579123747,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.9680511008625112,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.32793781339330863,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.33837617359212535,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -2.3850154016836655,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.3250982796040756,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.37389781605469175,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.601155431706458,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 3.780309640236923,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.5519996643066349,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.072498321533203,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.02396759033203466,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.3036016845703102,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.122987670898425,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.5802229309082065,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.9553658679485988,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.14425209747459533,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.226678064109965,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.9909607592564651,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.2016523996537076,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.5837081825802226,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.08500017438616081,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.04571424211774522,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.027999357376834677,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.028656536195722948,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.17601633190626,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.8200535986069402,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.012564155901239493,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.6178756289051918,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -4.94000244140625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.42999267578125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.6529884649868043,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.3030903102392521,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.319017004073042,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 3.4658156135895735,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.7825952039129955,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.085562489841919,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -5.2338365301665695,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -4.847034935027817,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.9267048527089594,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.5040872234843397,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.5112809259630757,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.7444581259447256,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.216192530686056,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.9629591827020167,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -5.050469178855266,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.04976993687851916,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.709500122070267,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -3.4510009765624545,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.9053997802734557,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -3.3905993652343795,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.2652999877930142,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.1513000488281477,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.124285146975279,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.773853521851886,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.0411372403565382,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.698437774648375,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.1373605815677035,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.14400250524445646,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.000714983258927937,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.049285888671875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.01820186562569215,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.011736034324299816,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.1540174169840096,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.1004491481356169,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.009279228786182703,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.065628328654834,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -20.2001953125,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -29.0,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.06589929734958089,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.660465222353158,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.6568666187676828,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.9164216155530545,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.8399310975268253,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.461336485471942,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -3.927546427641837,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -6.956835364390024,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.7921829096274258,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.8614621355982455,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.8491305406577165,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.1950641279082066,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.2735284242998848,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.3387331783320402,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -3.744179076330534,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -2.159570366240726,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -8.544995117186772,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -42.72001953124982,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -10.277998046874927,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -41.86799804687507,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -2.8385009765625,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -12.170002441405813,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.2865914890599952,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.3049247585127701,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.24505263192231475,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.23396065653672515,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.39042937564465063,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.4002659188116482,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.8714425223214306,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -2.078560965401792,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.013075909921081763,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.03911105514661117,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.42999268066604834,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.6173102559854495,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.08553797511691785,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.02291576162138531,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.779998779296875,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.529998779296875,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -3.641781421062107,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -3.1469606814001017,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -3.2516800143104874,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.012398263876002,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -3.838599852389679,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 4.694064915667839,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.04512698472431964,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 17.830502265064332,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -2.915497808784262,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -3.945963768155014,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -4.059416092420453,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.7089592237688458,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -3.2721971791627382,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 3.5714616085279367,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.13824036658698446,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 22.627767263213627,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.4564998626708956,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.6014999389648494,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.323399963378904,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.8157998657226528,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.20424999237060604,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.0809499931335438,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.309133656339645,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.22469980024792946,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.2021499574548908,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.6119886810692865,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.189238167116116,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.469595627424944,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.0750002179827014,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.1414282662527908,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.10559160931894773,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.03285497556649464,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.7370299213847242,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.3906252816056184,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.07838042155955338,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.08007595163079384,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.44000244140625,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.7099990844726562,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.646040227793999,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -4.378974670316316,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -4.462166349871777,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -5.333788273786633,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.8981845323899442,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 6.122962209402805,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.7184120710835629,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 19.875108210748294,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.9197566155161541,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -5.177977757071228,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -5.269902427981743,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -7.055145761431481,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.4645872056168852,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 5.000358902262903,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.5350447197722588,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 24.67237320889759,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.6284999847412109,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.929000091552723,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.4651998901367165,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.5501998901367102,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.24704998016358104,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.3098999595642056,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.0297716501602716,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.3307982786066486,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.9381290088379615,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.1374783834542157,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.8132675409541648,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.0856868021738002,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.036428724016462244,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.09142848423549088,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.04430028215726445,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.13112650181607544,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.37697261549394234,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.5764255894805346,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.2227827656685879,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.6858908258244403,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.5,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.25,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.4013849437087722,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.2520316900895168,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.2405437552704845,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -2.5191735853458908,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.3178395650639487,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.5285444819053362,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.3934136050465109,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.8838467371505954,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.127668555986617,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -2.0510347768444293,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -2.048279833380451,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -4.240531072990739,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.8842422382908888,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.405941174765434,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.5767809563578141,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 3.9134182609987023,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.18899993896485512,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.8364669799804716,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.017626800537101417,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.006428070068352554,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.016849479675300927,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.08323947906494311,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.38626098145682075,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.409514305141224,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.6450508805440958,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.30329553753025706,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.6203349081937648,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.20223242723107493,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.022142682756696397,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.0242854527064732,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.021106122180220677,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.026622260641400164,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.6037347613075505,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.2063298505032729,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.18191897329339524,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.681029309815001,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.019998550415039062,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.1400012969970703,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.13723052849130557,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.00033973831591316284,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.00034161921831366016,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.8292624616371813,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.7317415498395929,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.4557097261352894,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.18596777979669188,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.6930393423339796,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.8635141407691505,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.7986633484389993,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.8073944588916526,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.8920950260076665,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.1653388766126529,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.5783130332751916,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.3693351311079951,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 6.490304340483277,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.004000091552732954,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.06949996948242188,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.023200035095214844,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.09560001373290916,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.008450002670286949,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.04379999160766346,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.08279771008501413,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.2433611479774389,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.15271685186706296,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.15036682878284413,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.10315285599904467,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.33881789151102293,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.002857072012765069,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.010000092642647881,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.010110925003129378,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.036568437374486784,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.06865276687674227,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.48060865441297285,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.1556976403368266,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.23077178558804623,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.0099945068359375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.48000335693359375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 8.171393706124519e-06,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.16875947527466018,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.16983200165612278,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.6614662498850454,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.054997046738569644,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.4581158358388802,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.024484667820412476,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.21346010666921655,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.726291783671551,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.9677625620295727,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.9775680797660891,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.0598912377598024,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.5114056264883704,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.33551252869897796,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.2078520191317157,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 4.5838048914800815,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.03400001525879759,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.07614974975587074,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.02688796997070142,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.14807968139648153,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.0002841567993101535,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.0015435028076211665,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.05731860008530987,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.5235283080020192,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.021581956107885603,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.8047586922078631,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.013194564190621705,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.6182004714761713,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.006428309849330349,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.021428789411272298,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.008335376599013067,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.02535737299718599,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.012630119151191277,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.6065831651888454,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.2328709865869768,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.20956062255346386,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.15000152587890625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.05999755859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.3646561721332042,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.8925857387003022,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.8907882493434438,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.8111570677627689,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.14271842891810937,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.6147247461691707,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.1601547007624493,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.9676707449319033,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.090939784411049,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.6915888254552147,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.69852432745341,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -2.5325145554076167,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.42368424430883067,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.5078785609707315,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.3435220520737525,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 3.8295942532173943,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.10950012207031534,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.4961330413818388,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.028970947265619884,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.11660507202148551,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.013468818664549076,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.0654304504394645,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.038154258098810345,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.5475119064997092,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.17250746656054528,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.05494655302629159,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.15420418796162627,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.004171890471049711,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.029285430908203125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.0014294215611048156,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.027263903798072198,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.0010209873439326334,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.14156951418852204,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.05662492546557596,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.5766871383769807,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.39206709601685574,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.29000091552734375,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.8299999237060547,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 5.196705543387448,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -12.3737640552098,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -10.995288530512127,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -25.230013768299877,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.4536761980298296,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -16.500203730385657,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 6.573743075422954,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.1796903643686907,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 5.9229891556652925,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -13.172767141964714,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -11.803024608622092,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -26.95137125594472,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.0200788712567697,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -17.622807037525558,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 6.797573546549839,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 5.08540763677847,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.04050006866455291,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.48800005912780975,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.02380001068115334,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.2658000183105482,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.006800003051758097,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.0564500093460083,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.4833281346144256,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -14.286918337366284,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.646032378702289,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -13.353460987056298,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.555308724204174,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -10.356551368782386,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.0364287240164618,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.21142877851213715,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.01095577755260635,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.2575680074878175,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.4507299592186218,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -6.06733587136714,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.15000152587890625,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.75,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.5688987005937802,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -6.698195892366865,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -6.3985743082558555,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -12.543215912209883,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.37521220886529427,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -4.917945850996163,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.8368391849304175,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 8.634959900176252,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 3.295182312871625,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -7.4971989791217775,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -7.206310386365821,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -14.264573399854731,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.19119046436164577,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -6.0405491581360655,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 3.0202065362417208,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 13.43222489832555,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.0395000457763679,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.3689999580383301,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.016000022888185583,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.09259998321533303,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.00260000228881907,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.03320000648498578,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.5817503011808833,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -6.112144876509728,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.7194863983173594,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -4.589720890388538,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.719777331885763,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -3.8174914461564513,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.022142818995884328,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.10857132502964562,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.06953396387757493,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.7577675460387381,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.7317147603849055,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.9064097196218697,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.4000015258789062,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -9.930000305175781,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 4.3048297099957615,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -12.712691121072293,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -11.378294137363032,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -25.803209695839612,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.4472275241051102,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -12.657508864836633,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 4.017910169796002,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 9.779818113052418,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 5.031113322273606,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -13.511694207827208,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -12.186030215472998,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -27.524567183484457,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.8808248508781702,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -13.780112171976533,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 4.201277521107305,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 14.577083111201716,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.29999999999999716,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.756999969482422,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.2296000671386622,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.0995999145507795,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.015299987792971592,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.2054999923706049,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.1555499881225062,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -13.93307410999467,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.2669323759054052,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -12.321613556844625,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.4321619202363967,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -10.278435874589274,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.24714224679129337,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.5692841666085382,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.11244782801678888,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.4375478929908567,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.2737707935875022,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -9.034664702316874,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.0100021362304688,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -13.299995422363281,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.324034526141261,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -12.429480906939029,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -10.999695787766196,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -16.692832413589432,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -4.006156066669698,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -27.243040826867414,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 3.1208055277843734,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -19.809262359401547,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 3.050318138419106,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -13.228483993693942,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -11.807431865876161,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -18.41418990123428,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -3.827387417303264,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -28.626933712633907,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 5.313881605305468,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -16.4274786237124,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.8454998016357393,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.3994995117187585,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.37119995117187443,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.5990000915527247,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.1531999969482314,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.8405000114440924,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.22734044775837248,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -11.636903929532206,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.5623513106109543,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -18.36323652025671,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.5484791498946002,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -18.713533412837727,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.21428571428571352,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.7885709490094861,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.17182179518760243,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.09929094942429462,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.8890863994690612,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -11.707742606522231,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.720001220703125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.4499969482421875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.3760449974793967,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 3.5983989955540974,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 3.652151966036876,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.9941936518071643,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.7581343478030869,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.9423442302253795,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -4.1640219515999615,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -14.23577458866182,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.1023286097572416,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.799395908799185,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.84441588792691,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.2728361641623165,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.1917316745761468,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -3.0649475373652812,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -3.980654600288658,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -9.438509590512524,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.859999847412098,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -3.322000122070307,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.07313659667968864,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.7517248535156398,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.14141921997068607,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.7317532348632767,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.4002698426012308,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.04817355037693,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.7430673765715712,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.9761861126754146,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.9164636712365892,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.3362975559418224,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.10785675048828125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.21214185442243316,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.027865019888916986,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.11897312422754869,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.7189438142494389,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.6060846492848118,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.14876827277322946,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.4484910832199085,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.8699951171875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 9.05999755859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.10361019860000154,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.063387051468979,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.1027081108771273,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 5.142222883104452,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.149459111076089,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.2678122828176264,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.0060194790253671,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -24.716365091569315,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.6226734136778433,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.2643839647140664,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.294972032767161,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 3.4208653954596047,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.41694356215085104,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -2.390415589957528,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.1893868303366704,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -19.91910009342002,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.867001342773392,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 4.4770019531249545,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.9348004150390921,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 4.312040405273478,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.3121859741210642,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.3796951293945199,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.32760837936514076,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.8718169995311831,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.35952202127094157,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.9051132661415329,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.2863565993451509,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.6969954180049847,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.5085710797991059,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.22214181082589413,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.09922258720818711,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.0792253774995042,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.16008742251275576,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.6671262038986394,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.5677992804118059,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.9507794204135653,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -10.810012817382812,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -6.5900115966796875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -4.8385319280198065,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.3239977740802207,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.3294585575911224,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.9127427862798076,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -3.9761069934181603,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -2.1896592120108527,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -2.3592024781816434,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -21.0548921648269,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -4.112248315741962,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.4750053126746918,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.47827752051884387,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -2.6341002739246555,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -3.4097043201912203,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -3.312262519150755,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -2.175835126870341,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -16.2576271666776,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.2220001220703125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.4355010986328125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.44100006103516876,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.3160000610351688,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.005949935913093896,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.12139999389648892,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -4.1531872809058346,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -2.7528799124944774,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -4.071831125136782,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -2.0822103508453265,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -4.444138312636836,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -2.759021515460236,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.33000074114118316,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.11428724016462066,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.25154073146484546,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.029935512548194154,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -3.806074655140712,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -2.320263309482229,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.3883925092626046,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.9810311319396599,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -41.07000732421875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -40.399993896484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -13.985650341882616,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -9.492676545256817,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -9.512293535962247,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -5.30186188133769,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -10.511979458288558,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -10.790651093724646,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -7.724058750670082,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -17.991833615670373,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -13.259366729604771,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -10.29167963201173,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -10.320029614072213,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -7.023219368982538,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -9.945576785061615,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -11.913254400864547,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -7.540691399358781,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -13.194568617521075,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -2.7209991455077898,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -7.180500793457043,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.2135711669922102,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -3.155436401367183,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.2574882507324219,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.37164230346684235,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -11.411949184160385,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -9.97885709433156,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -11.731513033003726,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -10.998340734411714,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -11.985405860380103,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -11.757008590713435,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.72285897391183,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.29429190499442,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.3181270723908773,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.1808194660194369,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -10.88214122779171,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -10.70461068372427,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.9474267368079787,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 4.265025414383388,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 12.030029296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -24.3299560546875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 3.205675485094883,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 8.94170232308148,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 8.44063092334586,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 8.177486207652993,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.5699277260675775,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.586625957337162,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.8978859421912242,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -4.730742753342909,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 3.931959097372728,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 8.142699236326568,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 7.632894845235893,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 6.456128720008146,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.1363303992945166,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.4640226501972595,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.0812532935025274,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.06652224480638846,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -5.070498657226608,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -26.339996337890625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.5784118652344432,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 5.782647705078148,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.024747314453065883,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.41109771728508804,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.3616513102492025,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.09969849790203433,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.5829242932105299,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -4.487226263469036,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.9094900598552456,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -3.787235546156331,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.7371433803013403,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.7192818777901806,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.03767423948239301,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.2686950581514256,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.5470915111300734,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -3.128892503042568,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.2397034701319305,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.6301097014575667,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -3.1899986267089844,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 5.140003204345703,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -12.308951882192186,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 5.071640347105088,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 5.831474421516082,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 29.462724085337257,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -4.8030131451053855,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 6.889855486217108,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.9932648895082963,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -23.845816316851998,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -11.582668269914343,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 4.2726372603501765,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 5.023738343406116,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 27.741366597692412,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -4.236610471878443,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 5.767252179077211,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.8098975381969957,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -19.048551318702703,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.3914999008178626,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -7.030749893188471,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.6026000213623064,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -4.158500061035156,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.13370000839233853,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.5907749938964884,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -2.769564431595539,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 14.440991501373835,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -3.3848173027277397,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 9.834621325658588,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -3.3835329403552272,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 6.005629032283196,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.14571435110909547,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.04892866952078734,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.7631980999892214,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.0796909701423427,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -2.961105102855889,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 4.771190053077156,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.2914645986408888,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.8725029355055902,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -48.9599609375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 77.780029296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -10.844308223604049,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.2787739268460996,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.4680018184132901,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 17.108185660035492,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -7.178015702340613,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 5.870839412149541,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -5.546466877312973,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -11.301037175535589,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -10.118024611326204,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.4797708400911871,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.6602657403033234,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 15.386828172390643,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -6.611613029113673,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 4.748236105009639,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -5.363099526001671,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -6.50377217738629,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -8.147363281250023,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -36.7742919921875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.05385009765632276,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -3.6568591308594023,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.9819390869140534,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 14.665446166992183,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -4.237909734348033,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 11.392842812252692,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -4.9884649934272,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 8.258310564888882,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -7.113814474761405,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 8.140516792109679,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.3446995189032478,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.2346071563214025,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.400065790345872,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.4527998736225003,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -4.462193733169984,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 7.088844693674199,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.31126349042443713,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.3941165363205037,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -2.3699989318847656,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 6.069999694824219,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -11.505043192187681,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.6997695061033333,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 3.1985884809657676,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 20.68724172113653,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -6.234649663628579,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 8.196809968060613,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -2.300211061195012,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -5.553634822523035,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -10.778759579909835,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.9007664193484208,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.390852402855801,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 18.96588423349168,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -5.668246990401638,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 7.074206660920712,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -2.116843709883709,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.7563698243737371,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.5139999389648438,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -2.67549991607666,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.06779998779296648,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.6619998931884794,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -3.507010111093456,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 15.720012181228991,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -4.104010542336622,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 11.756444271960786,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.11714281354631684,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.1878569466727118,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.4544174724747263,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.3108415242437532,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -3.7252420177218504,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 9.541024515456389,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.21022206404025778,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.5998341118019713,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.9799957275390625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 50.33000183105469,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -15.257828884618775,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 9.032435410103012,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 11.219080329606658,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 34.654404858468794,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.7567416388200021,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 20.18372420492728,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.5219645188906288,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.786923342173484,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -14.531545272340932,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 8.2334323233481,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 10.41134425149669,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 32.93304737082394,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.19033896559306207,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 19.061120897787376,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.3385971675793247,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 5.584188340322781,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.00999984741210369,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -7.078498840332031,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.3003207397460983,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -6.3003030395507835,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.3665952301025186,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.26724678039551,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.3229006898759508,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 24.88918143376081,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.3483645543470035,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 22.722950831336576,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.9809651330000886,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 18.290719511173407,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.6878564017159601,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.3632114955357153,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.21286875719844556,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.26586734043970495,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.0144045582317212,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 17.132569285726678,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.8748981617779432,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.17704883225051482,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -2.2599945068359375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 6.4000091552734375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.9801160998570655,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.105182160199559,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.2051650799258082,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 7.130633550237741,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -2.1586395777590695,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.7678388877512834,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.6722252391432093,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -7.954507524322629,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.2538324875792206,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.3061790734446466,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.397429001815842,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 5.409276062592894,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.5922369045321294,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.6452355806113808,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.4888578878319061,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -3.1572425261733317,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.45349960327149574,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -2.003999328613304,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.10628112792966249,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.009677429199228982,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.21393226623536066,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.0560721588134925,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.9431319978226549,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 4.317806036198347,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.2479934322158326,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 3.3791752031999245,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.479956391956506,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 3.107682048438921,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.09142848423549044,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.19785635811941926,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.0744227241987816,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.029739501764015408,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.1188091617999607,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 3.1683213639967516,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.03827833858163909,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.5831636899216855,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.26000213623046875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.1399993896484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.027990996897497844,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.2454585392336792,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.2616787567669263,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.16970721756328633,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.7154838857899026,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.646024892005805,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.940630541411693,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 4.71078203519777,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.7542746091753427,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.4464554524787667,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.45394267865696003,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.5516502700815615,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.1490812125629635,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.5234215848659023,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 3.1239978927229934,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 9.508047033347065,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.30049991607666016,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.7229997634887724,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.11011367797850369,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.6675670623779268,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.11311679840087407,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.5857625198364218,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.0741511524118943,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.9738517163988547,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.2215306743043044,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.6728179753663133,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.21767047441028353,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.7772085272659268,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.01857103620256706,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.022143500191824872,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.0192886633843683,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.06760348693514606,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.3733517210069315,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.353613665696606,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.10768508766108764,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.5263522619397474,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.80999755859375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.2899971008300781,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.995686940734064,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.3545649108182891,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.351310296326357,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.984925499488388,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.3971805508355306,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.621765773229745,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.2001411738817302,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.7809451363730688,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.721970553011909,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.4444381759366234,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.45642578178360926,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -3.706282987133236,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.9635832240624707,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.4991624660898433,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.3835085251930335,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 3.016319861776229,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.17399997711181214,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.5485002517700153,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.006745758056638351,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.14859313964844034,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.016826515197756464,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.037270870208743645,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.1461361346985166,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.5051851592089207,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.4619226311609612,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.7880199216161898,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.4839507057985868,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.46903394250397135,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.034999847412109375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.01857103620256695,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.04408937064299501,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.02630259364611698,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.3880878974157906,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.49696627067217225,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.270053225593309,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.10518634011187722,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.6399993896484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 3.4000091552734375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.6338994189179381,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.9120962260718244,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.9322804047855469,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.730161405755971,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.02076362771570306,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.1274005268024587,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.9067401268173185,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -3.0913683647243113,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.360183031195783,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.113093139316912,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.1245443266755806,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.008803918111123,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.545639045511237,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.0047972196625565,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.0901074781286226,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.7058966334249863,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.07450027465819176,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.2919990539550952,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.2266458129882949,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.6708578491210915,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.03709106445313637,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.1813397979736351,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.9305695442880291,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.1930056232169037,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.0913231356644348,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.937622156638686,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.9294309871725193,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.8687473171328906,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.09571511404854904,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.023570469447544706,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.04203459358122008,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.04508725128949442,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.8816723646134736,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.827862943461211,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.0802647430587542,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.4103027203074401,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 4.3199920654296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.739990234375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.1023570161914806,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.0848565592548098,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.0754022000645014,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.808242491117861,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 4.024634529864147,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 4.005373615261388,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.2450497028302365,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 3.0626135710545945,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.8286406284693255,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.28585347249989734,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.2676661219545351,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -2.529599978762709,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 4.591037203091087,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.8827703081214864,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.4284170541415389,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 7.859878569203892,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.8919998168945256,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.709500122070324,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.18059570312499318,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.1304766845703114,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.14609809875489077,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.6097781372070301,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.9443877250581387,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.06593353972670357,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.4058987618670757,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.8959868747509203,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.636508211619205,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.292146475375013,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.1150011335100447,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.03571537562779037,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.022828451912077385,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.0061793357716668496,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.8714847239156609,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.0,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.751712188385927,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.5806734678568806,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.3400039672851562,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.80999755859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.8987868394974239,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.763089098972559,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.7013740919288534,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -5.8299723831336525,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.030254615126358,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.3746927294308051,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.6286982740907785,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.33160628097108624,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.6250704517752688,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -2.5620921857274714,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -2.5091101700388196,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -7.5513298707785,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.596657288353298,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.4972960365707078,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.8120656254020817,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 5.128871279120384,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.3924999237060547,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.5635002136230582,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.04410873413085881,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.24604568481444744,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.04301574707031364,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.2513384628295796,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.0983583266610975,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -4.072774237395205,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.5357794056392038,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -2.459837828300304,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.5505767632945755,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -2.4918842623525617,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.05928584507533485,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.08499962942940842,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.04400892325341976,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.12607812443873412,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.4890587833035762,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -2.0113319275035346,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.12455894695041758,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.7050676308288624,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.8699951171875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.1899948120117188,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.8582896900079628,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.2044494569106057,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.2078006737742175,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.3761208378733505,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.8287682289231046,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.5403835098896987,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.44666274870345246,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -5.114206345134398,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.5845733022858077,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.4054463701556932,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.40006459566425123,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -2.0974783255181983,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.3951709021500447,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.417780202749796,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.6300301000147557,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.3169413469851001,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.36949996948241903,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.3990001678466797,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.04258773803709914,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.2543406677246054,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.0362126922607473,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.19404071807862522,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.4348609514399637,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.21948116667420692,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.8071829836850952,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.2795674620941222,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.7867293775628115,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.2009680010175106,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.025714329310825734,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.17071424211774544,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.01144563940497556,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.13355122785467555,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.7274413720797623,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.9950072612086247,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.0011956439797348173,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.24883418499856902,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.9300003051757812,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -6.209999084472656,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.446448497191255,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.44883065549342627,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.43094762914481777,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.3164385595011767,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.884735158604089,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -2.1770344820457703,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.7718542444182805,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -6.826834301870921,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.7201648849134101,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.2478337422483388,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.2386837072547836,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -3.0377960471460246,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.31833248537714987,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -3.299637789185672,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.5884868931069764,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -2.0295693037216243,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.436500167846674,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.9615001678466797,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.19488647460937614,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.7799322509765574,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.07312034606933082,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.3216402053832894,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.393896543084761,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -3.956622891300232,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.5787823503603082,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -4.928070793533402,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.657055484391579,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -5.251055375387348,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.09107153756277908,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.20392826625279037,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.12282003067467562,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.2964919083860469,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.6819174772773735,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -5.411763908037171,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.3794575724072764,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.6865929031098912,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.6499977111816406,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.2700004577636719,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.3698988390397746,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.5416597644584575,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.5368585228463951,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -2.2993531931083444,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.986481963102138,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.19792283396977695,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.4998589708983054,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 3.3760384794151443,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 3.0961824513176195,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.34066285121337,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.3445946009563614,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -4.020710680753192,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.552884636329078,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.3205261411096796,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.6832263222096087,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 8.173303477564442,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.17299995422363423,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.8000001907348633,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.011173782348635086,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.107400283813476,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.005830478668208627,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.030602550506586113,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.133096545312462,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.3577951810102906,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.5888805648849091,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.9136509239574098,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.4711745471102433,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.5480314888248627,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.019285746983119356,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.07571383884974892,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.023302072784499472,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.18570590028477896,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.4760529588671134,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 3.426270828966394,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.21469687521587144,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.03786919044312431,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.9300003051757812,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.5400009155273438,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.937891039044438,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.11378030074063,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.1035645520855342,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.007790402767593463,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.868384440967442,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 3.7617104948696634,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.012405042379583,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.7734040672687033,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 3.664174651322283,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.31477721398571745,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.2958284739755679,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.7135670848772544,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 3.434787114194382,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.639107187729761,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.195772393690887,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 7.570669065418,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.11900005340576314,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.3579999923706083,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.031089324951167896,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.19926513671875057,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.015464248657231394,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.07568374633789432,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.9358836697972226,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.4134862791027816,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.258797024597836,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.7356875308837783,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.1394736204669362,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.086630853986792,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.012857164655412978,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.025928497314453125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.0028114964408370025,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.041804494187941854,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.0675228185761725,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.5359198932581535,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.2697059573359156,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.5924996587424981,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.6699981689453125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.8400001525878906,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.1374329453178955,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.5709718842515477,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.5728497398426624,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.6098899751487918,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.7313142153412278,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 4.174129849472185,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.06053515770789719,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.11283998249067562,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.8637165575957404,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.22803120250336484,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.23488633826730387,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -2.3312474627936397,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.297716888568168,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 3.051526542332283,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.2439025090192004,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 4.684425015658622,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.19949989318848083,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.6625000000000014,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.005011749267580967,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.02665199279785213,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.022089424133298508,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.11104623794555835,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.9193660655924418,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.3028602593333485,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.306666446663507,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.703978667588335,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.276862767657816,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.4329653493360128,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.023571014404296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.02857208251953125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.028920401527205097,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.07606929927552852,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.2541112637093899,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.5723231819221084,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.456715468410297,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.4855440722518397,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -6.0,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 38.32000732421875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -2.793574016884215,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 4.933713554573316,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 5.351526167690346,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 13.672725345228098,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -2.3004004099889457,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 3.763597921011785,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.012975709046347816,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -5.203492617029992,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -2.06729040460637,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 4.134710467818403,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 4.54379008958038,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 11.95136785758325,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.7339977367620047,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.6409946138718823,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.1703916422649554,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.4062276188806946,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -2.8070007324218977,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -14.207003784179733,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.014999999999986358,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -2.9112011718750637,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.8506999206542787,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 4.103649749755846,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.5638225316849876,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 8.853116653090277,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.0489453790607173,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 7.143747611321748,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.3361419521660913,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 6.581653212801175,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.14285714285714235,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.36714390345982295,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.009536274479287954,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.17024491641175477,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.9465214969105027,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 6.0451184490234695,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.06645411166838677,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.280407612914277,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -3.94000244140625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.75,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -3.63699257637794,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -3.428794861800011,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -3.529400673586369,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.11307174633398143,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -5.3397804449321296,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.7054664532584196,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -3.141803947722366,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -11.126664031984678,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -2.910708964100095,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -4.227797948554923,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -4.3371367516963355,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.6082857413108664,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -4.7733777717051895,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -2.828069760398322,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -2.9584365964110635,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -6.329399033835381,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.013000106811517753,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.113499450683591,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.10320007324219205,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.7304000854492188,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.023196868896476985,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.1467914581298828,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -3.5870883910128604,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.7057546581058403,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -3.7852220692655036,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.4003768759244695,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -4.223762126194908,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.9795571605038411,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.20785740443638412,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.21214239937918533,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.2850509359296636,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.21458707387913112,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -3.496940184110364,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.665660790084865,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.3559666640539121,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.28102195697778276,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.8499908447265625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.6500091552734375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.604201953584238,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.6560873718013616,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.6677514438197418,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.3301150849556178,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -3.4742811431424556,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.2927809987101302,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 4.271037998124672,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 6.374765186517539,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.12208165869360688,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.14291571495355093,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.13998463429022445,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.39124240268923,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -2.9078784699155147,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.17017769157022755,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 4.454405349435973,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 11.172030184666834,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.7610000610351619,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 5.127499389648449,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.278600158691404,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.9078527832031398,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.35715209960937955,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.8874164199829124,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.8311457584603499,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.3429121358822904,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.5980920645524135,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.34763850329302404,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.7528604428314729,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.25363698129714507,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.05857195172991059,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.020002092633928825,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.018768166932972008,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.023042605304821162,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.4149130343620633,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.8549797558184413,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.2988481643923858,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.1502699449349805,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.20001220703125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 30.899993896484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.3495850807531675,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 3.9192793670653203,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 4.252989954874797,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 8.08741216242861,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.0950248055083165,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 11.38992837860091,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.6092134018736104,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 3.4691849094148353,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.37669853152467736,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 3.120276280310408,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 3.4452538767648306,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 6.366054674783761,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.5286221322813764,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 10.26732507146101,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.7925807531849136,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 8.266449907564134,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.3389999389648324,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 5.1204986572265625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.21580017089843295,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.4410003662109148,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.43684997558591476,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.2663497924804688,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.6674908787973388,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 6.628762369921748,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.24426576317537751,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 8.037236763243882,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.41550243183967606,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 7.23456061745783,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.08857291085379515,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.5157143729073663,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.03002382155774974,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.09717003003995028,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.27486651792102457,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 7.077739439934128,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.0882371815297072,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.8528293174650061,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 6.55999755859375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 9.82000732421875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.4207131612778987,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 3.79436223324473,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 3.8548554755821307,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 5.981630228336243,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.7387389581230437,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 6.9007500095070835,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.067180755271826,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.6052740686481215,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 3.1469967735557436,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.9953591464898177,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 3.0471193974721644,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 4.260272740691395,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 3.3051416313499837,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 5.778146702367182,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.2505481065831283,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 3.191990929501177,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.31300048828126137,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.4969985961913892,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.6312994384765602,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -4.266396484375008,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.11322380065919901,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.6017039489746026,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 3.0238647449792433,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 4.99288566323437,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 3.3309931569452167,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 6.41105413162486,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.912882419761753,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 4.527729171506013,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.36071341378348265,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.6442838396344865,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.10883286100249046,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.2165287701154528,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.5936347850491366,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 3.882549095184551,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.54038956537115,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.30891459085680606,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.1900005340576172,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.3600006103515625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.7465895202333095,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 3.6283418195362405,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 3.7716141896313005,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 7.537869825908016,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.38290467722453814,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 6.516566098488219,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.3486193848289316,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -5.252925034608635,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.4728731325111544,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.829338732781328,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.963878111521334,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 5.816512338263169,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.9493073504514782,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 5.393962791348317,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.531986736140235,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.4556600364593377,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.048999977111815696,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.3957499504089377,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.05299999237060504,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.38779998779296676,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.014749994277948986,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.06864999771117652,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.7655850260054997,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 5.561772446695402,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.7580130479948877,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 5.394862938206669,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.6274601418894576,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 4.375780434059439,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.031071390424455947,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.022714342389787978,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.08572846008433421,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.03608388578302568,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.5450388144892742,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 3.9013212465283544,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.21602169428236218,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.3322124405799014,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.75,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.4499969482421875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.6876406275203926,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.494616269113469,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.4884239003900124,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -3.192168443849419,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.3150764733502509,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 2.0879444668975067,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.5775854817489998,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.84860421528189,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 2.4139242397982374,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -2.2936193558683815,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -2.2961599784999787,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -4.9135259314942665,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.881479146577191,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.9653411597576045,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.760952833060303,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 3.9486607828674067,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.14550018310546875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.5709999084472628,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.03430511474608977,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.4000019836425679,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.038780956268311684,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.16629995346069393,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.8517975414478629,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.19955600001451135,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.0917596660025897,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.1842866176673628,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 1.0100405154162662,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.39584246784485355,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.04499980381556923,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.008572169712611544,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.04403041370566241,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.022817011875421178,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.9678835247328044,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.5807261765115372,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.1734377218071116,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.5511274297184351,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -4.8899993896484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 3.0999908447265625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_1d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -3.3336451950708,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.4516046255538595,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_5d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -1.5221882810150467,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 3.2669363709869503,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_20d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -4.797965117444747,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.8272422039800063,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_60d_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -3.222671096823815,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -9.508612922881278,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_1d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -2.6073615827929553,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -2.250607712308772,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_5d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -2.329924359125013,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.5455788833421025,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_20d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -4.231562444217807,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.7046388968401041,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_60d_pp",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -3.0393037455125125,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -4.711347924731982,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma20",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.02299957275391762,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.3784996032714787,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma50",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.5876000976562352,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma200",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.19290000915526662,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.0022500610351415,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma20_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -2.923218727828092,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.0359155059357472,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma50_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -3.046750597543557,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.5243319143237066,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma200_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -3.7656328400324846,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.3811811631009512,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_sma",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.21857125418526735,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.472143990652901,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.21209825004341942,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.23065997344712308,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.drawdown_from_63d_high_pct",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -2.7960428879376336,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.7725375124622795,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.volume_vs_previous20_ratio",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.6706998191539808,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 1.1367733844865775,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS2.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.03000000000000025,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.13999999999999968,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLH0A0HYM2.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.040000000000000036,
        "unit": "percentage_points"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.1299999999999999,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLC0A0CM.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.020000000000000018,
        "unit": "percentage_points"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.020000000000000018,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS10.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.05999999999999961,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.08000000000000007,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DFII10.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.029999999999999805,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.08999999999999986,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.T10YIE.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.029999999999999805,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.03000000000000025,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.STLFSI4.value",
    "available_prior_observations": 2,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.04910000000000003,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.CBOE_VIX.value",
    "available_prior_observations": 9,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.28999999999999915,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -1.8300000000000018,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.GPRD.value",
    "available_prior_observations": 2,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -83.41177368164062,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.GPRD_ACT.value",
    "available_prior_observations": 2,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -80.4246826171875,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.GPRD_THREAT.value",
    "available_prior_observations": 2,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -122.77737426757812,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.GPRD_MA7.value",
    "available_prior_observations": 2,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.4905548095703125,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.GPRD_MA30.value",
    "available_prior_observations": 2,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.572418212890625,
        "unit": "index"
      }
    ],
    "status": "comparable"
  }
]
```

## 判断依据 · 恐慌还是过热？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 恐慌还是过热？ |
| 事实指标引用 | ["premarket.VIX.value", "macro.BAMLH0A0HYM2.value", "macro.DGS10.value", "prices.^MOVE.value"] |
| 推断与解释 | VIX盘前上升且科技加速下修，但等权金融医疗仍相对强；不是已证实的全面极端恐慌。 |
| 反证与缺口 | 信用至28日、VIX3M至29日，不能证明30日风险安全。 |
| 确认条件 | 信用不扩张、油价与利率稳定且次日波动率不突升 |
| 失效条件 | 股票再跌同时VIX期限倒挂/信用走阔、油价冲击加剧 |
| 观察期限 | 30日及未来1–3日 |
| 条件式指导 | 等待多市场共振；不因单个VIX低值扩大方向风险 |
| 主观置信等级 | medium |
| 判断变化原因 | 新增30日盘前价格、VIX及XOM/ABBV业绩和AMZN10-Q；29日收盘窗口未变，信用数据仍滞后。 |

## 判断依据 · 反弹是否可靠？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 反弹是否可靠？ |
| 事实指标引用 | ["prices.QQQ.distance_sma20_pct", "prices.SMH.distance_sma20_pct", "prices.SPY.distance_sma20_pct", "prices.RSP.return_1d_pct", "prices.RSP.return_5d_pct"] |
| 推断与解释 | 盘前失守早报警戒，反弹仍不可靠；今晚常规区间与VWAP未形成。 |
| 反证与缺口 | 金融医疗和等权收盘走强，盘后薄量可逆。 |
| 确认条件 | 今晚首30–60分钟低点抬高、站回实际常规VWAP且回踩不失守；QQQ先收回704.40，再争取711.62/715.34，SMH先收回546.67，再看555.50/561.67。RSP与金融医疗同步承接，收盘保留修复才升级。首个突破只是观察信号，价格关口来自已发生交易，不是必然支撑。 |
| 失效条件 | 盘前已经低于QQQ704.40、SMH546.67；若常规开盘后反抽仍不能收回，或突破后跌破开盘区间低点且反抽失败，修复判为失败。若RSP/金融医疗亦失守29日低点，风险由科技向全市场扩散。 |
| 观察期限 | 30日及未来1–3日 |
| 条件式指导 | 等下一常规时段的回踩和收盘共同确认；单次越线不追。 |
| 主观置信等级 | medium |
| 判断变化原因 | 新增30日盘前价格、VIX及XOM/ABBV业绩和AMZN10-Q；29日收盘窗口未变，信用数据仍滞后。 |

## 判断依据 · 优先观察哪些板块？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 优先观察哪些板块？ |
| 事实指标引用 | ["prices.XLF.return_1d_pct", "prices.XLV.return_1d_pct", "prices.SMH.relative_spy_5d_pp", "prices.XLE.return_1d_pct"] |
| 推断与解释 | 金融医疗优先检验承接，能源有新现金流催化；工业转弱需分化看待。 |
| 反证与缺口 | 19ETF价格轮动非资金流，现金流披露与市场预期可能分化 |
| 确认条件 | 行业相对QQQ强，回踩后高低点抬升，金融等权扩散 |
| 失效条件 | 好财报仍持续弱于指数、资金现金回报恶化 |
| 观察期限 | 30日及未来1–3日 |
| 条件式指导 | 分行业看，不把相对收益叫净流入。 |
| 主观置信等级 | medium |
| 判断变化原因 | 新增30日盘前价格、VIX及XOM/ABBV业绩和AMZN10-Q；29日收盘窗口未变，信用数据仍滞后。 |

## 判断依据 · AI需求与估值如何区分？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | AI需求与估值如何区分？ |
| 事实指标引用 | ["prices.NVDA.return_1d_pct", "prices.CRWV.distance_sma20_pct", "prices.MU.return_1d_pct"] |
| 推断与解释 | AWS增长与负TTM公司FCF并存，需求增长不等于资本回报改善。 |
| 反证与缺口 | H10029日仍2.90、存储公司指引强；不支持普遍需求崩塌。 |
| 确认条件 | 现金回收改善、融资压力不增且价格重新获得承接 |
| 失效条件 | 投入加速而现金回收放缓、稀释/信用压力同步上升 |
| 观察期限 | 30日及未来1–3日 |
| 条件式指导 | 新披露先更新财务桥，四家公司暂不输出旧DCF。 |
| 主观置信等级 | medium |
| 判断变化原因 | 新增30日盘前价格、VIX及XOM/ABBV业绩和AMZN10-Q；29日收盘窗口未变，信用数据仍滞后。 |

## AI云：收入兑现不等于现金回报 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | Amazon Q3销售2019亿美元、AWS459.8亿美元同比39.3%；公司口径TTM经营现金1683亿减净现金资本支出2106.57亿，FCF为−423.57亿。这是TTM，不是单季，也不是FCFF。Q4销售指引2400–2470亿、营业利润285–335亿。 |
| 事实：市场反应 | 29日AMZN收243.79、GOOGL283.82；现在盘前 AMZN 227.87（较29日常规收盘-6.53%）；GOOGL 281.00（较29日常规收盘-0.99%）；MSFT 525.74（较29日常规收盘-0.83%）。 |
| 推断：解释 | 推断：AI云增长和投入回报的估值冲突继续影响价格。30日新10-Q核验了AMZN披露，但不足以仅凭强收入宣布价格见底；29日盘后业绩不能倒推解释29日常规跌幅。 |
| 受益篮子 | ["现金回收与价格承接更好的云公司观察篮子"] |
| 受损篮子 | ["持续投入超现金回收且估值承压者"] |
| 反证 | AWS增长反驳普遍需求崩塌；H10029日2.90美元/GPU小时，与28日相同。 |
| 下一催化剂 | 30日开盘后的缺口承接、融资与资本支出明细 |
| 证据 | ["https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm", "https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Third-Quarter-Results/default.aspx", "https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm", "https://www.silicondata.com/products/silicon-index/h100"] |

## 存储与芯片：强业绩仍需承接 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | Sandisk FY27Q1收入110.31亿美元、同比378%，non-GAAP EPS49.51；Q2收入指引122–126亿、EPS55–57（拆分前）。Intel Q4收入指引150–160亿，官方同时提到PC疲弱与数据中心供给约束。 |
| 事实：市场反应 | 30日盘前 SNDK 1211.69（较29日常规收盘-8.90%）；MU 882.00（较29日常规收盘-5.59%）；DRAM 48.51（较29日常规收盘-6.26%）；INTC 69.08（较29日常规收盘-24.97%）；SMH 533.42（较29日常规收盘-5.03%）。 |
| 推断：解释 | 推断：高增长业绩没有阻止存储及芯片再定价；跨标的同步下跌增加共同估值/风险预算因素的解释力，但不足以证实需求突然消失，也不能归因于某一竞争者。 |
| 受益篮子 | ["财报后守住开盘区间、强于SMH的存储/设备观察篮子"] |
| 受损篮子 | ["高预期且反抽反复失守者"] |
| 反证 | Sandisk收入及指引强、AWS增速高；盘前价格可能反转。VRT昨日上涨但现在盘前VRT 230.63（较29日常规收盘-6.22%），强弱关系必须刷新。 |
| 下一催化剂 | 30日价格承接；AMD11月3日17:00EST电话会；SNDK11月20日按8拆1调整交易 |
| 证据 | ["https://investor.sandisk.com/news-releases/news-release-details/sandisk-reports-fiscal-first-quarter-2027-financial-results", "https://www.intc.com/filings-reports/all-sec-filings/content/0000050863-26-000188/q326earningsrelease.htm", "https://ir.amd.com/news-events/press-releases/detail/1300/amd-to-report-fiscal-third-quarter-2026-financial-results"] |

## 金融医疗与等权：相对承接继续 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 29日金融医疗与等权收涨；30日ABBV官方新财报收入174.04亿美元、调整EPS3.82，全年调整EPS指引升至13.95–13.99。 |
| 事实：市场反应 | XLF 57.36（较29日常规收盘+0.74%）；XLV 186.90（较29日常规收盘+1.55%）；RSP 220.34（较29日常规收盘+0.14%）；XLI 169.41（较29日常规收盘-0.42%）。 |
| 推断：解释 | 推断：非科技存在独立业绩支撑，但工业盘前转弱；优先检验金融和医疗承接，不能把XLV大型药企强势等同所有生物科技走强。 |
| 受益篮子 | ["金融", "医疗", "现金回报稳健的工业观察篮子"] |
| 受损篮子 | ["相对弱势科技权重"] |
| 反证 | XLI仍略低于50日线约170.74；医疗不能由单一大型药企延伸为所有生物科技普涨。 |
| 下一催化剂 | 30日能否守29日收盘/低点并继续强于SPY |
| 证据 | ["https://www.sec.gov/Archives/edgar/data/1551152/000155115226000033/abbv-20260930xexhibit991.htm", "https://www.ici.org/research/stats/etf_flows", "https://query1.finance.yahoo.com/v8/finance/chart/XLV"] |

## 增长与通胀：并非简单衰退交易 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | BEA29日08:30EDT：Q3实际GDP年化环比3.4%；9月PCE同比3.6%、核心3.1%，环比0.5%/0.3%，实际消费环比接近零。季度年化价格指标与月度同比不得混用。 |
| 事实：市场反应 | 29日GLD跌1.32%、TLT涨0.62%；当前盘前 GLD 363.51（较29日常规收盘-1.37%）；TLT 81.95（较29日常规收盘+0.56%）。 |
| 推断：解释 | 推断：风险资产弱、国债强而黄金弱，并非统一避险交易。增长尚稳、通胀偏高的已知组合限制简单降息救市想象；不把新盘前走势全归单一数据。 |
| 受益篮子 | ["能传导成本且现金稳健者"] |
| 受损篮子 | ["折现率敏感且现金回收慢者"] |
| 反证 | 国债上涨说明单日价格并不只交易加息；收益率/信用最新仅28日，不能替代29日数据后的反应。 |
| 下一催化剂 | 下一就业/CPI与实际利率；油价和供应消息 |
| 证据 | ["https://www.bea.gov/news/2026/gdp-advance-estimate-3rd-quarter-2026", "https://www.bea.gov/news/2026/personal-income-and-outlays-september-2026"] |

## 能源现金回报与地缘溢价 · 新增

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | XOM30日Q3净利154亿美元、调整EPS4.23、经营现金257亿、公司FCF191亿；CVX净利99亿、调整EPS5.28、经营现金160亿、公司FCF120亿。CVX调整FCF142亿含TCO偿还贷款及资产出售影响，不应直接年化。中东军情与供应损失仍待核验。 |
| 事实：市场反应 | XOM 186.64（较29日常规收盘+1.83%）；CVX 235.00（较29日常规收盘+1.53%）；XLE 69.75（较29日常规收盘+1.51%）。WTI约104.14、Brent113.54为本次分钟报价，未对齐具体交割月，不与早报直接算涨幅。 |
| 推断：解释 | 推断：能源的现金回报和供应风险溢价与AI投入回收问题形成对比；油价上涨利于部分上游，却也会抬高通胀和全市场折现压力。 |
| 受益篮子 | ["实际供应受益且价格有承接的油气观察篮子"] |
| 受损篮子 | ["燃料成本敏感企业、融资依赖链条"] |
| 反证 | 军情细节未独立核实，油价可能反向；财报后高开回落可否定追价。 |
| 下一催化剂 | XOM09:30EDT、CVX11:00EDT电话会与实际供应报告 |
| 证据 | ["https://investor.exxonmobil.com/company-information/press-releases/detail/1213/exxonmobil-announces-third-quarter-2026-results", "https://www.sec.gov/Archives/edgar/data/93410/000009341026000196/cvx-20261030.htm", "https://www.sec.gov/Archives/edgar/data/93410/000009341026000196/a09302026ex9918-k.htm"] |

## tc 报价（供应商时戳不等于成交时戳）

| 标的 | 价格 USD | 变化% | 观测时间 | 供应商时间 | 抓取时间 | 质量 |
| --- | --- | --- | --- | --- | --- | --- |
| AMD | 520.75 | -8.06 | 2026-10-30T12:01:50+00:00 | 2026-10-30T12:01:50+00:00 | 2026-10-30T12:02:05.989582+00:00 | ok |
| AMZN | 227.87 | -6.53 | 2026-10-30T12:01:53+00:00 | 2026-10-30T12:01:53+00:00 | 2026-10-30T12:02:05.989582+00:00 | ok |
| AVGO | 331.60 | -3.88 | 2026-10-30T12:01:42+00:00 | 2026-10-30T12:01:42+00:00 | 2026-10-30T12:02:05.989582+00:00 | ok |
| CAT | 634.00 | -2.07 | 2026-10-30T12:00:40+00:00 | 2026-10-30T12:00:40+00:00 | 2026-10-30T12:02:05.989582+00:00 | ok |
| CEG | 256.90 | -2.90 | 2026-10-30T12:01:50+00:00 | 2026-10-30T12:01:50+00:00 | 2026-10-30T12:02:05.989582+00:00 | ok |
| CVX | 235.00 | 1.53 | 2026-10-30T12:01:08+00:00 | 2026-10-30T12:01:08+00:00 | 2026-10-30T12:02:05.989582+00:00 | ok |
| DRAM | 48.51 | -6.26 | 2026-10-30T12:01:38+00:00 | 2026-10-30T12:01:38+00:00 | 2026-10-30T12:02:05.989582+00:00 | ok |
| GEV | 854.00 | -3.81 | 2026-10-30T12:01:33+00:00 | 2026-10-30T12:01:33+00:00 | 2026-10-30T12:02:05.989582+00:00 | ok |
| GLD | 363.51 | -1.37 | 2026-10-30T12:01:15+00:00 | 2026-10-30T12:01:15+00:00 | 2026-10-30T12:02:05.989582+00:00 | ok |
| GLW | 119.76 | -7.08 | 2026-10-30T12:00:53+00:00 | 2026-10-30T12:00:53+00:00 | 2026-10-30T12:02:05.989582+00:00 | ok |
| GOOGL | 281.00 | -0.99 | 2026-10-30T12:01:50+00:00 | 2026-10-30T12:01:50+00:00 | 2026-10-30T12:02:05.989582+00:00 | ok |
| IGV | 106.81 | -1.07 | 2026-10-30T11:45:34+00:00 | 2026-10-30T11:45:34+00:00 | 2026-10-30T12:02:05.989582+00:00 | stale |
| ILMN | 253.00 | -12.78 | 2026-10-30T11:21:00+00:00 | 2026-10-30T11:21:00+00:00 | 2026-10-30T12:02:05.989582+00:00 | stale |
| INTC | 69.08 | -24.97 | 2026-10-30T12:02:01+00:00 | 2026-10-30T12:02:01+00:00 | 2026-10-30T12:02:05.989582+00:00 | ok |
| IWM | 282.66 | -0.48 | 2026-10-30T12:01:25+00:00 | 2026-10-30T12:01:25+00:00 | 2026-10-30T12:02:05.989582+00:00 | ok |
| LLY | 1,410.01 | 2.64 | 2026-10-30T12:00:30+00:00 | 2026-10-30T12:00:30+00:00 | 2026-10-30T12:02:05.989582+00:00 | ok |
| META | 612.05 | -2.00 | 2026-10-30T12:01:41+00:00 | 2026-10-30T12:01:41+00:00 | 2026-10-30T12:02:05.989582+00:00 | ok |
| MSFT | 525.74 | -0.83 | 2026-10-30T12:01:45+00:00 | 2026-10-30T12:01:45+00:00 | 2026-10-30T12:02:05.989582+00:00 | ok |
| MU | 882.00 | -5.59 | 2026-10-30T12:02:01+00:00 | 2026-10-30T12:02:01+00:00 | 2026-10-30T12:02:05.989582+00:00 | ok |
| NOW | 109.11 | -0.51 | 2026-10-30T12:00:35+00:00 | 2026-10-30T12:00:35+00:00 | 2026-10-30T12:02:05.989582+00:00 | ok |
| NVDA | 207.11 | -3.07 | 2026-10-30T12:01:57+00:00 | 2026-10-30T12:01:57+00:00 | 2026-10-30T12:02:05.989582+00:00 | ok |
| NXPI | 260.79 | -1.96 | 2026-10-30T11:14:01+00:00 | 2026-10-30T11:14:01+00:00 | 2026-10-30T12:02:05.989582+00:00 | stale |
| ORCL | 134.30 | -3.77 | 2026-10-30T12:01:42+00:00 | 2026-10-30T12:01:42+00:00 | 2026-10-30T12:02:05.989582+00:00 | ok |
| PLTR | 193.41 | -1.53 | 2026-10-30T12:02:01+00:00 | 2026-10-30T12:02:01+00:00 | 2026-10-30T12:02:05.989582+00:00 | ok |
| QQQ | 697.75 | -2.46 | 2026-10-30T12:01:47+00:00 | 2026-10-30T12:01:47+00:00 | 2026-10-30T12:02:05.989582+00:00 | ok |
| RSP | 220.34 | 0.14 | 2026-10-30T11:55:16+00:00 | 2026-10-30T11:55:16+00:00 | 2026-10-30T12:02:05.989582+00:00 | ok |
| SMH | 533.42 | -5.03 | 2026-10-30T11:59:20+00:00 | 2026-10-30T11:59:20+00:00 | 2026-10-30T12:02:05.989582+00:00 | ok |
| SNDK | 1,211.69 | -8.90 | 2026-10-30T12:01:57+00:00 | 2026-10-30T12:01:57+00:00 | 2026-10-30T12:02:05.989582+00:00 | ok |
| SPY | 761.63 | -1.00 | 2026-10-30T12:01:53+00:00 | 2026-10-30T12:01:53+00:00 | 2026-10-30T12:02:05.989582+00:00 | ok |
| STX | 649.48 | -7.28 | 2026-10-30T12:01:22+00:00 | 2026-10-30T12:01:22+00:00 | 2026-10-30T12:02:05.989582+00:00 | ok |
| TLT | 81.95 | 0.56 | 2026-10-30T12:01:43+00:00 | 2026-10-30T12:01:43+00:00 | 2026-10-30T12:02:05.989582+00:00 | ok |
| VRT | 230.63 | -6.22 | 2026-10-30T12:01:58+00:00 | 2026-10-30T12:01:58+00:00 | 2026-10-30T12:02:05.989582+00:00 | ok |
| XLE | 69.75 | 1.51 | 2026-10-30T12:01:04+00:00 | 2026-10-30T12:01:04+00:00 | 2026-10-30T12:02:05.989582+00:00 | ok |
| XLF | 57.36 | 0.74 | 2026-10-30T11:46:47+00:00 | 2026-10-30T11:46:47+00:00 | 2026-10-30T12:02:05.989582+00:00 | stale |
| XLI | 169.41 | -0.42 | 2026-10-30T11:40:37+00:00 | 2026-10-30T11:40:37+00:00 | 2026-10-30T12:02:05.989582+00:00 | stale |
| XLV | 186.90 | 1.55 | 2026-10-30T12:00:42+00:00 | 2026-10-30T12:00:42+00:00 | 2026-10-30T12:02:05.989582+00:00 | ok |
| XOM | 186.64 | 1.83 | 2026-10-30T12:01:56+00:00 | 2026-10-30T12:01:56+00:00 | 2026-10-30T12:02:05.989582+00:00 | ok |

## 核心行情与风险代理

| 标的 | 价格/指数 | 单位 | 观测日 | 1日% | 5日% | 20日% | 质量 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 769.36 | USD_per_share | 2026-10-29 | -0.38 | 0.71 | 0.70 | ok |
| QQQ | 715.34 | USD_per_share | 2026-10-29 | -1.42 | 1.54 | -3.60 | ok |
| IWM | 284.01 | USD_per_share | 2026-10-29 | 0.97 | 2.65 | 1.79 | ok |
| RSP | 220.04 | USD_per_share | 2026-10-29 | 1.20 | 0.83 | 5.28 | ok |
| GLD | 368.57 | USD_per_share | 2026-10-29 | -1.32 | -0.12 | -3.71 | ok |
| GC=F | 4,031.40 | USD_per_troy_ounce | 2026-10-29 | -0.50 | -0.71 | -4.07 | ok |
| CL=F | 102.00 | USD_per_barrel | 2026-10-29 | -0.76 | 2.54 | 9.83 | ok |
| BZ=F | 114.88 | USD_per_barrel | 2026-10-29 | -0.38 | 1.51 | 12.29 | ok |
| TLT | 81.49 | USD_per_share | 2026-10-29 | 0.62 | -0.31 | 4.86 | ok |
| UUP | 29.04 | USD_per_share | 2026-10-29 | -0.07 | 0.48 | 0.28 | ok |
| HYG | 77.58 | USD_per_share | 2026-10-29 | -0.01 | 0.62 | 0.88 | ok |
| LQD | 104.22 | USD_per_share | 2026-10-29 | 0.14 | -0.06 | 2.15 | ok |
| ^VIX | 17.20 | index | 2026-10-29 | 1.71 | -9.62 | 4.94 | ok |
| ^VIX3M | 19.37 | index | 2026-10-29 | 0.78 | -3.73 | 4.25 | ok |
| ^VVIX | 98.01 | index | 2026-10-29 | 1.45 | -9.20 | 6.52 | ok |
| ^MOVE | 93.54 | index | 2026-10-29 | -1.07 | -12.45 | -15.31 | ok |
| NVDA | 213.66 | USD_per_share | 2026-10-29 | -0.80 | 0.68 | -7.45 | ok |
| MSFT | 530.14 | USD_per_share | 2026-10-29 | -0.16 | 1.74 | 3.38 | ok |
| AMZN | 243.79 | USD_per_share | 2026-10-29 | -4.25 | -2.63 | -1.79 | ok |
| GOOGL | 283.82 | USD_per_share | 2026-10-29 | -12.64 | -12.46 | -16.09 | ok |
| META | 624.52 | USD_per_share | 2026-10-29 | 1.96 | -3.75 | -13.97 | ok |
| CRWV | 60.74 | USD_per_share | 2026-10-29 | -4.99 | 9.24 | -31.42 | ok |
| MU | 934.27 | USD_per_share | 2026-10-29 | -4.98 | 9.08 | -14.85 | ok |
| DRAM | 51.75 | USD_per_share | 2026-10-29 | -4.38 | 13.29 | -16.57 | ok |
| VRT | 245.92 | USD_per_share | 2026-10-29 | 1.23 | 25.73 | -0.08 | ok |

## 跨资产风险解释

截至30日盘前，科技压力加剧，全面恐慌证据仍不足。盘前VIX18.60（11:46UTC）较29日17.20上升；29日同日VIX3M19.37、VVIX98.01、MOVE93.54，昨日期限未倒挂，不用今日VIX与昨日3M造今日期限结构。FRED2年4.67%、10年5.05%、实际10年2.67%、HY314bp/IG86bp仍仅28日，不能证明新财报冲击后信用无压力。29日盈亏平衡2.35%；STLFSI23日−0.5837、GPR26日165.25/MA7 181.42均滞后。黄金GLD盘前走弱、TLT走强、能源走强，风险渠道不同，不合成未经验证的避险/战争指数。CNN418；CME页面有方法但概率矩阵因referrer拒绝访问，不报二手政策概率。美元UUP保留29日收盘29.04。WTI/Brent交割月未对齐，不算跨期涨幅。

## 宏观与地缘风险指标

| 指标 | 数值 | 单位 | 观测日 | 20次观测变化 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- | --- |
| DGS2 | 4.67 | percent | 2026-10-28 | -0.22 | lagged | https://fred.stlouisfed.org/series/DGS2 |
| BAMLH0A0HYM2 | 3.14 | percentage_points | 2026-10-28 | 0.02 | lagged | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| BAMLC0A0CM | 0.86 | percentage_points | 2026-10-28 | 0.02 | lagged | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| DGS10 | 5.05 | percent | 2026-10-28 | -0.21 | lagged | https://fred.stlouisfed.org/series/DGS10 |
| DFII10 | 2.67 | percent | 2026-10-28 | -0.24 | lagged | https://fred.stlouisfed.org/series/DFII10 |
| T10YIE | 2.35 | percent | 2026-10-29 | -0.01 | ok | https://fred.stlouisfed.org/series/T10YIE |
| STLFSI4 | -0.58 | index | 2026-10-23 | 0.28 | lagged | https://fred.stlouisfed.org/series/STLFSI4 |
| CBOE_VIX | 17.20 | index | 2026-10-29 | 0.81 | ok | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| GPRD | 165.25 | index | 2026-10-26 | -36.19 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_ACT | 149.77 | index | 2026-10-26 | -147.74 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_THREAT | 187.38 | index | 2026-10-26 | 26.08 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_MA7 | 181.42 | index | 2026-10-26 | 0.55 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_MA30 | 175.44 | index | 2026-10-26 | 12.06 | lagged | https://www.matteoiacoviello.com/gpr.htm |

## CNN Fear & Greed

缺失：CNN 无可核验数据，不使用替代指数

## 19 板块与主题 ETF：价格量能证据

| 标的 | 板块 | 1日% | 5日% | 20日% | 相对SPY 1日pp | 相对SPY 5日pp | 相对SPY 20日pp | 成交量/前20日 | 观测日 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLK | 科技 | -1.18 | 3.51 | -4.59 | -0.80 | 2.80 | -5.29 | 0.85 | 2026-10-29 |
| XLE | 能源 | 0.38 | 1.69 | 9.59 | 0.76 | 0.98 | 8.88 | 0.78 | 2026-10-29 |
| XLF | 金融 | 1.44 | 0.51 | 6.51 | 1.83 | -0.19 | 5.81 | 1.00 | 2026-10-29 |
| XLI | 工业 | 0.97 | 2.04 | 0.88 | 1.36 | 1.33 | 0.18 | 1.04 | 2026-10-29 |
| XLV | 医疗 | 2.40 | 1.51 | 10.73 | 2.79 | 0.80 | 10.03 | 1.77 | 2026-10-29 |
| XLP | 必需消费 | 1.54 | -2.01 | 9.77 | 1.93 | -2.72 | 9.07 | 1.08 | 2026-10-29 |
| XLY | 可选消费 | 0.75 | 1.03 | 6.79 | 1.14 | 0.33 | 6.09 | 0.90 | 2026-10-29 |
| XLC | 通信 | -1.87 | -5.78 | -7.94 | -1.49 | -6.49 | -8.64 | 1.63 | 2026-10-29 |
| XLU | 公用事业 | 1.53 | 0.63 | 8.72 | 1.91 | -0.08 | 8.02 | 0.78 | 2026-10-29 |
| XLRE | 房地产 | 2.21 | 1.27 | 5.85 | 2.59 | 0.56 | 5.15 | 0.83 | 2026-10-29 |
| XLB | 材料 | 1.29 | 1.63 | 8.22 | 1.67 | 0.92 | 7.52 | 1.32 | 2026-10-29 |
| SMH | 半导体 | -1.06 | 7.32 | -9.09 | -0.67 | 6.62 | -9.79 | 0.68 | 2026-10-29 |
| IGV | 软件 | -3.52 | -0.69 | -0.24 | -3.14 | -1.40 | -0.94 | 1.49 | 2026-10-29 |
| XOP | 油气开采 | -0.42 | 1.35 | 8.26 | -0.04 | 0.64 | 7.56 | 0.43 | 2026-10-29 |
| OIH | 油服 | -0.29 | 8.20 | 7.03 | 0.09 | 7.49 | 6.32 | 0.49 | 2026-10-29 |
| ITA | 航空与国防 | 3.16 | 4.80 | 3.01 | 3.54 | 4.10 | 2.31 | 1.31 | 2026-10-29 |
| ARKX | 航天主题 | 0.62 | 4.59 | -3.07 | 1.00 | 3.88 | -3.77 | 0.77 | 2026-10-29 |
| KRE | 区域银行 | 1.04 | 0.62 | 4.16 | 1.42 | -0.09 | 3.46 | 0.61 | 2026-10-29 |
| SKYY | 云计算 | -2.84 | 1.89 | 0.28 | -2.46 | 1.18 | -0.43 | 1.73 | 2026-10-29 |

## 资金证据分层

19ETF均有29日完整日线，无需补接：金融+1.44%、医疗+2.40%、工业+0.97%、能源+0.38%，软件−3.52%、半导体−1.06%；SMH五日相对SPY仍+6.62个百分点，最新一日转弱与此前反弹同时成立。今盘前金融/医疗/能源继续相对强，工业约169.41转弱；首30–60分钟是否守前日收盘/低点比盘前涨幅更有验证意义。军工ITA29日+3.16%、航天ARKX+0.62%，只列观察，不把地缘新闻等同订单兑现。ICI最新仍27日发布截至21日周净发行：全ETF458.21亿美元、国内股票278.23亿、债券95.67亿；不是30日19ETF资金流。发行人VanEck本次两次超时，不能刷新份额/拆分桥，保持当期申赎缺口；没有当期机构持仓证据。

## 最近可核验 ETF 申赎窗口

| 标的 | 金额 USD million | 起始日 | 结束日 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- |

## Polymarket 搜索覆盖与限制

2026-10-30T12:08:37.599365+00:00：基础全主题加10组主动搜索（沙特管线、AMD/Palantir财报、Oracle AI、AI破产、银行倒闭、衰退、11月CPI、Meta融资、Anthropic IPO）；CPI/Meta/Anthropic主动搜索分别27/87/30结果，仅首10条，其余基础查询亦有截断。已检查参考/风险/临近事件，不能称全市场覆盖；没有匹配直接代表AI信贷传染的合格合约。

## Polymarket · 值得警惕的信号

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["AI bubble burst in 2026?", "期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。", "https://polymarket.com/event/ai-bubble-burst-by"] | [9.2, {"status": "comparable", "change_pp": -0.9999999999999996}] | {"spread": 0.0020000000000000018, "volume24h_usd": 3515.139845999999, "liquidity_usd": 26666.19375, "quality_flags": [], "retrieved_at": "2026-10-30T12:02:06.001197+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["本次报价9.2%，24h成交约3515美元；结合价差与专门定义，不等于客观事件或股价概率。", "AI估值与融资风险"] | ["同规则价格持续上行并有经营/信用证据", "现金流和信用改善"] | [null, null] |
| ["Will WTI Crude Oil (WTI) hit (HIGH) $105 in October?", "10月交易时段内，Pyth的ICE WTI活跃月合约1分钟最终高价达到105美元即Yes；按规则提前3个交易时段换月，数据不可用时可依ICE日高低。不是月末价格，也不能以Yahoo CL=F直接结算。", "https://polymarket.com/event/what-price-will-wti-hit-in-october-2026"] | [48.0, {"status": "comparable", "change_pp": 13.5}] | {"spread": 0.10000000000000003, "volume24h_usd": 83441.06831399997, "liquidity_usd": 22157.4019, "quality_flags": ["spread_over_5pp_or_invalid"], "retrieved_at": "2026-10-30T12:02:06.001197+00:00", "contract_end_at": "2026-11-01T03:59:59.999000+00:00"} | ["本次报价48%，24h成交约83441美元；结合价差与专门定义，不等于客观事件或股价概率。", "能源成本→利率→成长估值"] | ["供应中断与可核验油价共同走强", "通行恢复及供应增加"] | [null, null] |
| ["Military action against Saudi Oil Pipeline (East-West) by October 31?", "截至10月31日利雅得23:59，空袭或地对地武器直接命中东西输油管线或泵站才算Yes；拦截弹碎片、未执行威胁、网络攻击等排除。按沙特官方及可信报道共识裁决，争议可等待三天。价格不证明已命中或发生供应损失。", "https://polymarket.com/event/military-action-against-saudi-oil-pipeline-east-west-byptptpt"] | [6.0, {"status": "comparable", "change_pp": -3.0}] | {"spread": 0.020000000000000004, "volume24h_usd": 2567.0823870000004, "liquidity_usd": 18219.7925, "quality_flags": [], "retrieved_at": "2026-10-30T12:01:58.852051+00:00", "contract_end_at": "2026-10-31T20:59:00+00:00"} | ["本次报价6%，24h成交约2567美元；结合价差与专门定义，不等于客观事件或股价概率。", "若管线或泵站实际受损，可能影响绕行出口能力，抬高能源成本。"] | ["沙特官方/独立来源证实直接命中与供应影响，且市场恢复交易后油价持续走强。", "只有已拦截导弹或警报解除，未发生合格命中；供应正常且价格回落。"] | [null, null] |

## Polymarket · 有参考价值的事件

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["US x Iran ceasefire continues through October 31?", "截至10月31日伊朗标准时间23:59，美国未对伊朗领土及内水实施规则列明的直接命中空袭或地对地打击才为Yes。海域/空域、拦截碎片、小型打击、网络战等不计；争议信息允许三日核验。不是所有交战方全面停火，也不等于海峡畅通。", "https://polymarket.com/event/us-iran-ceasefire-continues-throughptptpt"] | [92.35, {"status": "comparable", "change_pp": 14.749999999999996}] | {"spread": 0.0050000000000000044, "volume24h_usd": 824672.0423489999, "liquidity_usd": 76661.38896, "quality_flags": [], "retrieved_at": "2026-10-30T12:02:06.001197+00:00", "contract_end_at": "2026-10-31T23:59:00+00:00"} | ["本次报价92.35%，24h成交约824672美元；结合价差与专门定义，不等于客观事件或股价概率。", "仅美国对伊朗领土合格打击的定义，与沙特/胡塞管线风险不同。"] | ["规则所列打击事实及资产反应共同核验。", "其他地区攻击不能自动算作该合约触发。"] | [null, null] |
| ["Strait of Hormuz traffic returns to normal by December 31?", "期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。", "https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31"] | [10.5, {"status": "comparable", "change_pp": -1.0000000000000009}] | {"spread": 0.009999999999999995, "volume24h_usd": 123000.39090199997, "liquidity_usd": 298851.5745, "quality_flags": [], "retrieved_at": "2026-10-30T12:02:06.001197+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["本次报价10.5%，24h成交约123000美元；结合价差与专门定义，不等于客观事件或股价概率。", "IMF七日平均船舶到达不少于60，不能由单日放行新闻替代。"] | ["官方Portwatch连续数据达到定义。", "只出现局部绕行或有限通航。"] | [null, null] |
| ["Will Anthropic IPO by December 31, 2026?", "Anthropic股份在2026年12月31日23:59美东前于公开证券交易所挂牌并开始交易才为Yes；仅提交S-1不算。被已上市公司收购则No。官方文件/公司与交易所公告优先，可信报道共识可辅助。", "https://polymarket.com/event/anthropic-ipo-by"] | [93.60000000000001, {"status": "comparable", "change_pp": -1.19999999999999}] | {"spread": 0.009999999999999898, "volume24h_usd": 5342.164388, "liquidity_usd": 39295.84383, "quality_flags": [], "retrieved_at": "2026-10-30T12:02:01.424076+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["本次报价93.6%，24h成交约5342美元；结合价差与专门定义，不等于客观事件或股价概率。", "AI一级市场融资窗口与公开估值参照；不等于云供应商利润"] | ["官方招股文件、定价及交易所首日交易依次核验", "仅保密/公开申报、尚未挂牌交易；不以媒体时刻替代官方"] | [null, null] |

## Polymarket · 将要发生的事件及概率

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Will AMD (AMD) beat quarterly earnings?", "AMD下一季度首次主要non-GAAP EPS四舍五入至美分后严格大于固定1.97美元才Yes；优先稀释EPS、官方财报，其次SeekingAlpha。公告日16点后96小时仍无non-GAAP则转GAAP（稀释优先），仍无为No；预定日后45天未披露亦No。除明显即时错误外不取后续重述。门槛固定于建约，不是最新一致预期，更非股价上涨概率。", "https://polymarket.com/event/amd-quarterly-earnings-nongaap-eps-11-03-2026-1pt97"] | [84.5, {"status": "comparable", "change_pp": -3.0000000000000027}] | {"spread": 0.06999999999999995, "volume24h_usd": 203.128948, "liquidity_usd": 219.4803, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"], "retrieved_at": "2026-10-30T12:01:58.547359+00:00", "contract_end_at": "2026-11-03T22:00:00+00:00"} | ["本次报价84.5%，24h成交约203美元；结合价差与专门定义，不等于客观事件或股价概率。", "AMD11月3日电话会时间已核验；PLTR官方预告11月2日盘后，具体分钟未核验故留空。两者检验AI硬件/软件兑现。"] | ["官方主要non-GAAP EPS按固定阈值核验，再看订单、现金和财报后价格。", "EPS过线但指引/价格承接失败，不能当作买入依据。"] | ["2026-11-03T17:00:00-05:00", "https://ir.amd.com/news-events/press-releases/detail/1300/amd-to-report-fiscal-third-quarter-2026-financial-results"] |
| ["Will Palantir (PLTR) beat quarterly earnings?", "Palantir下一季度首次主要non-GAAP EPS四舍五入至美分后严格大于固定0.42美元才Yes；优先稀释EPS、官方财报，其次SeekingAlpha。公告日16点后96小时仍无non-GAAP则转GAAP（稀释优先），仍无为No；预定日后45天未披露亦No。除明显即时错误外不取后续重述。门槛固定于建约，不是最新一致预期，更非股价上涨概率。", "https://polymarket.com/event/pltr-quarterly-earnings-nongaap-eps-11-02-2026-0pt42"] | [79.0, {"status": "comparable", "change_pp": -11.5}] | {"spread": 0.020000000000000018, "volume24h_usd": 17.29443, "liquidity_usd": 675.8291, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"], "retrieved_at": "2026-10-30T12:01:58.965935+00:00", "contract_end_at": "2026-11-02T22:00:00+00:00"} | ["本次报价79%，24h成交约17美元；结合价差与专门定义，不等于客观事件或股价概率。", "AMD11月3日电话会时间已核验；PLTR官方预告11月2日盘后，具体分钟未核验故留空。两者检验AI硬件/软件兑现。"] | ["官方主要non-GAAP EPS按固定阈值核验，再看订单、现金和财报后价格。", "EPS过线但指引/价格承接失败，不能当作买入依据。"] | [null, null] |

## US x Iran ceasefire continues through October 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1038648 / 4641065 |
| Yes 概率 % | 92.35 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-4.75, 14.85] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 14.749999999999996} |
| 24h成交量 / 流动性 USD | [824672.0423489999, 76661.38896] |
| 价差 pp | 0.50 |
| 到期 | 2026-10-31T23:59:00+00:00 |
| 结算规则摘要 | 截至10月31日伊朗标准时间23:59，美国未对伊朗领土及内水实施规则列明的直接命中空袭或地对地打击才为Yes。海域/空域、拦截碎片、小型打击、网络战等不计；争议信息允许三日核验。不是所有交战方全面停火，也不等于海峡畅通。 |
| 规则指纹 | 4ad99c00bba55951472643794eca27dab0743ff8891a0f80509306b4b3c87506 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-30T11:59:34.869447Z |
| 抓取时间 | 2026-10-30T12:02:06.001197+00:00 |
| 来源 | https://polymarket.com/event/us-iran-ceasefire-continues-throughptptpt |

## Will the Fed increase interest rates by 25 bps after the December 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 770450 / 3215008 |
| Yes 概率 % | 71.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-5.0, -1.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [295917.456995, 417832.6186] |
| 价差 pp | 1.00 |
| 到期 | 2026-12-09T23:59:00+00:00 |
| 结算规则摘要 | 以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。 |
| 规则指纹 | 933a10a15eeec0ff1de30468fa20540301ed243f75cc3572d42946192f81a123 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-30T11:59:34.869447Z |
| 抓取时间 | 2026-10-30T12:02:06.001197+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-december-20260729232808632 |

## Strait of Hormuz traffic returns to normal by October 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 830253 / 3501950 |
| Yes 概率 % | 0.05 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, -0.3] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [265846.25, 686747.93975] |
| 价差 pp | 缺失 |
| 到期 | 2026-11-01T03:59:00+00:00 |
| 结算规则摘要 | 10月31日前IMF Portwatch海峡船舶通行7日均值任一天达到60才为Yes；非宣布开放。末日数据等待14日，有窗口内修订和明显数据错误处理。 |
| 规则指纹 | be893052d9d9b648fb6ffa8b901ed6d9775d1cd3d1be9f830e1dcf5d0f046390 |
| 质量 | ["spread_over_5pp_or_invalid"] |
| 元数据更新（不是成交时间） | 2026-10-30T11:59:34.869447Z |
| 抓取时间 | 2026-10-30T12:02:06.001197+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-october-31-20260810151043583 |

## Strait of Hormuz traffic returns to normal by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 455875 / 2176270 |
| Yes 概率 % | 10.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-1.0, -1.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -1.0000000000000009} |
| 24h成交量 / 流动性 USD | [123000.39090199997, 298851.5745] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。 |
| 规则指纹 | b0c8ba27f4437b0d8ab819ae170bec118166232e39cdcaefb95bd352d29073d4 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-30T11:55:34.751508Z |
| 抓取时间 | 2026-10-30T12:02:06.001197+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31 |

## Will WTI Crude Oil (WTI) hit (HIGH) $105 in October?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1078055 / 4951227 |
| Yes 概率 % | 48.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [20.5, -5.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 13.5} |
| 24h成交量 / 流动性 USD | [83441.06831399997, 22157.4019] |
| 价差 pp | 10.00 |
| 到期 | 2026-11-01T03:59:59.999000+00:00 |
| 结算规则摘要 | 10月交易时段内，Pyth的ICE WTI活跃月合约1分钟最终高价达到105美元即Yes；按规则提前3个交易时段换月，数据不可用时可依ICE日高低。不是月末价格，也不能以Yahoo CL=F直接结算。 |
| 规则指纹 | 0c455b139d74a669b793323a95aea1e08486656281c457348bd488137e37ae8a |
| 质量 | ["spread_over_5pp_or_invalid"] |
| 元数据更新（不是成交时间） | 2026-10-30T11:57:34.396634Z |
| 抓取时间 | 2026-10-30T12:02:06.001197+00:00 |
| 来源 | https://polymarket.com/event/what-price-will-wti-hit-in-october-2026 |

## AI bubble burst in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 691340 |
| Yes 概率 % | 9.20 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [0.9, 0.3] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.9999999999999996} |
| 24h成交量 / 流动性 USD | [3515.139845999999, 26666.19375] |
| 价差 pp | 0.20 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | fc153b2136a8dfbadcd169dce1add40690acb1748566b99716fe7ae8fcb07330 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-30T11:55:34.751508Z |
| 抓取时间 | 2026-10-30T12:02:06.001197+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## Tesla and SpaceX merger officially announced by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 192962 / 2252540 |
| Yes 概率 % | 20.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [1.5, 1.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 1.4999999999999987} |
| 24h成交量 / 流动性 USD | [1399.059026, 30541.2384] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59纽约时间前，Tesla或SpaceX正式宣布双方合并或一方收购另一方的控制权即Yes；无需在期限内完成交易。控制权通常为过半权益或等效治理权；少数股权投资及仅讨论不算。以公司公告或可信报道共识核验；旧URL中的june-30不是本合约期限。 |
| 规则指纹 | 909906ae3b6db7e473468713ea6a1e1e4cf4c931fe247c7d3d576e7986513008 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-30T12:01:35.801365Z |
| 抓取时间 | 2026-10-30T12:02:06.001197+00:00 |
| 来源 | https://polymarket.com/event/tesla-and-spacex-merger-officially-announced-by-june-30 |

## AI bubble burst by June 30, 2027?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 4838928 |
| Yes 概率 % | 22.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, 2.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [895.2530449999999, 12045.2903] |
| 价差 pp | 1.00 |
| 到期 | 2027-07-01T03:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | bd0420587e08487fffa5050e7fd9b79ffff909a9f843d3f620207ee859462505 |
| 质量 | ["volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-10-30T11:55:34.751508Z |
| 抓取时间 | 2026-10-30T12:02:06.001197+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## Military action against Saudi Oil Pipeline (East-West) by October 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1147445 / 5401795 |
| Yes 概率 % | 6.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.5, -9.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -3.0} |
| 24h成交量 / 流动性 USD | [2567.0823870000004, 18219.7925] |
| 价差 pp | 2.00 |
| 到期 | 2026-10-31T20:59:00+00:00 |
| 结算规则摘要 | 截至10月31日利雅得23:59，空袭或地对地武器直接命中东西输油管线或泵站才算Yes；拦截弹碎片、未执行威胁、网络攻击等排除。按沙特官方及可信报道共识裁决，争议可等待三天。价格不证明已命中或发生供应损失。 |
| 规则指纹 | 069363ea2366e79b0328bfc26ff2cd674087f85aac50b63930c45e30f0b86adf |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-30T12:01:35.801365Z |
| 抓取时间 | 2026-10-30T12:01:58.852051+00:00 |
| 来源 | https://polymarket.com/event/military-action-against-saudi-oil-pipeline-east-west-byptptpt |

## Will Anthropic IPO by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 549019 / 2413330 |
| Yes 概率 % | 93.60 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-1.15, 12.1] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -1.19999999999999} |
| 24h成交量 / 流动性 USD | [5342.164388, 39295.84383] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | Anthropic股份在2026年12月31日23:59美东前于公开证券交易所挂牌并开始交易才为Yes；仅提交S-1不算。被已上市公司收购则No。官方文件/公司与交易所公告优先，可信报道共识可辅助。 |
| 规则指纹 | 91cad6e5770d0b925976d3fbba5e8c61a7f0561a5ee40474d459b9851b8bf4e0 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-30T12:01:35.801365Z |
| 抓取时间 | 2026-10-30T12:02:01.424076+00:00 |
| 来源 | https://polymarket.com/event/anthropic-ipo-by |

## Will AMD (AMD) beat quarterly earnings?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1262633 / 6280962 |
| Yes 概率 % | 84.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-4.0, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -3.0000000000000027} |
| 24h成交量 / 流动性 USD | [203.128948, 219.4803] |
| 价差 pp | 7.00 |
| 到期 | 2026-11-03T22:00:00+00:00 |
| 结算规则摘要 | AMD下一季度首次主要non-GAAP EPS四舍五入至美分后严格大于固定1.97美元才Yes；优先稀释EPS、官方财报，其次SeekingAlpha。公告日16点后96小时仍无non-GAAP则转GAAP（稀释优先），仍无为No；预定日后45天未披露亦No。除明显即时错误外不取后续重述。门槛固定于建约，不是最新一致预期，更非股价上涨概率。 |
| 规则指纹 | 45fb7613b172228eb6c9f337a9f40f9667816eecd866e1137e8b1f62ff7355e6 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"] |
| 元数据更新（不是成交时间） | 2026-10-30T12:01:35.801365Z |
| 抓取时间 | 2026-10-30T12:01:58.547359+00:00 |
| 来源 | https://polymarket.com/event/amd-quarterly-earnings-nongaap-eps-11-03-2026-1pt97 |

## Will Palantir (PLTR) beat quarterly earnings?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1262630 / 6280959 |
| Yes 概率 % | 79.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-6.5, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -11.5} |
| 24h成交量 / 流动性 USD | [17.29443, 675.8291] |
| 价差 pp | 2.00 |
| 到期 | 2026-11-02T22:00:00+00:00 |
| 结算规则摘要 | Palantir下一季度首次主要non-GAAP EPS四舍五入至美分后严格大于固定0.42美元才Yes；优先稀释EPS、官方财报，其次SeekingAlpha。公告日16点后96小时仍无non-GAAP则转GAAP（稀释优先），仍无为No；预定日后45天未披露亦No。除明显即时错误外不取后续重述。门槛固定于建约，不是最新一致预期，更非股价上涨概率。 |
| 规则指纹 | d3c8b7becbdaf8a9088e9ce0ead238b19bc1a5cf62e8f1a6ee479a1e1d8a7bef |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-10-30T11:59:34.869447Z |
| 抓取时间 | 2026-10-30T12:01:58.965935+00:00 |
| 来源 | https://polymarket.com/event/pltr-quarterly-earnings-nongaap-eps-11-02-2026-0pt42 |

## AI 压力：合约、经营与估值分开

三层分开：专门AI2026合约9.2%，至2027年6月22.5%，两者均有90天三项极端条件，不能视作普通股价回调的客观概率。经营层：AWS增长39.3%、Sandisk指引强、H10029日仍2.90美元/GPU小时，反驳普遍需求崩塌；Amazon TTM公司FCF−423.57亿美元显示投入回收压力，不等于季度FCF或企业FCFF。H100网页7D标题与日表不一致：22日2.88至29日2.90自行算约+0.69%，不引用标题5.5%。融资层：MSFT本次SEC列表最新仍29日初步424B2，最终规模票息未核验；Nscale担保仍媒体谈判线索，不能确认为NVDA负债。估值层：五家公司SEC重查成功，AMZN新增30日10-Q；MSFT/AMZN/GOOGL/META最新TTM、融资租赁/净债务和稀释桥未完整，继续暂停精确DCF。NVDA无新定期财报，复用已核验底稿按29日收盘重算三情景（不是盘前目标价）。公司整体价值不全归AI，情景权重不是客观崩盘概率。

## NVDA · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | scenario_analysis |
| 财务底稿 | TTM 至 2026-07-26；最新 10-Q / filed 2026-08-26 |
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001045810.json", "checked_at": "2026-10-30T12:04:52.022593+00:00", "latest_filing_date": "2026-08-26"} |
| 观测财务数据 | {"ttm_revenue_million": 302970, "revenue_quarters": [{"end": "2025-10-26", "value": 57006000000, "filed": "2025-11-19", "duration_days": 91}, {"end": "2026-01-25", "value": 68127000000, "filed": "2026-02-25", "duration_days": 91}, {"end": "2026-04-26", "value": 81615000000, "filed": "2026-05-20", "duration_days": 91}, {"end": "2026-07-26", "value": 96221000000, "filed": "2026-08-26", "duration_days": 91}], "cash_million": 22443.0, "liquid_investments_million": 34143.0, "debt_million": 33366.0, "finance_lease_million": 0, "diluted_shares_million": 24285.0, "latest_operating_income_million": 63734.0, "observed_end": "2026-07-26", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "Revenues", "latest_reported_revenue_million": 96221.0, "income_statement_window": "最近单季度", "ttm_bridge_note": "采用同版 FY2026全年 + FY2027半年 - FY2026半年；与四季逐项求和差1百万为披露舍入差。"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json", "https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。10-Q Note14 表明融资租赁费用不重大；模型按不重大近似零，不将其称为精确零负债。未确认担保仅作为压力情景，非已到期净债务。市场化股权42783和非市场化股权51157不作为类现金；非经营资产加回为0的保守假设。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | 无 |
| 价格 USD | 213.66 |
| 基期输入 USD million / million shares | {"revenue": 302970, "net_debt": -23220.0, "diluted_shares": 24285.0, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.2905020367807417, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## NVDA · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 98.77 | -53.77 | 14.00 | 60.00 | 12.00 | 68.42 |
| 基准 | 154.12 | -27.87 | 20.00 | 65.00 | 11.00 | 74.20 |
| 乐观 | 242.58 | 13.54 | 26.00 | 70.00 | 10.00 | 79.05 |

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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0000789019.json", "checked_at": "2026-10-30T12:04:53.657155+00:00", "latest_filing_date": "2026-10-28"} |
| 观测财务数据 | {"revenue_million": 92279, "operating_income_million": 45915, "operating_cashflow_million": 58000, "cash_capex_million": 39367, "cfo_less_cash_capex_million": 18633, "diluted_shares_million": 7446, "unit": "USD million; shares million", "observed_end": "2026-09-30", "published_at": null} |
| 来源 | ["https://www.microsoft.com/en-us/Investor/earnings/FY-2027-Q1/press-release-webcast"] |
| 口径 | 单季CFO减现金capex不等于FCFF；融资租赁新增/负债、优先权益、TTM及稀释桥须完整后重算；不假设缺失项为零。 |
| 主观假设说明 | 缺失 |
| 权益桥额外假设 | 无 |
| 缺失原因 | 已发现新季度披露；必要TTM、融资租赁及优先权益/稀释桥未完成，暂停旧底稿估值和价格反推。 |

## AMZN · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | unavailable |
| 财务底稿 | FY2026 Q3 ended 2026-09-30 |
| 披露检查 | {"checked_at": "2026-10-30T12:04:55.925679+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001018724.json", "latest_filing_date": "2026-10-30"} |
| 观测财务数据 | {"revenue_quarter_million": 201900, "aws_revenue_quarter_million": 45980, "cfo_ttm_million": 168300, "net_cash_capex_ttm_million": 210657, "company_cash_fcf_ttm_million": -42357, "gaap_eps": 1.89} |
| 来源 | ["https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Third-Quarter-Results/default.aspx", "https://data.sec.gov/submissions/CIK0001018724.json", "https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm"] |
| 口径 | TTM公司现金FCF=CFO减净现金资本支出；不等于FCFF；不能当单季。融资租赁和债务股数桥待补。 |
| 主观假设说明 | 缺失 |
| 权益桥额外假设 | 无 |
| 缺失原因 | 30日新增Q3 10-Q已核验；最新TTM、融资租赁/净债务与稀释桥尚未完整，不沿用旧估值。 |

## GOOGL · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | unavailable |
| 财务底稿 | 2026Q3 ended 2026-09-30 |
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001652044.json", "checked_at": "2026-10-30T12:04:57.679757+00:00", "latest_filing_date": "2026-10-29"} |
| 观测财务数据 | {"revenue_million": 127577, "operating_income_million": 40576, "net_income_million": 26468, "net_income_to_common_million": 26170, "operating_cashflow_million": 42290, "cash_capex_million": 51355, "cfo_less_cash_capex_million": -9065, "diluted_shares_million": 12368, "common_stock_net_proceeds_million": 12371, "unit": "USD million; shares million", "observed_end": "2026-09-30", "published_at": null, "finance_lease_liabilities_million": 3705} |
| 来源 | ["https://www.sec.gov/Archives/edgar/data/1652044/000165204426000080/googexhibit991q32026.htm", "https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm"] |
| 口径 | 单季CFO减现金capex不等于FCFF；融资租赁新增/负债、优先权益、TTM及稀释桥须完整后重算；不假设缺失项为零。 |
| 主观假设说明 | 缺失 |
| 权益桥额外假设 | 无 |
| 缺失原因 | 已发现新季度披露；必要TTM、融资租赁及优先权益/稀释桥未完成，暂停旧底稿估值和价格反推。 |

## META · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | unavailable |
| 财务底稿 | 2026Q3 ended 2026-09-30 |
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001326801.json", "checked_at": "2026-10-30T12:04:59.922820+00:00", "latest_filing_date": "2026-10-22"} |
| 观测财务数据 | {"revenue_million": 64601, "operating_cashflow_million": 32790, "reported_capex_including_finance_lease_principal_million": 34910, "company_defined_fcf_million": -2120, "diluted_shares_million": 2573, "reported_operating_income_million": 12988, "legal_charge_million": 9900, "observed_end": "2026-09-30", "published_at": "2026-10-21T16:01:00-04:00", "unit": "USD million; shares million", "noncancelable_commitments_million": 454520, "leases_not_commenced_million": 355730, "contingent_cloud_capacity_max_million": 14720, "restricted_cash_reclassified_million": 10800, "commitments_due_2026_million": 45850, "commitments_due_2027_million": 121410} |
| 来源 | ["https://www.prnewswire.com/news-releases/meta-reports-third-quarter-2026-results-302915964.html", "https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm", "https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Announces-Launch-of-Offering-of-Depositary-Shares-Representing-Series-A-Mandatory-Convertible-Preferred-Stock-and-Offering-of-Class-A-Common-Stock-in-Connection-with-Forward-Sale-Agreements/default.aspx", "https://www.prnewswire.com/news-releases/meta-announces-pricing-of-offering-of-depositary-shares-representing-series-a-mandatory-convertible-preferred-stock-and-offering-of-class-a-common-stock-in-connection-with-forward-sale-agreements-302920247.html"] |
| 口径 | 公司FCF扣除融资租赁本金，不能直接代替模型FCFF；融资租赁负债/新增资产未齐，不假设零。法律费用不全归AI经营。 |
| 主观假设说明 | 缺失 |
| 权益桥额外假设 | 无 |
| 缺失原因 | 22日10-Q已核验，本次无新增定期财报。27日普通股625美元定价、优先票息6.5%已核验；完整融资租赁负债/新增资产、优先权益/远期发行与现金到账桥未齐，不用不同承诺简单充当现有债务，暂停精确FCFF反推。 |

## 科技修复需重新建立

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 30日财报后的常规承接 |
| 关联标的 | ["QQQ", "SMH", "SPY", "RSP"] |
| 确认条件 | 今晚首30–60分钟低点抬高、站回实际常规VWAP且回踩不失守；QQQ先收回704.40，再争取711.62/715.34，SMH先收回546.67，再看555.50/561.67。RSP与金融医疗同步承接，收盘保留修复才升级。首个突破只是观察信号，价格关口来自已发生交易，不是必然支撑。 |
| 失效条件 | 盘前已经低于QQQ704.40、SMH546.67；若常规开盘后反抽仍不能收回，或突破后跌破开盘区间低点且反抽失败，修复判为失败。若RSP/金融医疗亦失守29日低点，风险由科技向全市场扩散。 |
| 观察期限 | 30日及随后1–3个交易日 |
| 反证 | 29日非科技与等权仍强，盘后薄量可能修复；反证不足不能升级为趋势反转。 |
| 状态 | 盘前警戒已触发，常规确认待开始 |

## 金融医疗相对强势延续

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | ABBV新指引及非科技相对承接 |
| 关联标的 | ["XLF", "XLV", "RSP"] |
| 确认条件 | 30日回踩形成更高低点，XLF守56.94/至少56.67、XLV守184.04/至少182.10，RSP守220.04；持续强于SPY，收盘不回吐主要涨幅。价格带是29日收盘/低点，不是保证支撑。 |
| 失效条件 | 跌破29日低点且反抽失败，金融/等权同步转弱或信用显著走阔。 |
| 观察期限 | 30日至未来1–3日 |
| 反证 | 工业盘前转弱；XLV不是生物科技ETF，单一药企业绩不能代表全行业。 |
| 状态 | 优先观察，等待回踩 |

## 存储强业绩要过价格检验

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | Sandisk业绩消化、AMD下周财报 |
| 关联标的 | ["SNDK", "MU", "DRAM", "VRT"] |
| 确认条件 | 先等实际开盘区间形成、低点抬高且站回常规VWAP并强于SMH，再观察MU927.24/934.27、DRAM51.23/51.75、VRT236.55/245.92是否重新夺回。当前距这些前日价位较远，没收回前只能称盘中修复，不能要求一跳越过所有关口。 |
| 失效条件 | 好业绩后仍跌破开盘区间下沿，反抽无力且相对SMH继续转弱。 |
| 观察期限 | 30日及财报后1–3日 |
| 反证 | 企业需求强与估值压缩可共存；SNDK11月拆股不改变总价值，比较必须调整。 |
| 状态 | 警戒已触发，等待价格验证 |

## 云公司等待现金回报和价格共同转好

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | AMZN/GOOGL财报消化及融资披露 |
| 关联标的 | ["AMZN", "GOOGL", "MSFT", "IGV"] |
| 确认条件 | 30日形成更高低点且缺口逐步回补，IGV先守105.94再回107.97/109.02；公司同时解释现金投入转化为回报的期限。 |
| 失效条件 | 低位反抽仍无法回收前日低点，现金回报指引继续下修或融资成本显著上升。 |
| 观察期限 | 未来1–3日，基本面跟踪至下一披露 |
| 反证 | AWS/Azure/Cloud增长强，可使价格迅速修复；缺口回补并不自动代表估值便宜。 |
| 状态 | 等待 |

## 能源财报后的承接

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | XOM/CVX新业绩及今晚电话会 |
| 关联标的 | ["XLE", "XOM", "CVX"] |
| 确认条件 | 电话会未削弱现金回报预期；开盘回踩守区间中枢或实际VWAP并继续强于SPY，XLE至少不失29日收盘68.71。 |
| 失效条件 | 油价溢价消退且高开低走、跌破开盘低点反抽失败；现金流含一次性项被过度年化。 |
| 观察期限 | 今晚至未来1–3交易日 |
| 反证 | 地缘溢价可迅速消退，上游与炼化的敏感方向不完全相同。 |
| 状态 | 新增观察，不追盘前跳升 |

## 跨期比较与上期剧本复核

相对30日早报：同一29日收盘窗口不制造新日收益。早报盘后末段QQQ704.30/SMH542.10，晚报实际盘前697.75/533.42，均继续低于704.40/546.67警戒；这是跨时段报价对照，不是常规日线收益。金融/医疗仍相对强，但工业转弱，不能维持无条件全面轮动乐观。VRT盘前失守早报236.55警戒，MU/DRAM仍远低于927.24/51.23；旧价格确认尚未完成。新增XOM、CVX、ABBV业绩及AMZN10-Q，前两者今晚电话会仍待。相同规则合约：3501950 0.05%→0.05%（+0.00个百分点）；4641065 77.6%→92.35%（+14.75个百分点）；3215008 71.5%→71.5%（+0.00个百分点）；2176270 11.5%→10.5%（-1.00个百分点）；4951227 34.5%→48%（+13.50个百分点）；2252540 19%→20.5%（+1.50个百分点）；691340 10.2%→9.2%（-1.00个百分点）；4838928 22.5%→22.5%（+0.00个百分点）；5401795 9%→6%（-3.00个百分点）；2413330 94.8%→93.6%（-1.20个百分点）；6280962 87.5%→84.5%（-3.00个百分点）；6280959 90.5%→79%（-11.50个百分点）。停火延续合约与霍尔木兹正常化合约指向不同定义，不能因停火定价高就宣称通航恢复。

## 可计算的跨期变化

```json
[
  {
    "mode": "daily",
    "baseline": "reports/daily/2026-10-29/20261030T002817.049748Z/evidence.json",
    "baseline_cutoff": "2026-10-30T00:28:07.912354+00:00",
    "close_change_pct": {
      "GC=F": 0.2935566822774405,
      "CL=F": -0.8264448096564347,
      "BZ=F": 3.0591154529219677,
      "^VIX": 0.0,
      "^VIX3M": 0.0,
      "^VVIX": 0.0,
      "^MOVE": 0.0016068151146297893
    },
    "quote_change_pct": {
      "AMZN": {
        "change_pct": 0.8329129607504759,
        "from_observed_at": "2026-10-29T23:59:59+00:00",
        "to_observed_at": "2026-10-30T12:01:53+00:00"
      },
      "AVGO": {
        "change_pct": -1.0533225912332411,
        "from_observed_at": "2026-10-29T23:59:30+00:00",
        "to_observed_at": "2026-10-30T12:01:42+00:00"
      },
      "CAT": {
        "change_pct": -1.4798227879966985,
        "from_observed_at": "2026-10-29T23:59:04+00:00",
        "to_observed_at": "2026-10-30T12:00:40+00:00"
      },
      "CEG": {
        "change_pct": -1.1923076923077036,
        "from_observed_at": "2026-10-29T23:55:34+00:00",
        "to_observed_at": "2026-10-30T12:01:50+00:00"
      },
      "DRAM": {
        "change_pct": -1.9621712620425225,
        "from_observed_at": "2026-10-29T23:59:44+00:00",
        "to_observed_at": "2026-10-30T12:01:38+00:00"
      },
      "GEV": {
        "change_pct": -0.825102629760599,
        "from_observed_at": "2026-10-29T23:54:46+00:00",
        "to_observed_at": "2026-10-30T12:01:33+00:00"
      },
      "GLD": {
        "change_pct": -0.9929240272580242,
        "from_observed_at": "2026-10-29T23:58:38+00:00",
        "to_observed_at": "2026-10-30T12:01:15+00:00"
      },
      "GLW": {
        "change_pct": -2.365970976683507,
        "from_observed_at": "2026-10-29T23:59:32+00:00",
        "to_observed_at": "2026-10-30T12:00:53+00:00"
      },
      "GOOGL": {
        "change_pct": 0.12114302002421695,
        "from_observed_at": "2026-10-30T00:00:00+00:00",
        "to_observed_at": "2026-10-30T12:01:50+00:00"
      },
      "INTC": {
        "change_pct": -2.546786785431132,
        "from_observed_at": "2026-10-29T23:59:58+00:00",
        "to_observed_at": "2026-10-30T12:02:01+00:00"
      },
      "IWM": {
        "change_pct": -0.4016913319238813,
        "from_observed_at": "2026-10-29T23:48:23+00:00",
        "to_observed_at": "2026-10-30T12:01:25+00:00"
      },
      "LLY": {
        "change_pct": 1.9316267738507475,
        "from_observed_at": "2026-10-29T23:56:51+00:00",
        "to_observed_at": "2026-10-30T12:00:30+00:00"
      },
      "META": {
        "change_pct": -1.4137117491886286,
        "from_observed_at": "2026-10-29T23:59:58+00:00",
        "to_observed_at": "2026-10-30T12:01:41+00:00"
      },
      "MSFT": {
        "change_pct": -0.626044202451892,
        "from_observed_at": "2026-10-29T23:59:52+00:00",
        "to_observed_at": "2026-10-30T12:01:45+00:00"
      },
      "MU": {
        "change_pct": -2.244389027431426,
        "from_observed_at": "2026-10-29T23:59:47+00:00",
        "to_observed_at": "2026-10-30T12:02:01+00:00"
      },
      "NOW": {
        "change_pct": 1.0839355197331813,
        "from_observed_at": "2026-10-29T23:59:51+00:00",
        "to_observed_at": "2026-10-30T12:00:35+00:00"
      },
      "NVDA": {
        "change_pct": -1.4450850548283434,
        "from_observed_at": "2026-10-29T23:59:57+00:00",
        "to_observed_at": "2026-10-30T12:01:57+00:00"
      },
      "ORCL": {
        "change_pct": -0.33395176252318803,
        "from_observed_at": "2026-10-29T23:59:57+00:00",
        "to_observed_at": "2026-10-30T12:01:42+00:00"
      },
      "QQQ": {
        "change_pct": -0.930001419849491,
        "from_observed_at": "2026-10-29T23:59:58+00:00",
        "to_observed_at": "2026-10-30T12:01:47+00:00"
      },
      "RSP": {
        "change_pct": 0.11058609722853774,
        "from_observed_at": "2026-10-29T23:55:58+00:00",
        "to_observed_at": "2026-10-30T11:55:16+00:00"
      },
      "SMH": {
        "change_pct": -1.6011805939863621,
        "from_observed_at": "2026-10-29T23:59:28+00:00",
        "to_observed_at": "2026-10-30T11:59:20+00:00"
      },
      "SNDK": {
        "change_pct": -5.2670752482879895,
        "from_observed_at": "2026-10-29T23:59:43+00:00",
        "to_observed_at": "2026-10-30T12:01:57+00:00"
      },
      "SPY": {
        "change_pct": -0.4027670620235124,
        "from_observed_at": "2026-10-29T23:58:46+00:00",
        "to_observed_at": "2026-10-30T12:01:53+00:00"
      },
      "STX": {
        "change_pct": -3.6385311572700196,
        "from_observed_at": "2026-10-29T23:59:58+00:00",
        "to_observed_at": "2026-10-30T12:01:22+00:00"
      },
      "TLT": {
        "change_pct": 0.2691790040376896,
        "from_observed_at": "2026-10-29T23:59:47+00:00",
        "to_observed_at": "2026-10-30T12:01:43+00:00"
      },
      "VRT": {
        "change_pct": -1.7885278712259978,
        "from_observed_at": "2026-10-29T23:59:10+00:00",
        "to_observed_at": "2026-10-30T12:01:58+00:00"
      },
      "XLE": {
        "change_pct": 0.7947976878612595,
        "from_observed_at": "2026-10-29T23:58:22+00:00",
        "to_observed_at": "2026-10-30T12:01:04+00:00"
      },
      "XLV": {
        "change_pct": 0.8814305839680125,
        "from_observed_at": "2026-10-29T23:56:59+00:00",
        "to_observed_at": "2026-10-30T12:00:42+00:00"
      }
    },
    "macro_change": {
      "DGS2": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-10-28"
      },
      "BAMLH0A0HYM2": {
        "change": 0.0,
        "unit": "percentage_points",
        "observation_date": "2026-10-28"
      },
      "BAMLC0A0CM": {
        "change": 0.0,
        "unit": "percentage_points",
        "observation_date": "2026-10-28"
      },
      "DGS10": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-10-28"
      },
      "DFII10": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-10-28"
      },
      "T10YIE": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-10-29"
      },
      "STLFSI4": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-23"
      },
      "CBOE_VIX": {
        "change": 0.28999999999999915,
        "unit": "index",
        "observation_date": "2026-10-29"
      },
      "GPRD": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-26"
      },
      "GPRD_ACT": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-26"
      },
      "GPRD_THREAT": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-26"
      },
      "GPRD_MA7": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-26"
      },
      "GPRD_MA30": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-26"
      }
    },
    "event_probability_change": {
      "4641065": {
        "status": "comparable",
        "change_pp": 14.749999999999996
      },
      "3215008": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "3501950": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "2176270": {
        "status": "comparable",
        "change_pp": -1.0000000000000009
      },
      "4951227": {
        "status": "comparable",
        "change_pp": 13.5
      },
      "691340": {
        "status": "comparable",
        "change_pp": -0.9999999999999996
      },
      "2252540": {
        "status": "comparable",
        "change_pp": 1.4999999999999987
      },
      "4838928": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "5401795": {
        "status": "comparable",
        "change_pp": -3.0
      },
      "2413330": {
        "status": "comparable",
        "change_pp": -1.19999999999999
      },
      "6280962": {
        "status": "comparable",
        "change_pp": -3.0000000000000027
      },
      "6280959": {
        "status": "comparable",
        "change_pp": -11.5
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
    "event": "下一常规开盘：核验盘后财报冲击",
    "date": "2026-10-30T09:30:00-04:00",
    "source": "tc:get_trading_calendar"
  },
  {
    "event": "AMD Q3电话会（11月已进入冬令时）",
    "date": "2026-11-03T17:00:00-05:00",
    "source": "https://ir.amd.com/news-events/press-releases/detail/1300/amd-to-report-fiscal-third-quarter-2026-financial-results"
  },
  {
    "event": "Sandisk按8拆1调整交易；不产生额外价值",
    "date": "2026-11-20T09:30:00-05:00",
    "source": "https://investor.sandisk.com/news-releases/news-release-details/sandisk-reports-fiscal-first-quarter-2027-financial-results"
  },
  {
    "event": "10月非农就业报告",
    "date": "2026-11-06T08:30:00-05:00",
    "source": "https://www.bls.gov/schedule/2026/11_sched.htm"
  },
  {
    "event": "10月CPI；官方日程为10日，不是12日",
    "date": "2026-11-10T08:30:00-05:00",
    "source": "https://www.bls.gov/schedule/2026/11_sched.htm"
  },
  {
    "event": "NVIDIA FY2027Q3电话会：8月官方实录预告日期，具体分钟及临近更新待复核",
    "date": "2026-11-17 America/New_York",
    "source": "https://investor.nvidia.com/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf"
  },
  {
    "event": "XOM Q3电话会（官方08:30中央时间）",
    "date": "2026-10-30T09:30:00-04:00",
    "source": "https://investor.exxonmobil.com/news-events/ir-calendar/detail/20261030-3q-2026-earnings-call"
  },
  {
    "event": "CVX Q3电话会",
    "date": "2026-10-30T11:00:00-04:00",
    "source": "https://chevroncorp.gcs-web.com/"
  },
  {
    "event": "ABBV Q3电话会（官方08:00中央时间）",
    "date": "2026-10-30T09:00:00-04:00",
    "source": "https://investors.abbvie.com/upcoming-events"
  }
]
```

## 新闻事件去重与时间

| 事件 | 摘要 | 发生时间（未知留空） | 各来源发布时间 / 抓取时间 |
| --- | --- | --- | --- |
| bea-gdp-q3-advance | Q3实际GDP年化环比3.4%；强增长与月度通胀分别解释。 | 2026-10-29T08:30:00-04:00 | [{"source": "https://www.bea.gov/news/2026/gdp-advance-estimate-3rd-quarter-2026", "published_at": "2026-10-29T08:30:00-04:00", "retrieved_at": "2026-10-30T00:28:00.796032+00:00"}] |
| bea-pce-september | 9月PCE同比3.6%、核心3.1%，实际消费环比接近零。 | 2026-10-29T08:30:00-04:00 | [{"source": "https://www.bea.gov/news/2026/personal-income-and-outlays-september-2026", "published_at": "2026-10-29T08:30:00-04:00", "retrieved_at": "2026-10-30T00:28:00.796032+00:00"}] |
| amzn-q326 | 盘后AWS增长强但TTM现金支出压力大；现金FCF负值不是单季数。 | 缺失 | [{"source": "https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Third-Quarter-Results/default.aspx", "published_at": null, "retrieved_at": "2026-10-30T00:28:00.796032+00:00"}] |
| sndk-fy27q1 | 盘后业绩及Q2指引增长；宣布8拆1，11月20日调整交易。 | 2026-10-29T16:05:00-04:00 | [{"source": "https://investor.sandisk.com/news-releases/news-release-details/sandisk-reports-fiscal-first-quarter-2027-financial-results", "published_at": "2026-10-29T16:05:00-04:00", "retrieved_at": "2026-10-30T00:28:00.796032+00:00"}] |
| intc-q326 | Q4收入指引150–160亿美元；PC弱与数据中心供给约束并存。 | 缺失 | [{"source": "https://www.intc.com/filings-reports/all-sec-filings/content/0000050863-26-000188/q326earningsrelease.htm", "published_at": null, "retrieved_at": "2026-10-30T00:28:00.796032+00:00"}] |
| nvda-nscale-credit-talks | Reuters转述The Information谈判消息且未独立确认，不作已成交担保或负债。 | 缺失 | [{"source": "https://www.boursorama.com/bourse/actualites/selon-information-nvidia-serait-en-pourparlers-pour-apporter-un-soutien-financier-a-l-accord-conclu-entre-nscale-et-anthropic-2f2a778a7b8f5d0b9e87ab8c7f3c9978", "published_at": null, "retrieved_at": "2026-10-30T00:28:00.796032+00:00"}] |
| saudi-houthi-claim | AP转述胡塞声称袭击油设施，实际供应损失未独立确认。 | 缺失 | [{"source": "https://apnews.com/article/c11dac838a072af25ba8d0eb81d01035", "published_at": null, "retrieved_at": "2026-10-30T00:28:00.796032+00:00"}] |
| amzn-10q-20261030 | SEC新增Q3 10-Q；现金FCF与融资租赁仍须桥接，旧Q2估值不可复用。 | 缺失 | [{"source": "https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm", "published_at": null, "retrieved_at": "2026-10-30T12:08:37.599365+00:00"}] |
| xom-q326 | Q3调整EPS4.23，经营现金257亿美元、公司FCF191亿；不等于所有油企同质受益。 | 缺失 | [{"source": "https://investor.exxonmobil.com/company-information/press-releases/detail/1213/exxonmobil-announces-third-quarter-2026-results", "published_at": null, "retrieved_at": "2026-10-30T12:08:37.599365+00:00"}] |
| abbv-q326 | Q3收入174.04亿美元、调整EPS3.82，全年调整EPS指引上调至13.95–13.99。 | 缺失 | [{"source": "https://www.sec.gov/Archives/edgar/data/1551152/000155115226000033/abbv-20260930xexhibit991.htm", "published_at": null, "retrieved_at": "2026-10-30T12:08:37.599365+00:00"}] |
| cvx-q326 | Q3调整EPS5.28、经营现金160亿美元、公司FCF120亿；调整FCF含TCO还贷及出售资产影响。 | 2026-10-30T05:15:00-05:00 | [{"source": "https://www.sec.gov/Archives/edgar/data/93410/000009341026000196/a09302026ex9918-k.htm", "published_at": "2026-10-30T05:15:00-05:00", "retrieved_at": "2026-10-30T12:08:48.737544+00:00"}] |

## 覆盖范围与数据缺口

```json
[
  "CNN418；CME官方概率矩阵访问失败，不采用tc温度或加密指数替代。",
  "没有30日常规开盘区间/VWAP、全市场成分广度；盘前ETF成交稀疏，各标的时点不同。",
  "FRED信用/多数利率至28日，GPR26日、金融压力23日；滞后值不能确认最新冲击后的风险。",
  "期货日线和分钟具体合约月未对齐，Brent两者基准显著不同；只展示原始时点和水平，不算跨期收益或称油价统一上涨。",
  "19ETF当期申赎/精确份额和拆分桥缺失；ICI至21日，VanEck本次访问超时；不能把相对上涨当资金净流入。",
  "MSFT/AMZN/GOOGL/META新财报后的完整TTM与FCFF桥未齐，暂停精确估值。",
  "军情、Nscale信用担保讨论、微软最终债券条款未完整独立核验；不用社媒断言已发生事件。",
  "tc高影响和焦点两次查询均限50条；Polymarket多组查询截断，低流动性/宽价差合约仅作线索。",
  "H100标题7D与日期表不一致，仅采用日期表29日2.90及手算同口径变化。",
  "原始采集存在请求失败，见采集质量记录",
  "MSFT 估值: 已发现新季度披露；必要TTM、融资租赁及优先权益/稀释桥未完成，暂停旧底稿估值和价格反推。",
  "AMZN 估值: 30日新增Q3 10-Q已核验；最新TTM、融资租赁/净债务与稀释桥尚未完整，不沿用旧估值。",
  "GOOGL 估值: 已发现新季度披露；必要TTM、融资租赁及优先权益/稀释桥未完成，暂停旧底稿估值和价格反推。",
  "META 估值: 22日10-Q已核验，本次无新增定期财报。27日普通股625美元定价、优先票息6.5%已核验；完整融资租赁负债/新增资产、优先权益/远期发行与现金到账桥未齐，不用不同承诺简单充当现有债务，暂停精确FCFF反推。",
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
  "tc 报价质量 stale: IGV, ILMN, NXPI, XLF, XLI；不作为新成交证据",
  "history.DRAM: insufficient_history",
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
  "指标缺失/历史不足: prices.^VIX.volume_vs_previous20_ratio, prices.^VIX3M.volume_vs_previous20_ratio, prices.^VVIX.volume_vs_previous20_ratio, prices.^MOVE.volume_vs_previous20_ratio, prices.DRAM.sma200, prices.DRAM.distance_sma200_pct, quotes.IGV.value, quotes.ILMN.value, quotes.NXPI.value, quotes.XLF.value, quotes.XLI.value"
]
```

## 来源、时间与核验记录

```json
[
  {
    "url": "https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Third-Quarter-Results/default.aspx",
    "checked_at": "2026-10-30T00:28:00.796032+00:00",
    "note": "29日新业绩；公司TTM FCF口径"
  },
  {
    "url": "https://investor.sandisk.com/news-releases/news-release-details/sandisk-reports-fiscal-first-quarter-2027-financial-results",
    "checked_at": "2026-10-30T00:28:00.796032+00:00",
    "note": "29日16:05EDT财报及拆分"
  },
  {
    "url": "https://www.intc.com/filings-reports/all-sec-filings/content/0000050863-26-000188/q326earningsrelease.htm",
    "checked_at": "2026-10-30T00:28:00.796032+00:00",
    "note": "Q3官方SEC附件"
  },
  {
    "url": "https://www.bea.gov/news/2026/personal-income-and-outlays-september-2026",
    "checked_at": "2026-10-30T00:28:00.796032+00:00",
    "note": "29日08:30EDT月度数据"
  },
  {
    "url": "https://www.bea.gov/news/2026/gdp-advance-estimate-3rd-quarter-2026",
    "checked_at": "2026-10-30T00:28:00.796032+00:00",
    "note": "29日08:30EDT季度年化数据"
  },
  {
    "url": "https://ir.amd.com/news-events/press-releases/detail/1300/amd-to-report-fiscal-third-quarter-2026-financial-results",
    "checked_at": "2026-10-30T00:28:00.796032+00:00",
    "note": "11月3日17:00ET，冬令时"
  },
  {
    "url": "https://investors.palantir.com/news-details/2026/Palantir-Announces-Date-of-Third-Quarter-2026-Earnings-Release-and-Webcast/",
    "checked_at": "2026-10-30T00:28:00.796032+00:00",
    "note": "官方搜索结果确认11月2日盘后，正文动态无精确分钟"
  },
  {
    "url": "https://www.ici.org/research/stats/etf_flows",
    "checked_at": "2026-10-30T00:28:00.796032+00:00",
    "note": "27日发布截至21日；滞后汇总"
  },
  {
    "url": "https://www.silicondata.com/products/silicon-index/h100",
    "checked_at": "2026-10-30T00:28:00.796032+00:00",
    "note": "带日期29日2.90，与28日相同"
  },
  {
    "url": "https://www.boursorama.com/bourse/actualites/selon-information-nvidia-serait-en-pourparlers-pour-apporter-un-soutien-financier-a-l-accord-conclu-entre-nscale-et-anthropic-2f2a778a7b8f5d0b9e87ab8c7f3c9978",
    "checked_at": "2026-10-30T00:28:00.796032+00:00",
    "note": "Reuters转述且未独立核验"
  },
  {
    "url": "https://apnews.com/article/c11dac838a072af25ba8d0eb81d01035",
    "checked_at": "2026-10-30T00:28:00.796032+00:00",
    "note": "胡塞声称，供应损失未核验"
  },
  {
    "url": "https://www.cmegroup.com/fedwatch",
    "checked_at": "2026-10-30T00:28:00.796032+00:00",
    "note": "页面可读，矩阵失败"
  },
  {
    "url": "https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm",
    "checked_at": "2026-10-30T12:08:37.599365+00:00",
    "note": "30日SEC新10-Q全文核验"
  },
  {
    "url": "https://investor.exxonmobil.com/company-information/press-releases/detail/1213/exxonmobil-announces-third-quarter-2026-results",
    "checked_at": "2026-10-30T12:08:37.599365+00:00",
    "note": "30日新官方业绩"
  },
  {
    "url": "https://www.sec.gov/Archives/edgar/data/93410/000009341026000196/cvx-20261030.htm",
    "checked_at": "2026-10-30T12:08:37.599365+00:00",
    "note": "30日SEC8-K，业绩附件另核验"
  },
  {
    "url": "https://www.sec.gov/Archives/edgar/data/1551152/000155115226000033/abbv-20260930xexhibit991.htm",
    "checked_at": "2026-10-30T12:08:37.599365+00:00",
    "note": "30日SEC官方业绩附件"
  },
  {
    "url": "https://www.ici.org/research/stats/etf_flows",
    "checked_at": "2026-10-30T12:08:37.599365+00:00",
    "note": "本次复核仍27日发布至21日"
  },
  {
    "url": "https://www.silicondata.com/products/silicon-index/h100",
    "checked_at": "2026-10-30T12:08:37.599365+00:00",
    "note": "29日日期表2.90，标题周变动冲突"
  },
  {
    "url": "https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool",
    "checked_at": "2026-10-30T12:08:37.599365+00:00",
    "note": "矩阵null referrer错误，概率缺失"
  },
  {
    "url": "https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/",
    "checked_at": "2026-10-30T12:08:37.599365+00:00",
    "note": "本次超时，不引用为当期数据"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AMD",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AMZN",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AVGO",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CAT",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CEG",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CVX",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/DRAM",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GEV",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GLD",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GLW",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GOOGL",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/IGV",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/ILMN",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/INTC",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/IWM",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/LLY",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/META",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/MSFT",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/MU",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NOW",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NVDA",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NXPI",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/ORCL",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/PLTR",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/QQQ",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/RSP",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SMH",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SNDK",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SPY",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/STX",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/TLT",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/VRT",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLE",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLF",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLI",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLV",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XOM",
    "checked_at": "2026-10-30T12:02:05.989582+00:00",
    "note": "30日盘前分钟；独立实际成交时戳，稀疏行情可能滞后"
  },
  {
    "url": "https://www.sec.gov/Archives/edgar/data/93410/000009341026000196/a09302026ex9918-k.htm",
    "checked_at": "2026-10-30T12:08:48.737544+00:00",
    "note": "官方Q3业绩附件，发布05:15中央夏令时间；现金流非同质"
  }
]
```

## 付费信源建议（未订阅）

```json
[]
```
