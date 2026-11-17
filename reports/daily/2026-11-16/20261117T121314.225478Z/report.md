# 每日交易总结 · 2026-11-16

## 一分钟读懂 · Agent 摘要

### 当前判断

当前是弱势市场中的盘前修复，尚不足以确认可靠反弹；继续以条件观察为主。

### 与上次相比

早报后新增NVDA合规监督委员会公告；CNN已从缺失恢复为31/恐惧。12:00 UTC附近芯片回升，但宽基仍低于早报修复区，伊朗停火合约回落、Anthropic较低估值档继续升温。

### 最重要的信号

- SPY约741.23、QQQ665.43、SMH468.96，尚低于747.89、671.71、473.33的首道观察位。
- NVDA158.08、MU734.40盘前反抽；涨幅不是常规时段回踩承接证据。
- VIX盘前22.49较昨收回落，原油反弹；信用数据仍滞后，不能据此判断风险已解除。

### 接下来观察

- 北京21:30零售与进口价格、22:15工业生产；观察数据后股债是否同步稳定。
- 开盘后先看关键区收复、回踩不破及RSP/IWM跟随，再考虑升级反弹判断。
- 北京18日05:20左右NVDA结果、06:00电话会；财报后次日收盘比第一跳更有参考价值。

### 不要忽略

盘前成交稀疏、报价时点不同；没有常规VWAP/回踩证据，当期ETF净申赎与四家公司完整估值仍缺。

## 研究结论

17日晚间：芯片盘前反抽，宽基仍弱，反弹尚待确认。NVIDIA新增出口合规监督委员会是治理措施，不能替代今晚财报的订单、回款与指引验证。CNN为31/恐惧；先看21:30零售和进口价格，再看常规时段承接与盘后NVDA结果。

## 时点与口径

| 项目 | 内容 |
| --- | --- |
| 模式 | 每日交易总结 |
| 常规交易窗口 | 2026-11-16 → 2026-11-16（纽约交易日） |
| 截止·纽约 | 2026-11-17T07:12:36.377324-05:00 |
| 截止·北京 | 2026-11-17T20:12:36.377324+08:00 |
| 实际生成时间 | 2026-11-17T12:12:36.879722+00:00 |
| 市场阶段 | 盘前 |
| 下一交易日 | 2026-11-17 |
| 运行重点 | 全市场 |
| 上一版本 | reports/daily/2026-11-16/20261117T041705.970365Z/evidence.json |
| 质量 | partial |
| Daily 北京时间计划时段 | 2026-11-17T20:00:00+08:00 |

## 采集、补查与剩余缺口

| 目标 | 补查结果 | 来源 | 观测 / 抓取时间 | 说明 |
| --- | --- | --- | --- | --- |
| 1219851 | 已校验接入 | https://gamma-api.polymarket.com/events/1219851 | 2026-11-17T12:00:02.054151+00:00 / 2026-11-17T12:00:02.054151+00:00 | Gamma snapshot; metadata update is not last trade time |
| 1360126 | 已校验接入 | https://gamma-api.polymarket.com/events/1360126 | 2026-11-17T12:00:02.856627+00:00 / 2026-11-17T12:00:02.856627+00:00 | Gamma snapshot; metadata update is not last trade time |
| 478472 | 已校验接入 | https://gamma-api.polymarket.com/events/478472 | 2026-11-17T12:00:02.856627+00:00 / 2026-11-17T12:00:02.856627+00:00 | Gamma snapshot; metadata update is not last trade time |
| QQQ | 已校验接入 | https://query1.finance.yahoo.com/v8/finance/chart/QQQ | 2026-11-16T16:00:00-05:00 / 2026-11-17T12:08:21.472857+00:00 | yahoo_auto_adjust_ohlc_v1 |
| NVDA | 已校验接入 | https://query1.finance.yahoo.com/v8/finance/chart/NVDA | 2026-11-16T16:00:00-05:00 / 2026-11-17T12:08:21.094584+00:00 | yahoo_auto_adjust_ohlc_v1 |
| VRT | 已校验接入 | https://query1.finance.yahoo.com/v8/finance/chart/VRT | 2026-11-16T16:00:00-05:00 / 2026-11-17T12:08:20.830320+00:00 | yahoo_auto_adjust_ohlc_v1 |
| IGV | 已校验接入 | https://query1.finance.yahoo.com/v8/finance/chart/IGV | 2026-11-16T16:00:00-05:00 / 2026-11-17T12:08:21.513953+00:00 | yahoo_auto_adjust_ohlc_v1 |
| KRE | 已校验接入 | https://query1.finance.yahoo.com/v8/finance/chart/KRE | 2026-11-16T16:00:00-05:00 / 2026-11-17T12:04:19.043312+00:00 | yahoo_auto_adjust_ohlc_v1 |

## 仍需核验的数据与影响

| 数据 | 状态 | 需要核验 | 影响 |
| --- | --- | --- | --- |
| history.DRAM | insufficient_history | 连续完整交易日 OHLC；SMA200 至少200条，ATR14至少15条 | 降低相关判断可信度；保留缺口 |
| polymarket.query.AI bubble | truncated | 按主题或事件ID补查；不能声称全市场覆盖 | 降低相关判断可信度；保留缺口 |
| polymarket.query.CPI | truncated | 按主题或事件ID补查；不能声称全市场覆盖 | 降低相关判断可信度；保留缺口 |
| polymarket.query.Fed rate | truncated | 按主题或事件ID补查；不能声称全市场覆盖 | 降低相关判断可信度；保留缺口 |
| polymarket.query.Hormuz | truncated | 按主题或事件ID补查；不能声称全市场覆盖 | 降低相关判断可信度；保留缺口 |
| polymarket.query.Iran | truncated | 按主题或事件ID补查；不能声称全市场覆盖 | 降低相关判断可信度；保留缺口 |
| polymarket.query.Microsoft | truncated | 按主题或事件ID补查；不能声称全市场覆盖 | 降低相关判断可信度；保留缺口 |
| polymarket.query.Nvidia | truncated | 按主题或事件ID补查；不能声称全市场覆盖 | 降低相关判断可信度；保留缺口 |
| polymarket.query.SpaceX | truncated | 按主题或事件ID补查；不能声称全市场覆盖 | 降低相关判断可信度；保留缺口 |
| polymarket.query.bank | truncated | 按主题或事件ID补查；不能声称全市场覆盖 | 降低相关判断可信度；保留缺口 |
| polymarket.query.inflation | truncated | 按主题或事件ID补查；不能声称全市场覆盖 | 降低相关判断可信度；保留缺口 |
| cnn | missing | 核验 CNN Fear & Greed 原值及更新时间 | 降低相关判断可信度；保留缺口 |
| request.9572e2289a18 | request_failed | 核验该来源失败影响，见本地原始错误 | 降低相关判断可信度；保留缺口 |
| request.bd27b9ca2062 | request_failed | 核验该来源失败影响，见本地原始错误 | 降低相关判断可信度；保留缺口 |
| request.fde2888814e2 | request_failed | 核验该来源失败影响，见本地原始错误 | 降低相关判断可信度；保留缺口 |
| request.fd24b1315edc | request_failed | 核验该来源失败影响，见本地原始错误 | 降低相关判断可信度；保留缺口 |
| request.c5d45ab239a3 | request_failed | 核验该来源失败影响，见本地原始错误 | 降低相关判断可信度；保留缺口 |
| request.c5498122be43 | request_failed | 核验该来源失败影响，见本地原始错误 | 降低相关判断可信度；保留缺口 |
| request.7a9f2148a1a7 | request_failed | 核验该来源失败影响，见本地原始错误 | 降低相关判断可信度；保留缺口 |
| request.38906ddc2d63 | request_failed | 核验该来源失败影响，见本地原始错误 | 降低相关判断可信度；保留缺口 |

## 决策指标：趋势、相对强弱、波动与宏观

| ID | 数值 | 单位 | 观测日/时间 | 质量 | 定义 | 来源 |
| --- | --- | --- | --- | --- | --- | --- |
| prices.SPY.value | 739.95 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_1d_pct | -1.91 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_5d_pct | -1.69 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_20d_pct | -3.46 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_60d_pct | -3.13 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_1d_pp | 0.00 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_5d_pp | 0.00 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma20 | 757.69 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma50 | 763.52 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma200 | 729.58 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma20_pct | -2.34 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma50_pct | -3.09 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma200_pct | 1.42 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_sma | 13.51 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_pct | 1.83 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.drawdown_from_63d_high_pct | -5.02 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.volume_vs_previous20_ratio | 1.47 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SPY/history/ |
| prices.IWM.value | 272.94 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_1d_pct | -1.66 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_5d_pct | -3.39 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_20d_pct | 0.61 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_60d_pct | -8.77 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_1d_pp | 0.25 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_5d_pp | -1.69 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma20 | 278.46 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma50 | 280.23 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma200 | 278.55 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma20_pct | -1.98 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma50_pct | -2.60 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma200_pct | -2.01 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_sma | 5.61 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_pct | 2.06 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.drawdown_from_63d_high_pct | -9.30 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.volume_vs_previous20_ratio | 1.10 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IWM/history/ |
| prices.RSP.value | 218.93 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_1d_pct | -1.01 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_5d_pct | -0.91 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_20d_pct | 2.59 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_60d_pct | -0.86 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_1d_pp | 0.90 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_5d_pp | 0.78 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma20 | 218.93 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma50 | 214.84 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma200 | 207.83 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma20_pct | -0.00 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma50_pct | 1.91 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma200_pct | 5.34 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_sma | 3.13 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_pct | 1.43 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.drawdown_from_63d_high_pct | -1.97 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.volume_vs_previous20_ratio | 0.98 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/RSP/history/ |
| prices.GLD.value | 352.93 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_1d_pct | -0.71 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_5d_pct | -7.01 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_20d_pct | -7.05 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_60d_pct | -16.64 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_1d_pp | 1.20 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_5d_pp | -5.32 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma20 | 367.45 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma50 | 379.83 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma200 | 407.96 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma20_pct | -3.95 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma50_pct | -7.08 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma200_pct | -13.49 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_sma | 7.57 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_pct | 2.14 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.drawdown_from_63d_high_pct | -17.55 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.volume_vs_previous20_ratio | 1.04 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GC=F.value | 3,853.00 | USD_per_troy_ounce | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_1d_pct | -0.86 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_5d_pct | -6.36 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_20d_pct | -7.38 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_60d_pct | -17.68 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_1d_pp | 1.05 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_5d_pp | -4.66 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma20 | 4,019.85 | USD_per_troy_ounce | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma50 | 4,169.04 | USD_per_troy_ounce | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma200 | 4,467.78 | USD_per_troy_ounce | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma20_pct | -4.15 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma50_pct | -7.58 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma200_pct | -13.76 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_sma | 97.64 | USD_per_troy_ounce | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_pct | 2.53 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.drawdown_from_63d_high_pct | -17.98 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.volume_vs_previous20_ratio | 0.89 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.CL=F.value | 85.72 | USD_per_barrel | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_1d_pct | -3.21 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_5d_pct | -1.30 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_20d_pct | -17.31 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_60d_pct | -1.54 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_1d_pp | -1.30 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_5d_pp | 0.39 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma20 | 94.83 | USD_per_barrel | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma50 | 95.25 | USD_per_barrel | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma200 | 87.88 | USD_per_barrel | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma20_pct | -9.61 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma50_pct | -10.01 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma200_pct | -2.46 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_sma | 4.65 | USD_per_barrel | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_pct | 5.42 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.drawdown_from_63d_high_pct | -19.00 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.volume_vs_previous20_ratio | 0.67 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.BZ=F.value | 92.44 | USD_per_barrel | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_1d_pct | -3.55 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_5d_pct | -0.14 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_20d_pct | -15.62 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_60d_pct | -2.07 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_1d_pp | -1.64 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_5d_pp | 1.55 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma20 | 104.28 | USD_per_barrel | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma50 | 104.18 | USD_per_barrel | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma200 | 94.10 | USD_per_barrel | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma20_pct | -11.35 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma50_pct | -11.27 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma200_pct | -1.77 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_sma | 5.62 | USD_per_barrel | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_pct | 6.08 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.drawdown_from_63d_high_pct | -21.42 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.volume_vs_previous20_ratio | 0.65 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.TLT.value | 79.38 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_1d_pct | 0.00 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_5d_pct | -3.15 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_20d_pct | 0.32 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_60d_pct | -2.08 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_1d_pp | 1.91 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_5d_pp | -1.46 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma20 | 80.94 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma50 | 79.78 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma200 | 82.69 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma20_pct | -1.92 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma50_pct | -0.50 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma200_pct | -4.01 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_sma | 0.78 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_pct | 0.98 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.drawdown_from_63d_high_pct | -3.75 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.volume_vs_previous20_ratio | 0.86 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/TLT/history/ |
| prices.UUP.value | 29.56 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_1d_pct | 0.20 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_5d_pct | 2.04 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_20d_pct | 1.93 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_60d_pct | 5.95 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_1d_pp | 2.11 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_5d_pp | 3.73 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma20 | 29.09 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma50 | 28.83 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma200 | 28.05 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma20_pct | 1.62 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma50_pct | 2.53 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma200_pct | 5.40 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_sma | 0.13 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_pct | 0.45 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.drawdown_from_63d_high_pct | 0.00 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.volume_vs_previous20_ratio | 1.31 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/UUP/history/ |
| prices.HYG.value | 76.73 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_1d_pct | -0.27 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_5d_pct | -1.01 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_20d_pct | 0.39 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_60d_pct | -2.15 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_1d_pp | 1.64 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_5d_pp | 0.69 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma20 | 77.02 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma50 | 77.10 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma200 | 77.49 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma20_pct | -0.37 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma50_pct | -0.49 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma200_pct | -0.98 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_sma | 0.31 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_pct | 0.41 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.drawdown_from_63d_high_pct | -2.53 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.volume_vs_previous20_ratio | 0.55 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/HYG/history/ |
| prices.LQD.value | 102.80 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_1d_pct | -0.01 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_5d_pct | -1.79 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_20d_pct | 0.31 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_60d_pct | -1.74 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_1d_pp | 1.90 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_5d_pp | -0.09 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma20 | 103.71 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma50 | 103.14 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma200 | 105.30 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma20_pct | -0.87 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma50_pct | -0.33 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma200_pct | -2.37 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_sma | 0.57 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_pct | 0.55 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.drawdown_from_63d_high_pct | -2.61 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.volume_vs_previous20_ratio | 0.64 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/LQD/history/ |
| prices.^VIX.value | 22.91 | index | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_1d_pct | 18.70 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_5d_pct | 15.01 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_20d_pct | 24.24 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_60d_pct | 44.54 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_1d_pp | 20.62 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_5d_pp | 16.70 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma20 | 19.61 | index | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma50 | 17.47 | index | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma200 | 18.48 | index | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma20_pct | 16.86 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma50_pct | 31.17 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma200_pct | 23.99 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_sma | 4.03 | index | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_pct | 17.59 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.drawdown_from_63d_high_pct | -18.70 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX3M.value | 23.02 | index | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_1d_pct | 11.64 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_5d_pct | 10.41 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_20d_pct | 17.45 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_60d_pct | 24.43 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_1d_pp | 13.55 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_5d_pp | 12.10 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma20 | 20.67 | index | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma50 | 19.36 | index | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma200 | 20.62 | index | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma20_pct | 11.36 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma50_pct | 18.89 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma200_pct | 11.63 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_sma | 2.32 | index | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_pct | 10.06 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.drawdown_from_63d_high_pct | -9.90 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VVIX.value | 114.23 | index | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_1d_pct | 12.51 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_5d_pct | 16.05 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_20d_pct | 6.83 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_60d_pct | 32.41 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_1d_pp | 14.42 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_5d_pp | 17.74 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma20 | 103.72 | index | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma50 | 95.92 | index | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma200 | 98.96 | index | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma20_pct | 10.13 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma50_pct | 19.09 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma200_pct | 15.43 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_sma | 15.62 | index | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_pct | 13.68 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.drawdown_from_63d_high_pct | -15.38 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^MOVE.value | 101.28 | index | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_1d_pct | 2.52 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_5d_pct | 9.17 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_20d_pct | 0.18 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_60d_pct | 42.13 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_1d_pp | 4.43 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_5d_pp | 8.54 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma20 | 97.96 | index | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma50 | 94.88 | index | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma200 | 79.45 | index | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma20_pct | 3.39 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma50_pct | 6.75 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma200_pct | 27.48 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_sma | 5.13 | index | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_pct | 5.07 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.drawdown_from_63d_high_pct | -10.85 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.MSFT.value | 517.99 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_1d_pct | -1.12 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_5d_pct | -4.99 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_20d_pct | -2.91 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_60d_pct | 7.19 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_1d_pp | 0.79 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_5d_pp | -3.29 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma20 | 528.61 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma50 | 519.36 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma200 | 440.94 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma20_pct | -2.01 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma50_pct | -0.26 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma200_pct | 17.47 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_sma | 17.89 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_pct | 3.45 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.drawdown_from_63d_high_pct | -6.80 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.volume_vs_previous20_ratio | 1.15 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.AMZN.value | 257.75 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_1d_pct | -3.34 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_5d_pct | -3.44 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_20d_pct | -1.79 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_60d_pct | -0.34 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_1d_pp | -1.43 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_5d_pp | -1.75 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma20 | 257.10 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma50 | 254.80 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma200 | 244.69 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma20_pct | 0.25 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma50_pct | 1.16 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma200_pct | 5.34 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_sma | 11.03 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_pct | 4.28 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.drawdown_from_63d_high_pct | -4.84 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.volume_vs_previous20_ratio | 0.96 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.GOOGL.value | 283.72 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_1d_pct | -4.07 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_5d_pct | -1.54 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_20d_pct | -17.57 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_60d_pct | -17.67 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_1d_pp | -2.16 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_5d_pp | 0.16 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma20 | 300.39 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma50 | 327.09 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma200 | 337.93 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma20_pct | -5.55 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma50_pct | -13.26 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma200_pct | -16.04 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_sma | 12.32 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_pct | 4.34 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.drawdown_from_63d_high_pct | -20.07 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.volume_vs_previous20_ratio | 0.85 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.META.value | 626.41 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_1d_pct | -2.38 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_5d_pct | -2.33 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_20d_pct | -11.20 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_60d_pct | 14.00 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_1d_pp | -0.47 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_5d_pp | -0.64 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma20 | 633.11 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma50 | 679.91 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma200 | 629.58 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma20_pct | -1.06 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma50_pct | -7.87 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma200_pct | -0.50 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_sma | 21.69 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_pct | 3.46 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.drawdown_from_63d_high_pct | -19.44 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.volume_vs_previous20_ratio | 0.49 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/META/history/ |
| prices.CRWV.value | 49.88 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_1d_pct | -6.12 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_5d_pct | 1.84 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_20d_pct | -18.39 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_60d_pct | -43.22 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_1d_pp | -4.21 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_5d_pp | 3.53 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma20 | 54.43 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma50 | 71.81 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma200 | 88.77 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma20_pct | -8.35 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma50_pct | -30.54 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma200_pct | -43.81 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_sma | 6.42 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_pct | 12.88 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.drawdown_from_63d_high_pct | -50.04 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.volume_vs_previous20_ratio | 0.72 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.MU.value | 719.02 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_1d_pct | -7.62 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_5d_pct | -1.93 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_20d_pct | -20.54 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_60d_pct | -25.62 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_1d_pp | -5.71 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_5d_pp | -0.23 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma20 | 828.71 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma50 | 937.74 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma200 | 766.94 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma20_pct | -13.24 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma50_pct | -23.32 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma200_pct | -6.25 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_sma | 66.99 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_pct | 9.32 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.drawdown_from_63d_high_pct | -34.47 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.volume_vs_previous20_ratio | 0.87 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MU/history/ |
| prices.DRAM.value | 39.27 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_1d_pct | -7.38 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_5d_pct | -6.01 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_20d_pct | -18.75 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_60d_pct | -31.92 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_1d_pp | -5.47 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_5d_pp | -4.32 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma20 | 45.52 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma50 | 52.90 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma200 | 缺失 | USD_per_share | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma20_pct | -13.72 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma50_pct | -25.77 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma200_pct | 缺失 | percent | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_sma | 3.61 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_pct | 9.20 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.drawdown_from_63d_high_pct | -38.27 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.volume_vs_previous20_ratio | 0.92 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.XLK.value | 164.76 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_1d_pct | -3.24 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_5d_pct | -3.58 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_20d_pct | -11.40 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_60d_pct | -10.01 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_1d_pp | -1.33 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_5d_pp | -1.89 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma20 | 177.60 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma50 | 186.61 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma200 | 170.65 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma20_pct | -7.23 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma50_pct | -11.71 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma200_pct | -3.45 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_sma | 6.43 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_pct | 3.90 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.drawdown_from_63d_high_pct | -18.44 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.volume_vs_previous20_ratio | 1.05 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLE.value | 63.69 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_1d_pct | -1.96 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_5d_pct | 2.83 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_20d_pct | -6.06 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_60d_pct | 0.67 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_1d_pp | -0.04 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_5d_pp | 4.52 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma20 | 65.96 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma50 | 64.91 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma200 | 59.01 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma20_pct | -3.45 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma50_pct | -1.88 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma200_pct | 7.93 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_sma | 1.70 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_pct | 2.66 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.drawdown_from_63d_high_pct | -9.04 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.volume_vs_previous20_ratio | 0.86 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLF.value | 58.18 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_1d_pct | -0.85 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_5d_pct | 0.33 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_20d_pct | 5.67 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_60d_pct | 1.58 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_1d_pp | 1.06 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_5d_pp | 2.02 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma20 | 57.22 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma50 | 55.93 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma200 | 53.69 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma20_pct | 1.68 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma50_pct | 4.02 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma200_pct | 8.36 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_sma | 1.04 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_pct | 1.78 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.drawdown_from_63d_high_pct | -1.72 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.volume_vs_previous20_ratio | 1.17 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLI.value | 165.66 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_1d_pct | -1.85 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_5d_pct | -1.91 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_20d_pct | -0.61 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_60d_pct | -7.85 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_1d_pp | 0.06 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_5d_pp | -0.22 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma20 | 167.77 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma50 | 168.68 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma200 | 172.80 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma20_pct | -1.26 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma50_pct | -1.79 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma200_pct | -4.13 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_sma | 3.54 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_pct | 2.13 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.drawdown_from_63d_high_pct | -8.71 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.volume_vs_previous20_ratio | 1.04 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLV.value | 187.88 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_1d_pct | -0.51 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_5d_pct | -0.24 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_20d_pct | 6.96 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_60d_pct | 8.01 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_1d_pp | 1.40 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_5d_pp | 1.45 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma20 | 184.26 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma50 | 175.26 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma200 | 159.48 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma20_pct | 1.97 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma50_pct | 7.20 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma200_pct | 17.81 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_sma | 3.83 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_pct | 2.04 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.drawdown_from_63d_high_pct | -0.94 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.volume_vs_previous20_ratio | 0.87 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLP.value | 92.60 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_1d_pct | 0.27 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_5d_pct | 1.88 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_20d_pct | 6.18 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_60d_pct | 8.40 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_1d_pp | 2.18 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_5d_pp | 3.57 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma20 | 89.75 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma50 | 85.71 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma200 | 84.13 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma20_pct | 3.17 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma50_pct | 8.04 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma200_pct | 10.06 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_sma | 1.66 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_pct | 1.79 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.drawdown_from_63d_high_pct | 0.00 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.volume_vs_previous20_ratio | 1.01 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLY.value | 118.15 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_1d_pct | -1.53 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_5d_pct | -2.36 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_20d_pct | 3.22 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_60d_pct | 0.33 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_1d_pp | 0.39 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_5d_pp | -0.67 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma20 | 117.52 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma50 | 113.85 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma200 | 115.07 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma20_pct | 0.53 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma50_pct | 3.78 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma200_pct | 2.67 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_sma | 2.63 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_pct | 2.23 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.drawdown_from_63d_high_pct | -3.42 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.volume_vs_previous20_ratio | 0.98 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLC.value | 106.82 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_1d_pct | -1.72 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_5d_pct | -0.50 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_20d_pct | -2.97 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_60d_pct | -3.80 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_1d_pp | 0.19 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_5d_pp | 1.19 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma20 | 105.32 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma50 | 109.22 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma200 | 111.80 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma20_pct | 1.43 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma50_pct | -2.19 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma200_pct | -4.45 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_sma | 2.29 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_pct | 2.14 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.drawdown_from_63d_high_pct | -6.91 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.volume_vs_previous20_ratio | 0.78 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLU.value | 44.12 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_1d_pct | 0.18 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_5d_pct | 0.75 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_20d_pct | 6.67 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_60d_pct | 3.91 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_1d_pp | 2.09 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_5d_pp | 2.45 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma20 | 43.21 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma50 | 41.86 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma200 | 43.88 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma20_pct | 2.10 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma50_pct | 5.40 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma200_pct | 0.54 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_sma | 0.60 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_pct | 1.37 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.drawdown_from_63d_high_pct | 0.00 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.volume_vs_previous20_ratio | 0.73 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLRE.value | 44.25 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_1d_pct | -0.27 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_5d_pct | -0.87 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_20d_pct | 6.19 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_60d_pct | -1.01 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_1d_pp | 1.64 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_5d_pp | 0.82 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma20 | 43.53 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma50 | 42.53 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma200 | 42.98 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma20_pct | 1.65 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma50_pct | 4.03 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma200_pct | 2.94 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_sma | 0.70 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_pct | 1.57 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.drawdown_from_63d_high_pct | -1.93 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.volume_vs_previous20_ratio | 0.78 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLB.value | 51.47 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_1d_pct | -1.46 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_5d_pct | -2.78 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_20d_pct | 1.02 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_60d_pct | -3.42 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_1d_pp | 0.46 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_5d_pp | -1.08 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma20 | 52.26 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma50 | 50.86 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma200 | 50.94 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma20_pct | -1.51 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma50_pct | 1.19 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma200_pct | 1.05 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_sma | 1.05 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_pct | 2.05 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.drawdown_from_63d_high_pct | -4.51 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.volume_vs_previous20_ratio | 1.16 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLB/history/ |
| prices.SMH.value | 461.90 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_1d_pct | -5.11 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_5d_pct | -5.23 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_20d_pct | -15.78 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_60d_pct | -17.58 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_1d_pp | -3.19 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_5d_pp | -3.54 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma20 | 513.81 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma50 | 557.70 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma200 | 524.18 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma20_pct | -10.10 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma50_pct | -17.18 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma200_pct | -11.88 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_sma | 27.80 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_pct | 6.02 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.drawdown_from_63d_high_pct | -27.13 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.volume_vs_previous20_ratio | 0.85 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SMH/history/ |
| prices.XOP.value | 179.98 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_1d_pct | -2.61 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_5d_pct | 3.35 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_20d_pct | -9.77 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_60d_pct | -4.67 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_1d_pp | -0.70 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_5d_pp | 5.04 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma20 | 189.80 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma50 | 189.90 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma200 | 172.21 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma20_pct | -5.18 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma50_pct | -5.23 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma200_pct | 4.51 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_sma | 5.81 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_pct | 3.23 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.drawdown_from_63d_high_pct | -12.14 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.volume_vs_previous20_ratio | 0.63 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XOP/history/ |
| prices.OIH.value | 361.14 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_1d_pct | -3.84 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_5d_pct | 0.16 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_20d_pct | -6.23 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_60d_pct | -13.05 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_1d_pp | -1.93 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_5d_pp | 1.85 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma20 | 381.60 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma50 | 389.58 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma200 | 399.15 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma20_pct | -5.36 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma50_pct | -7.30 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma200_pct | -9.52 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_sma | 13.40 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_pct | 3.71 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.drawdown_from_63d_high_pct | -17.28 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.volume_vs_previous20_ratio | 0.74 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/OIH/history/ |
| prices.ITA.value | 69.75 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_1d_pct | -2.46 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_5d_pct | -2.68 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_20d_pct | 0.72 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_60d_pct | -11.73 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_1d_pp | -0.55 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_5d_pp | -0.99 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma20 | 70.16 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma50 | 70.29 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma200 | 75.78 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma20_pct | -0.58 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma50_pct | -0.76 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma200_pct | -7.96 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_sma | 2.11 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_pct | 3.02 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.drawdown_from_63d_high_pct | -14.89 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.volume_vs_previous20_ratio | 0.72 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ARKX.value | 28.05 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_1d_pct | -4.00 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_5d_pct | -6.59 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_20d_pct | -6.59 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_60d_pct | -15.64 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_1d_pp | -2.09 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_5d_pp | -4.90 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma20 | 29.70 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma50 | 31.06 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma200 | 32.23 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma20_pct | -5.55 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma50_pct | -9.68 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma200_pct | -12.98 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_sma | 1.08 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_pct | 3.86 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.drawdown_from_63d_high_pct | -16.62 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.volume_vs_previous20_ratio | 0.34 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.SKYY.value | 149.30 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_1d_pct | -2.10 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_5d_pct | -0.94 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_20d_pct | -7.31 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_60d_pct | -7.40 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_1d_pp | -0.19 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_5d_pp | 0.76 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma20 | 158.71 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma50 | 162.61 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma200 | 138.08 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma20_pct | -5.93 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma50_pct | -8.19 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma200_pct | 8.13 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_sma | 5.59 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_pct | 3.75 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.drawdown_from_63d_high_pct | -14.63 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.volume_vs_previous20_ratio | 0.77 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.QQQ.value | 661.75 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| prices.QQQ.return_1d_pct | -2.67 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| prices.QQQ.return_5d_pct | -2.59 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| prices.QQQ.return_20d_pct | -7.88 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| prices.QQQ.return_60d_pct | -7.15 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| prices.QQQ.relative_spy_1d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| prices.QQQ.relative_spy_5d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| prices.QQQ.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| prices.QQQ.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| prices.QQQ.sma20 | 692.62 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| prices.QQQ.sma50 | 716.59 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| prices.QQQ.sma200 | 681.41 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| prices.QQQ.distance_sma20_pct | -4.46 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| prices.QQQ.distance_sma50_pct | -7.65 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| prices.QQQ.distance_sma200_pct | -2.89 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| prices.QQQ.atr14_sma | 19.23 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| prices.QQQ.atr14_pct | 2.91 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| prices.QQQ.drawdown_from_63d_high_pct | -12.89 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| prices.QQQ.volume_vs_previous20_ratio | 0.87 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| prices.NVDA.value | 156.14 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| prices.NVDA.return_1d_pct | -4.12 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| prices.NVDA.return_5d_pct | -12.61 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| prices.NVDA.return_20d_pct | -28.08 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| prices.NVDA.return_60d_pct | -27.20 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| prices.NVDA.relative_spy_1d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| prices.NVDA.relative_spy_5d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| prices.NVDA.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| prices.NVDA.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| prices.NVDA.sma20 | 195.64 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| prices.NVDA.sma50 | 213.15 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| prices.NVDA.sma200 | 203.75 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| prices.NVDA.distance_sma20_pct | -20.19 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| prices.NVDA.distance_sma50_pct | -26.75 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| prices.NVDA.distance_sma200_pct | -23.37 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| prices.NVDA.atr14_sma | 11.33 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| prices.NVDA.atr14_pct | 7.26 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| prices.NVDA.drawdown_from_63d_high_pct | -34.73 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| prices.NVDA.volume_vs_previous20_ratio | 1.59 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| prices.VRT.value | 188.67 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://query1.finance.yahoo.com/v8/finance/chart/VRT |
| prices.VRT.return_1d_pct | -6.63 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://query1.finance.yahoo.com/v8/finance/chart/VRT |
| prices.VRT.return_5d_pct | -5.89 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://query1.finance.yahoo.com/v8/finance/chart/VRT |
| prices.VRT.return_20d_pct | -8.45 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://query1.finance.yahoo.com/v8/finance/chart/VRT |
| prices.VRT.return_60d_pct | -27.96 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://query1.finance.yahoo.com/v8/finance/chart/VRT |
| prices.VRT.relative_spy_1d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://query1.finance.yahoo.com/v8/finance/chart/VRT |
| prices.VRT.relative_spy_5d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://query1.finance.yahoo.com/v8/finance/chart/VRT |
| prices.VRT.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://query1.finance.yahoo.com/v8/finance/chart/VRT |
| prices.VRT.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://query1.finance.yahoo.com/v8/finance/chart/VRT |
| prices.VRT.sma20 | 208.11 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://query1.finance.yahoo.com/v8/finance/chart/VRT |
| prices.VRT.sma50 | 229.47 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://query1.finance.yahoo.com/v8/finance/chart/VRT |
| prices.VRT.sma200 | 271.50 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://query1.finance.yahoo.com/v8/finance/chart/VRT |
| prices.VRT.distance_sma20_pct | -9.34 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://query1.finance.yahoo.com/v8/finance/chart/VRT |
| prices.VRT.distance_sma50_pct | -17.78 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://query1.finance.yahoo.com/v8/finance/chart/VRT |
| prices.VRT.distance_sma200_pct | -30.51 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://query1.finance.yahoo.com/v8/finance/chart/VRT |
| prices.VRT.atr14_sma | 20.94 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://query1.finance.yahoo.com/v8/finance/chart/VRT |
| prices.VRT.atr14_pct | 11.10 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://query1.finance.yahoo.com/v8/finance/chart/VRT |
| prices.VRT.drawdown_from_63d_high_pct | -35.11 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://query1.finance.yahoo.com/v8/finance/chart/VRT |
| prices.VRT.volume_vs_previous20_ratio | 0.85 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://query1.finance.yahoo.com/v8/finance/chart/VRT |
| prices.IGV.value | 99.00 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://query1.finance.yahoo.com/v8/finance/chart/IGV |
| prices.IGV.return_1d_pct | -2.16 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://query1.finance.yahoo.com/v8/finance/chart/IGV |
| prices.IGV.return_5d_pct | -2.42 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://query1.finance.yahoo.com/v8/finance/chart/IGV |
| prices.IGV.return_20d_pct | -6.59 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://query1.finance.yahoo.com/v8/finance/chart/IGV |
| prices.IGV.return_60d_pct | -4.23 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://query1.finance.yahoo.com/v8/finance/chart/IGV |
| prices.IGV.relative_spy_1d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://query1.finance.yahoo.com/v8/finance/chart/IGV |
| prices.IGV.relative_spy_5d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://query1.finance.yahoo.com/v8/finance/chart/IGV |
| prices.IGV.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://query1.finance.yahoo.com/v8/finance/chart/IGV |
| prices.IGV.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://query1.finance.yahoo.com/v8/finance/chart/IGV |
| prices.IGV.sma20 | 104.70 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://query1.finance.yahoo.com/v8/finance/chart/IGV |
| prices.IGV.sma50 | 106.01 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://query1.finance.yahoo.com/v8/finance/chart/IGV |
| prices.IGV.sma200 | 94.21 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://query1.finance.yahoo.com/v8/finance/chart/IGV |
| prices.IGV.distance_sma20_pct | -5.45 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://query1.finance.yahoo.com/v8/finance/chart/IGV |
| prices.IGV.distance_sma50_pct | -6.61 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://query1.finance.yahoo.com/v8/finance/chart/IGV |
| prices.IGV.distance_sma200_pct | 5.08 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://query1.finance.yahoo.com/v8/finance/chart/IGV |
| prices.IGV.atr14_sma | 3.20 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://query1.finance.yahoo.com/v8/finance/chart/IGV |
| prices.IGV.atr14_pct | 3.23 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://query1.finance.yahoo.com/v8/finance/chart/IGV |
| prices.IGV.drawdown_from_63d_high_pct | -12.13 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://query1.finance.yahoo.com/v8/finance/chart/IGV |
| prices.IGV.volume_vs_previous20_ratio | 0.80 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://query1.finance.yahoo.com/v8/finance/chart/IGV |
| prices.KRE.value | 72.19 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://query1.finance.yahoo.com/v8/finance/chart/KRE |
| prices.KRE.return_1d_pct | -0.76 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://query1.finance.yahoo.com/v8/finance/chart/KRE |
| prices.KRE.return_5d_pct | -1.72 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://query1.finance.yahoo.com/v8/finance/chart/KRE |
| prices.KRE.return_20d_pct | 4.23 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://query1.finance.yahoo.com/v8/finance/chart/KRE |
| prices.KRE.return_60d_pct | -3.02 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://query1.finance.yahoo.com/v8/finance/chart/KRE |
| prices.KRE.relative_spy_1d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://query1.finance.yahoo.com/v8/finance/chart/KRE |
| prices.KRE.relative_spy_5d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://query1.finance.yahoo.com/v8/finance/chart/KRE |
| prices.KRE.relative_spy_20d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://query1.finance.yahoo.com/v8/finance/chart/KRE |
| prices.KRE.relative_spy_60d_pp | 缺失 | pp | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://query1.finance.yahoo.com/v8/finance/chart/KRE |
| prices.KRE.sma20 | 72.53 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://query1.finance.yahoo.com/v8/finance/chart/KRE |
| prices.KRE.sma50 | 71.58 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://query1.finance.yahoo.com/v8/finance/chart/KRE |
| prices.KRE.sma200 | 70.66 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://query1.finance.yahoo.com/v8/finance/chart/KRE |
| prices.KRE.distance_sma20_pct | -0.47 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://query1.finance.yahoo.com/v8/finance/chart/KRE |
| prices.KRE.distance_sma50_pct | 0.85 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://query1.finance.yahoo.com/v8/finance/chart/KRE |
| prices.KRE.distance_sma200_pct | 2.17 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://query1.finance.yahoo.com/v8/finance/chart/KRE |
| prices.KRE.atr14_sma | 1.57 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://query1.finance.yahoo.com/v8/finance/chart/KRE |
| prices.KRE.atr14_pct | 2.17 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://query1.finance.yahoo.com/v8/finance/chart/KRE |
| prices.KRE.drawdown_from_63d_high_pct | -3.55 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://query1.finance.yahoo.com/v8/finance/chart/KRE |
| prices.KRE.volume_vs_previous20_ratio | 1.18 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://query1.finance.yahoo.com/v8/finance/chart/KRE |
| macro.DGS2.value | 4.88 | percent | 2026-11-13 | lagged | source_series_v1:DGS2 | https://fred.stlouisfed.org/series/DGS2 |
| macro.BAMLH0A0HYM2.value | 3.23 | percentage_points | 2026-11-13 | lagged | source_series_v1:BAMLH0A0HYM2 | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| macro.BAMLC0A0CM.value | 0.89 | percentage_points | 2026-11-13 | lagged | source_series_v1:BAMLC0A0CM | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| macro.DGS10.value | 5.15 | percent | 2026-11-13 | lagged | source_series_v1:DGS10 | https://fred.stlouisfed.org/series/DGS10 |
| macro.DFII10.value | 2.91 | percent | 2026-11-13 | lagged | source_series_v1:DFII10 | https://fred.stlouisfed.org/series/DFII10 |
| macro.T10YIE.value | 2.20 | percent | 2026-11-16 | ok | source_series_v1:T10YIE | https://fred.stlouisfed.org/series/T10YIE |
| macro.STLFSI4.value | -0.49 | index | 2026-11-06 | lagged | source_series_v1:STLFSI4 | https://fred.stlouisfed.org/series/STLFSI4 |
| macro.CBOE_VIX.value | 22.91 | index | 2026-11-16 | ok | source_series_v1:CBOE_VIX | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| macro.GPRD.value | 189.55 | index | 2026-11-16 | ok | source_series_v1:GPRD | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_ACT.value | 215.96 | index | 2026-11-16 | ok | source_series_v1:GPRD_ACT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_THREAT.value | 195.14 | index | 2026-11-16 | ok | source_series_v1:GPRD_THREAT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA7.value | 145.08 | index | 2026-11-16 | ok | source_series_v1:GPRD_MA7 | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA30.value | 151.47 | index | 2026-11-16 | ok | source_series_v1:GPRD_MA30 | https://www.matteoiacoviello.com/gpr.htm |
| quotes.SPY.value | 741.23 | USD_per_share | 2026-11-17T12:00:19+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SPY |
| quotes.QQQ.value | 665.43 | USD_per_share | 2026-11-17T12:00:19+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| quotes.SMH.value | 468.96 | USD_per_share | 2026-11-17T12:00:18+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SMH |
| quotes.RSP.value | 218.90 | USD_per_share | 2026-11-17T11:44:12+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/RSP |
| quotes.IWM.value | 272.26 | USD_per_share | 2026-11-17T12:00:15+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/IWM |
| quotes.NVDA.value | 158.08 | USD_per_share | 2026-11-17T12:00:19+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| quotes.MSFT.value | 516.75 | USD_per_share | 2026-11-17T12:00:16+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/MSFT |
| quotes.AMZN.value | 259.98 | USD_per_share | 2026-11-17T12:00:13+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AMZN |
| quotes.GOOGL.value | 284.50 | USD_per_share | 2026-11-17T12:00:14+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GOOGL |
| quotes.META.value | 624.85 | USD_per_share | 2026-11-17T12:00:05+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/META |
| quotes.MU.value | 734.40 | USD_per_share | 2026-11-17T12:00:19+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/MU |
| observed.Treasury2Y.value | 4.83 | percent | 2026-11-16T15:30:00-05:00 | ok | 财政部16日平价曲线指示报价，非实时成交；与FRED较旧观测并列 | https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value_month=202611&type=daily_treasury_yield_curve |
| observed.Treasury10Y.value | 5.12 | percent | 2026-11-16T15:30:00-05:00 | ok | 财政部16日平价曲线指示报价，非实时成交；与FRED较旧观测并列 | https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value_month=202611&type=daily_treasury_yield_curve |
| observed.SPY.low | 738.07 | USD_per_share | 2026-11-16T16:00:00-05:00 | ok | 16日完整常规时段日线low；非盘中开盘区间或VWAP | https://query1.finance.yahoo.com/v8/finance/chart/SPY |
| observed.SPY.high | 749.82 | USD_per_share | 2026-11-16T16:00:00-05:00 | ok | 16日完整常规时段日线high；非盘中开盘区间或VWAP | https://query1.finance.yahoo.com/v8/finance/chart/SPY |
| observed.QQQ.low | 660.48 | USD_per_share | 2026-11-16T16:00:00-05:00 | ok | 16日完整常规时段日线low；非盘中开盘区间或VWAP | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| observed.QQQ.high | 672.15 | USD_per_share | 2026-11-16T16:00:00-05:00 | ok | 16日完整常规时段日线high；非盘中开盘区间或VWAP | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| observed.SMH.low | 460.64 | USD_per_share | 2026-11-16T16:00:00-05:00 | ok | 16日完整常规时段日线low；非盘中开盘区间或VWAP | https://query1.finance.yahoo.com/v8/finance/chart/SMH |
| observed.SMH.high | 473.33 | USD_per_share | 2026-11-16T16:00:00-05:00 | ok | 16日完整常规时段日线high；非盘中开盘区间或VWAP | https://query1.finance.yahoo.com/v8/finance/chart/SMH |
| observed.NVDA.low | 155.01 | USD_per_share | 2026-11-16T16:00:00-05:00 | ok | 16日完整常规时段日线low；非盘中开盘区间或VWAP | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| observed.NVDA.high | 163.20 | USD_per_share | 2026-11-16T16:00:00-05:00 | ok | 16日完整常规时段日线high；非盘中开盘区间或VWAP | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| observed.MU.low | 716.38 | USD_per_share | 2026-11-16T16:00:00-05:00 | ok | 16日完整常规时段日线low；非盘中开盘区间或VWAP | https://query1.finance.yahoo.com/v8/finance/chart/MU |
| observed.MU.high | 739.12 | USD_per_share | 2026-11-16T16:00:00-05:00 | ok | 16日完整常规时段日线high；非盘中开盘区间或VWAP | https://query1.finance.yahoo.com/v8/finance/chart/MU |
| observed.XLP.low | 92.38 | USD_per_share | 2026-11-16T16:00:00-05:00 | ok | 16日完整常规时段日线low；非盘中开盘区间或VWAP | https://query1.finance.yahoo.com/v8/finance/chart/XLP |
| observed.XLP.high | 93.48 | USD_per_share | 2026-11-16T16:00:00-05:00 | ok | 16日完整常规时段日线high；非盘中开盘区间或VWAP | https://query1.finance.yahoo.com/v8/finance/chart/XLP |
| observed.XLF.low | 57.89 | USD_per_share | 2026-11-16T16:00:00-05:00 | ok | 16日完整常规时段日线low；非盘中开盘区间或VWAP | https://query1.finance.yahoo.com/v8/finance/chart/XLF |
| observed.XLF.high | 58.81 | USD_per_share | 2026-11-16T16:00:00-05:00 | ok | 16日完整常规时段日线high；非盘中开盘区间或VWAP | https://query1.finance.yahoo.com/v8/finance/chart/XLF |
| observed.XLV.low | 187.60 | USD_per_share | 2026-11-16T16:00:00-05:00 | ok | 16日完整常规时段日线low；非盘中开盘区间或VWAP | https://query1.finance.yahoo.com/v8/finance/chart/XLV |
| observed.XLV.high | 191.33 | USD_per_share | 2026-11-16T16:00:00-05:00 | ok | 16日完整常规时段日线high；非盘中开盘区间或VWAP | https://query1.finance.yahoo.com/v8/finance/chart/XLV |
| observed.CNN.value | 31 | index | 2026-11-17T06:45:31-05:00 | ok | CNN Fear and Greed官方可见页面；0-100，Fear；非tc温度或加密指数 | https://edition.cnn.com/markets/fear-and-greed |
| observed.premarket.SPY | 741.23 | USD_per_share | 2026-11-17T12:00:19+00:00 | ok | Yahoo最新可见分钟价格；并非同步成交、官方结算或常规时段VWAP | https://query1.finance.yahoo.com/v8/finance/chart/SPY |
| observed.premarket.QQQ | 665.43 | USD_per_share | 2026-11-17T12:00:19+00:00 | ok | Yahoo最新可见分钟价格；并非同步成交、官方结算或常规时段VWAP | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| observed.premarket.SMH | 468.96 | USD_per_share | 2026-11-17T12:00:18+00:00 | ok | Yahoo最新可见分钟价格；并非同步成交、官方结算或常规时段VWAP | https://query1.finance.yahoo.com/v8/finance/chart/SMH |
| observed.premarket.IWM | 272.26 | USD_per_share | 2026-11-17T12:00:15+00:00 | ok | Yahoo最新可见分钟价格；并非同步成交、官方结算或常规时段VWAP | https://query1.finance.yahoo.com/v8/finance/chart/IWM |
| observed.premarket.NVDA | 158.08 | USD_per_share | 2026-11-17T12:00:19+00:00 | ok | Yahoo最新可见分钟价格；并非同步成交、官方结算或常规时段VWAP | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| observed.premarket.MU | 734.40 | USD_per_share | 2026-11-17T12:00:19+00:00 | ok | Yahoo最新可见分钟价格；并非同步成交、官方结算或常规时段VWAP | https://query1.finance.yahoo.com/v8/finance/chart/MU |
| observed.premarket.CL=F | 86.24 | USD_per_barrel | 2026-11-17T11:50:22+00:00 | ok | Yahoo最新可见分钟价格；并非同步成交、官方结算或常规时段VWAP | https://query1.finance.yahoo.com/v8/finance/chart/CL=F |
| observed.premarket.BZ=F | 92.94 | USD_per_barrel | 2026-11-17T11:50:21+00:00 | ok | Yahoo最新可见分钟价格；并非同步成交、官方结算或常规时段VWAP | https://query1.finance.yahoo.com/v8/finance/chart/BZ=F |
| observed.premarket.GC=F | 3,873.30 | USD_per_troy_ounce | 2026-11-17T11:50:20+00:00 | ok | Yahoo最新可见分钟价格；并非同步成交、官方结算或常规时段VWAP | https://query1.finance.yahoo.com/v8/finance/chart/GC=F |
| observed.premarket.^VIX | 22.49 | index | 2026-11-17T11:45:16+00:00 | ok | Yahoo最新可见分钟价格；并非同步成交、官方结算或常规时段VWAP | https://query1.finance.yahoo.com/v8/finance/chart/^VIX |

## 指标历史比较（不同日期观测，非连续交易日）

```json
[
  {
    "id": "prices.SPY.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -14.41998291015625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -12.739990234375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -26.52996826171875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.548308057704939,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.277943215265267,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.3347143179643925,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -4.287491519674436,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.7710451747923517,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.19921385370731404,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.297827045092171,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.19562973574549503,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.5537079255984363,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.2919286940002004,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.3198983245214948,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -7.111434540730754,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.3264984130859148,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.3979980468750455,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -13.138003540039108,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.5666442871093977,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.3334948730467886,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -3.781208496093768,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.2667111206054642,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.5920501708983466,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 7.255191955566374,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.7291408530431207,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.1081314270712905,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.7772530153410515,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.8153444578777655,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.4967102178029768,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.9799833592405456,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.0142847480788317,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.9718221968601846,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -4.691542561702944,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.7407139369419653,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.5285688127790191,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 6.436436244419643,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.13308301036258974,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.23397764688113076,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.9029222066600148,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.8508750482094554,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.635239804800948,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -3.405250657462267,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.6748482270432485,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.4060690554349695,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.551236209843897,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -4.600006103515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -9.57000732421875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.660003662109375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.3341936723833991,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.8875871221793155,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.9680244817332326,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -4.801603216746453,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.594770872485743,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.0053430352845005,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.0134382701808784,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.0469606015705235,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 5.6192646594945055,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.2512094266477156,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.6109713636644045,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.1824867991838577,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.21411438532153992,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.609643906914048,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.3666898362311599,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.5141116970720172,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.823725697693391,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.8061291815771865,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.08300018310546875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.3860000610351335,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.13699798583985512,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.4459783935546966,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.4658294677734034,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -7.851186523437491,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.07519775390625227,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.43210411071777344,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.8776631164550963,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.6816683902188045,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.9442807654223477,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.6440459919317187,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.484160425287262,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.8904950624549453,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.2307493511421144,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.6783019907816943,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.593194986076842,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.06499593466141595,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.14714486258370574,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.5585719517299115,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.7478572300502235,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.08707978278262907,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.2673351654313214,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.6317243835102071,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.528576293331529,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.1431308912014053,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.547367303239012,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.37267650470275127,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.035337850681316896,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.3550260205048955,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.230010986328125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.0200042724609375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 5.529998779296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.2076734141036938,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.276315382324546,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.6860292113280764,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.279429427296421,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.3551856765731118,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.0127356088039052,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.7109757602112632,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.0485657735451737,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.252839842085952,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.6417100231752357,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.42066025895960424,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.1608155625737249,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.3406346436012453,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.0016278329407213,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.6486851066363162,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 1.0080620923780148,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.41585949821923984,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.8135217550965912,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.2764999389648608,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.823000335693365,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 7.356498718261719,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.015002441406238631,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.27618530273437614,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.3901501464843875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.11595527648927373,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.6152324676513672,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.3610088348388842,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.1463305421492764,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.7700790692747992,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.8632633181640426,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.045189949300629,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.0726328777464378,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.754103385003348,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.1324106499551512,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.2876099874848945,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.4809508607459332,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.11214338030133897,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.17571585518973176,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.1164289202008928,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.06514575214054275,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.09261896527286662,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.4860549793413771,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.9985272771434905,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.904493017462582,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.8758634783107686,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.36801571960118107,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.14521969050058825,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.2550076191375843,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.52001953125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -26.600006103515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -26.760009765625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.8667606218558666,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.5907467796507655,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.10165009666760483,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.426372032287494,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -11.952678317004873,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -6.364946187407705,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.0951605990914155,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -6.362263960610671,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.3563562229516384,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.2329351006709057,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -11.168684797281601,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -18.730610216357924,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.6815474358490725,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.687196435614502,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.2330642212967877,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 1.861119487386941,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -10.181633142212522,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -6.165732333700392,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.3380004882812386,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -5.213499450683571,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -15.940000915527321,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.0767999267578148,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.542799682617158,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -16.97920043945311,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.4601000976562659,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.892050018310556,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -6.938750305175802,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.33485098851567807,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -5.79416032128095,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.9864718490723474,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.39891147288942985,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -5.8222045240926,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.767900837584503,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.519562333642476,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -5.865431435917712,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -5.002992263366012,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.03142656598772309,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.5935756138392856,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.584278651646205,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.006356661975597255,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.3066414754852824,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.8317125504435552,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.5886933184135366,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -6.213938292427214,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -6.251316211779601,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.2561632259804041,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.20535999999423216,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.37696871409443056,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -33.300048828125,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -261.5,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -307.10009765625,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.8825954192303698,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.8286627901583197,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.3545972222697258,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.7272408046378525,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -10.005811046481227,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -5.627752370040451,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.3312591451819946,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -5.566064898192458,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.2769971469228327,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.694842260688157,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -10.406805553759822,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -19.875168721737488,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.6657126384745693,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.4492804251069478,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.9801170956946668,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 2.5602507150365827,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -8.234765871688875,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -5.428538516333137,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -15.355004882812409,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -57.05999755859375,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -183.07000732421875,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -12.472001953125073,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -53.073999023436954,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -200.58199707031235,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -4.460500488281468,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -29.384500732421657,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -72.00750610351588,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.4605063884268952,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -5.072674284430622,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -3.1318390448057394,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.5207088901615258,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -5.031824140387187,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.7856758243975825,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.6585803705716149,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -5.251279137321784,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -5.396746897229708,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.6214076450892918,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 9.064296177455347,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 25.88575962611607,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.005724810821006621,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.3813643961116835,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.809314679051095,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.7088435057385354,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -5.5664355841445925,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -6.5371048240459935,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.4277098773299718,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.18452436718385024,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.027091140852049778,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.839996337890625,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.1299972534179688,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -17.94000244140625,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.0040212498463226,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.1749544288819909,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -5.425577378046698,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 1.1980882346734112,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 8.661588857543078,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -11.883559256381771,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -4.63524119601597,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -9.956464082792037,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -25.533773452071284,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.370310431892464,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -6.939645859656474,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -17.606801104414814,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.4557131921413835,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 5.452897644147258,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -3.090863060082305,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 5.485579754347847,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 10.432634032335432,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -11.684345402674456,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.8970001220703097,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.834000396728513,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.502499771118167,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.11520004272460938,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.28360031127930085,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.759799652099602,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.10255001068115632,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.5936499977111822,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.457550010681146,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.1196786297681296,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.465782597608289,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -20.676710147941602,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.8692511819964235,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.9156557462445036,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -23.306416952614416,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.3494148780920607,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.9579921457037575,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -25.245196143589645,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.07785742623465364,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.25999886648995574,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.7092862810407361,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.2617686666967298,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.2288293130712118,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.622485715730131,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.6835455813601357,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.0677475516081678,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -16.951717028263293,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.2423118724329869,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.3372108395903396,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.29736935334794223,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.399993896484375,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.12999725341796875,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -17.110000610351562,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.568442031848551,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.3006775624610065,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -3.2653979732151672,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 2.3819480381099933,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 11.504120899847093,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.8596075622957406,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.856738667974657,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.4163748406649255,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -24.797238323929193,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -4.262521428185506,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -6.641134446889119,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -15.26077314653369,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.020133974143612,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 6.5786207777262735,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.9306836552507747,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 6.669439557784429,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 13.275166074639444,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.660393708588426,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.8555000305175753,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.436500167846674,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.12549972534179688,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.07679992675781477,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.0843998718261787,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 5.25,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.10875000000000057,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.626949996948241,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.9512000274658305,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.5126359453633516,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.707534973532354,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -16.534731704063,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.195659202279078,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.05285535293842969,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -22.002483468012347,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.730871578187045,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.7979168920613344,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -23.28433966095832,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.10285731724330383,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.06642804827008941,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.7664277212960378,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.3229734235546253,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.06322319904132101,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.5618605809964095,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.8901682371000987,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.11050429623633562,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -21.1391077013784,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.2811194942771671,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.38143004407163417,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.2786730891474346,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.0,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.5800018310546875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.0800018310546875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.4264976945294596,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.048829243678505385,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.7370442783164899,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.04729215803299658,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.429288456646462,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -4.954408401685562,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.7394021315450305,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.689837852308232,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.7891813267456267,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.3448583076475442,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.7710785970421536,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.331519290765082,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 1.9748057522343987,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 4.229113971586762,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.0717585962808824,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 4.240199361641439,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.6582432818541104,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -4.755194547978247,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.012651062011713066,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.023797607421869316,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.399226760864252,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.04314102172851619,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.4283921813964895,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.5403305053710881,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.022301063537597088,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.4464845657348633,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.6892769622802746,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.015333101998171728,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.2175180894596256,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -3.0980970230896743,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.05377154868492218,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.6851378817332794,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.5697059656117998,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.02588175649813529,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.587733405580184,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.6976023186350933,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.01579220776703183,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.041593200149147136,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.051783544444029994,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.01989444231978965,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.08168629706244868,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.0641797980054325,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -8.904334725112761e-06,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.711877571200483,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.8008269135422963,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.012770751476212427,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.10898434686644176,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.24807826364110575,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.05999946594238281,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.5900001525878906,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.5599994659423828,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.06853558114316982,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.7526494414333951,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.07323688820697338,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.7664190213511723,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.002058972234222,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.4828625998096876,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.07449959317604726,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.480294062470356,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.1051883078880822,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.2529369074185661,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.8904155405809595,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 4.480260919838841,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 1.4797724765617692,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 5.030592656698662,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.261477429757419,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 5.053910541025608,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 3.7731041470265736,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.6820764535170016,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.02799997329712056,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.09599990844726847,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.2074997901916511,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.02959999084472642,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.12779998779296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.4073999404907198,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.01354999542236257,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.06829999923706254,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.1997999763488778,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.10855141367216437,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.6984991065251642,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.208870404949125,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.10294991767740846,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.5990397467275042,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.5006143471786517,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.16308917939606982,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.8515158081794159,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.254796842582473,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.002857208251953125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.02071448734828403,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.005714144025530138,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.010599577567668217,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.06234979877161745,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.028382956021594574,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.0,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.5492614212897151,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.44627244940566024,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.2481933810996022,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.052975461460975204,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.806837712006758,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.20999908447265625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.779998779296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.09999847412109375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.220976019132213,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.6354905701460356,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.2339083369070516,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.6308172451419791,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.8126704698880225,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.41116027224568086,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.23545902384285444,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.10511036168434629,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.306592160968479,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.3294648748835116,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.35942222165809,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.5630549335268409,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 1.327332038572726,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 3.642452645119232,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.100805981057341,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 3.6566742745324565,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.04162529509567081,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.21194641853836682,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.014894866943350848,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.15705833435059446,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.17443771362304972,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.03342376708984318,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.49346343994140796,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.9874617004394537,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.002338409423828125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.3951002883911059,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.4118480682373047,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.291988215546124,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.8079438235306879,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.09559064763912106,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.22911871284631014,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.3723453792089826,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.130287957071685,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.26801499868938095,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.4991626672513294,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.3951592139966986,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.014841699208844261,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.016757593777999846,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.011621569117638453,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.018178264492977048,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.01752109368525051,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.014596209221454992,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.26675861964697845,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.4809140074408469,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.37840651914449186,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.17801968224837028,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.1777728683515457,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.08209932965896533,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.0099945068359375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.8699951171875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.07999420166015625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.22318063830490953,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.14365359739926253,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.4931841410278026,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.14110085273970618,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.712219883508138,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.079012874870023,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.49474259253816655,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.730387250088894,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.987583204526222,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.12016929001039678,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.2157576548569748,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.1637900872324516,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 1.7714886960098486,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 4.1342896178660045,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.827898458992195,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 4.14639066693473,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.9411747087157862,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.8797990211627091,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.015733718872070312,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.1039276123046875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.1232563018798913,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.03647842407227131,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.4802128601074287,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.8605931091308605,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.017653388977052487,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.47332557678223,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.6717212295532278,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.024679603652455473,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.7021091234870611,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.1633667336562126,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.025553240293163526,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.3427723368713784,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.7478754278276489,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.006874537991241603,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.3310729799629217,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.5433490551482678,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.002047295073941191,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.004768351931668469,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.06175907521898594,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.0019378194921825243,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.005279983769993946,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.05960214194617752,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.009469012475959993,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.3912414667426543,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.2981382930737908,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.09901563134769165,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.04003945223096672,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.0797803424408321,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 3.6100006103515625,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.989999771118164,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 4.469999313354492,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 15.496119255237037,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 41.01355732300942,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 26.45854032492827,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 39.73702921744608,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 20.825639731553302,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -6.225993181352596,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 27.692505059406624,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -6.725693115815698,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.23270199996581198,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 16.98145150244845,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 13.403671008622386,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 45.77450272332594,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 17.044427312941977,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 45.29150053827469,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 28.793254642892663,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 44.02452073712052,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 22.596684906345654,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -6.026779327645279,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.2234999656677239,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.5414999008178718,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.6959999084472663,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.15219999313354649,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.4433999824523944,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.8053999900817868,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.024549999237059694,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.06424999237060547,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.3312500047683713,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 17.278451809711093,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 12.365064695841088,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.9487071919311632,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 19.698001169633052,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 14.148607061568843,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 13.421395526628977,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 19.397793998100465,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 15.805250048168482,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 22.369284102677266,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.29285730634416884,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.3750004087175647,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.4142861366271977,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.7734459039920587,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.7582877066781109,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 8.827810319058367,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 12.810505930649398,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 10.610361031717222,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -7.955809453046834,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 2.3999996185302734,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.1700000762939453,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.4200000762939453,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 8.847550888453837,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 26.883085135957664,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 16.02942497493003,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 26.586533713317607,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 13.87989619731218,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.0936748848785474,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 16.863609694006577,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.1634245573015392,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 9.041897428113966,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 16.247747514375455,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 11.485514996052437,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 28.869294181608552,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 10.395858946158775,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 31.16102835122293,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 18.36413929289442,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 30.87402523299204,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 15.65094137210453,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.2928887385858605,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.17100000381469727,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.4119999885559089,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.3799999237060554,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.10819999694824389,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.29919998168945483,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.9418000411987322,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.014750003814697266,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.03125000953674473,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.16940001487731848,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 10.777897732584286,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 8.446217362570074,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 4.20769276334958,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 11.796816591822811,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 9.517268384350785,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 12.487678589274509,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 11.567153644826188,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 10.369892325720407,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 15.797894533988176,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.18999998910086502,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.25142846788678863,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.402856963021415,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.2497780585545435,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.15860121391492754,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 5.401598758915135,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 9.393345167106883,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 8.493151237148911,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.0649406318123713,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 12.700004577636719,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 15.800003051757812,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 7.3000030517578125,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 7.52465036795087,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 31.788597924911688,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 15.219935018410702,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 32.789762252414945,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 26.950906996117077,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -8.386476651554009,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 14.45132310324534,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -7.719825091329891,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -17.84373705719331,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 19.42301867814318,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 19.892742206754278,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 26.254820245501854,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 9.07295842565581,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 36.06654114017695,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 17.554649336375096,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 37.07725377208938,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 28.72195217090943,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -8.187262797846692,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.3650001525878963,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.5165000915527287,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 13.806001663208008,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.5962001037597702,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.3511999511718784,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 6.302600402832027,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.03025001525878679,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.059200019836424644,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.5199000167846748,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 11.898367995550219,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 14.757830144222906,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -8.79065564952679,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 12.578053407051716,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 15.005732921310601,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.22943012400835272,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 12.801688377222776,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 16.02499605587451,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 6.805845970993364,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 1.056428636823382,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.8849999564034601,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 8.019998822893417,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.6704101175945212,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.296465776003748,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 6.566455140070656,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 9.408107312270495,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 11.704572493374652,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -12.667605696562358,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.value",
    "available_prior_observations": 20,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 2.4899978637695312,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": 8.510002136230469,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": 0.18000030517578125,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_1d_pct",
    "available_prior_observations": 20,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 2.1547530696261363,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": 7.7798929218381385,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": 3.876725149192828,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_5d_pct",
    "available_prior_observations": 20,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 8.284743523579042,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": 16.588396928361185,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": 8.77600574621087,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_20d_pct",
    "available_prior_observations": 20,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 3.788147248449658,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": 8.052918258192797,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": -32.46430511510701,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_60d_pct",
    "available_prior_observations": 20,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 10.372284714363154,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": 13.441048591706071,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": 9.641499775671562,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_1d_pp",
    "available_prior_observations": 20,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 3.7030611273310754,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": 10.003831230478632,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": 4.681735924392472,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_5d_pp",
    "available_prior_observations": 20,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 10.56639073918635,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": 13.251247371202814,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": 6.7622686983326865,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma20",
    "available_prior_observations": 20,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.009000015258791905,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": -1.2649993896484375,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": -1.7869983673095646,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma50",
    "available_prior_observations": 20,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.431399993896477,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": 2.063400115966786,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": 9.785799865722652,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma200",
    "available_prior_observations": 20,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.2192499923706066,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": 0.9742000198364309,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": 3.697449989318855,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma20_pct",
    "available_prior_observations": 20,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 2.5325211079729737,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": 9.894274040995764,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": 2.032607062664682,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma50_pct",
    "available_prior_observations": 20,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 2.148870646499046,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": 6.795802724570099,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": -12.06544616811074,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma200_pct",
    "available_prior_observations": 20,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 2.7900503352232384,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": 9.261905168623219,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": -5.984917202603345,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_sma",
    "available_prior_observations": 20,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.020714351109096363,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": 0.07714353288923004,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": -0.3249991280691962,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_pct",
    "available_prior_observations": 20,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.10678811720022363,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": -0.381806956403703,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": -0.330487433177991,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.drawdown_from_63d_high_pct",
    "available_prior_observations": 20,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 2.1918995574078064,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": 7.491199164205186,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": 0.15845097499432903,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -5.8900146484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -27.19000244140625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -15.530029296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.2925670330809713,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.8702037500066067,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.9692227687979513,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.7189962703871644,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -12.492470726922445,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -3.577383035957748,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.93364146792393,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.6555660255363165,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -9.272384503523012,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.689764864246234,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.0645698464128124,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -32.84677233559819,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.25574102462396775,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.4077394652586608,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.3654915491664412,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.5684952492872712,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -10.721425552130093,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -3.378169182250434,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.7765014648437045,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.9995025634765398,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 6.793495178222656,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.36579956054697504,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.0841992187500864,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 13.30809448242195,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.45206298828122726,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.6867803955078102,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 6.6495726013183685,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.9688795573143505,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.561765966600517,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -4.251890779839518,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.205179367056386,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -5.658204392685839,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -5.691663432179606,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.4577042252500902,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -6.641103699859819,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -5.37457818961613,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.34000069754464235,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.3535679408482117,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 6.41928972516741,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.10373880745417141,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.420563184287404,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.3037492077852333,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.0597363759985319,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.892048045804264,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -4.975592848762133,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.15151678598464435,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.1629532284592764,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.3450851775920255,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -8.910003662109375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -9.17999267578125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -4.70001220703125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.0496811170668825,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -6.283874483610541,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -8.321339743588773,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -6.2775185958481305,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -12.110675297837869,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -4.564217191737829,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -8.45482333126596,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.64212766201052,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -3.338509934161882,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.8584288719557094,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.9698008940323808,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -13.411649826630546,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.5013730593619434,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.0059312683452735,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -5.986625425624381,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.990027076173695,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -10.339630123045517,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -4.365003338030515,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.2350006103515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.4510009765625114,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.6735008239746207,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.015200195312473852,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.8362005615234409,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.0389993286132437,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.09224998474121548,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.608750152587902,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.801500244140641,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.3708688246841367,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.569905214072212,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -3.3077930240252185,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.490668107026096,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.947818000829706,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.0268743341948605,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.6824791361352416,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.023795553311738,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.716367253980013,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.28643035888671875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.4742867606026788,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 4.413566589355469,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.25041964171717357,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.3248719490164733,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.7583242108197066,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.2894022308578745,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.712699119142805,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.750877502725701,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.34123191522889673,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.1054101972783772,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.6092941975788895,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -12.04998779296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.42999267578125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -60.459991455078125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.0931826319144484,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -5.257475574064419,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -5.128159861556814,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -5.396507116843141,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.8206644387201125,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.8837951468306682,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -4.406867970799821,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.7399197268415634,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -14.526691678949643,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -4.542394960804376,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.0244742136644867,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -25.37940427950565,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.5448745742095094,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.9795323587991511,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.793445543592421,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.1090155971687055,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.049619263927761,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.0830090005379822,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.0229995727539176,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -13.819499206543014,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -45.480999755859386,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.0947998046874545,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.650804443359334,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -17.203059082031245,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.26811782836915654,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.088939514160188,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.7837499999999977,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.030415753640126,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.7441410819437397,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -5.060632812210309,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.382338362305836,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.11932981217441885,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -13.226481882956332,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.4964180737518937,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.0370290561648403,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -17.05904583979132,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.4092843191964288,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.6557094029017847,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.275713239397321,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.3152895637252868,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.2943166229438656,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.7145308952063578,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.394649618708666,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.2479907204966594,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -11.26799452674181,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.09434811231267282,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.08424549621656519,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.06153281577207048,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -15.280029296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -14.96002197265625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -79.030029296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -5.280467404251377,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -7.49798622559622,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.832809783662681,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -7.501727296315686,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -8.041807103700481,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.717562048895073,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.667180356207286,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.4707455658856805,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -6.371912949756574,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.651686861684535,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 5.1830905720520395,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -4.613704079683913,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.7321593465464376,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.220043010330953,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.5019045343017114,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.21423577664125,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -6.270761928908131,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.916775902602387,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.9515014648437727,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -24.482998657226517,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -100.87349548339841,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.20252685546870453,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 3.8606616210937545,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 22.673969726562518,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.44124999999996817,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.4904620361328398,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.719485473632858,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.784809434320156,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.408747890132589,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.8305491817191775,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.2754964298718816,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.739007300348484,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -15.20315957739311,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.3556262763963387,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.1355806953134326,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -12.24758068313616,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.7285723005022291,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.0485621861049133,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.27857753208705205,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.19598049586871324,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.39456574778427367,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.42735063300383525,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.965049546567176,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.9238958134730417,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -10.163457164756606,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.1436442036053821,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.27353357405510137,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.2598213838448473,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.25,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.9000015258789062,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -11.239997863769531,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.013666420233725773,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -11.677411581127085,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -5.677259417304648,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -12.666821061178311,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 4.170492701553941,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 25.684986817006074,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -4.935091691371229,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 20.583289668269455,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 10.065998209114536,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.4125741636392988,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 10.246207495579775,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -28.252006241400306,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 1.5619744779386648,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -7.399468365861817,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -3.3425450993402555,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -8.379329541503877,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 5.941537876346292,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 25.884200670713387,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.5619998931884709,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.3339998245239215,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -27.320750045776364,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.7895999908447209,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.0495999145507824,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -14.636300277709964,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.21655000686645565,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.1839999771118244,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -3.6169250679016187,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -4.973615157522271,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 6.847938226254923,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 16.87891769744858,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.721302406172157,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 4.03229357879966,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.2411889992621,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.5154712346709758,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.740084410015875,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -9.966332685766531,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.015357153756277775,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.9108573368617465,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.4532141004289896,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.7588107820616301,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.6230321531632033,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.1096631462277653,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.2555343487823194,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 4.499426752865446,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -6.769485352730534,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.3513601821908644,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.012182837933024215,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.8208892207100464,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -59.28997802734375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -14.1300048828125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -185.8800048828125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -5.096617579707285,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -13.87141118445282,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -10.583056493899246,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -14.725850979455592,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 10.121788176677248,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 6.565534266515572,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -9.102551057242724,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 5.319396041462255,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -7.2347125933328815,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -5.509767987421245,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.0808649986607364,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -23.888335322848086,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.548309522002346,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -9.593467969187552,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -8.248342175934852,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -10.438359459781157,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 11.892833351469598,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 6.764748120222886,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -9.294000244140648,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -37.498504638671875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -197.21109619140623,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -5.948200683593768,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -19.801220703125068,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -45.77982788085944,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 1.5222196960448855,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 8.742123870849582,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 46.217359313964835,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -6.112901469940103,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.1248178160929605,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.439824090637332,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -5.799487693116234,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.10994059287786584,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -15.330427843201655,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -7.9325530776189535,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.9446066611639177,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -31.802803170982383,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 2.1257149832589306,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 6.867143903459819,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 18.36805075376075,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.9828187634172316,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.1162169137658484,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.9435607394877508,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -5.403667881416986,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.287803707977524,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -16.941038698305057,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.031408504355417644,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.17411638954043618,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.07848528659569631,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.1300010681152344,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.509998321533203,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -9.060001373291016,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -4.49614477524981,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -13.719562596001245,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -11.429442713841741,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -13.923156821466854,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 3.7937284084754834,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 5.6699748778315735,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -10.027071594179993,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 4.901542199450759,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.7706030166570805,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -5.554155005668626,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.806517516893251,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -22.763342095411566,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.9478367175448716,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -9.441619380735977,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -9.09472839587735,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -9.635665301792418,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 5.564773583267835,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 5.8691887315388875,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.4530000686645508,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.813500213623044,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -12.006000137329096,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.40839996337891193,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.4606000518798865,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -4.170600051879887,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -5.958721294414149,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.997397643129629,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.2573239283823483,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -5.302408532683501,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.622683491376719,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -10.449843020484227,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.10714312962123351,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.29214341299874436,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.1614295414515903,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.9321189940302279,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.2521677513687877,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 4.128456779775027,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -4.91983829089088,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.94529764802504,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -14.240807176044083,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.1682167454014699,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.14639584754936463,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.052722998276578004,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -5.5200042724609375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -6.1200103759765625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -21.20001220703125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.2333170307478047,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -6.968806662136762,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -4.598895147672499,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -6.944337289407243,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.6643524695891698,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.7149246089790182,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -4.211119766933146,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.5758567163685626,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -6.837823786902852,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.121468083216861,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.05164712417364825,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -15.869155384239232,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.3149910269571343,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.6908634468714943,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.2641808297081067,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.6568457697328074,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.10669270520318186,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.9141384626863323,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.0600006103515511,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.662499999999994,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -17.781999206542963,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.4460342407226676,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.4765899658203239,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -3.1542187500000125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.10698543548585349,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.603042068481443,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.25556728363037,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.539302736521198,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.9845901602154372,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.407247770921617,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.7404292298581314,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.5606667089387845,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -9.704111492921584,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.2973523270132254,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.941484682783547,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -14.54273880873762,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.16714259556361633,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.7114290509905139,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.8092847551618307,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.22471259695847312,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.5561510725135683,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.9557548674427117,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.7326753824064127,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.0297081069190934,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -10.495055548035271,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.2675311551976053,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.20165804676308352,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.05159418260161486,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.2700004577636719,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.75,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -4.110004425048828,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.934371049573803,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.474361418787352,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.3102744572949576,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.5950035366931745,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 10.721227706172819,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.11360323732263478,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.2553897303118395,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.10378442547240851,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -14.611431295321541,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.8302907656758238,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.03028468153336572,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -13.722754932172565,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.3860629918688638,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.8035817964779155,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.024439860669435,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 1.6924879829812616,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 12.49227288096517,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.3128170910299488,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.20550022125243572,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.9434997558593636,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.7745000839233427,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.00017051696777059533,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.040886306762686786,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.3853993225097696,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.06816030502319137,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.36464025497436836,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.8985038566589338,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.6194737884448251,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 3.9771740781018083,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -9.072275446360557,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.9568353870318078,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.7561337616511694,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -8.60992983088501,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.2795237095296637,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.312986005859763,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -10.78457921847886,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.013571058000837022,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.12571362086704796,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.38214220319475456,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.03118273628715551,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.2782145887041185,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.7250959658007026,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.8137682357193148,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.499286038131066,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -8.395496271788671,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.3590386587099991,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.24870633366436057,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.03220018677990022,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.5,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.18999862670898438,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.1199989318847656,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.6595025835303034,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.304146656453343,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.023550464976407337,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.3315627278910345,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.4194067530930434,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.30947113433374973,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.02509882414700737,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.3259395414428212,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 7.169227100484166,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.826376239482319,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.51545244459379,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.449832600840441,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.11119452582536438,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.9737965588119244,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.311163852987985,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 1.9559287917834012,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.3516384216993083,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.5086849880410638,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.15599994659424254,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.8399999618530316,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.814000511169432,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.005698013305668326,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.07560050964355725,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.1763726806640591,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.026928710937504263,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.14409442901611413,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.35202976226806726,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.1541979539917868,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.1779372251047526,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.4755756826364088,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.9046279503775123,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.19936744023536512,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 5.8876173588302,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.9860916035492764,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.06322953011645893,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 5.13418752046122,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.025000163487025606,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.022857393537248916,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.3492862156459263,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.0577833179234335,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.03357945185703959,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.533428987344791,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.84459458370989,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.32094362206145366,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.9210362768884566,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.28228723825797886,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.15180361407601173,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.4326748981863734,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.1199951171875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.2299957275390625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.019989013671875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.459036807033176,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -5.67225030723354,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.2047794397329392,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -5.668555884839554,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.4293034138074256,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.4522417322552319,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.2199584911368522,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.45823799640505314,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.3294622357847508,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.9862679215690289,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.3565342260532525,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.6559420579675628,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.089271250671763,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.394307091968272,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.1299348782314533,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.3810643651651189,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.34174176098492604,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.25302787854791786,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.0509994506835767,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.27700119018555824,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.1004974365234261,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.1828039550781284,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.4911355590820108,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -4.7873687744140625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.0076482391357330926,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.12614784240722088,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.5590050506591808,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.829081634970131,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.0916966736835407,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.0394664273552614,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.7412993855990488,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.6241580433635439,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.122299316467713,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.8098430767802487,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.940576460951693,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.9033030871463121,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.15571267264229904,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.05500030517578125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.9864305768694197,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.13171988037699034,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.07339255435941316,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.6048745206705568,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.8985408613228163,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.49553518955284304,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.6836465129629214,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.27857174314298305,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.020865468486632066,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.24065966153094864,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.970001220703125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.4499969482421875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 12.230010986328125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.0566823014497406,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.423808258042548,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.0862243068630919,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.4305007161615766,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.259523326914148,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.3669645482550683,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.09270402187977478,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.537833493860674,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.0339550528424963,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.9619656454996868,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.948389539713306,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.4538567801950055,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.49162575625519844,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.8541349572227195,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.4209386248274845,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 1.856990803512859,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.48847815212179624,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.1677506945477543,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.6115005493163892,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 3.4610000610351506,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 13.784502410888678,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.34167327880859943,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.7159664916992199,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 5.439056091308601,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.175176315307624,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.8773959350586154,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.946331634521499,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.8677182711340103,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.2008505898261976,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.0708665390200434,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.7639468164101659,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.3192842021782623,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.7682663471316324,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.7384656345221998,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.9354884375500028,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 5.595698722666542,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.13857051304408508,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.0642852783203125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.9478574480329245,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.08385832267030291,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.0390107177254988,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.3975323215713873,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.5114421606946973,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.23726507410802844,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.06939255296610769,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.35255782121043666,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.011626615300524334,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.16192729408436413,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.25,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.7099990844726562,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 5.3899993896484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.1459401443795647,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.6284887192075983,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.7386431240136604,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.6385843618614162,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.8153393175300403,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.4357428533360084,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.7821774118987213,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.4963268940870522,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.2770375386934143,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.5562584678344908,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.1252691610870853,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 4.052416779125357,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.40236791332537436,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 3.649454496057669,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.073357441978053,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 3.6489071578130194,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 3.586384492322392,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.236528999628694,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.2694999694824247,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.3364994049072294,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 6.650999450683599,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.17145248413085312,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.7134155273437557,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.8996244812011724,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.05334266662597997,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.2620679092407272,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.034932441711419,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.031339289985554686,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.3745034472610209,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.7711138480564825,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.0757136729046648,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.1050264771849339,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.982412857294926,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.2275070535832313,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.6949151006382408,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 5.115484263545823,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.012143271309988712,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.13285555158342643,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.4971417018345423,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.008308823895230244,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.17981167640727658,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.459542429028849,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.0,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.1420524514636377,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.46793386128416437,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.0514548595419676,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.06291604703191533,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.1415051265231082,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.8300018310546875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.8600006103515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.69000244140625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.126786714253425,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.442418689397831,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -3.3036658083400505,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -4.40460622971327,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.775423885314723,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -4.314098405273025,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.4629900222373777,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.560973802321255,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.2368486781312305,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.7240821557970696,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.2721703911962265,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -4.515430113609198,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.42152134345151415,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.1644754741325638,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.968951490375658,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.11711471003883478,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.0043787105223707,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -4.114884551565712,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.18450012207031818,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.822000122070321,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 6.311000823974609,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.06985046386718352,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.4897785949707014,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.2366143798828091,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.011356735229497872,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.023732414245614564,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.36914398193358977,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.717684336079195,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.055088089004832,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.387104167710663,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.6721139200530644,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.9713798707045713,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.0317919898747103,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.5800071556891782,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.4636955345275213,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.524723442669664,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.07714353288923004,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.000713348388671875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.147857666015625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.09829505264243066,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.052091788400582484,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.9309865895633227,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.4959550426411616,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.337938827387087,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.8779484890708233,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.32282135118338906,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.051033414712382985,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.05978619016430997,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.8700027465820312,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.5400009155273438,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -3.2699966430664062,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.7710729397186773,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.173015736950658,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.51200450131872,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -4.2247120720811715,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -7.584567674561282,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.7172972568617597,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.4927766228218786,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.699509823745692,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.090711290784041,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.320962274629179,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.8405407814228827,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -7.701986563482066,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.2227648820137382,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.10492747831460925,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.8227098166456726,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.06277944759326415,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -5.813522499768931,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.9165111105690738,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.1634998321533203,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.8259998321533146,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -6.246999359130854,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.09683975219726904,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.37799743652344375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.451080932617188,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.060876235961913494,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.23259300231933366,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.0601799392700144,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.615618321417922,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.280547506929274,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.748297878489947,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.6240495486160467,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.15538734007978228,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.7815027850290202,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.6197431632179455,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.28364033167890224,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.9998688999757426,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.1321427481515065,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.0003569466727117998,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.6307144165039062,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.15845568693913892,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.011113678033003893,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.6365750536840264,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.6296320231651622,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.4705890331392908,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.8496702771820486,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.0006391680593103022,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.19200207977147166,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.12538957674207707,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.07999801635742188,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.3299980163574219,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.759998321533203,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.3433446974712151,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.348608435054155,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.195385783146775,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.3563077294527437,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.4787976808914518,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.4021639911369177,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 2.3376400017634857,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.4845445248914624,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 4.951514376523747,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 2.5582206223432324,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 4.361800606409128,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 13.908177012797662,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 1.204963360233724,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.9293347802111125,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 4.5301001011111675,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 2.931183790221692,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.2498428556838035,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.6013778448442317,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.13799991607666584,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.5354999542236385,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.5974998474121094,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.02708900451660412,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.15017807006836392,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.06620223999023978,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.008771533966061895,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.03865337371826172,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.11768743515014535,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.1414046917870504,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.5079629645381445,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.26549635357810963,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.12298307849945012,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.4116835377728334,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 6.437142026271914,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.16223828207522217,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.6640370536795892,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 6.0361584968468,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.004999978201729927,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.03642872401646202,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.07928575788225445,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.008865333526135055,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.09351109764748644,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.2830943208853427,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.0,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.4468894482402619,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 9.993265854628797,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.17788114650010156,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.29201225990999813,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.045693756745959546,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.11999893188476562,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.3899993896484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.5800018310546875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.2929896553388822,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.724994675391578,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.8917924665648558,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.7145612220232143,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.1651303010549303,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.27728048679775963,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.9495760145829424,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.29704346785015545,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 8.351645481927928,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.26843166939035656,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.45330030068945204,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 7.536212844301172,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 1.2553184023660569,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.5529485398736895,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.2265067845292483,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 2.5729302976512214,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.3940851262625786,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.07806663309044559,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.12900009155273295,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.6504999160766616,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.1074998855590863,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.013733673095700283,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.0785369873046875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.2969304656982459,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.01897304534912081,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.10439422607421989,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.34530630111694194,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.5785828253155101,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.451426724512684,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.0567682698091385,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.3158099626641597,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.1110279307133597,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 6.744747529974859,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.32475216209815194,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.1601430499386556,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 5.217125641038933,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.0010713849748883453,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.06228583199637283,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.08757128034319195,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.006666782480615696,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.12579328444294258,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.11280913425163153,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.2659550858277293,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.8643603698599289,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 6.74220937267329,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.21372747584305174,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.44632752243823504,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.22146945667677165,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.7599983215332031,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.4699974060058594,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.5200004577636719,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.244933754904498,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.3607736276776823,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.5140202736547037,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.315700974472735,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.4165603854427666,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -5.830935069327836,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.5520564674346815,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -6.058678899710324,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.4738620135391178,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.519937384134453,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.64888300858497,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -3.2765214515719565,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.303374302800441,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.9171695875875852,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.8206940443096888,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.9717905452017006,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.35448478934958505,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -5.631721215620521,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.026000022888183594,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.5045000076293888,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.6000001907348604,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.014595489501949999,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.006874618530275711,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.12781814575195227,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.014123649597166832,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.07920082092284986,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.42515079498291186,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.5041154583221306,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.8006344006481285,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -4.1099711414422035,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.4647227455359735,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.9041295742237017,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.2734257849218333,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.5204762227519097,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.047768424935682,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.17896932221808104,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.019999912806919706,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.0400000980922155,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.32214246477399555,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.06807732501589436,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.13239588629818555,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.611380275689666,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.4100153989203612,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.727267837460212,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.12277842644398174,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.5648338020324778,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.189694254055223,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.4096335652969286,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -24.850006103515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -25.510009765625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -86.56002807617188,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.119619736413936,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -10.15960919526554,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -6.711479831718104,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -10.145852031432025,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.1221257536637061,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.9626052961850817,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -5.956337157153191,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.7441443610789467,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -7.801234222518916,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -4.08993114011278,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.49791083175437834,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -15.311280505900983,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.5713116787089971,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -5.881665980000273,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -4.376765513753711,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -5.8583605117575885,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.6489194211286455,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.1618191498923953,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -4.328001403808571,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -17.949000549316338,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -84.85150909423828,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.102200317382767,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -6.619398803710851,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -20.643400268554615,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.2922000122069903,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.9864500427246412,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 11.89114959716801,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -4.045108535141818,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.7629031101141894,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.7173471054072085,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -4.128037833167099,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.548987494994172,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -12.010602531321247,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -4.7925478176788605,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -5.220389756913358,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -18.942186040928778,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.5657130650111597,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.4478541782924097,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 11.767139979771205,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.4234984297000306,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.8172265268163192,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.0953927706330395,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.92017749588911,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.02429543826014,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -13.655154557878834,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.17626157598748493,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.4140835733257072,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.2101289759422308,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -4.82000732421875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 5.8300018310546875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -19.490005493164062,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.531172852282083,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.8269029161891,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.154090072524062,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.9997799933848546,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 13.375590287357708,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.6815681076178137,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.9956677672837477,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.5950522938552041,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -17.73841990156162,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.644555905023983,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.5372316149318666,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -19.72713770481687,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.9828647945771438,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.4510402990761673,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.18062424544033062,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 1.2877115262895806,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 15.146635462150059,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.8807819613251269,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.9745002746582259,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.442500305175798,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.1554985046386719,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.1994522094726392,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.010516967773441,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.070665283203141,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.2076731872558355,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.1291758728027332,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 5.987526893615723,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.04212640162651,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 5.16999134631415,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -10.912166983833005,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.436041129395106,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 3.5553850980780783,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -11.421066243265566,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.928563518834948,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.7179995463331386,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -15.490447310936716,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.05428641183035676,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.375003269740513,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.179284232003348,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.054831756718539904,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.3234147514573893,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.9066653482832785,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.3528298886352665,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.8458468289002337,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -11.690742821207067,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.056455288825314365,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.5432428298700136,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.024434151686854366,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -14.40997314453125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.560028076171875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -23.97998046875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -5.573493187669287,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -5.080887873052853,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -4.606303660880928,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -5.291828303732049,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 7.468376983736391,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.0763362818628774,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -4.491839700735733,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.0077516799491537,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -3.3246743219747743,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.3108710418572755,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.3711772876845458,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -11.377632078934296,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -4.025185129964348,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.8029446577875854,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.2715893429165357,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.0043367840576134,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 9.239422158528743,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.2755501355701915,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.198999023437466,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.101498413085892,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -5.358003234863247,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.327799682617183,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -6.3055993652344,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -14.790399780273447,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.06375000000002728,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.4791998291015602,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 5.389649505615239,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.4679660619430726,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.1515831683085347,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -4.886665346568708,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.3713741430778983,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.6179332622770612,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.5395898037790516,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.6252021637051435,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.03172053455308088,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -7.328432331831703,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.529998779296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.6628570556640625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 4.054288591657366,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.2834525059655659,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.4669227798738169,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.283697195449915,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.30064904203895,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.1282761678034774,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -5.492688901528631,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.19356711443927466,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.017039805020137577,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.09121839047323688,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.7600021362304688,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.9199981689453125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -138.00999450683594,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.154489762974565,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -6.360870508554884,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.834606646076431,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -6.346670507550522,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.8326606975346835,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -3.518624151441385,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.8943923486593128,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.6414138808575247,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 4.594291579999776,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.143431678259267,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 3.258075024550177,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.6503763714146977,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.6061817052696261,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.082927293289616,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.5001076718879616,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.059178987876087,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.0616155227423318,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -3.319410297734071,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.024833297729486503,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.7291664123535213,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -138.06383171081544,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.10732498168945881,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.3448196411132898,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -151.90899169921875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.037579383850086856,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.15096637725829964,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -153.8609832763672,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.5446930509759325,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.809500656938991,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.36036913495605116,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.3489360637596435,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.2338789204728093,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 5.733882401095558,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.275787000845419,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.3456531623161636,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.5723376144591068,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.07761928013392883,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.000713348388671875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.183573041643415,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.18284547092817016,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.07988051831545295,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.4357309933876874,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.06788233298587976,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.0989001649573602,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.965347243099526,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.13170678748471365,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.01357933983823989,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.38029187516200424,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.1700000762939453,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.980001449584961,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.980001449584961,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.9591838597976645,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -9.66913389432248,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -4.522937881653511,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -9.408327648772886,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -8.149045346768236,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.1463094757862002,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -4.400940352127025,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.1463094757862002,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.12999513182619,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -4.399734724852022,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.7836788136165183,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -14.519573719546363,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.41087580209272545,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -5.391190679057212,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.1882235636891183,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -5.12083612909845,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -6.378000171975884,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.9470956220788866,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.09900007247924592,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.25150012969970703,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.2475000381469705,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.0834000396728527,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.26520004272460795,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.4188999938964812,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.019700002670290928,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.0929500102996812,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.3589750099182112,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.6127863849644832,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -5.8180273539537914,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.447009314742453,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.5154254356844046,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -5.556891972216116,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.150691744660559,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.574247986376312,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -5.874567907976525,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -5.116398400204337,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.02857140132359115,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.012857028416225047,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.40385723114013683,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.25223461492876886,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.297148015174181,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.5991799625054095,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.608882224781084,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.7617020030325072,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.7617020030325072,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.1473981159915022,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.889494130350606,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.15719027406471664,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.209991455078125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.410003662109375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -11.779998779296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.0152045360368844,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -5.013623824621316,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -3.7261279750310683,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -5.073503469507723,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.5490563704695481,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 5.690124807251196,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.527885215694093,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 5.323806420135268,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -3.0743835726257718,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.0708961722921586,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.4490644345939838,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -29.46665131292108,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.5331035216680546,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.7356806093560486,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.3914136570666757,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.7860119498332874,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 3.3201015452619,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 5.88933866095851,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.5889999389648324,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.0749999999999886,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -8.373498535156244,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.2451998901367176,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.0119998168945301,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.3971994018554597,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.15085002899169808,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.6968500137329272,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.2772001647949196,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.667221688374143,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.9163903494444403,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.3359944310319958,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.8328316985736883,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.293871438218817,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -6.400428356482134,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.4455470178987397,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.5747905640877136,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -11.367434997715776,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.12285723005022309,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.44357081821986544,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.1571469988141736,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.15939274384006996,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.3293633731162493,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.9922868514473535,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.8354345395853002,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.8062231499972423,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -6.735661741899534,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.2586585347135826,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.3940828857379668,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.011738381653249808,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.value",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -53.59000000000003,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_1d_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -1.2527218782454996,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_5d_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -4.133716392392239,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_20d_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -4.283554615415531,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_60d_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -6.979199467570085,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma20",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -38.52399768066414,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma50",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -8.508378369140587,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma200",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": 3.400496350097683,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma20_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -2.2954373641510766,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma50_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -6.307115065971457,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma200_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -8.39108141026843,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_sma",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": 6.676435546874998,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": 1.1510548672431846,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.drawdown_from_63d_high_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -7.054471986745591,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.volume_vs_previous20_ratio",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -0.14304748410364576,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.value",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -57.52000061035156,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_1d_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -3.321769334127,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_5d_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -13.293121054093572,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_20d_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -20.625509197341742,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_60d_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -24.77346856456445,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma20",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -27.28399945068361,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma50",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -8.771214526367203,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma200",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -0.23504751281740255,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma20_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -16.03444729766107,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma50_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -23.02358569633839,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma200_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -28.110188517449174,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_sma",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": 5.385711539132255,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": 4.4739367710486215,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.drawdown_from_63d_high_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -24.042801910065624,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.volume_vs_previous20_ratio",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": 0.8357374586607809,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.value",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -57.250001831054675,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_1d_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -7.858008964264274,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_5d_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -31.618570753879872,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_20d_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -8.366917976699861,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_60d_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -16.458365643325823,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma20",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -17.96199884033203,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma50",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -13.760366857910157,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma200",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": 1.3743528656005992,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma20_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -18.120605237150123,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma50_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -18.886071009457083,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma200_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -21.547323738120074,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_sma",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": 6.85171565464565,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": 5.369442539113479,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.drawdown_from_63d_high_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -18.823466430637104,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.volume_vs_previous20_ratio",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -0.5980021229767766,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.value",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -8.969999999999999,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_1d_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": 1.3564415836286425,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_5d_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -1.7347533577744434,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_20d_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -6.3547276704095985,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_60d_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -10.801419422890135,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma20",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -4.764499221801756,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma50",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -0.9385998291015625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma200",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": 0.27413864746093,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma20_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -4.078851126291461,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma50_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -7.567861602653703,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma200_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -9.855698562685731,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_sma",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": 0.1564291163853233,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": 0.41347898723291454,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.drawdown_from_63d_high_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -7.961303049414948,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.volume_vs_previous20_ratio",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -0.6824772053670715,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.value",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -0.6699975585937494,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_1d_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -1.7961882123735395,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_5d_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -2.33690131665909,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_20d_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": 0.07031743658660883,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_60d_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": 2.2386210827928026,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma20",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": 1.9744995422363303,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma50",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -0.26391768188476306,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma200",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": 0.3439789039611867,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma20_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -3.7350362382839952,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma50_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -0.5620823220072957,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma200_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": -1.452656803351915,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_sma",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": 0.2782152666364399,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": 0.4017843543586064,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": 2.4276543590787907,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.volume_vs_previous20_ratio",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-11-16",
        "change": 0.5773746037376194,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS2.value",
    "available_prior_observations": 20,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-12",
        "to": "2026-11-13",
        "change": 0.019999999999999574,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-13",
        "change": 0.41999999999999993,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-15",
        "to": "2026-11-13",
        "change": 0.11000000000000032,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLH0A0HYM2.value",
    "available_prior_observations": 20,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-12",
        "to": "2026-11-13",
        "change": 0.029999999999999805,
        "unit": "percentage_points"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-13",
        "change": -0.25,
        "unit": "percentage_points"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-15",
        "to": "2026-11-13",
        "change": 0.0,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLC0A0CM.value",
    "available_prior_observations": 20,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-12",
        "to": "2026-11-13",
        "change": 0.0,
        "unit": "percentage_points"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-13",
        "change": -0.040000000000000036,
        "unit": "percentage_points"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-15",
        "to": "2026-11-13",
        "change": 0.050000000000000044,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS10.value",
    "available_prior_observations": 20,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-12",
        "to": "2026-11-13",
        "change": 0.05000000000000071,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-13",
        "change": 0.3100000000000005,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-15",
        "to": "2026-11-13",
        "change": 0.05000000000000071,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DFII10.value",
    "available_prior_observations": 20,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-12",
        "to": "2026-11-13",
        "change": 0.050000000000000266,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-13",
        "change": 0.31000000000000005,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-15",
        "to": "2026-11-13",
        "change": 0.13000000000000034,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.T10YIE.value",
    "available_prior_observations": 20,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.040000000000000036,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": -0.029999999999999805,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": -0.1499999999999999,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.STLFSI4.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.03059999999999996,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.CBOE_VIX.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 3.6099999999999994,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.9899999999999984,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 4.469999999999999,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.GPRD.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-16",
        "change": 75.60165405273438,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.GPRD_ACT.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-16",
        "change": 86.13592529296875,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.GPRD_THREAT.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-16",
        "change": 86.85680389404297,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.GPRD_MA7.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-16",
        "change": -13.762054443359375,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.GPRD_MA30.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-16",
        "change": -33.277984619140625,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "observed.Treasury2Y.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "observed.Treasury10Y.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "observed.SPY.low",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "observed.SPY.high",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "observed.QQQ.low",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "observed.QQQ.high",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "observed.SMH.low",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "observed.SMH.high",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "observed.NVDA.low",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "observed.NVDA.high",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "observed.MU.low",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "observed.MU.high",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "observed.XLP.low",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "observed.XLP.high",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "observed.XLF.low",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "observed.XLF.high",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "observed.XLV.low",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "observed.XLV.high",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  }
]
```

## 判断依据 · 反弹是否可靠

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 反弹是否可靠 |
| 事实指标引用 | ["prices.QQQ.sma200", "prices.SPY.value", "prices.QQQ.value", "prices.RSP.return_1d_pct", "observed.SPY.low", "observed.QQQ.low", "observed.premarket.SPY", "observed.premarket.QQQ"] |
| 推断与解释 | 推断：盘前反抽但仍低于第一修复区，可靠性未确认。 |
| 反证与缺口 | 仍可能出现空头回补；没有本轮分钟数据证明常规VWAP或回踩。 |
| 确认条件 | SPY先收复747.89–749.82，QQQ671.71–672.15；回踩形成更高低点且收盘站稳，RSP/IWM同步改善、涨跌家数扩散。进一步看SPY20日757.69、QQQ200日681.41；第一段反抽只是修复。 |
| 失效条件 | SPY跌破16日低738.07、QQQ660.48且反抽失败，或突破后又收回区间下方 |
| 观察期限 | 11月17–20日；财报后按实际新信息复核 |
| 条件式指导 | 按确认、失效和事件风险分批评估；无法承受财报跳空则等待事件落地，不依据低价本身升级。 |
| 主观置信等级 | medium |
| 判断变化原因 | 同一16日完整收盘；新增17日晚间盘前价格与治理公告、CNN31；确认阈值仍待常规时段验证。 |

## 判断依据 · AI合约与现实压力是否一致

| 要素 | 记录 |
| --- | --- |
| 评估问题 | AI合约与现实压力是否一致 |
| 事实指标引用 | ["prices.NVDA.return_1d_pct", "prices.CRWV.return_1d_pct", "prices.SMH.sma200"] |
| 推断与解释 | 推断：股价风险折价与政策压力强化；专门泡沫合约尚未证明全行业现金流崩塌。 |
| 反证与缺口 | H100价格高不等于股票见底；财报跳空可越过止损，杠杆ETF每日重置存在路径损耗。 |
| 确认条件 | SMH收复16日高473.33并回踩守稳；NVDA先158.39再163.20，MU先739.12再750.25；相对SPY转强、更多芯片同行跟随，财报后次日收盘承接才升级。 |
| 失效条件 | SMH460.64、NVDA155.01、MU716.38再失且反抽失败；或明确订单/回款/融资恶化。 |
| 观察期限 | 11月17–20日；财报后按实际新信息复核 |
| 条件式指导 | 按确认、失效和事件风险分批评估；无法承受财报跳空则等待事件落地，不依据低价本身升级。 |
| 主观置信等级 | medium |
| 判断变化原因 | 同一16日完整收盘；新增17日晚间盘前价格与治理公告、CNN31；确认阈值仍待常规时段验证。 |

## 判断依据 · 哪些板块优先观察

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 哪些板块优先观察 |
| 事实指标引用 | ["prices.XLF.value", "prices.XLV.value", "prices.XLP.sma20"] |
| 推断与解释 | 推断：防御/金融相对强，但只有少数绝对上涨；排序不等于买点或资金净流入。 |
| 反证与缺口 | XLP收盘低于开盘，XLV/XLF仍下跌；相对抗跌不自动成为买点。 |
| 确认条件 | XLP92.38、XLV187.60、XLF57.89是16日低点参考；回踩守住后再突破各自16日高93.48/191.33/58.81，且收盘维持相对领先。支撑不是保证，按实际波动修订。 |
| 失效条件 | 关键低点破位且无法收复、相对强度反转；金融另看信用扩散。 |
| 观察期限 | 11月17–20日；财报后按实际新信息复核 |
| 条件式指导 | 按确认、失效和事件风险分批评估；无法承受财报跳空则等待事件落地，不依据低价本身升级。 |
| 主观置信等级 | medium |
| 判断变化原因 | 同一16日完整收盘；新增17日晚间盘前价格与治理公告、CNN31；确认阈值仍待常规时段验证。 |

## 判断依据 · 是否为全面恐慌或过热

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 是否为全面恐慌或过热 |
| 事实指标引用 | ["prices.^VIX.value", "prices.^VIX3M.value", "macro.BAMLH0A0HYM2.value", "observed.Treasury10Y.value", "observed.CNN.value"] |
| 推断与解释 | 推断：风险收缩加重；曲线接近平坦，信用资料滞后，无法断言系统性恐慌。 |
| 反证与缺口 | CNN31为恐惧但非机械买点；VIX盘前回落不代表信用已经改善，利率与信用时间滞后。 |
| 确认条件 | VIX/短期期限结构、当期信用利差与市场广度持续同步恶化才升级风险判断。 |
| 失效条件 | 价格收复、广度扩散且信用与波动同步稳定，撤销恐慌升级假设。 |
| 观察期限 | 11月17–20日并随新信用数据更新 |
| 条件式指导 | 同时观察股、债、波动与信用；不把单一阈值机械转换成仓位。 |
| 主观置信等级 | medium |
| 判断变化原因 | 同一16日完整收盘；新增17日晚间盘前价格与治理公告、CNN31；确认阈值仍待常规时段验证。 |

## AI政策、治理与现金流兑现 · 待核验

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | NVDA新增合规监督委员会，今晚财报将检验经营兑现 |
| 事实：市场反应 | 盘前NVDA约+1.24%、SMH+1.53%、MU+2.14%，低于首道修复位 |
| 推断：解释 | 推断：存在空头回补与治理改善预期；无法区分各驱动贡献，财务风险未解除 |
| 受益篮子 | ["现金流稳健且能验证需求的软件/云公司，条件观察"] |
| 受损篮子 | ["半导体、算力融资、高杠杆主题"] |
| 反证 | H100租价仍高，需求崩塌未验证 |
| 下一催化剂 | 17日NVDA结果、订单回款与指引 |
| 证据 | ["https://nvidianews.nvidia.com/news/nvidia-board-of-directors-establishes-national-security-and-export-control-oversight-committee", "https://www.bis.gov/press-release/bis-issues-rule-addressing-remote-access-american-super-intelligence-technology", "https://www.bis.gov/media/documents/rin-0694-ak50.pdf", "https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/default.aspx", "https://www.silicondata.com/products/silicon-index/h100"] |

## 利率下降没有换来股市止跌 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 零售、进口价格与工业生产今晚发布；此前利率下降未换来股市止跌 |
| 事实：市场反应 | 盘前股指小幅反抽，当前美债收益率缺失 |
| 推断：解释 | 推断：折现率只是变量之一，盈利和风险溢价仍主导 |
| 受益篮子 | ["高质量现金流，待价格确认"] |
| 受损篮子 | ["长久期高预期股票"] |
| 反证 | 单日共振不构成因果识别 |
| 下一催化剂 | 17日08:30零售/进口价格、09:15工业生产，18日FOMC纪要 |
| 证据 | ["https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value_month=202611&type=daily_treasury_yield_curve", "https://www.federalreserve.gov/newsevents/speech/warsh20261116a.htm", "https://www.federalreserve.gov/newsevents/2026-November.htm"] |

## 防御相对占优，绝对承接有限 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 19ETF中仅必需消费和公用事业上涨 |
| 事实：市场反应 | 16日防御相对领先，17日盘前芯片反抽而IWM仍弱 |
| 推断：解释 | 推断：避险偏好比全面风险回归更明显 |
| 受益篮子 | ["XLP", "XLV", "XLF", "XLU"] |
| 受损篮子 | ["SMH", "XLK", "ARKX"] |
| 反证 | 不同报价时点，不能直接推断全市场广度或新净流入 |
| 下一催化剂 | 下一交易日回踩和收盘 |
| 证据 | ["https://finance.yahoo.com/quote/XLP/", "https://www.ici.org/research/stats/etf_flows"] |

## 油价与航运风险分化 · 待核验

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | AP报道巴林雷达设施遭攻击；停火合约规则另查 |
| 事实：市场反应 | 盘前原油约反弹1.5%，停火22日档66.5% |
| 推断：解释 | 推断：地缘溢价可能回升，但单一报道与价格共振不证明因果 |
| 受益篮子 | ["运输/消费者仅为油价下降条件受益"] |
| 受损篮子 | ["XLE", "XOP", "OIH"] |
| 反证 | 停火合约上涨不等于实际运输恢复 |
| 下一催化剂 | 可核验过境量、供应与指定合约价格 |
| 证据 | ["https://apnews.com/article/582e0b5d51be06f0ed630fac24f39b72", "https://www.matteoiacoviello.com/gpr.htm"] |

## AI融资市场接受度 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | Anthropic拟上市临近 |
| 事实：市场反应 | 低于1.25万亿档36.35%，较早报+3.10pp |
| 推断：解释 | 推断：部分合约风险偏好转弱，不是已完成IPO定价 |
| 受益篮子 | ["以发行文件和真实回款验证的公司"] |
| 受损篮子 | ["依赖持续融资的算力链"] |
| 反证 | 分档不完整、私募承诺有条件 |
| 下一催化剂 | 18/19日指示日程及实际公告 |
| 证据 | ["https://www.sec.gov/Archives/edgar/data/2130357/000162828026073040/anthropicpbc-fwpxeeaprospea.htm"] |

## 航天与工业暂缺价格确认 · 减弱

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 继续监测Starship规则与上市公司订单映射 |
| 事实：市场反应 | ARKX−4.00%、ITA−2.46%、XLI−1.85% |
| 推断：解释 | 推断：工程叙事尚未转为篮子相对承接 |
| 受益篮子 | ["有明确订单且价格确认的供应商，未选定"] |
| 受损篮子 | ["无订单映射的概念交易"] |
| 反证 | 低质量预测盘口不证明技术或盈利突破 |
| 下一催化剂 | 官方进度及订单披露 |
| 证据 | ["https://www.spacex.com/", "https://finance.yahoo.com/quote/ARKX/"] |

## tc 报价（供应商时戳不等于成交时戳）

| 标的 | 价格 USD | 变化% | 观测时间 | 供应商时间 | 抓取时间 | 质量 |
| --- | --- | --- | --- | --- | --- | --- |
| SPY | 741.23 | 缺失 | 2026-11-17T12:00:19+00:00 | 2026-11-17T12:00:19+00:00 | 2026-11-17T12:00:21.933201+00:00 | ok |
| QQQ | 665.43 | 缺失 | 2026-11-17T12:00:19+00:00 | 2026-11-17T12:00:19+00:00 | 2026-11-17T12:00:21.933201+00:00 | ok |
| SMH | 468.96 | 缺失 | 2026-11-17T12:00:18+00:00 | 2026-11-17T12:00:18+00:00 | 2026-11-17T12:00:21.933201+00:00 | ok |
| RSP | 218.90 | 缺失 | 2026-11-17T11:44:12+00:00 | 2026-11-17T11:44:12+00:00 | 2026-11-17T12:00:21.933201+00:00 | stale |
| IWM | 272.26 | 缺失 | 2026-11-17T12:00:15+00:00 | 2026-11-17T12:00:15+00:00 | 2026-11-17T12:00:21.933201+00:00 | ok |
| NVDA | 158.08 | 缺失 | 2026-11-17T12:00:19+00:00 | 2026-11-17T12:00:19+00:00 | 2026-11-17T12:00:21.933201+00:00 | ok |
| MSFT | 516.75 | 缺失 | 2026-11-17T12:00:16+00:00 | 2026-11-17T12:00:16+00:00 | 2026-11-17T12:00:21.933201+00:00 | ok |
| AMZN | 259.98 | 缺失 | 2026-11-17T12:00:13+00:00 | 2026-11-17T12:00:13+00:00 | 2026-11-17T12:00:21.933201+00:00 | ok |
| GOOGL | 284.50 | 缺失 | 2026-11-17T12:00:14+00:00 | 2026-11-17T12:00:14+00:00 | 2026-11-17T12:00:21.933201+00:00 | ok |
| META | 624.85 | 缺失 | 2026-11-17T12:00:05+00:00 | 2026-11-17T12:00:05+00:00 | 2026-11-17T12:00:21.933201+00:00 | ok |
| MU | 734.40 | 缺失 | 2026-11-17T12:00:19+00:00 | 2026-11-17T12:00:19+00:00 | 2026-11-17T12:00:21.933201+00:00 | ok |

## 核心行情与风险代理

| 标的 | 价格/指数 | 单位 | 观测日 | 1日% | 5日% | 20日% | 质量 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 739.95 | USD_per_share | 2026-11-16 | -1.91 | -1.69 | -3.46 | ok |
| IWM | 272.94 | USD_per_share | 2026-11-16 | -1.66 | -3.39 | 0.61 | ok |
| RSP | 218.93 | USD_per_share | 2026-11-16 | -1.01 | -0.91 | 2.59 | ok |
| GLD | 352.93 | USD_per_share | 2026-11-16 | -0.71 | -7.01 | -7.05 | ok |
| GC=F | 3,853.00 | USD_per_troy_ounce | 2026-11-16 | -0.86 | -6.36 | -7.38 | ok |
| CL=F | 85.72 | USD_per_barrel | 2026-11-16 | -3.21 | -1.30 | -17.31 | ok |
| BZ=F | 92.44 | USD_per_barrel | 2026-11-16 | -3.55 | -0.14 | -15.62 | ok |
| TLT | 79.38 | USD_per_share | 2026-11-16 | 0.00 | -3.15 | 0.32 | ok |
| UUP | 29.56 | USD_per_share | 2026-11-16 | 0.20 | 2.04 | 1.93 | ok |
| HYG | 76.73 | USD_per_share | 2026-11-16 | -0.27 | -1.01 | 0.39 | ok |
| LQD | 102.80 | USD_per_share | 2026-11-16 | -0.01 | -1.79 | 0.31 | ok |
| ^VIX | 22.91 | index | 2026-11-16 | 18.70 | 15.01 | 24.24 | ok |
| ^VIX3M | 23.02 | index | 2026-11-16 | 11.64 | 10.41 | 17.45 | ok |
| ^VVIX | 114.23 | index | 2026-11-16 | 12.51 | 16.05 | 6.83 | ok |
| ^MOVE | 101.28 | index | 2026-11-16 | 2.52 | 9.17 | 0.18 | ok |
| MSFT | 517.99 | USD_per_share | 2026-11-16 | -1.12 | -4.99 | -2.91 | ok |
| AMZN | 257.75 | USD_per_share | 2026-11-16 | -3.34 | -3.44 | -1.79 | ok |
| GOOGL | 283.72 | USD_per_share | 2026-11-16 | -4.07 | -1.54 | -17.57 | ok |
| META | 626.41 | USD_per_share | 2026-11-16 | -2.38 | -2.33 | -11.20 | ok |
| CRWV | 49.88 | USD_per_share | 2026-11-16 | -6.12 | 1.84 | -18.39 | ok |
| MU | 719.02 | USD_per_share | 2026-11-16 | -7.62 | -1.93 | -20.54 | ok |
| DRAM | 39.27 | USD_per_share | 2026-11-16 | -7.38 | -6.01 | -18.75 | ok |
| QQQ | 661.75 | USD_per_share | 2026-11-16 | -2.67 | -2.59 | -7.88 | ok |
| NVDA | 156.14 | USD_per_share | 2026-11-16 | -4.12 | -12.61 | -28.08 | ok |
| VRT | 188.67 | USD_per_share | 2026-11-16 | -6.63 | -5.89 | -8.45 | ok |

## 跨资产风险解释

风险偏好仍偏弱，盘前只有初步降温，不能称风险消除或市场过热。CNN官网17日06:45:31纽约时间显示31/恐惧，前收盘也是31；API仍418，本轮以可见官方页面核验，未用代理指数替代。VIX在11:45 UTC约22.49，低于16日22.91，但VIX3M23.02、VVIX114.23、MOVE101.28仍是16日收盘，不能混时计算当前期限结构。16日同日VIX/VIX3M约0.995，接近平坦。
盘前11:50 UTC附近WTI86.24、Brent92.94较16日日线84.96/91.59约+1.51%/+1.47%，黄金3873.30接近16日3873。连续合约与交易所正式结算不同；并列观察美元、原油和黄金，不制造战争或避险统一指数。财政部16日2年4.83%、10年5.12%，本次^TNX报价也停16日，不能当盘前利率已下行；FRED信用仍13日HY323bp、IG89bp，金融压力6日−0.4918，均是滞后证据。GPR16日189.55是新闻报道密度。
AP17日10:07UTC可见摘要报道伊朗无人机攻击巴林美军雷达设施，全文访问失败，保留为报道线索，未独立核验损害。更不能把伊朗攻击巴林自动算成“美国打击伊朗领土”的专门停火合约失败。伊朗22日合约66.5%，较早报−6pp；海峡年底正常通行档仍4.5%，两种规则不等价。来源：[AP](https://apnews.com/article/582e0b5d51be06f0ed630fac24f39b72)、[CNN](https://edition.cnn.com/markets/fear-and-greed)。

## 宏观与地缘风险指标

| 指标 | 数值 | 单位 | 观测日 | 20次观测变化 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- | --- |
| DGS2 | 4.88 | percent | 2026-11-13 | 0.11 | lagged | https://fred.stlouisfed.org/series/DGS2 |
| BAMLH0A0HYM2 | 3.23 | percentage_points | 2026-11-13 | -0.08 | lagged | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| BAMLC0A0CM | 0.89 | percentage_points | 2026-11-13 | 0.04 | lagged | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| DGS10 | 5.15 | percent | 2026-11-13 | 0.05 | lagged | https://fred.stlouisfed.org/series/DGS10 |
| DFII10 | 2.91 | percent | 2026-11-13 | 0.13 | lagged | https://fred.stlouisfed.org/series/DFII10 |
| T10YIE | 2.20 | percent | 2026-11-16 | -0.15 | ok | https://fred.stlouisfed.org/series/T10YIE |
| STLFSI4 | -0.49 | index | 2026-11-06 | 0.46 | lagged | https://fred.stlouisfed.org/series/STLFSI4 |
| CBOE_VIX | 22.91 | index | 2026-11-16 | 4.47 | ok | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| GPRD | 189.55 | index | 2026-11-16 | 47.79 | ok | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_ACT | 215.96 | index | 2026-11-16 | 111.83 | ok | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_THREAT | 195.14 | index | 2026-11-16 | 9.03 | ok | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_MA7 | 145.08 | index | 2026-11-16 | -28.92 | ok | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_MA30 | 151.47 | index | 2026-11-16 | -13.58 | ok | https://www.matteoiacoviello.com/gpr.htm |

## CNN Fear & Greed

31/恐惧；CNN官方页面观测2026-11-17 06:45:31 America/New_York（北京19:45:31），本轮12:01UTC经浏览器核验；API418，页面恢复可读。

## 19 板块与主题 ETF：价格量能证据

| 标的 | 板块 | 1日% | 5日% | 20日% | 相对SPY 1日pp | 相对SPY 5日pp | 相对SPY 20日pp | 成交量/前20日 | 观测日 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLK | 科技 | -3.24 | -3.58 | -11.40 | -1.33 | -1.89 | 缺失 | 1.05 | 2026-11-16 |
| XLE | 能源 | -1.96 | 2.83 | -6.06 | -0.04 | 4.52 | 缺失 | 0.86 | 2026-11-16 |
| XLF | 金融 | -0.85 | 0.33 | 5.67 | 1.06 | 2.02 | 缺失 | 1.17 | 2026-11-16 |
| XLI | 工业 | -1.85 | -1.91 | -0.61 | 0.06 | -0.22 | 缺失 | 1.04 | 2026-11-16 |
| XLV | 医疗 | -0.51 | -0.24 | 6.96 | 1.40 | 1.45 | 缺失 | 0.87 | 2026-11-16 |
| XLP | 必需消费 | 0.27 | 1.88 | 6.18 | 2.18 | 3.57 | 缺失 | 1.01 | 2026-11-16 |
| XLY | 可选消费 | -1.53 | -2.36 | 3.22 | 0.39 | -0.67 | 缺失 | 0.98 | 2026-11-16 |
| XLC | 通信 | -1.72 | -0.50 | -2.97 | 0.19 | 1.19 | 缺失 | 0.78 | 2026-11-16 |
| XLU | 公用事业 | 0.18 | 0.75 | 6.67 | 2.09 | 2.45 | 缺失 | 0.73 | 2026-11-16 |
| XLRE | 房地产 | -0.27 | -0.87 | 6.19 | 1.64 | 0.82 | 缺失 | 0.78 | 2026-11-16 |
| XLB | 材料 | -1.46 | -2.78 | 1.02 | 0.46 | -1.08 | 缺失 | 1.16 | 2026-11-16 |
| SMH | 半导体 | -5.11 | -5.23 | -15.78 | -3.19 | -3.54 | 缺失 | 0.85 | 2026-11-16 |
| XOP | 油气开采 | -2.61 | 3.35 | -9.77 | -0.70 | 5.04 | 缺失 | 0.63 | 2026-11-16 |
| OIH | 油服 | -3.84 | 0.16 | -6.23 | -1.93 | 1.85 | 缺失 | 0.74 | 2026-11-16 |
| ITA | 航空与国防 | -2.46 | -2.68 | 0.72 | -0.55 | -0.99 | 缺失 | 0.72 | 2026-11-16 |
| ARKX | 航天主题 | -4.00 | -6.59 | -6.59 | -2.09 | -4.90 | 缺失 | 0.34 | 2026-11-16 |
| SKYY | 云计算 | -2.10 | -0.94 | -7.31 | -0.19 | 0.76 | 缺失 | 0.77 | 2026-11-16 |
| IGV | 软件 | -2.16 | -2.42 | -6.59 | 缺失 | 缺失 | 缺失 | 0.80 | 2026-11-16 |
| KRE | 区域银行 | -0.76 | -1.72 | 4.23 | 缺失 | 缺失 | 缺失 | 1.18 | 2026-11-16 |

## 资金证据分层

完整收盘轮动仍以16日为主体：19个ETF中2涨17跌；XLP+0.27%、XLU+0.18%，XLV−0.51%、XLF−0.85%相对抗跌；SMH−5.11%、ARKX−4.00%、OIH−3.84%、XLK−3.24%落后。20日同端点相对SPY：XLV+10.42pp、XLU+10.13pp、XLP+9.64pp、XLF+9.13pp，SMH−12.32pp。没有新收盘就不编新日线轮动。
17日12:00UTC附近SMH较昨收+1.53%，QQQ+0.56%、SPY+0.17%，IWM却约−0.25%；这是芯片领先的盘前反抽，尚非全面广度修复。XLF/XLV可得成交时点更旧，不用其报价判断当前资金切换。价格量能不等于主力净流入。
本轮重查[ICI](https://www.ici.org/research/stats/etf_flows)仍截至4日一周，美国股票ETF净发行308.68亿美元、债券138.89亿美元、商品1.29亿美元；[VanEck](https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/overview/)16日SMH净值461.74、净资产611.3亿美元仍仅单点，缺连续精确份额与拆分核验。未核验当期细分申赎和机构持仓，以上排序只为价格观察优先级。

## 最近可核验 ETF 申赎窗口

| 标的 | 金额 USD million | 起始日 | 结束日 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- |
| US_DOMESTIC_EQUITY_ETFS | 30868 | 2026-10-29 | 2026-11-04 | public_report | https://www.ici.org/research/stats/etf_flows |
| US_BOND_ETFS | 13889 | 2026-10-29 | 2026-11-04 | public_report | https://www.ici.org/research/stats/etf_flows |
| US_COMMODITY_ETFS | 129 | 2026-10-29 | 2026-11-04 | public_report | https://www.ici.org/research/stats/etf_flows |

## Polymarket 搜索覆盖与限制

17日11:59UTC起固定采集并主动搜索17组，覆盖Fed/衰退、AI、NVDA、AMD、CRWV、伊朗/俄乌、Hormuz、油价、关税、政府、银行、航天、数据中心与故障。每词最多10事件，部分hasMore=true，固定查询有截断及ceasefire/Starship 503；定向搜索补回重点事件，核验15份规则hash未变。新增风险变化为停火22日档回落及Anthropic低估值档升温；政府/银行/数据中心发现未形成已核验可交易信号。临近宏观与财报列入催化剂，IPO具体时分未知，upcoming_events不虚构时间。

## Polymarket · 值得警惕的信号

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["AI bubble burst in 2026?", "期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。", "https://polymarket.com/event/ai-bubble-burst-by"] | [7.8, {"status": "comparable", "change_pp": 0.050000000000000044}] | {"spread": 0.0020000000000000018, "volume24h_usd": 3692.5593209999997, "liquidity_usd": 177513.84849, "quality_flags": [], "retrieved_at": "2026-11-17T12:01:33.169591+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["本轮7.8%，较早报+0.05pp；结合专门结算规则与质量标记判断，不视为客观概率。", "AI估值/融资"] | ["多个实际阈值与信用持续恶化共同出现", "需求、回款与融资恢复且阈值未满足"] | [null, null] |
| ["CoreWeave downgraded by Moody's or S&P by December 31, 2026?", "2026年12月31日23:59ET前，Moody’s或S&P正式下调CoreWeave长期主体/企业家族或高级无担保债信用评级则Yes；仅负面展望/观察名单不算，不要求降至某统一评级档。成交很薄，不视为客观违约概率。", "https://polymarket.com/event/coreweave-downgraded-by-moodys-or-sp-by"] | [25.0, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.04000000000000001, "volume24h_usd": 50.106663999999995, "liquidity_usd": 590.4225, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"], "retrieved_at": "2026-11-17T12:00:02.054151+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["本轮25%，较早报+0.00pp；结合专门结算规则与质量标记判断，不视为客观概率。", "算力融资成本"] | ["正式评级行动及实际融资成本共同转坏", "仅展望变化或评级不变；薄盘口不足确认"] | [null, null] |
| ["US x Iran Effective Ceasefire by November 22?", "须完成连续14个伊朗标准时间日，美国未实施合资格命中伊朗陆地及内水的空袭或地对地导弹行动，首日在创建后至11月22日范围内；最后合资格行动次日为首日，无行动则创建日。第14日后再留3个日历日报道窗口。拦截碎片、海域/领空、网络、地面入侵和部分小型袭击不算。不是双边全面停火；期限不同于15日档，首次基线。", "https://polymarket.com/event/us-x-iran-effective-ceasefire-begins-by-2-week-pause-20261108"] | [66.5, {"status": "comparable", "change_pp": -5.999999999999995}] | {"spread": 0.010000000000000009, "volume24h_usd": 15315.767014000005, "liquidity_usd": 33106.4761, "quality_flags": [], "retrieved_at": "2026-11-17T12:01:33.169591+00:00", "contract_end_at": "2026-11-22T20:29:00+00:00"} | ["本轮66.5%，较早报-6.00pp；结合专门结算规则与质量标记判断，不视为客观概率。", "原油、运输及风险溢价"] | ["按正式规则核验命中行动及完整观察窗，另查实际航运", "出现合资格行动，或把海上袭击错误等同此结算条件"] | [null, null] |

## Polymarket · 有参考价值的事件

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Strait of Hormuz traffic returns to normal by December 31?", "期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。", "https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31"] | [4.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.010000000000000002, "volume24h_usd": 17209.942050000005, "liquidity_usd": 255038.7555, "quality_flags": [], "retrieved_at": "2026-11-17T12:01:33.169591+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["本轮4.5%，较早报+0.00pp；结合专门结算规则与质量标记判断，不视为客观概率。", "油运/能源"] | ["Portwatch量持续改善并满足规则", "航运事件持续且量未恢复"] | [null, null] |
| ["Russia x Ukraine energy ceasefire agreement by November 30, 2026?", "11月30日23:59基辅时间前，双方同意相互暂停至少一类明确能源设施打击；双方官宣或可信报道共识确认。第三方单方声称、谈判或单一设施暂停不算。正式协议可先于实际生效；不同于15日截止档，首次基线。", "https://polymarket.com/event/russia-x-ukraine-energy-ceasefire-agreement-by"] | [4.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.010000000000000002, "volume24h_usd": 4124.484191, "liquidity_usd": 139190.9504, "quality_flags": [], "retrieved_at": "2026-11-17T12:00:02.856627+00:00", "contract_end_at": "2026-11-30T21:59:00+00:00"} | ["本轮4.5%，较早报+0.00pp；结合专门结算规则与质量标记判断，不视为客观概率。", "能源供给/风险溢价"] | ["双方确认合格能源设施互停安排", "仅换囚或第三方声称"] | [null, null] |
| ["Russia x Ukraine ceasefire agreement by December 31, 2026?", "2026年末23:59ET前，双方官宣或可信共识确认相互暂停直接交战，包含明确生效日的全面暂停；仅限定目标/地点的局部能源安排不算。达成协议可先于实际生效，单方暂停不算。", "https://polymarket.com/event/russia-x-ukraine-ceasefire-agreement-by"] | [9.5, {"status": "comparable", "change_pp": -2.0000000000000004}] | {"spread": 0.010000000000000009, "volume24h_usd": 5436.111416, "liquidity_usd": 106685.4321, "quality_flags": [], "retrieved_at": "2026-11-17T12:00:02.856627+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["本轮9.5%，较早报-2.00pp；结合专门结算规则与质量标记判断，不视为客观概率。", "军工/欧洲风险偏好"] | ["双边明确全面暂停及生效日", "仅局部或单方暂停"] | [null, null] |
| ["Will WTI Crude Oil (WTI) hit (HIGH) $110 in November?", "11月规定Pyth时段内，ICE Europe WTI活跃月CLL最终1分钟High达到110美元即Yes，不取整，末三个交易日换月。仅因系统/数据故障无法核验时使用ICE官方日高低；正常Pyth收市不属于故障，不计该时段后价格。结构变动依Pyth调整价。规则与11月14日建立的新基线一致，不跨此前规则变更比较；Yahoo连续WTI不能直接裁决。", "https://polymarket.com/event/what-price-will-wti-hit-in-november-2026"] | [2.9000000000000004, {"status": "comparable", "change_pp": 0.15000000000000013}] | {"spread": 0.006000000000000002, "volume24h_usd": 5213.649601, "liquidity_usd": 35324.48523, "quality_flags": [], "retrieved_at": "2026-11-17T12:01:33.169591+00:00", "contract_end_at": "2026-12-01T04:59:59.999000+00:00"} | ["本轮2.9%，较早报+0.15pp；结合专门结算规则与质量标记判断，不视为客观概率。", "通胀与油气"] | ["指定Pyth/ICE价格和实际供应压力同向", "供应改善且指定价格未触发"] | [null, null] |
| ["New NVIDIA CEO named by December 31, 2026?", "2026年12月31日23:59纽约时间前，英伟达正式宣布黄仁勋的CEO继任者即满足；实际就任可以更晚，临时CEO不计。以公司公开声明为主要来源，可参照可信报道共识。与离任宣布合约不同。", "https://polymarket.com/event/new-nvidia-ceo-named-by-december-31-2026"] | [19.5, {"status": "comparable", "change_pp": -0.9999999999999981}] | {"spread": 0.010000000000000009, "volume24h_usd": 3840.527337999999, "liquidity_usd": 73302.0343, "quality_flags": [], "retrieved_at": "2026-11-17T12:01:33.169591+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["本轮19.5%，较早报-1.00pp；结合专门结算规则与质量标记判断，不视为客观概率。", "管理连续性、客户信任与估值风险溢价"] | ["公司正式公告永久CEO且符合截止要求", "只有临时任命或到期无永久继任宣布"] | [null, null] |
| ["Will the Fed increase interest rates by 50+ bps after the December 2026 meeting?", "衡量12月8–9日该次FOMC前后联邦基金目标区间上限上调至少50bp；非标准变化向上取整到最近25bp对应档。按正式声明，若下一次会议结束仍无声明则按不变档处理。不是全年累计加息幅度。", "https://polymarket.com/event/fed-decision-in-december-20260729232808632"] | [5.35, {"status": "comparable", "change_pp": 0.20000000000000018}] | {"spread": 0.0010000000000000009, "volume24h_usd": 290381.92349200003, "liquidity_usd": 401428.15027, "quality_flags": [], "retrieved_at": "2026-11-17T12:01:33.169591+00:00", "contract_end_at": "2026-12-09T23:59:00+00:00"} | ["本轮5.35%，较早报+0.20pp；结合专门结算规则与质量标记判断，不视为客观概率。", "利率与长久期估值"] | ["官方政策及融资/利率同步趋紧", "数据转弱与实际政策不符"] | [null, null] |
| ["Will the Fed increase interest rates by 25 bps after the December 2026 meeting?", "以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。", "https://polymarket.com/event/fed-decision-in-december-20260729232808632"] | [91.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.010000000000000009, "volume24h_usd": 164988.806514, "liquidity_usd": 487288.6796, "quality_flags": [], "retrieved_at": "2026-11-17T12:01:33.169591+00:00", "contract_end_at": "2026-12-09T23:59:00+00:00"} | ["本轮91.5%，较早报+0.00pp；结合专门结算规则与质量标记判断，不视为客观概率。", "利率和估值"] | ["以正式目标区间变动匹配专门档位", "实际政策与对应档不符"] | [null, null] |
| ["SpaceX Starship fully reusable before 2027?", "2026年12月31日23:59ET之前SpaceX、Musk或正式代表宣布Starship上面级完全可复用即Yes；不要求Super Heavy可复用，也不要求已经实际复飞。捕获画面不自动替代正式声明及平台裁决。当前价差13个百分点，24h成交缺失，低质量。", "https://polymarket.com/event/spacex-starship-fully-reusable-before-2027"] | [30.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.10999999999999999, "volume24h_usd": 40.6, "liquidity_usd": 3248.0589, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"], "retrieved_at": "2026-11-17T12:01:33.169591+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["本轮30.5%，较早报+0.00pp；结合专门结算规则与质量标记判断，不视为客观概率。", "可能影响航天叙事；不能直接推导上市供应商利润或Tesla合并"] | ["结算须SpaceX/Musk正式宣布上面级完全可复用；投资判断另需工程/订单证据及后续相对强势，规则不要求实际复飞。", "公告不满足专门定义，或上市标的无业务受益且价格确认失败"] | [null, null] |
| ["Will Anthropic's market cap be less than $1.25T at market close on IPO day?", "按Anthropic IPO首个交易日正式收盘价乘在外股数确定市值；边界归入较高区间，以主要交易所正式上市页优先。缩短/中断日取正式收盘，若无则下一交易日正式收盘；至2027年12月31日23:59ET无IPO则No IPO档。当前档位分别小于1.25万亿、1.25万亿至小于1.5万亿美元；元数据截止并非上市日期。", "https://polymarket.com/event/anthropic-ipo-closing-market-cap-higher-strikes"] | [36.35, {"status": "comparable", "change_pp": 3.099999999999997}] | {"spread": 0.0030000000000000027, "volume24h_usd": 352254.66964000004, "liquidity_usd": 100090.77887, "quality_flags": [], "retrieved_at": "2026-11-17T12:01:33.169591+00:00", "contract_end_at": "2028-01-01T04:59:00+00:00"} | ["本轮36.35%，较早报+3.10pp；结合专门结算规则与质量标记判断，不视为客观概率。", "AI融资风险偏好和关联企业承诺"] | ["正式上市及首日官方收盘/股份数，承诺按条件完成", "延期、未完成融资或首日规模不支持叙事"] | [null, null] |
| ["Will Anthropic's market cap be between $1.25T and $1.5T at market close on IPO day?", "按Anthropic IPO首个交易日正式收盘价乘在外股数确定市值；边界归入较高区间，以主要交易所正式上市页优先。缩短/中断日取正式收盘，若无则下一交易日正式收盘；至2027年12月31日23:59ET无IPO则No IPO档。当前档位分别小于1.25万亿、1.25万亿至小于1.5万亿美元；元数据截止并非上市日期。", "https://polymarket.com/event/anthropic-ipo-closing-market-cap-higher-strikes"] | [35.699999999999996, {"status": "comparable", "change_pp": -4.2500000000000036}] | {"spread": 0.006000000000000005, "volume24h_usd": 96686.10358799998, "liquidity_usd": 27476.5299, "quality_flags": [], "retrieved_at": "2026-11-17T12:01:33.169591+00:00", "contract_end_at": "2028-01-01T04:59:00+00:00"} | ["本轮35.7%，较早报-4.25pp；结合专门结算规则与质量标记判断，不视为客观概率。", "AI融资风险偏好和关联企业承诺"] | ["正式上市及首日官方收盘/股份数，承诺按条件完成", "延期、未完成融资或首日规模不支持叙事"] | [null, null] |

## Polymarket · 将要发生的事件及概率

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |

## 将要发生的事件及概率 · 本次无合格合约

本次未纳入合格合约，不代表相关风险或事件不存在。见搜索覆盖与限制。

## Will Anthropic's market cap be less than $1.25T at market close on IPO day?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 548858 / 2412744 |
| Yes 概率 % | 36.35 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [11.7, 9.9] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 3.099999999999997} |
| 24h成交量 / 流动性 USD | [352254.66964000004, 100090.77887] |
| 价差 pp | 0.30 |
| 到期 | 2028-01-01T04:59:00+00:00 |
| 结算规则摘要 | 按Anthropic IPO首个交易日正式收盘价乘在外股数确定市值；边界归入较高区间，以主要交易所正式上市页优先。缩短/中断日取正式收盘，若无则下一交易日正式收盘；至2027年12月31日23:59ET无IPO则No IPO档。当前档位分别小于1.25万亿、1.25万亿至小于1.5万亿美元；元数据截止并非上市日期。 |
| 规则指纹 | 33fa2aa35789c12e9a89f5398066c46fb0549dd1e70a1dbd7a8a329d96258d60 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-17T12:00:09.534678Z |
| 抓取时间 | 2026-11-17T12:01:33.169591+00:00 |
| 来源 | https://polymarket.com/event/anthropic-ipo-closing-market-cap-higher-strikes |

## Will the Fed increase interest rates by 50+ bps after the December 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 770450 / 3215009 |
| Yes 概率 % | 5.35 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-3.6, 0.1] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.20000000000000018} |
| 24h成交量 / 流动性 USD | [290381.92349200003, 401428.15027] |
| 价差 pp | 0.10 |
| 到期 | 2026-12-09T23:59:00+00:00 |
| 结算规则摘要 | 衡量12月8–9日该次FOMC前后联邦基金目标区间上限上调至少50bp；非标准变化向上取整到最近25bp对应档。按正式声明，若下一次会议结束仍无声明则按不变档处理。不是全年累计加息幅度。 |
| 规则指纹 | a05ecc7aefe678e9936425027277135b8c37cdaf659af595020eb1668ec48e58 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-17T11:56:34.100112Z |
| 抓取时间 | 2026-11-17T12:01:33.169591+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-december-20260729232808632 |

## Will the Fed increase interest rates by 25 bps after the December 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 770450 / 3215008 |
| Yes 概率 % | 91.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [4.0, 5.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [164988.806514, 487288.6796] |
| 价差 pp | 1.00 |
| 到期 | 2026-12-09T23:59:00+00:00 |
| 结算规则摘要 | 以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。 |
| 规则指纹 | 933a10a15eeec0ff1de30468fa20540301ed243f75cc3572d42946192f81a123 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-17T11:56:34.100112Z |
| 抓取时间 | 2026-11-17T12:01:33.169591+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-december-20260729232808632 |

## Will Anthropic's market cap be between $1.25T and $1.5T at market close on IPO day?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 548858 / 2412745 |
| Yes 概率 % | 35.70 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-6.7, 2.65] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -4.2500000000000036} |
| 24h成交量 / 流动性 USD | [96686.10358799998, 27476.5299] |
| 价差 pp | 0.60 |
| 到期 | 2028-01-01T04:59:00+00:00 |
| 结算规则摘要 | 按Anthropic IPO首个交易日正式收盘价乘在外股数确定市值；边界归入较高区间，以主要交易所正式上市页优先。缩短/中断日取正式收盘，若无则下一交易日正式收盘；至2027年12月31日23:59ET无IPO则No IPO档。当前档位分别小于1.25万亿、1.25万亿至小于1.5万亿美元；元数据截止并非上市日期。 |
| 规则指纹 | 615259a7206c78ca706da6d0de3e855413e1933333789449adf38e0aabdfed46 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-17T12:00:10.31316Z |
| 抓取时间 | 2026-11-17T12:01:33.169591+00:00 |
| 来源 | https://polymarket.com/event/anthropic-ipo-closing-market-cap-higher-strikes |

## Strait of Hormuz traffic returns to normal by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 455875 / 2176270 |
| Yes 概率 % | 4.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, -4.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [17209.942050000005, 255038.7555] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。 |
| 规则指纹 | b0c8ba27f4437b0d8ab819ae170bec118166232e39cdcaefb95bd352d29073d4 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-17T11:58:34.699806Z |
| 抓取时间 | 2026-11-17T12:01:33.169591+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31 |

## US x Iran Effective Ceasefire by November 22?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1337182 / 6831495 |
| Yes 概率 % | 66.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [7.0, 7.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -5.999999999999995} |
| 24h成交量 / 流动性 USD | [15315.767014000005, 33106.4761] |
| 价差 pp | 1.00 |
| 到期 | 2026-11-22T20:29:00+00:00 |
| 结算规则摘要 | 须完成连续14个伊朗标准时间日，美国未实施合资格命中伊朗陆地及内水的空袭或地对地导弹行动，首日在创建后至11月22日范围内；最后合资格行动次日为首日，无行动则创建日。第14日后再留3个日历日报道窗口。拦截碎片、海域/领空、网络、地面入侵和部分小型袭击不算。不是双边全面停火；期限不同于15日档，首次基线。 |
| 规则指纹 | 78780fef798e8d3d9f3bb09d7cf3b6ef6c296271b6a12297a43b7d1800e94f75 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-17T11:58:34.699806Z |
| 抓取时间 | 2026-11-17T12:01:33.169591+00:00 |
| 来源 | https://polymarket.com/event/us-x-iran-effective-ceasefire-begins-by-2-week-pause-20261108 |

## Will WTI Crude Oil (WTI) hit (HIGH) $110 in November?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1250301 / 6172751 |
| Yes 概率 % | 2.90 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-1.3, -5.6] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.15000000000000013} |
| 24h成交量 / 流动性 USD | [5213.649601, 35324.48523] |
| 价差 pp | 0.60 |
| 到期 | 2026-12-01T04:59:59.999000+00:00 |
| 结算规则摘要 | 11月规定Pyth时段内，ICE Europe WTI活跃月CLL最终1分钟High达到110美元即Yes，不取整，末三个交易日换月。仅因系统/数据故障无法核验时使用ICE官方日高低；正常Pyth收市不属于故障，不计该时段后价格。结构变动依Pyth调整价。规则与11月14日建立的新基线一致，不跨此前规则变更比较；Yahoo连续WTI不能直接裁决。 |
| 规则指纹 | 33ad0c642348432662de13f0d7c28f03c826ab7031226c102e452236917b6b7c |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-17T12:00:34.532256Z |
| 抓取时间 | 2026-11-17T12:01:33.169591+00:00 |
| 来源 | https://polymarket.com/event/what-price-will-wti-hit-in-november-2026 |

## AI bubble burst by June 30, 2027?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 4838928 |
| Yes 概率 % | 18.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, -4.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [4196.178422, 117442.57] |
| 价差 pp | 2.00 |
| 到期 | 2027-07-01T03:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | bd0420587e08487fffa5050e7fd9b79ffff909a9f843d3f620207ee859462505 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-17T11:56:34.100112Z |
| 抓取时间 | 2026-11-17T12:01:33.169591+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## New NVIDIA CEO named by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1367877 / 6977205 |
| Yes 概率 % | 19.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-1.0, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.9999999999999981} |
| 24h成交量 / 流动性 USD | [3840.527337999999, 73302.0343] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59纽约时间前，英伟达正式宣布黄仁勋的CEO继任者即满足；实际就任可以更晚，临时CEO不计。以公司公开声明为主要来源，可参照可信报道共识。与离任宣布合约不同。 |
| 规则指纹 | 09c6c6ee9faa8f03a8b6caf37ffb4757f33e53eedba525eae02360d329bf2d68 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-17T11:58:34.699806Z |
| 抓取时间 | 2026-11-17T12:01:33.169591+00:00 |
| 来源 | https://polymarket.com/event/new-nvidia-ceo-named-by-december-31-2026 |

## AI bubble burst in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 691340 |
| Yes 概率 % | 7.80 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [0.1, 1.75] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.050000000000000044} |
| 24h成交量 / 流动性 USD | [3692.5593209999997, 177513.84849] |
| 价差 pp | 0.20 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | fc153b2136a8dfbadcd169dce1add40690acb1748566b99716fe7ae8fcb07330 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-17T11:56:34.100112Z |
| 抓取时间 | 2026-11-17T12:01:33.169591+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## Tesla and SpaceX merger officially announced by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 192962 / 2252540 |
| Yes 概率 % | 27.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, 18.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [265.901291, 32635.7515] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59纽约时间前，Tesla或SpaceX正式宣布双方合并或一方收购另一方的控制权即Yes；无需在期限内完成交易。控制权通常为过半权益或等效治理权；少数股权投资及仅讨论不算。以公司公告或可信报道共识核验；旧URL中的june-30不是本合约期限。 |
| 规则指纹 | 909906ae3b6db7e473468713ea6a1e1e4cf4c931fe247c7d3d576e7986513008 |
| 质量 | ["volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-17T11:56:34.100112Z |
| 抓取时间 | 2026-11-17T12:01:33.169591+00:00 |
| 来源 | https://polymarket.com/event/tesla-and-spacex-merger-officially-announced-by-june-30 |

## SpaceX Starship fully reusable before 2027?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 79056 / 676812 |
| Yes 概率 % | 30.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [0.5, 1.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [40.6, 3248.0589] |
| 价差 pp | 11.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59ET之前SpaceX、Musk或正式代表宣布Starship上面级完全可复用即Yes；不要求Super Heavy可复用，也不要求已经实际复飞。捕获画面不自动替代正式声明及平台裁决。当前价差13个百分点，24h成交缺失，低质量。 |
| 规则指纹 | f9fb2d12d212bf90423007fe92524df34a8bd934a8f723520205802b8ad8d31a |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"] |
| 元数据更新（不是成交时间） | 2026-11-17T11:58:34.699806Z |
| 抓取时间 | 2026-11-17T12:01:33.169591+00:00 |
| 来源 | https://polymarket.com/event/spacex-starship-fully-reusable-before-2027 |

## CoreWeave downgraded by Moody's or S&P by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1219851 / 5939467 |
| Yes 概率 % | 25.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-2.5, -5.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [50.106663999999995, 590.4225] |
| 价差 pp | 4.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59ET前，Moody’s或S&P正式下调CoreWeave长期主体/企业家族或高级无担保债信用评级则Yes；仅负面展望/观察名单不算，不要求降至某统一评级档。成交很薄，不视为客观违约概率。 |
| 规则指纹 | 040e522db15913bd31de0e1a7f935727361429e7c42b3c1fc5286a0cf1b0fc42 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-17T11:58:34.699806Z |
| 抓取时间 | 2026-11-17T12:00:02.054151+00:00 |
| 来源 | https://polymarket.com/event/coreweave-downgraded-by-moodys-or-sp-by |

## Russia x Ukraine energy ceasefire agreement by November 30, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1360126 / 6947942 |
| Yes 概率 % | 4.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-1.0, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [4124.484191, 139190.9504] |
| 价差 pp | 1.00 |
| 到期 | 2026-11-30T21:59:00+00:00 |
| 结算规则摘要 | 11月30日23:59基辅时间前，双方同意相互暂停至少一类明确能源设施打击；双方官宣或可信报道共识确认。第三方单方声称、谈判或单一设施暂停不算。正式协议可先于实际生效；不同于15日截止档，首次基线。 |
| 规则指纹 | 4d97d360ed855920071504ae11e5ea8f81585c041447e5901a083ae049db5223 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-17T11:58:34.699806Z |
| 抓取时间 | 2026-11-17T12:00:02.856627+00:00 |
| 来源 | https://polymarket.com/event/russia-x-ukraine-energy-ceasefire-agreement-by |

## Russia x Ukraine ceasefire agreement by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 478472 / 2243897 |
| Yes 概率 % | 9.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-2.0, -5.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -2.0000000000000004} |
| 24h成交量 / 流动性 USD | [5436.111416, 106685.4321] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年末23:59ET前，双方官宣或可信共识确认相互暂停直接交战，包含明确生效日的全面暂停；仅限定目标/地点的局部能源安排不算。达成协议可先于实际生效，单方暂停不算。 |
| 规则指纹 | 2ea22f9548269db3205e41396a99073a2d5788dc4fde17989e34c8051ae6b75b |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-17T11:58:34.699806Z |
| 抓取时间 | 2026-11-17T12:00:02.856627+00:00 |
| 来源 | https://polymarket.com/event/russia-x-ukraine-ceasefire-agreement-by |

## AI 压力：合约、经营与估值分开

第一层，AI泡沫2026档7.8%、2027年6月档18%，为专门规则定价：90日窗口内6条件至少3项触发，不是行业崩盘客观概率。CRWV降级25%，价差4pp、24h约50美元，低质量；H100日期表16日3.08美元/GPU小时，仍高于连续5天≤1美元的专门条件，页面标题与日期表不一致时仅采日期表。历史所有触发项未完整审计。
第二层，[NVIDIA今日公告](https://nvidianews.nvidia.com/news/nvidia-board-of-directors-establishes-national-security-and-export-control-oversight-committee)成立国家安全与出口管制监督委员会，由Suzanne Nora Johnson主持，相关团队向委员会及临时CEO Colette Kress报告。治理安排可改善监督，却不等于调查结束、永久CEO任命、收入恢复或客户付款改善。NVDA盘前158.08只是修复；今晚还需订单、毛利、应收与资本开支证据。早报已核验的BIS远程算力规则与Warsh AI情景讨论作为背景沿用原抓取时点，不声称今日新增政策。
第三层，本轮SEC五家公司定期披露检查全部成功，最新财报发布日期仍NVDA8月26日、MSFT10月28日、AMZN10月30日、GOOGL10月29日、META10月22日；未把今晚尚未发布结果当已知。复用已核验底稿，估值使用16日完整收盘，不用盘前价混入。NVDA五年公司整体FCFF情景/折现敏感性/反推按假设展示，其余四家关键财务桥接不完整，保持无结论；整体公司价值不能全部归因AI。
Anthropic首日市值低于1.25万亿档36.35%，较早报+3.10pp；1.25–1.5万亿35.7%，−4.25pp。只比较同规则分档，不以两个档重建完整分布。SEC指示日程仍预计18日定价、19日交易，可变更，融资承诺不等于现金到账。

## NVDA · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | scenario_analysis |
| 财务底稿 | TTM 至 2026-07-26；最新 10-Q / filed 2026-08-26 |
| 披露检查 | {"checked_at": "2026-11-17T12:07:50.011593+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001045810.json", "latest_filing_date": "2026-08-26"} |
| 观测财务数据 | {"ttm_revenue_million": 302970, "revenue_quarters": [{"end": "2025-10-26", "value": 57006000000, "filed": "2025-11-19", "duration_days": 91}, {"end": "2026-01-25", "value": 68127000000, "filed": "2026-02-25", "duration_days": 91}, {"end": "2026-04-26", "value": 81615000000, "filed": "2026-05-20", "duration_days": 91}, {"end": "2026-07-26", "value": 96221000000, "filed": "2026-08-26", "duration_days": 91}], "cash_million": 22443.0, "liquid_investments_million": 34143.0, "debt_million": 33366.0, "finance_lease_million": 0, "diluted_shares_million": 24285.0, "latest_operating_income_million": 63734.0, "observed_end": "2026-07-26", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "Revenues", "latest_reported_revenue_million": 96221.0, "income_statement_window": "最近单季度", "ttm_bridge_note": "采用同版 FY2026全年 + FY2027半年 - FY2026半年；与四季逐项求和差1百万为披露舍入差。"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json", "https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。10-Q Note14 表明融资租赁费用不重大；模型按不重大近似零，不将其称为精确零负债。未确认担保仅作为压力情景，非已到期净债务。市场化股权42783和非市场化股权51157不作为类现金；非经营资产加回为0的保守假设。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | 无 |
| 价格 USD | 156.14 |
| 基期输入 USD million / million shares | {"revenue": 302970, "net_debt": -23220.0, "diluted_shares": 24285.0, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.20352679491937098, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## NVDA · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 98.77 | -36.74 | 14.00 | 60.00 | 12.00 | 68.42 |
| 基准 | 154.12 | -1.30 | 20.00 | 65.00 | 11.00 | 74.20 |
| 乐观 | 242.58 | 55.36 | 26.00 | 70.00 | 10.00 | 79.05 |

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
| 披露检查 | {"checked_at": "2026-11-17T12:08:17.690311+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0000789019.json", "latest_filing_date": "2026-10-28"} |
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
| 披露检查 | {"checked_at": "2026-11-17T12:08:23.404010+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001018724.json", "latest_filing_date": "2026-10-30"} |
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
| 披露检查 | {"checked_at": "2026-11-17T12:08:29.100197+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001652044.json", "latest_filing_date": "2026-10-29"} |
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
| 披露检查 | {"checked_at": "2026-11-17T12:08:48.309785+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001326801.json", "latest_filing_date": "2026-10-22"} |
| 观测财务数据 | {"revenue_million": 64601, "operating_cashflow_million": 32790, "reported_capex_including_finance_lease_principal_million": 34910, "company_defined_fcf_million": -2120, "diluted_shares_million": 2573, "reported_operating_income_million": 12988, "legal_charge_million": 9900, "observed_end": "2026-09-30", "published_at": "2026-10-21T16:01:00-04:00", "unit": "USD million; shares million", "noncancelable_commitments_million": 454520, "leases_not_commenced_million": 355730, "contingent_cloud_capacity_max_million": 14720, "restricted_cash_reclassified_million": 10800, "commitments_due_2026_million": 45850, "commitments_due_2027_million": 121410} |
| 来源 | ["https://www.prnewswire.com/news-releases/meta-reports-third-quarter-2026-results-302915964.html", "https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm", "https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Announces-Launch-of-Offering-of-Depositary-Shares-Representing-Series-A-Mandatory-Convertible-Preferred-Stock-and-Offering-of-Class-A-Common-Stock-in-Connection-with-Forward-Sale-Agreements/default.aspx", "https://www.prnewswire.com/news-releases/meta-announces-pricing-of-offering-of-depositary-shares-representing-series-a-mandatory-convertible-preferred-stock-and-offering-of-class-a-common-stock-in-connection-with-forward-sale-agreements-302920247.html"] |
| 口径 | 公司FCF扣除融资租赁本金，不能直接代替模型FCFF；融资租赁负债/新增资产未齐，不假设零。法律费用不全归AI经营。 |
| 主观假设说明 | 缺失 |
| 权益桥额外假设 | 无 |
| 缺失原因 | 沿用底稿的历史核验说明（其中“本次”指原核验日）；本轮最新定期财报列表检查见disclosure_check。22日10-Q已核验，本次无新增定期财报。27日普通股625美元定价、优先票息6.5%已核验；完整融资租赁负债/新增资产、优先权益/远期发行与现金到账桥未齐，不用不同承诺简单充当现有债务，暂停精确FCFF反推。 |

## 宽基：先止跌，再收复失守区

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 宏观数据、NVDA结果与次日市场反应 |
| 关联标的 | ["SPY", "QQQ", "RSP", "IWM"] |
| 确认条件 | SPY先收复747.89–749.82，QQQ671.71–672.15；回踩形成更高低点且收盘站稳，RSP/IWM同步改善、涨跌家数扩散。进一步看SPY20日757.69、QQQ200日681.41；第一段反抽只是修复。 |
| 失效条件 | SPY跌破16日低738.07、QQQ660.48且反抽失败，或突破后又收回区间下方 |
| 观察期限 | 11月17–20日；财报后按实际新信息复核 |
| 反证 | SPY/QQQ仍在首道修复区下；盘前价不构成常规VWAP、开盘区间或收盘确认。 |
| 状态 | 条件观察；盘前反抽不能确认常规时段突破和回踩 |

## 芯片：等待经营证据与板块修复

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | NVDA17日财报、政策影响和现金回收披露 |
| 关联标的 | ["SMH", "NVDA", "MU"] |
| 确认条件 | SMH收复16日高473.33并回踩守稳；NVDA先158.39再163.20，MU先739.12再750.25；相对SPY转强、更多芯片同行跟随，财报后次日收盘承接才升级。 |
| 失效条件 | SMH460.64、NVDA155.01、MU716.38再失且反抽失败；或明确订单/回款/融资恶化。 |
| 观察期限 | 11月17–20日；财报后按实际新信息复核 |
| 反证 | 监督委员会是治理措施，不等于现金流改善；今晚财报可跳空越过风控价格，杠杆ETF每日重置带来路径风险。 |
| 状态 | 条件观察；盘前反抽不能确认常规时段突破和回踩 |

## 防御与金融：优先观察但不追涨

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 相对强势能否转化为绝对上涨 |
| 关联标的 | ["XLP", "XLV", "XLF", "XLU"] |
| 确认条件 | XLP92.38、XLV187.60、XLF57.89是16日低点参考；回踩守住后再突破各自16日高93.48/191.33/58.81，且收盘维持相对领先。支撑不是保证，按实际波动修订。 |
| 失效条件 | 关键低点破位且无法收复、相对强度反转；金融另看信用扩散。 |
| 观察期限 | 11月17–20日；财报后按实际新信息复核 |
| 反证 | XLP收盘低于开盘，XLV/XLF仍下跌；相对抗跌不自动成为买点。 |
| 状态 | 条件观察；盘前反抽不能确认常规时段突破和回踩 |

## 能源：等待油价和价格同步

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 真实航运、供给及需求变化 |
| 关联标的 | ["XLE", "XOP", "OIH"] |
| 确认条件 | XLE/XOP/OIH先收复20日65.96/189.80/381.60并回踩守稳，油价与企业盈利预期同向支持。 |
| 失效条件 | 油价继续弱、突破失败或供给改善兑现。 |
| 观察期限 | 11月17–20日；财报后按实际新信息复核 |
| 反证 | 地缘风险高也可能伴随能源股下跌，不能用新闻单向定价。 |
| 状态 | 条件观察；盘前反抽不能确认常规时段突破和回踩 |

## 工业与航天：保留次级观察

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 官方工程与企业订单披露 |
| 关联标的 | ["XLI", "ARKX", "ITA"] |
| 确认条件 | XLI先收20日167.77、ARKX29.70、ITA70.16并保持相对SPY改善；航天还需实际订单映射。 |
| 失效条件 | 重新跌破修复区且反抽失败，或工程/订单归因不成立。 |
| 观察期限 | 11月17–20日；财报后按实际新信息复核 |
| 反证 | Starship合约价差11pp且24h40.60美元；不据此推导上市篮子上涨。 |
| 状态 | 条件观察；盘前反抽不能确认常规时段突破和回踩 |

## 跨期比较与上期剧本复核

与17日07:15时段早报（实际中午生成）相比：完整收盘仍16日，不重复计算为新交易日。新增盘前芯片反抽、CNN31、NVIDIA委员会公告；SPY/QQQ/SMH及NVDA/MU尚未达到早报首道修复位，原宽基失效条件仍有效，不能升级为趋势反转。以下15合约同ID同rule_hash：Strait of Hormuz traffic returns to normal by December 31?：4.5%（较早报+0.00pp）；Will the Fed increase interest rates by 25 bps after the December 2026 meeting?：91.5%（较早报+0.00pp）；AI bubble burst in 2026?：7.8%（较早报+0.05pp）；AI bubble burst by June 30, 2027?：18%（较早报+0.00pp）；Tesla and SpaceX merger officially announced by December 31?：27.5%（较早报+0.00pp）；Will the Fed increase interest rates by 50+ bps after the December 2026 meeting?：5.35%（较早报+0.20pp）；CoreWeave downgraded by Moody's or S&P by December 31, 2026?：25%（较早报+0.00pp）；Russia x Ukraine ceasefire agreement by December 31, 2026?：9.5%（较早报-2.00pp）；New NVIDIA CEO named by December 31, 2026?：19.5%（较早报-1.00pp）；Will WTI Crude Oil (WTI) hit (HIGH) $110 in November?：2.9%（较早报+0.15pp）；SpaceX Starship fully reusable before 2027?：30.5%（较早报+0.00pp）；Will Anthropic's market cap be less than $1.25T at market close on IPO day?：36.35%（较早报+3.10pp）；Will Anthropic's market cap be between $1.25T and $1.5T at market close on IPO day?：35.7%（较早报-4.25pp）；US x Iran Effective Ceasefire by November 22?：66.5%（较早报-6.00pp）；Russia x Ukraine energy ceasefire agreement by November 30, 2026?：4.5%（较早报+0.00pp）。薄盘口变化降权，停火与运输规则分开。

## 可计算的跨期变化

```json
[
  {
    "mode": "daily",
    "baseline": "reports/daily/2026-11-16/20261117T041705.970365Z/evidence.json",
    "baseline_cutoff": "2026-11-17T04:16:39.595176+00:00",
    "close_change_pct": {
      "SPY": 0.0,
      "IWM": 0.0,
      "RSP": 0.0,
      "GLD": 0.0,
      "GC=F": -0.516395558998195,
      "CL=F": 0.8945411304381423,
      "BZ=F": 0.9280556146981533,
      "TLT": 0.0,
      "UUP": 0.0,
      "HYG": 0.0,
      "LQD": 0.0,
      "^VIX": 0.0,
      "^VIX3M": 0.0,
      "^VVIX": 0.0,
      "^MOVE": -0.002372830056329711,
      "MSFT": 0.0,
      "AMZN": 0.0,
      "GOOGL": 0.0,
      "META": 0.0,
      "CRWV": 0.0,
      "MU": 0.0,
      "DRAM": 0.0,
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
      "XOP": 0.0,
      "OIH": 0.0,
      "ITA": 0.0,
      "ARKX": 0.0,
      "SKYY": 0.0
    },
    "quote_change_pct": {},
    "macro_change": {
      "DGS2": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-11-13"
      },
      "BAMLH0A0HYM2": {
        "change": 0.0,
        "unit": "percentage_points",
        "observation_date": "2026-11-13"
      },
      "BAMLC0A0CM": {
        "change": 0.0,
        "unit": "percentage_points",
        "observation_date": "2026-11-13"
      },
      "DGS10": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-11-13"
      },
      "DFII10": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-11-13"
      },
      "T10YIE": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-11-16"
      },
      "STLFSI4": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-11-06"
      },
      "CBOE_VIX": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-11-16"
      },
      "GPRD": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-11-16"
      },
      "GPRD_ACT": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-11-16"
      },
      "GPRD_THREAT": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-11-16"
      },
      "GPRD_MA7": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-11-16"
      },
      "GPRD_MA30": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-11-16"
      }
    },
    "event_probability_change": {
      "2412744": {
        "status": "comparable",
        "change_pp": 3.099999999999997
      },
      "3215009": {
        "status": "comparable",
        "change_pp": 0.20000000000000018
      },
      "3215008": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "2412745": {
        "status": "comparable",
        "change_pp": -4.2500000000000036
      },
      "2176270": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "6831495": {
        "status": "comparable",
        "change_pp": -5.999999999999995
      },
      "6172751": {
        "status": "comparable",
        "change_pp": 0.15000000000000013
      },
      "4838928": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "6977205": {
        "status": "comparable",
        "change_pp": -0.9999999999999981
      },
      "691340": {
        "status": "comparable",
        "change_pp": 0.050000000000000044
      },
      "2252540": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "676812": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "5939467": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "6947942": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "2243897": {
        "status": "comparable",
        "change_pp": -2.0000000000000004
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
    "event": "10月零售销售，纽约17日08:30/北京21:30；同时有9月月度销售修订",
    "date": "2026-11-17T08:30:00-05:00",
    "source": "https://www.census.gov/retail/release_schedule.html"
  },
  {
    "event": "10月进口/出口价格，北京17日21:30",
    "date": "2026-11-17T08:30:00-05:00",
    "source": "https://www.bls.gov/schedule/2026/"
  },
  {
    "event": "10月工业生产与产能利用率，纽约17日09:15/北京17日22:15",
    "date": "2026-11-17T09:15:00-05:00",
    "source": "https://www.federalreserve.gov/newsevents/2026-November.htm"
  },
  {
    "event": "NVDA结果预计纽约17日16:20/北京18日05:20；电话会17:00/06:00",
    "date": "2026-11-17T16:20:00-05:00",
    "source": "https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/default.aspx"
  },
  {
    "event": "10月FOMC会议纪要，纽约18日14:00/北京19日03:00",
    "date": "2026-11-18T14:00:00-05:00",
    "source": "https://www.federalreserve.gov/newsevents/2026-November.htm"
  },
  {
    "event": "NVDA永久CEO任命，时间未定，临时任命不满足相关预测合约",
    "date": null,
    "source": "https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-CEO-Transition/default.aspx"
  },
  {
    "event": "Barr谈AI，纽约19日14:15/北京20日03:15",
    "date": "2026-11-19T14:15:00-05:00",
    "source": "https://www.federalreserve.gov/newsevents/2026-November.htm"
  },
  {
    "event": "未来30天：GDP第二次估计、企业利润与10月PCE，纽约25日08:30/北京25日21:30",
    "date": "2026-11-25T08:30:00-05:00",
    "source": "https://www.bea.gov/news/schedule/"
  },
  {
    "event": "未来30天：褐皮书，纽约25日14:00/北京26日03:00",
    "date": "2026-11-25T14:00:00-05:00",
    "source": "https://www.federalreserve.gov/newsevents/2026-November.htm"
  },
  {
    "event": "未来30天：11月26日感恩节休市、27日纽约13:00半日市；日期事项不虚构发布时间",
    "date": null,
    "source": "https://www.nyse.com/trade/hours-calendars"
  },
  {
    "event": "未来30天：11月非农，纽约12月4日08:30/北京4日21:30",
    "date": "2026-12-04T08:30:00-05:00",
    "source": "https://www.bls.gov/schedule/2026/"
  },
  {
    "event": "未来30天：12月8–9日FOMC和经济预测，日期已确认，具体发布时刻本轮未独立核验",
    "date": null,
    "source": "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm"
  },
  {
    "event": "未来30天：11月CPI，纽约12月10日08:30/北京10日21:30",
    "date": "2026-12-10T08:30:00-05:00",
    "source": "https://www.bls.gov/schedule/2026/"
  },
  {
    "event": "Anthropic指示时间表：纽约11月18日预计定价、19日预计NASDAQ交易；可变更，未核验具体时刻，不以合约2027年截止冒充上市日",
    "date": null,
    "source": "https://www.sec.gov/Archives/edgar/data/2130357/000162828026073040/anthropicpbc-fwpxeeaprospea.htm"
  },
  {
    "event": "新远程算力规则展示稿的正式发表、生效与公司量化影响仍待核验，不猜具体时刻",
    "date": null,
    "source": "https://www.bis.gov/media/documents/rin-0694-ak50.pdf"
  }
]
```

## 新闻事件去重与时间

| 事件 | 摘要 | 发生时间（未知留空） | 各来源发布时间 / 抓取时间 |
| --- | --- | --- | --- |
| 20261116-us-close | 16日宽基和半导体下跌，NYSE跌涨比3.45:1；用同源ETF日线计算，指数与ETF涨幅不混用。 报道16:21纽约更新为收盘版本，不能把完整收盘数据归入14:52首发时点。 | 2026-11-16T16:00:00-05:00 | [{"source": "https://www.marketscreener.com/news/wall-street-slumps-on-ai-jitters-ahead-of-nvidia-results-anthropic-ipo-ce785edfdd8ef425", "published_at": "2026-11-16T14:52:00-05:00", "retrieved_at": "2026-11-17T04:14:13.777825+00:00"}] |
| 20261116-remote-compute-rule | BIS公布远程算力规则；网站正文日期16日与搜索/PDF15日标注存在差异，精确发布时间未知，展示稿生效日期仍占位。 | 缺失 | [{"source": "https://www.bis.gov/press-release/bis-issues-rule-addressing-remote-access-american-super-intelligence-technology", "published_at": null, "retrieved_at": "2026-11-17T04:14:13.777825+00:00"}] |
| 20261116-warsh-ai-scenarios | Warsh讨论AI生产率、就业替代与回报失望三情景，明确非预测。 | 2026-11-16T12:00:00-05:00 | [{"source": "https://www.federalreserve.gov/newsevents/speech/warsh20261116a.htm", "published_at": null, "retrieved_at": "2026-11-17T04:14:13.777825+00:00"}] |
| 20261116-hormuz-tracking | Reuters引用Kpler周末过境减缓数据；不同统计窗口和后续补报须区分，不据外交合约宣称通行正常。 | 缺失 | [{"source": "https://www.gulf-times.com/article/731298/shopping/shipping-slows-through-strait-of-hormuz-after-tanker-attacks/amp", "published_at": null, "retrieved_at": "2026-11-17T04:14:13.777825+00:00"}] |
| 20261117-nvda-preview | 公司确认17日盘后结果及电话会；本轮未发现新的定期财报，结果尚未公布。 | 缺失 | [{"source": "https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/default.aspx", "published_at": null, "retrieved_at": "2026-11-17T04:14:13.777825+00:00"}] |
| 20261117-nvda-oversight | NVDA成立国家安全与出口管制监督委员会，临时CEO身份不变；精确公告时分未提供，不推断收入影响已消除。 | 缺失 | [{"source": "https://nvidianews.nvidia.com/news/nvidia-board-of-directors-establishes-national-security-and-export-control-oversight-committee", "published_at": null, "retrieved_at": "2026-11-17T12:04:00+00:00"}] |
| 20261117-bahrain-radar | AP可见摘要报道伊朗无人机攻击巴林美军雷达设施；全文访问失败、损害未独立核验，不等于停火合约自动失败。 | 缺失 | [{"source": "https://apnews.com/article/582e0b5d51be06f0ed630fac24f39b72", "published_at": "2026-11-17T10:07:42+00:00", "retrieved_at": "2026-11-17T12:04:00+00:00"}] |

## 覆盖范围与数据缺口

```json
[
  "tc五个授权工具当前未加载，不能刷新tc日历/市场概览/新闻；使用显式标源的NYSE日历、Yahoo/Cboe及公开来源。",
  "没有本轮逐分钟VWAP、开盘前30分钟区间或回踩序列；日线高低只作已完成全日参考。",
  "FRED名义/实际利率与信用至13日，财政部另有16日曲线；金融压力至6日，不能混成同刻证据。",
  "ICI申赎窗口截至4日；SMH仅16日单点净值/净资产，未核验连续份额、拆分及当日申赎；机构持仓未核验。",
  "除NVDA外四家FCFF关键输入不全，保留缺口；新财报出现前不编造基本面。",
  "AI泡沫历史各触发项未全面审计，H100标题与日期表不一致，采用日期表。",
  "CRWV/Starship成交稀少且价差宽；预测市场不是客观概率，旧到期合约未作最终裁决审计。",
  "Gamma主动搜索每词最多10事件，固定搜索也有截断；新闻按事件去重但非全量。",
  "BIS展示稿日期存在占位，正式生效与公司收入冲击未核验；CEO讨论/支持不等于官方永久任命。",
  "期货连续合约不等于正式结算，换月与交易时段可影响比较；不以单次油价下跌证明运输安全。",
  "DRAM历史不足200交易日；当期单公司CDS、完整盈利一致预期、CME原始FedWatch与逐股广度未独立核验。",
  "IPO日程有条件，未核验实际融资到账；航天工程进展与上市供应链订单映射不足。",
  "API缺失QQQ/NVDA/VRT/IGV/KRE，使用同源完整复权历史补查，原始失败保留。",
  "盘前快照不同证券时点不同，XLF/XLV旧成交与16日^TNX不代表当前状态；无常规时段VWAP及回踩验证。",
  "AP巴林报道仅可见摘要，原文不可访问；不将报道推成已独立核验战况。",
  "今日新增公告、日程与重点来源重新检查；未重开的早报背景保留原抓取时间。",
  "补查合并后部分相对强弱计算因原快照只留15日基准尾部而为空；正文20日相对强弱沿用本日早报同一16日端点，非新增盘前计算。",
  "原始采集存在请求失败，见采集质量记录",
  "MSFT 估值: 沿用底稿的历史核验说明（其中“本次”指原核验日）；本轮最新定期财报列表检查见disclosure_check。本次新增30日FWP，29日已定价250亿美元债券、11月4日预定结算；新财报完整TTM/租赁/净债务桥仍缺，不沿用旧精确DCF。",
  "AMZN 估值: 沿用底稿的历史核验说明（其中“本次”指原核验日）；本轮最新定期财报列表检查见disclosure_check。30日新增Q3 10-Q已核验；最新TTM、融资租赁/净债务与稀释桥尚未完整，不沿用旧估值。",
  "GOOGL 估值: 沿用底稿的历史核验说明（其中“本次”指原核验日）；本轮最新定期财报列表检查见disclosure_check。已发现新季度披露；必要TTM、融资租赁及优先权益/稀释桥未完成，暂停旧底稿估值和价格反推。",
  "META 估值: 沿用底稿的历史核验说明（其中“本次”指原核验日）；本轮最新定期财报列表检查见disclosure_check。22日10-Q已核验，本次无新增定期财报。27日普通股625美元定价、优先票息6.5%已核验；完整融资租赁负债/新增资产、优先权益/远期发行与现金到账桥未齐，不用不同承诺简单充当现有债务，暂停精确FCFF反推。",
  "Polymarket 查询 AI bubble 达到页数上限，存在遗漏",
  "Polymarket 查询 CPI 达到页数上限，存在遗漏",
  "Polymarket 查询 Fed rate 达到页数上限，存在遗漏",
  "Polymarket 查询 Hormuz 达到页数上限，存在遗漏",
  "Polymarket 查询 Iran 达到页数上限，存在遗漏",
  "Polymarket 查询 Microsoft 达到页数上限，存在遗漏",
  "Polymarket 查询 Nvidia 达到页数上限，存在遗漏",
  "Polymarket 查询 SpaceX 达到页数上限，存在遗漏",
  "Polymarket 查询 bank 达到页数上限，存在遗漏",
  "Polymarket 查询 inflation 达到页数上限，存在遗漏",
  "tc 报价质量 stale: RSP；不作为新成交证据",
  "history.DRAM: insufficient_history",
  "polymarket.query.AI bubble: truncated",
  "polymarket.query.CPI: truncated",
  "polymarket.query.Fed rate: truncated",
  "polymarket.query.Hormuz: truncated",
  "polymarket.query.Iran: truncated",
  "polymarket.query.Microsoft: truncated",
  "polymarket.query.Nvidia: truncated",
  "polymarket.query.SpaceX: truncated",
  "polymarket.query.bank: truncated",
  "polymarket.query.inflation: truncated",
  "cnn: missing",
  "request.9572e2289a18: request_failed",
  "request.bd27b9ca2062: request_failed",
  "request.fde2888814e2: request_failed",
  "request.fd24b1315edc: request_failed",
  "request.c5d45ab239a3: request_failed",
  "request.c5498122be43: request_failed",
  "request.7a9f2148a1a7: request_failed",
  "request.38906ddc2d63: request_failed",
  "Polymarket 临近事件：本次未纳入合格合约，见搜索说明",
  "指标缺失/历史不足: prices.SPY.relative_spy_20d_pp, prices.SPY.relative_spy_60d_pp, prices.IWM.relative_spy_20d_pp, prices.IWM.relative_spy_60d_pp, prices.RSP.relative_spy_20d_pp, prices.RSP.relative_spy_60d_pp, prices.GLD.relative_spy_20d_pp, prices.GLD.relative_spy_60d_pp, prices.GC=F.relative_spy_20d_pp, prices.GC=F.relative_spy_60d_pp, prices.CL=F.relative_spy_20d_pp, prices.CL=F.relative_spy_60d_pp, prices.BZ=F.relative_spy_20d_pp, prices.BZ=F.relative_spy_60d_pp, prices.TLT.relative_spy_20d_pp, prices.TLT.relative_spy_60d_pp, prices.UUP.relative_spy_20d_pp, prices.UUP.relative_spy_60d_pp, prices.HYG.relative_spy_20d_pp, prices.HYG.relative_spy_60d_pp, prices.LQD.relative_spy_20d_pp, prices.LQD.relative_spy_60d_pp, prices.^VIX.relative_spy_20d_pp, prices.^VIX.relative_spy_60d_pp, prices.^VIX.volume_vs_previous20_ratio, prices.^VIX3M.relative_spy_20d_pp, prices.^VIX3M.relative_spy_60d_pp, prices.^VIX3M.volume_vs_previous20_ratio, prices.^VVIX.relative_spy_20d_pp, prices.^VVIX.relative_spy_60d_pp, prices.^VVIX.volume_vs_previous20_ratio, prices.^MOVE.relative_spy_20d_pp, prices.^MOVE.relative_spy_60d_pp, prices.^MOVE.volume_vs_previous20_ratio, prices.MSFT.relative_spy_20d_pp, prices.MSFT.relative_spy_60d_pp, prices.AMZN.relative_spy_20d_pp, prices.AMZN.relative_spy_60d_pp, prices.GOOGL.relative_spy_20d_pp, prices.GOOGL.relative_spy_60d_pp, prices.META.relative_spy_20d_pp, prices.META.relative_spy_60d_pp, prices.CRWV.relative_spy_20d_pp, prices.CRWV.relative_spy_60d_pp, prices.MU.relative_spy_20d_pp, prices.MU.relative_spy_60d_pp, prices.DRAM.relative_spy_20d_pp, prices.DRAM.relative_spy_60d_pp, prices.DRAM.sma200, prices.DRAM.distance_sma200_pct, prices.XLK.relative_spy_20d_pp, prices.XLK.relative_spy_60d_pp, prices.XLE.relative_spy_20d_pp, prices.XLE.relative_spy_60d_pp, prices.XLF.relative_spy_20d_pp, prices.XLF.relative_spy_60d_pp, prices.XLI.relative_spy_20d_pp, prices.XLI.relative_spy_60d_pp, prices.XLV.relative_spy_20d_pp, prices.XLV.relative_spy_60d_pp, prices.XLP.relative_spy_20d_pp, prices.XLP.relative_spy_60d_pp, prices.XLY.relative_spy_20d_pp, prices.XLY.relative_spy_60d_pp, prices.XLC.relative_spy_20d_pp, prices.XLC.relative_spy_60d_pp, prices.XLU.relative_spy_20d_pp, prices.XLU.relative_spy_60d_pp, prices.XLRE.relative_spy_20d_pp, prices.XLRE.relative_spy_60d_pp, prices.XLB.relative_spy_20d_pp, prices.XLB.relative_spy_60d_pp, prices.SMH.relative_spy_20d_pp, prices.SMH.relative_spy_60d_pp, prices.XOP.relative_spy_20d_pp, prices.XOP.relative_spy_60d_pp, prices.OIH.relative_spy_20d_pp, prices.OIH.relative_spy_60d_pp, prices.ITA.relative_spy_20d_pp, prices.ITA.relative_spy_60d_pp, prices.ARKX.relative_spy_20d_pp, prices.ARKX.relative_spy_60d_pp, prices.SKYY.relative_spy_20d_pp, prices.SKYY.relative_spy_60d_pp, prices.QQQ.relative_spy_1d_pp, prices.QQQ.relative_spy_5d_pp, prices.QQQ.relative_spy_20d_pp, prices.QQQ.relative_spy_60d_pp, prices.NVDA.relative_spy_1d_pp, prices.NVDA.relative_spy_5d_pp, prices.NVDA.relative_spy_20d_pp, prices.NVDA.relative_spy_60d_pp, prices.VRT.relative_spy_1d_pp, prices.VRT.relative_spy_5d_pp, prices.VRT.relative_spy_20d_pp, prices.VRT.relative_spy_60d_pp, prices.IGV.relative_spy_1d_pp, prices.IGV.relative_spy_5d_pp, prices.IGV.relative_spy_20d_pp, prices.IGV.relative_spy_60d_pp, prices.KRE.relative_spy_1d_pp, prices.KRE.relative_spy_5d_pp, prices.KRE.relative_spy_20d_pp, prices.KRE.relative_spy_60d_pp, quotes.RSP.value"
]
```

## 来源、时间与核验记录

```json
[
  {
    "url": "https://www.federalreserve.gov/newsevents/speech/warsh20261116a.htm",
    "checked_at": "2026-11-17T04:14:13.777825+00:00",
    "note": "本轮公开网页核验；来源观测日期另列，抓取时间不是发生时间。"
  },
  {
    "url": "https://www.bis.gov/press-release/bis-issues-rule-addressing-remote-access-american-super-intelligence-technology",
    "checked_at": "2026-11-17T04:14:13.777825+00:00",
    "note": "本轮公开网页核验；来源观测日期另列，抓取时间不是发生时间。"
  },
  {
    "url": "https://www.bis.gov/media/documents/rin-0694-ak50.pdf",
    "checked_at": "2026-11-17T04:14:13.777825+00:00",
    "note": "本轮公开网页核验；来源观测日期另列，抓取时间不是发生时间。"
  },
  {
    "url": "https://www.marketscreener.com/news/wall-street-slumps-on-ai-jitters-ahead-of-nvidia-results-anthropic-ipo-ce785edfdd8ef425",
    "checked_at": "2026-11-17T04:14:13.777825+00:00",
    "note": "本轮公开网页核验；来源观测日期另列，抓取时间不是发生时间。"
  },
  {
    "url": "https://www.gulf-times.com/article/731298/shopping/shipping-slows-through-strait-of-hormuz-after-tanker-attacks/amp",
    "checked_at": "2026-11-17T04:14:13.777825+00:00",
    "note": "本轮公开网页核验；来源观测日期另列，抓取时间不是发生时间。"
  },
  {
    "url": "https://www.silicondata.com/products/silicon-index/h100",
    "checked_at": "2026-11-17T04:14:13.777825+00:00",
    "note": "本轮公开网页核验；来源观测日期另列，抓取时间不是发生时间。"
  },
  {
    "url": "https://www.ici.org/research/stats/etf_flows",
    "checked_at": "2026-11-17T04:14:13.777825+00:00",
    "note": "本轮公开网页核验；来源观测日期另列，抓取时间不是发生时间。"
  },
  {
    "url": "https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/overview/",
    "checked_at": "2026-11-17T04:14:13.777825+00:00",
    "note": "本轮公开网页核验；来源观测日期另列，抓取时间不是发生时间。"
  },
  {
    "url": "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value_month=202611&type=daily_treasury_yield_curve",
    "checked_at": "2026-11-17T04:14:13.777825+00:00",
    "note": "本轮公开网页核验；来源观测日期另列，抓取时间不是发生时间。"
  },
  {
    "url": "https://www.matteoiacoviello.com/gpr.htm",
    "checked_at": "2026-11-17T04:14:13.777825+00:00",
    "note": "本轮公开网页核验；来源观测日期另列，抓取时间不是发生时间。"
  },
  {
    "url": "https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/default.aspx",
    "checked_at": "2026-11-17T04:14:13.777825+00:00",
    "note": "本轮公开网页核验；来源观测日期另列，抓取时间不是发生时间。"
  },
  {
    "url": "https://www.federalreserve.gov/newsevents/2026-November.htm",
    "checked_at": "2026-11-17T04:14:13.777825+00:00",
    "note": "本轮公开网页核验；来源观测日期另列，抓取时间不是发生时间。"
  },
  {
    "url": "https://www.bls.gov/mxp/",
    "checked_at": "2026-11-17T04:14:13.777825+00:00",
    "note": "本轮公开网页核验；来源观测日期另列，抓取时间不是发生时间。"
  },
  {
    "url": "https://www.sec.gov/Archives/edgar/data/2130357/000162828026073040/anthropicpbc-fwpxeeaprospea.htm",
    "checked_at": "2026-11-17T04:14:13.777825+00:00",
    "note": "本轮公开网页核验；来源观测日期另列，抓取时间不是发生时间。"
  },
  {
    "url": "https://www.nyse.com/trade/hours-calendars",
    "checked_at": "2026-11-17T04:14:13.777825+00:00",
    "note": "本轮公开网页核验；来源观测日期另列，抓取时间不是发生时间。"
  },
  {
    "url": "https://www.cnn.com/markets/fear-and-greed",
    "checked_at": "2026-11-17T04:14:13.777825+00:00",
    "note": "本轮抓取失败；不提供新CNN数值。"
  },
  {
    "url": "https://nvidianews.nvidia.com/news/nvidia-board-of-directors-establishes-national-security-and-export-control-oversight-committee",
    "checked_at": "2026-11-17T12:04:00+00:00",
    "note": "本轮官方公告已读；后续重开失败不撤销先前观察。"
  },
  {
    "url": "https://www.census.gov/retail/release_schedule.html",
    "checked_at": "2026-11-17T12:11:21.129205+00:00",
    "note": "官方日程重新核验。"
  },
  {
    "url": "https://edition.cnn.com/markets/fear-and-greed",
    "checked_at": "2026-11-17T12:01:40+00:00",
    "note": "官方可见页面31/Fear，API失败。"
  },
  {
    "url": "https://apnews.com/article/582e0b5d51be06f0ed630fac24f39b72",
    "checked_at": "2026-11-17T12:04:00+00:00",
    "note": "只核验搜索可见报道摘要，原文打开失败。"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0001045810.json",
    "checked_at": "2026-11-17T12:07:50.011593+00:00",
    "note": "本轮SEC定期披露列表核验；关键财务输入完整度另列。"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0000789019.json",
    "checked_at": "2026-11-17T12:08:17.690311+00:00",
    "note": "本轮SEC定期披露列表核验；关键财务输入完整度另列。"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0001018724.json",
    "checked_at": "2026-11-17T12:08:23.404010+00:00",
    "note": "本轮SEC定期披露列表核验；关键财务输入完整度另列。"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0001652044.json",
    "checked_at": "2026-11-17T12:08:29.100197+00:00",
    "note": "本轮SEC定期披露列表核验；关键财务输入完整度另列。"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0001326801.json",
    "checked_at": "2026-11-17T12:08:48.309785+00:00",
    "note": "本轮SEC定期披露列表核验；关键财务输入完整度另列。"
  }
]
```

## 付费信源建议（未订阅）

```json
[]
```
