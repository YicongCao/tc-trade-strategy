# 每日交易总结 · 2026-11-03

## 一分钟读懂 · Agent 摘要

### 当前判断

盘前修复增强，但不是整个AI板块一起转强，更不是已确认趋势反转。大盘与金融改善，部分算力、云和存储仍掉队。

### 与上次相比

相对早报，主流媒体已判定民主党赢得两院；大盘与黄金走强，AMD财报后的涨幅有所回吐。今晚重点从“有没有反弹”转向“谁能守住反弹”。

### 最重要的信号

- 北京时间20:03附近SPY762.45、QQQ690.59，但SMH522.01仍略低于522.49观察位；MU、SNDK弱于大盘。
- VIX盘前18.19低于昨收20.83；黄金与长债上涨、油价回落，恐慌缓和中仍有避险需求。
- Oracle新SEC文件确认100亿美元股票发行条款；融资仍开放，但现金回报、债务成本与稀释压力未消失。

### 接下来观察

- 今晚22:30开盘后看30–60分钟：QQQ690.49、SMH522.49能否一起守住回踩，且等权/金融持续参与。
- 优先观察金融、医疗与工业的承接；芯片须分化筛选，警惕指数涨而AI基础设施持续弱。
- 23:00北京ISM服务业及盘后QCOM财报是新检验点；QQQ失683.45、SMH失511.63且反抽不回则修复降级。

### 不要忽略

盘前报价异步、部分ETF稀疏；VWAP与全成分广度、当期申赎、CNN及四家公司估值桥仍缺。

## 研究结论

11月4日晚报：选举后大盘修复、黄金走强；AI链条分化，可靠反弹仍待今晚常规交易验证。

## 时点与口径

| 项目 | 内容 |
| --- | --- |
| 模式 | 每日交易总结 |
| 常规交易窗口 | 2026-11-03 → 2026-11-03（纽约交易日） |
| 截止·纽约 | 2026-11-04T07:09:46.338083-05:00 |
| 截止·北京 | 2026-11-04T20:09:46.338083+08:00 |
| 实际生成时间 | 2026-11-04T12:09:46.647943+00:00 |
| 市场阶段 | 盘前 |
| 下一交易日 | 2026-11-04 |
| 运行重点 | 全市场 |
| 上一版本 | reports/daily/2026-11-03/20261103T232406.152751Z/evidence.json |
| 质量 | partial |
| Daily 北京时间计划时段 | 2026-11-04T20:00:00+08:00 |

## 采集、补查与剩余缺口

| 目标 | 补查结果 | 来源 | 观测 / 抓取时间 | 说明 |
| --- | --- | --- | --- | --- |
| 1219847 | 已校验接入 | https://gamma-api.polymarket.com/events/1219847 | 2026-11-04T12:04:00.023864+00:00 / 2026-11-04T12:04:00.023864+00:00 | Gamma snapshot quote not last trade; distinct expiry and rule hash stays separate |
| 1262792 | 已校验接入 | https://gamma-api.polymarket.com/events/1262792 | 2026-11-04T12:04:00.044767+00:00 / 2026-11-04T12:04:00.044767+00:00 | Gamma snapshot quote not last trade; distinct expiry and rule hash stays separate |
| 1147445 | 已校验接入 | https://gamma-api.polymarket.com/events/1147445 | 2026-11-04T12:04:00.035029+00:00 / 2026-11-04T12:04:00.035029+00:00 | Gamma snapshot quote not last trade; distinct expiry and rule hash stays separate |
| 549019 | 已校验接入 | https://gamma-api.polymarket.com/events/549019 | 2026-11-04T12:04:03.289116+00:00 / 2026-11-04T12:04:03.289116+00:00 | Gamma snapshot quote not last trade; distinct expiry and rule hash stays separate |
| 1038648 | 未接入 | 缺失 |  /  | 没有可核验的活跃Yes合约 |
| 652109 | 已校验接入 | https://gamma-api.polymarket.com/events/652109 | 2026-11-04T12:04:03.364195+00:00 / 2026-11-04T12:04:03.364195+00:00 | Gamma snapshot quote not last trade; distinct expiry and rule hash stays separate |
| 199777 | 已校验接入 | https://gamma-api.polymarket.com/events/199777 | 2026-11-04T12:04:04.696513+00:00 / 2026-11-04T12:04:04.696513+00:00 | Gamma snapshot quote not last trade; distinct expiry and rule hash stays separate |

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
| prices.SPY.value | 754.35 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_1d_pct | 0.30 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_5d_pct | -1.99 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_20d_pct | -3.18 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_60d_pct | -2.17 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_1d_pp | 0.00 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_5d_pp | 0.00 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_20d_pp | 0.00 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_60d_pp | 0.00 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma20 | 768.09 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma50 | 766.40 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma200 | 726.65 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma20_pct | -1.79 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma50_pct | -1.57 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma200_pct | 3.81 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_sma | 8.52 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_pct | 1.13 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.drawdown_from_63d_high_pct | -3.18 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.volume_vs_previous20_ratio | 0.82 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SPY/history/ |
| prices.QQQ.value | 685.28 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_1d_pct | 0.62 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_5d_pct | -4.99 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_20d_pct | -9.79 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_60d_pct | -4.84 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_1d_pp | 0.32 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_5d_pp | -3.00 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_20d_pp | -6.62 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_60d_pp | -2.66 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma20 | 720.71 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma50 | 723.67 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma200 | 679.01 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma20_pct | -4.92 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma50_pct | -5.30 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma200_pct | 0.92 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_sma | 14.54 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_pct | 2.12 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.drawdown_from_63d_high_pct | -9.79 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.volume_vs_previous20_ratio | 0.89 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.IWM.value | 279.79 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_1d_pct | 0.23 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_5d_pct | -0.14 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_20d_pct | -0.55 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_60d_pct | -6.49 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_1d_pp | -0.07 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_5d_pp | 1.85 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_20d_pp | 2.62 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_60d_pp | -4.31 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma20 | 277.12 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma50 | 283.28 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma200 | 277.85 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma20_pct | 0.96 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma50_pct | -1.23 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma200_pct | 0.70 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_sma | 3.85 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_pct | 1.38 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.drawdown_from_63d_high_pct | -8.05 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.volume_vs_previous20_ratio | 0.72 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IWM/history/ |
| prices.RSP.value | 219.26 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_1d_pct | -0.33 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_5d_pct | 0.80 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_20d_pct | 3.26 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_60d_pct | -0.06 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_1d_pp | -0.63 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_5d_pp | 2.79 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_20d_pp | 6.44 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_60d_pp | 2.11 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma20 | 215.68 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma50 | 214.67 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma200 | 206.75 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma20_pct | 1.66 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma50_pct | 2.14 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma200_pct | 6.05 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_sma | 2.22 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_pct | 1.01 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.drawdown_from_63d_high_pct | -1.21 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.volume_vs_previous20_ratio | 1.19 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/RSP/history/ |
| prices.GLD.value | 359.26 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_1d_pct | -0.66 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_5d_pct | -3.50 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_20d_pct | -6.02 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_60d_pct | -10.75 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_1d_pp | -0.96 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_5d_pp | -1.51 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_20d_pp | -2.84 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_60d_pp | -8.58 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma20 | 373.72 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma50 | 387.99 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma200 | 412.30 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma20_pct | -3.87 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma50_pct | -7.40 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma200_pct | -12.86 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_sma | 5.78 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_pct | 1.61 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.drawdown_from_63d_high_pct | -16.07 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.volume_vs_previous20_ratio | 0.71 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GC=F.value | 3,940.40 | USD_per_troy_ounce | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_1d_pct | -0.74 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_5d_pct | -3.29 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_20d_pct | -5.89 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_60d_pct | -10.84 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_1d_pp | -1.03 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_5d_pp | -1.30 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_20d_pp | -2.72 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_60d_pp | -8.67 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma20 | 4,093.34 | USD_per_troy_ounce | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma50 | 4,265.43 | USD_per_troy_ounce | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma200 | 4,512.77 | USD_per_troy_ounce | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma20_pct | -3.74 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma50_pct | -7.62 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma200_pct | -12.68 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_sma | 76.08 | USD_per_troy_ounce | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_pct | 1.93 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.drawdown_from_63d_high_pct | -16.12 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.volume_vs_previous20_ratio | 1.12 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.CL=F.value | 96.09 | USD_per_barrel | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_1d_pct | -0.38 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_5d_pct | -3.81 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_20d_pct | 7.44 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_60d_pct | 17.00 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_1d_pp | -0.68 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_5d_pp | -1.82 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_20d_pp | 10.61 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_60d_pp | 19.17 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma20 | 98.12 | USD_per_barrel | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma50 | 95.04 | USD_per_barrel | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma200 | 86.71 | USD_per_barrel | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma20_pct | -2.07 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma50_pct | 1.11 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma200_pct | 10.82 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_sma | 4.88 | USD_per_barrel | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_pct | 5.08 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.drawdown_from_63d_high_pct | -9.20 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.volume_vs_previous20_ratio | 1.45 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.BZ=F.value | 103.60 | USD_per_barrel | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_1d_pct | -1.12 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_5d_pct | -9.03 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_20d_pct | 3.00 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_60d_pct | 18.10 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_1d_pp | -1.42 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_5d_pp | -7.04 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_20d_pp | 6.18 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_60d_pp | 20.28 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma20 | 109.32 | USD_per_barrel | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma50 | 103.70 | USD_per_barrel | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma200 | 92.86 | USD_per_barrel | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma20_pct | -5.23 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma50_pct | -0.10 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma200_pct | 11.57 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_sma | 4.87 | USD_per_barrel | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_pct | 4.70 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.drawdown_from_63d_high_pct | -11.93 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.volume_vs_previous20_ratio | 1.52 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.TLT.value | 81.11 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_1d_pct | -0.76 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_5d_pct | -0.64 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_20d_pct | 4.96 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_60d_pct | -0.78 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_1d_pp | -1.06 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_5d_pp | 1.35 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_20d_pp | 8.13 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_60d_pp | 1.40 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma20 | 80.09 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma50 | 80.43 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma200 | 83.49 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma20_pct | 1.28 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma50_pct | 0.84 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma200_pct | -2.85 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_sma | 0.82 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_pct | 1.02 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.drawdown_from_63d_high_pct | -2.46 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.volume_vs_previous20_ratio | 0.79 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/TLT/history/ |
| prices.UUP.value | 29.01 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_1d_pct | 0.17 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_5d_pct | -0.38 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_20d_pct | 0.38 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_60d_pct | 3.09 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_1d_pp | -0.13 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_5d_pp | 1.61 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_20d_pp | 3.56 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_60d_pp | 5.27 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma20 | 29.01 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma50 | 28.63 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma200 | 27.94 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma20_pct | 0.02 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma50_pct | 1.34 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma200_pct | 3.83 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_sma | 0.10 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_pct | 0.35 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.drawdown_from_63d_high_pct | -0.41 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.volume_vs_previous20_ratio | 0.56 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/UUP/history/ |
| prices.HYG.value | 76.98 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_1d_pct | 0.12 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_5d_pct | -0.80 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_20d_pct | -0.38 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_60d_pct | -2.61 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_1d_pp | -0.18 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_5d_pp | 1.19 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_20d_pp | 2.80 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_60d_pp | -0.44 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma20 | 77.14 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma50 | 77.91 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma200 | 78.19 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma20_pct | -0.21 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma50_pct | -1.20 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma200_pct | -1.55 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_sma | 0.31 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_pct | 0.41 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.drawdown_from_63d_high_pct | -3.15 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.volume_vs_previous20_ratio | 0.75 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/HYG/history/ |
| prices.LQD.value | 103.72 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_1d_pct | 0.01 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_5d_pct | -0.56 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_20d_pct | 1.55 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_60d_pct | -1.70 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_1d_pp | -0.29 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_5d_pp | 1.43 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_20d_pp | 4.72 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_60d_pp | 0.47 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma20 | 103.37 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma50 | 103.95 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma200 | 106.22 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma20_pct | 0.34 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma50_pct | -0.22 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma200_pct | -2.35 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_sma | 0.62 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_pct | 0.60 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.drawdown_from_63d_high_pct | -2.53 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.volume_vs_previous20_ratio | 0.99 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/LQD/history/ |
| prices.^VIX.value | 20.83 | index | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_1d_pct | -1.51 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_5d_pct | 18.89 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_20d_pct | 38.77 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_60d_pct | 36.32 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_1d_pp | -1.81 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_5d_pp | 20.88 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_20d_pp | 41.95 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_60d_pp | 38.18 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma20 | 17.57 | index | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma50 | 16.40 | index | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma200 | 18.28 | index | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma20_pct | 18.53 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma50_pct | 27.04 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma200_pct | 13.93 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_sma | 2.66 | index | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_pct | 12.76 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.drawdown_from_63d_high_pct | -1.51 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-03 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX3M.value | 21.27 | index | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_1d_pct | -1.53 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_5d_pct | 8.69 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_20d_pct | 20.58 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_60d_pct | 12.07 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_1d_pp | -1.83 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_5d_pp | 10.68 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_20d_pp | 23.75 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_60d_pp | 14.24 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma20 | 19.35 | index | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma50 | 18.69 | index | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma200 | 20.53 | index | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma20_pct | 9.95 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma50_pct | 13.79 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma200_pct | 3.59 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_sma | 1.46 | index | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_pct | 6.85 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.drawdown_from_63d_high_pct | -1.53 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-03 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VVIX.value | 107.40 | index | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_1d_pct | -2.78 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_5d_pct | 7.99 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_20d_pct | 30.04 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_60d_pct | 16.10 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_1d_pp | -3.08 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_5d_pp | 9.98 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_20d_pp | 33.22 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_60d_pp | 18.27 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma20 | 98.00 | index | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma50 | 92.46 | index | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma200 | 98.88 | index | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma20_pct | 9.59 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma50_pct | 16.15 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma200_pct | 8.61 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_sma | 11.60 | index | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_pct | 10.80 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.drawdown_from_63d_high_pct | -2.78 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-03 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^MOVE.value | 99.97 | index | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_1d_pct | -0.39 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_5d_pct | 2.15 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_20d_pct | -12.00 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_60d_pct | 38.79 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_1d_pp | -0.69 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_5d_pp | 4.13 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_20d_pp | -9.36 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_60d_pp | 40.99 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma20 | 100.42 | index | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma50 | 91.43 | index | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma200 | 77.97 | index | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma20_pct | -0.45 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma50_pct | 9.34 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma200_pct | 28.21 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_sma | 4.49 | index | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_pct | 4.49 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.drawdown_from_63d_high_pct | -12.00 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-03 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.NVDA.value | 206.69 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_1d_pct | 2.29 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_5d_pct | -5.16 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_20d_pct | -13.61 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_60d_pct | -4.89 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_1d_pp | 1.99 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_5d_pp | -3.17 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_20d_pp | -10.43 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_60d_pp | -2.71 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma20 | 217.99 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma50 | 221.41 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma200 | 204.27 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma20_pct | -5.18 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma50_pct | -6.65 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma200_pct | 1.18 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_sma | 6.61 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_pct | 3.20 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.drawdown_from_63d_high_pct | -13.61 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.volume_vs_previous20_ratio | 0.90 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.MSFT.value | 520.99 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_1d_pct | 2.74 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_5d_pct | -1.95 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_20d_pct | -1.57 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_60d_pct | 3.14 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_1d_pp | 2.44 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_5d_pp | 0.04 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_20d_pp | 1.61 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_60d_pp | 5.32 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma20 | 529.66 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma50 | 514.06 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma200 | 437.44 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma20_pct | -1.64 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma50_pct | 1.35 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma200_pct | 19.10 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_sma | 13.01 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_pct | 2.50 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.drawdown_from_63d_high_pct | -4.13 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.volume_vs_previous20_ratio | 0.89 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.AMZN.value | 250.69 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_1d_pct | 2.06 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_5d_pct | -0.95 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_20d_pct | -2.19 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_60d_pct | -9.85 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_1d_pp | 1.76 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_5d_pp | 1.04 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_20d_pp | 0.99 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_60d_pp | -7.68 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma20 | 253.82 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma50 | 253.79 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma200 | 243.50 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma20_pct | -1.23 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma50_pct | -1.22 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma200_pct | 2.95 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_sma | 8.35 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_pct | 3.33 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.drawdown_from_63d_high_pct | -9.85 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.volume_vs_previous20_ratio | 0.88 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.GOOGL.value | 280.03 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_1d_pct | 0.37 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_5d_pct | -12.65 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_20d_pct | -19.46 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_60d_pct | -21.62 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_1d_pp | 0.07 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_5d_pp | -10.66 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_20d_pp | -16.28 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_60d_pp | -19.45 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma20 | 327.15 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma50 | 336.36 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma200 | 339.83 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma20_pct | -14.40 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma50_pct | -16.75 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma200_pct | -17.60 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_sma | 10.31 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_pct | 3.68 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.drawdown_from_63d_high_pct | -21.67 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.volume_vs_previous20_ratio | 1.02 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.META.value | 621.03 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_1d_pct | 2.36 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_5d_pct | 0.14 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_20d_pct | -15.95 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_60d_pct | 4.47 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_1d_pp | 2.06 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_5d_pp | 2.12 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_20d_pp | -12.77 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_60d_pp | 6.65 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma20 | 678.46 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma50 | 672.18 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma200 | 631.22 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma20_pct | -8.46 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma50_pct | -7.61 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma200_pct | -1.62 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_sma | 22.82 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_pct | 3.67 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.drawdown_from_63d_high_pct | -20.13 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.volume_vs_previous20_ratio | 0.58 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/META/history/ |
| prices.CRWV.value | 53.74 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_1d_pct | 7.16 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_5d_pct | -9.79 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_20d_pct | -41.41 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_60d_pct | -39.06 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_1d_pp | 6.86 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_5d_pp | -7.80 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_20d_pp | -38.23 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_60d_pp | -36.89 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma20 | 65.01 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma50 | 78.05 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma200 | 90.89 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma20_pct | -17.33 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma50_pct | -31.15 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma200_pct | -40.87 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_sma | 6.28 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_pct | 11.69 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.drawdown_from_63d_high_pct | -50.12 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.volume_vs_previous20_ratio | 0.60 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.MU.value | 855.10 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_1d_pct | 2.58 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_5d_pct | -7.93 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_20d_pct | -18.20 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_60d_pct | -0.67 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_1d_pp | 2.28 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_5d_pp | -5.94 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_20d_pp | -15.03 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_60d_pp | 1.50 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma20 | 929.53 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma50 | 974.83 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma200 | 751.57 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma20_pct | -8.01 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma50_pct | -12.28 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma200_pct | 13.77 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_sma | 51.08 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_pct | 5.97 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.drawdown_from_63d_high_pct | -22.07 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.volume_vs_previous20_ratio | 0.79 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MU/history/ |
| prices.DRAM.value | 47.64 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_1d_pct | 2.85 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_5d_pct | -5.70 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_20d_pct | -19.96 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_60d_pct | -3.95 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_1d_pp | 2.55 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_5d_pp | -3.71 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_20d_pp | -16.78 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_60d_pp | -1.78 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma20 | 50.61 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma50 | 55.61 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma200 | 缺失 | USD_per_share | 2026-11-03 | unavailable | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma20_pct | -5.87 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma50_pct | -14.33 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma200_pct | 缺失 | percent | 2026-11-03 | unavailable | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_sma | 2.89 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_pct | 6.07 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.drawdown_from_63d_high_pct | -25.12 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.volume_vs_previous20_ratio | 0.65 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.VRT.value | 235.97 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_1d_pct | 5.23 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_5d_pct | 13.14 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_20d_pct | -6.78 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_60d_pct | -12.61 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_1d_pp | 4.93 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_5d_pp | 15.13 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_20d_pp | -3.61 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_60d_pp | -10.44 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma20 | 222.76 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma50 | 241.45 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma200 | 270.99 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma20_pct | 5.93 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma50_pct | -2.27 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma200_pct | -12.92 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_sma | 15.46 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_pct | 6.55 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.drawdown_from_63d_high_pct | -19.67 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.volume_vs_previous20_ratio | 0.70 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/VRT/history/ |
| prices.XLK.value | 176.51 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_1d_pct | 1.31 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_5d_pct | -6.85 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_20d_pct | -12.62 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_60d_pct | -5.15 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_1d_pp | 1.02 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_5d_pp | -4.86 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_20d_pp | -9.44 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_60d_pp | -2.98 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma20 | 188.25 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma50 | 189.36 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma200 | 169.54 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma20_pct | -6.24 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma50_pct | -6.79 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma200_pct | 4.11 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_sma | 4.96 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_pct | 2.81 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.drawdown_from_63d_high_pct | -12.62 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.volume_vs_previous20_ratio | 1.12 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLE.value | 66.68 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_1d_pct | -0.85 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_5d_pct | -2.24 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_20d_pct | 4.60 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_60d_pct | 11.46 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_1d_pp | -1.15 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_5d_pp | -0.25 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_20d_pp | 7.77 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_60d_pp | 13.63 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma20 | 67.46 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma50 | 64.94 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma200 | 58.35 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma20_pct | -1.15 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma50_pct | 2.69 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma200_pct | 14.27 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_sma | 1.57 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_pct | 2.35 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.drawdown_from_63d_high_pct | -4.77 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.volume_vs_previous20_ratio | 0.94 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLF.value | 57.19 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_1d_pct | -0.64 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_5d_pct | 2.34 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_20d_pct | 5.89 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_60d_pct | -0.72 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_1d_pp | -0.94 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_5d_pp | 4.33 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_20d_pp | 9.06 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_60d_pp | 1.45 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma20 | 55.67 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma50 | 55.85 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma200 | 53.44 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma20_pct | 2.72 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma50_pct | 2.39 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma200_pct | 7.01 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_sma | 0.75 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_pct | 1.31 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.drawdown_from_63d_high_pct | -1.99 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.volume_vs_previous20_ratio | 0.92 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLI.value | 171.32 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_1d_pct | 0.95 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_5d_pct | 2.02 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_20d_pct | -0.15 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_60d_pct | -6.94 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_1d_pp | 0.65 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_5d_pp | 4.01 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_20d_pp | 3.02 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_60d_pp | -4.77 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma20 | 168.05 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma50 | 170.16 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma200 | 172.63 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma20_pct | 1.94 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma50_pct | 0.68 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma200_pct | -0.76 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_sma | 2.80 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_pct | 1.63 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.drawdown_from_63d_high_pct | -7.90 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.volume_vs_previous20_ratio | 1.26 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLV.value | 184.02 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_1d_pct | -0.31 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_5d_pct | 2.70 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_20d_pct | 10.13 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_60d_pct | 9.67 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_1d_pp | -0.61 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_5d_pp | 4.69 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_20d_pp | 13.31 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_60d_pp | 11.84 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma20 | 177.40 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma50 | 172.37 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma200 | 157.97 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma20_pct | 3.73 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma50_pct | 6.76 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma200_pct | 16.49 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_sma | 3.11 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_pct | 1.69 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.drawdown_from_63d_high_pct | -0.46 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.volume_vs_previous20_ratio | 1.17 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLP.value | 88.95 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_1d_pct | -2.07 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_5d_pct | 2.07 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_20d_pct | 8.74 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_60d_pct | 5.40 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_1d_pp | -2.37 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_5d_pp | 4.05 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_20d_pp | 11.92 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_60d_pp | 7.57 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma20 | 86.86 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma50 | 84.53 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma200 | 83.67 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma20_pct | 2.41 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma50_pct | 5.22 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma200_pct | 6.31 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_sma | 1.51 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_pct | 1.70 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.drawdown_from_63d_high_pct | -2.07 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.volume_vs_previous20_ratio | 1.41 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLY.value | 117.33 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_1d_pct | -0.70 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_5d_pct | 1.63 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_20d_pct | 5.02 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_60d_pct | -1.74 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_1d_pp | -1.00 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_5d_pp | 3.62 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_20d_pp | 8.20 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_60d_pp | 0.43 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma20 | 114.18 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma50 | 113.13 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma200 | 115.12 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma20_pct | 2.76 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma50_pct | 3.71 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma200_pct | 1.92 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_sma | 1.95 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_pct | 1.66 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.drawdown_from_63d_high_pct | -1.90 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.volume_vs_previous20_ratio | 1.39 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLC.value | 101.44 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_1d_pct | 1.18 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_5d_pct | -2.07 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_20d_pct | -9.14 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_60d_pct | -8.99 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_1d_pp | 0.88 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_5d_pp | -0.08 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_20d_pp | -5.97 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_60d_pp | -6.82 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma20 | 107.33 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma50 | 110.14 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma200 | 112.21 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma20_pct | -5.49 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma50_pct | -7.90 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma200_pct | -9.60 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_sma | 1.84 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_pct | 1.81 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.drawdown_from_63d_high_pct | -11.60 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.volume_vs_previous20_ratio | 1.91 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLU.value | 43.42 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_1d_pct | -0.57 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_5d_pct | 1.33 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_20d_pct | 5.49 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_60d_pct | 1.41 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_1d_pp | -0.87 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_5d_pp | 3.32 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_20d_pp | 8.67 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_60d_pp | 3.59 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma20 | 42.25 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma50 | 41.66 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma200 | 43.81 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma20_pct | 2.78 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma50_pct | 4.22 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma200_pct | -0.90 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_sma | 0.59 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_pct | 1.36 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.drawdown_from_63d_high_pct | -1.29 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.volume_vs_previous20_ratio | 0.92 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLRE.value | 43.67 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_1d_pct | 0.07 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_5d_pct | 2.90 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_20d_pct | 6.25 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_60d_pct | -0.82 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_1d_pp | -0.23 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_5d_pp | 4.89 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_20d_pp | 9.43 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_60d_pp | 1.36 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma20 | 42.23 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma50 | 42.46 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma200 | 42.80 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma20_pct | 3.42 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma50_pct | 2.86 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma200_pct | 2.04 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_sma | 0.63 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_pct | 1.43 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.drawdown_from_63d_high_pct | -2.92 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.volume_vs_previous20_ratio | 0.90 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLB.value | 52.59 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_1d_pct | -2.01 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_5d_pct | 1.56 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_20d_pct | 5.75 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_60d_pct | -0.65 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_1d_pp | -2.31 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_5d_pp | 3.55 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_20d_pp | 8.93 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_60d_pp | 1.52 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma20 | 51.05 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma50 | 50.89 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma200 | 50.77 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma20_pct | 3.01 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma50_pct | 3.34 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma200_pct | 3.58 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_sma | 0.77 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_pct | 1.46 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.drawdown_from_63d_high_pct | -2.01 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.volume_vs_previous20_ratio | 1.28 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLB/history/ |
| prices.SMH.value | 518.52 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_1d_pct | 2.01 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_5d_pct | -7.07 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_20d_pct | -18.02 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_60d_pct | -8.94 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_1d_pp | 1.71 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_5d_pp | -5.08 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_20d_pp | -14.85 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_60d_pp | -6.76 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma20 | 557.92 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma50 | 571.01 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma200 | 520.65 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma20_pct | -7.06 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma50_pct | -9.19 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma200_pct | -0.41 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_sma | 21.11 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_pct | 4.07 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.drawdown_from_63d_high_pct | -18.20 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.volume_vs_previous20_ratio | 0.92 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SMH/history/ |
| prices.IGV.value | 102.66 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_1d_pct | 0.75 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_5d_pct | -8.16 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_20d_pct | -7.65 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_60d_pct | -2.24 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_1d_pp | 0.45 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_5d_pp | -6.17 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_20d_pp | -4.47 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_60d_pp | -0.06 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma20 | 108.44 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma50 | 106.97 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma200 | 93.99 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma20_pct | -5.33 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma50_pct | -4.03 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma200_pct | 9.23 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_sma | 3.17 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_pct | 3.08 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.drawdown_from_63d_high_pct | -8.88 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.volume_vs_previous20_ratio | 0.98 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IGV/history/ |
| prices.XOP.value | 191.52 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_1d_pct | -1.05 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_5d_pct | -4.24 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_20d_pct | 1.62 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_60d_pct | 9.30 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_1d_pp | -1.35 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_5d_pp | -2.26 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_20d_pp | 4.80 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_60d_pp | 11.47 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma20 | 197.56 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma50 | 191.60 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma200 | 170.21 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma20_pct | -3.06 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma50_pct | -0.04 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma200_pct | 12.52 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_sma | 5.22 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_pct | 2.72 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.drawdown_from_63d_high_pct | -6.51 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.volume_vs_previous20_ratio | 1.23 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XOP/history/ |
| prices.OIH.value | 385.11 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_1d_pct | -1.01 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_5d_pct | -5.81 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_20d_pct | -1.62 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_60d_pct | -6.38 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_1d_pp | -1.31 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_5d_pp | -3.82 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_20d_pp | 1.55 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_60d_pp | -4.20 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma20 | 391.45 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma50 | 400.16 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma200 | 398.24 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma20_pct | -1.62 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma50_pct | -3.76 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma200_pct | -3.30 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_sma | 12.44 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_pct | 3.23 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.drawdown_from_63d_high_pct | -11.79 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.volume_vs_previous20_ratio | 1.01 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/OIH/history/ |
| prices.ITA.value | 216.17 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_1d_pct | 0.69 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_5d_pct | 4.82 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_20d_pct | 3.80 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_60d_pct | -13.82 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_1d_pp | 0.39 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_5d_pp | 6.81 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_20d_pp | 6.97 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_60d_pp | -11.65 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma20 | 207.39 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma50 | 213.84 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma200 | 228.33 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma20_pct | 4.23 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma50_pct | 1.09 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma200_pct | -5.32 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_sma | 5.05 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_pct | 2.33 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.drawdown_from_63d_high_pct | -14.53 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.volume_vs_previous20_ratio | 1.38 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ARKX.value | 29.91 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_1d_pct | 1.15 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_5d_pct | -3.02 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_20d_pct | -9.99 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_60d_pct | -13.08 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_1d_pp | 0.85 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_5d_pp | -1.03 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_20d_pp | -6.82 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_60d_pp | -10.90 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma20 | 30.66 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma50 | 31.63 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma200 | 32.43 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma20_pct | -2.45 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma50_pct | -5.45 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma200_pct | -7.78 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_sma | 0.83 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_pct | 2.79 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.drawdown_from_63d_high_pct | -14.20 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.volume_vs_previous20_ratio | 0.54 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.KRE.value | 72.88 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_1d_pct | -1.15 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_5d_pct | 0.41 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_20d_pct | 4.01 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_60d_pct | -3.60 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_1d_pp | -1.45 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_5d_pp | 2.40 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_20d_pp | 7.19 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_60d_pp | -1.42 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma20 | 70.92 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma50 | 71.76 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma200 | 70.41 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma20_pct | 2.76 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma50_pct | 1.56 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma200_pct | 3.51 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_sma | 1.37 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_pct | 1.88 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.drawdown_from_63d_high_pct | -5.95 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.volume_vs_previous20_ratio | 0.80 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/KRE/history/ |
| prices.SKYY.value | 155.98 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_1d_pct | 0.93 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_5d_pct | -9.03 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_20d_pct | -8.79 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_60d_pct | -2.99 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_1d_pp | 0.63 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_5d_pp | -7.04 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_20d_pp | -5.61 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_60d_pp | -0.81 | pp | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma20 | 166.15 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma50 | 164.61 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma200 | 136.81 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma20_pct | -6.12 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma50_pct | -5.24 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma200_pct | 14.01 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_sma | 5.19 | USD_per_share | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_pct | 3.33 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.drawdown_from_63d_high_pct | -10.81 | percent | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.volume_vs_previous20_ratio | 0.79 | ratio | 2026-11-03 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SKYY/history/ |
| macro.DGS2.value | 4.59 | percent | 2026-11-02 | lagged | source_series_v1:DGS2 | https://fred.stlouisfed.org/series/DGS2 |
| macro.BAMLH0A0HYM2.value | 3.43 | percentage_points | 2026-11-02 | lagged | source_series_v1:BAMLH0A0HYM2 | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| macro.BAMLC0A0CM.value | 0.94 | percentage_points | 2026-11-02 | lagged | source_series_v1:BAMLC0A0CM | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| macro.DGS10.value | 4.91 | percent | 2026-11-02 | lagged | source_series_v1:DGS10 | https://fred.stlouisfed.org/series/DGS10 |
| macro.DFII10.value | 2.62 | percent | 2026-11-02 | lagged | source_series_v1:DFII10 | https://fred.stlouisfed.org/series/DFII10 |
| macro.T10YIE.value | 2.30 | percent | 2026-11-03 | ok | source_series_v1:T10YIE | https://fred.stlouisfed.org/series/T10YIE |
| macro.STLFSI4.value | -0.58 | index | 2026-10-23 | lagged | source_series_v1:STLFSI4 | https://fred.stlouisfed.org/series/STLFSI4 |
| macro.CBOE_VIX.value | 20.83 | index | 2026-11-03 | ok | source_series_v1:CBOE_VIX | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| macro.GPRD.value | 97.67 | index | 2026-11-02 | lagged | source_series_v1:GPRD | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_ACT.value | 113.60 | index | 2026-11-02 | lagged | source_series_v1:GPRD_ACT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_THREAT.value | 94.75 | index | 2026-11-02 | lagged | source_series_v1:GPRD_THREAT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA7.value | 137.64 | index | 2026-11-02 | lagged | source_series_v1:GPRD_MA7 | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA30.value | 164.04 | index | 2026-11-02 | lagged | source_series_v1:GPRD_MA30 | https://www.matteoiacoviello.com/gpr.htm |
| quotes.AAPL.value | 335.12 | USD_per_share | 2026-11-04T12:04:06+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AAPL |
| quotes.AMD.value | 502.15 | USD_per_share | 2026-11-04T12:04:07+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AMD |
| quotes.AMZN.value | 258.20 | USD_per_share | 2026-11-04T12:03:40+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AMZN |
| quotes.AVGO.value | 334.63 | USD_per_share | 2026-11-04T12:03:36+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AVGO |
| quotes.BABA.value | 103.95 | USD_per_share | 2026-11-04T12:03:31+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/BABA |
| quotes.CAT.value | 616.12 | USD_per_share | 2026-11-04T12:03:29+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/CAT |
| quotes.CEG.value | 253.30 | USD_per_share | 2026-11-04T12:03:48+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/CEG |
| quotes.COIN.value | 147.30 | USD_per_share | 2026-11-04T12:03:09+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/COIN |
| quotes.CVX.value | 224.60 | USD_per_share | 2026-11-04T12:03:55+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/CVX |
| quotes.DRAM.value | 47.65 | USD_per_share | 2026-11-04T12:04:03+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/DRAM |
| quotes.GEV.value | 880.29 | USD_per_share | 2026-11-04T12:03:18+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GEV |
| quotes.GLD.value | 370.22 | USD_per_share | 2026-11-04T12:03:44+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GLD |
| quotes.GLW.value | 125.00 | USD_per_share | 2026-11-04T12:01:48+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GLW |
| quotes.GOOGL.value | 282.02 | USD_per_share | 2026-11-04T12:03:52+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GOOGL |
| quotes.IGV.value | 103.20 | USD_per_share | 2026-11-04T12:02:20+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/IGV |
| quotes.INTC.value | 59.63 | USD_per_share | 2026-11-04T12:04:01+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/INTC |
| quotes.IWM.value | 283.75 | USD_per_share | 2026-11-04T12:03:56+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/IWM |
| quotes.LITE.value | 673.51 | USD_per_share | 2026-11-04T12:03:24+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/LITE |
| quotes.LLY.value | 1,439.09 | USD_per_share | 2026-11-04T12:03:56+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/LLY |
| quotes.META.value | 629.68 | USD_per_share | 2026-11-04T12:03:42+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/META |
| quotes.MRVL.value | 170.80 | USD_per_share | 2026-11-04T12:03:57+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/MRVL |
| quotes.MSFT.value | 532.23 | USD_per_share | 2026-11-04T12:03:43+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/MSFT |
| quotes.MU.value | 851.99 | USD_per_share | 2026-11-04T12:04:00+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/MU |
| quotes.NOW.value | 111.63 | USD_per_share | 2026-11-04T12:03:56+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NOW |
| quotes.NVDA.value | 207.90 | USD_per_share | 2026-11-04T12:03:52+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| quotes.NXPI.value | 260.57 | USD_per_share | 2026-11-04T09:01:27+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NXPI |
| quotes.ORCL.value | 122.71 | USD_per_share | 2026-11-04T12:04:02+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/ORCL |
| quotes.PLTR.value | 170.77 | USD_per_share | 2026-11-04T12:04:01+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/PLTR |
| quotes.QQQ.value | 690.59 | USD_per_share | 2026-11-04T12:03:56+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| quotes.RSP.value | 221.79 | USD_per_share | 2026-11-04T11:43:00+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/RSP |
| quotes.SMH.value | 522.01 | USD_per_share | 2026-11-04T12:03:23+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SMH |
| quotes.SNDK.value | 1,116.00 | USD_per_share | 2026-11-04T12:04:04+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SNDK |
| quotes.SPY.value | 762.45 | USD_per_share | 2026-11-04T12:03:41+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SPY |
| quotes.STX.value | 598.50 | USD_per_share | 2026-11-04T12:03:34+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/STX |
| quotes.TLT.value | 81.46 | USD_per_share | 2026-11-04T12:01:34+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/TLT |
| quotes.VRT.value | 223.96 | USD_per_share | 2026-11-04T12:04:00+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/VRT |
| quotes.XLE.value | 66.40 | USD_per_share | 2026-11-04T12:00:14+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLE |
| quotes.XLF.value | 58.05 | USD_per_share | 2026-11-04T12:02:47+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLF |
| quotes.XLI.value | 171.52 | USD_per_share | 2026-11-04T11:39:00+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLI |
| quotes.XLV.value | 186.89 | USD_per_share | 2026-11-04T12:03:24+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLV |
| quotes.XOM.value | 176.40 | USD_per_share | 2026-11-04T12:04:00+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XOM |
| latest.BZ_F.value | 102.03 | USD/barrel | 2026-11-04T11:53:29+00:00 | lagged | 最后有效分钟；实际报价时间非请求时间，期货连续代码可能延迟且不拼接跨月收益 | https://query1.finance.yahoo.com/v8/finance/chart/BZ=F |
| latest.CL_F.value | 95.13 | USD/barrel | 2026-11-04T11:53:55+00:00 | lagged | 最后有效分钟；实际报价时间非请求时间，期货连续代码可能延迟且不拼接跨月收益 | https://query1.finance.yahoo.com/v8/finance/chart/CL=F |
| latest.DX-Y.NYB.value | 101.35 | index points | 2026-11-04T11:54:08+00:00 | lagged | 最后有效分钟；实际报价时间非请求时间，期货连续代码可能延迟且不拼接跨月收益 | https://query1.finance.yahoo.com/v8/finance/chart/DX-Y.NYB |
| latest.ES_F.value | 7,685.00 | index points | 2026-11-04T11:53:57+00:00 | lagged | 最后有效分钟；实际报价时间非请求时间，期货连续代码可能延迟且不拼接跨月收益 | https://query1.finance.yahoo.com/v8/finance/chart/ES=F |
| latest.GC_F.value | 4,050.80 | USD/troy_oz | 2026-11-04T11:54:02+00:00 | lagged | 最后有效分钟；实际报价时间非请求时间，期货连续代码可能延迟且不拼接跨月收益 | https://query1.finance.yahoo.com/v8/finance/chart/GC=F |
| latest.NQ_F.value | 28,584.00 | index points | 2026-11-04T11:54:01+00:00 | lagged | 最后有效分钟；实际报价时间非请求时间，期货连续代码可能延迟且不拼接跨月收益 | https://query1.finance.yahoo.com/v8/finance/chart/NQ=F |
| latest.TNX.value | 4.95 | percent | 2026-11-03T19:59:00+00:00 | lagged | 最后有效分钟；实际报价时间非请求时间，期货连续代码可能延迟且不拼接跨月收益 | https://query1.finance.yahoo.com/v8/finance/chart/^TNX |
| latest.VIX.value | 18.19 | index points | 2026-11-04T11:48:46+00:00 | ok | 最后有效分钟；实际报价时间非请求时间，期货连续代码可能延迟且不拼接跨月收益 | https://query1.finance.yahoo.com/v8/finance/chart/^VIX |

## 指标历史比较（不同日期观测，非连续交易日）

```json
[
  {
    "id": "prices.SPY.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 2.25,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -15.30999755859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.7781751188028818,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.2613479934080454,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.2553852692359193,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.06850652055931,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.24195408729956736,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -3.889973620758025,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.3207960438646462,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -4.008879035074509,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.237002563476608,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.3170074462890398,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.14457641601552496,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.2995422363280795,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.3402514648437318,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.837453613281241,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.4503737737331259,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.6918817289203414,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.3120910662391174,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.958426318067108,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.2611526031289335,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.375438874071434,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.4517822265625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.2371477399553568,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.06344804366702128,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.18320453951215376,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.2887984600549065,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.9651127637183796,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.45520057600697783,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.1104302881406124,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 4.19000244140625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -35.969970703125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.9765374897511068,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.6555180479838496,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.6190181003889901,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -5.4916085177816205,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.14134008368665718,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -7.530839312901161,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.8644025753539619,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -7.970790382027004,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.198362370948225,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.39417005457580423,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.36363283115307077,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -3.4231019972223105,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.38329417098622454,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -3.6408656921431364,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.5436065314893157,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -3.9619113469524954,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -3.718997192382858,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -12.471499633789108,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.4060949707030659,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.25519531249995,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.33064056396494834,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.961925964355487,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.066512753844406,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -3.288615213036661,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.6317823146169683,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -4.797952534658345,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.5682053869951575,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -5.605190016342432,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.6842869349888385,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.9871433803013385,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.11352289112733205,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.3813348007485877,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.5515628820170875,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -4.735009342960528,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.48209832119990925,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.040971600905858274,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.649993896484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.389984130859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.3008657220774591,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.9188111818487554,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.9154007190556257,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.734663018312621,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.9452901991586327,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.9702641490126673,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.7060561465091926,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.3189874823768886,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.4773093967254227,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.6574631884407101,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.6600154498197064,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.333843502246689,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.1872442864582,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 2.9197094717453576,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.3852601026445459,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 2.6898915526976195,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.0774993896484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.020501708984340894,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.3480755615234443,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.8017785644531727,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.07910354614256221,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.4756308746337936,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.26271572817655464,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.14820818805496572,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.35038097004300717,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.4874359207217793,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.20532462526594575,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.3132659753975586,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.2492871965680803,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.2864270891462053,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.09251079312384092,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.10414569051486788,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.21360631831022303,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.12815977941152923,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.28004003075664186,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.028784763240212174,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.720001220703125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.739990234375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.0922694615385864,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.433157428439801,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.43805612075196176,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.030903288523642658,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.9328817667324296,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.5643803075379594,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.3874010616456647,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.6271202273815502,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.8704445803414682,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.1718094350317556,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.18267085151604245,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 2.0994098090829527,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.6909276794328623,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 3.3255933132200655,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.7081971055103109,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 3.3817588076929583,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.34649963378905113,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 2.2409988403320256,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.03677795410158069,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.13158264160156818,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.11281204223632812,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.5695216369628895,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.4979388468644208,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.2521377870058128,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.3178446251668188,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.8726086411913192,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.4063350177057279,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.5509775098916814,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.027857099260602425,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.21857234409877235,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.00935486691219145,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.0923976333554517,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.32441877261679686,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.7840063043919265,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.42344708444994095,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.12523850111054635,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -2.389984130859375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -13.019989013671875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -2.310750207017387,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.8734028400226643,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.819910088861676,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.0754143607014663,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.303190742817172,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -3.248265587776655,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.511379878220385,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -10.905073328817515,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -3.0889253258202687,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.612054846614619,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.5645248196257566,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.006907840142156285,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.0612366555176047,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.64170803298137,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.8321759220850318,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -6.896194293743007,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.1504989624023665,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -4.339498901367222,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.3485998535156227,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -5.178599243164058,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.31014999389645936,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.4782499694824196,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.34251849446003124,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.3404798595608844,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.2931241555932713,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.0919434259553444,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.5137357752517904,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.835302945629026,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.3850032261439731,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.7078530447823654,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.09581990379897376,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.2464355401635745,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.5583161842612423,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -3.0415560050696566,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.3165774587290775,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.03298557570300742,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -15.300048828125,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -134.2001953125,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -2.1924178333465494,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.631994859603536,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.2457399744824738,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.6520983872201245,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.0540578732762373,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -3.3773738648174674,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.7530313574740894,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -10.455930463036823,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -2.970592952149431,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.3706468661954907,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.9903547052465544,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.4164081333391856,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.81210378597667,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.5125997559405575,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.073827401338736,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -6.447051427962315,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -11.640002441406523,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -50.16499023437473,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -14.8699951171875,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -60.47599609374993,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -3.205499267578489,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -15.883503417969223,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.09975596208898763,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.07335294535691,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.036519925840550194,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.8107774811713888,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.2768196980329254,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.657107772181444,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.6642717633928612,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 8.28574916294643,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.024260553393162798,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.26694141725199905,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.3256854158165474,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.856660583505377,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.1112248520708852,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.26729057785434696,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.26000213623046875,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -3.8100051879882812,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 7.078965589423114,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.4442492136176543,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.5026153560313005,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.9570556393319616,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.3027484567503791,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -4.334831022363828,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -6.243793203762095,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -7.349092294724759,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 6.300790470620233,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.7055972070256997,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.7580006252672198,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.11145088122734848,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.060794369450812624,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.44485740160580356,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -6.564589247626742,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -3.340213259650252,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.33799972534178835,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 2.408999633789051,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.223799896240223,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.4155998229980469,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.18379999160765692,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.00074998855591,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.6044052795551647,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -6.445525111239014,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.512863370122818,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -5.59819110528017,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.5358758916294235,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -5.739058693554355,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.30357197352818055,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.49071502685546875,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.3287767256109735,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.6848937799206851,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.24567904349612668,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -3.600118229299964,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.4482146784578909,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.4797664009328346,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.720001220703125,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -10.279998779296875,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 10.205948983101376,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.5497928744403802,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.8943762258770356,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -13.705780608224305,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.9846592267532595,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -8.002390915292,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -6.756308930862009,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -17.84060562293055,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 9.427773864298494,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.8111408678484255,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.149761495112955,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -11.637274087664995,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.7427051394536921,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -4.112417294533976,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -7.077104974726655,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -13.831726587856043,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.173499679565424,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 2.360999679565424,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.2375999450683537,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.8645999145507801,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.19959999084473168,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.1622999954223587,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.8103387880945778,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -11.703497678539932,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.9253109964088901,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -11.923679088187011,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.0173835698269897,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -12.625189589907727,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.3871427263532361,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.9057137625558034,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.4035833329909524,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.2200372575744707,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.6120377630386855,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -9.501540143158826,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.51314409589831,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.0090618881349185,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.6200027465820312,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.5199966430664062,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.6241986727912097,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.6973804728124144,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.698234843829193,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.508974744532655,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.0354377248874336,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.18960552748767956,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.3120509435667107,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.8796903646514642,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.4023737915940915,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.43603247940436907,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.4428495745932737,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.44046822397334484,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.7934836375878671,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 4.0795791482457044,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.6328469874313569,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 3.1291886704230443,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.19150009155274006,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.0055999755859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.15320571899414404,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.14422805786132642,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.27790332794189965,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.2068480300903417,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.018790673829617,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.945451174534174,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.9647585276834292,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.8288155073141956,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.0696027772875816,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.8657114026870416,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.03607177734375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.03642817905970974,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.03643264581931449,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.051094101022945426,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.1414977033607832,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.020743381290179,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.14281177009475643,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.37745313947331666,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.05000114440917969,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.1100006103515625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.3105900823226704,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.20652580333804238,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.2053910337643794,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.1389992465230536,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.48411128370060563,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.9063344864743472,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.07895519223359848,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.28069718146130906,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.46758503648021144,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.054822190070002996,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.049994235471539916,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.9295072740362564,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.726065371000173,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 2.9836391342836777,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.39975123609824426,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 3.7281818536132,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.0055000305175774145,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.02800006866455007,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.021000022888181036,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.10560005187988253,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.007899999618530273,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.041249990463256836,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.153449174354503,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.476248894499709,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.10039872158331686,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.7608635823156851,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.14963973710784284,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.5477808697205822,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.011428424290248318,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.0121427263532366,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.04006220329098875,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.040387485991617345,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.17164828647342478,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.377619682528918,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.7910430409829644,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.15408032309573894,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.09000396728515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.6199951171875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.8144607788413305,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.40108121977406874,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.39741153801583495,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.8011710797449898,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.2583800586729357,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.1318355117361012,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.15937370648310134,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.4324888465120589,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.036285660038448686,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.13973322636602337,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.14202626877991564,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.26733544081432026,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.01642597137336832,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 2.7581381090219237,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.48016975034774756,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 2.5763901885624496,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.014499664306640625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.07709960937501137,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.1424623107910179,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.026825714111325283,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.3023985671997025,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.2993862533569285,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.13540924890939054,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.9043778916909995,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.06525571905711125,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.8300449661815201,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.266675895579227,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.1743781848085444,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.010714394705636121,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.025714874267578125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.01441043420155097,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.03638481602386373,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.31716061281750196,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.2143907794810782,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.17002002901754332,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.14874291922688965,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.01000213623046875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.5800018310546875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.5467092367876347,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.2595408421274925,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.2580726722133164,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.6024005628226146,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.29931332966153246,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.7380740239180783,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.13198012234385548,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.8358495933192378,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.2314658820152471,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.0018071512805528656,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.002687402977397113,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.4661059577366955,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.0573592423619651,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 3.1518995968399466,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.18881592152079074,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 3.1730294417552707,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.07900009155272869,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.5209499359130803,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.202665557861323,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.11206207275390057,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.38807353973389525,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.33027614593505916,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.06705715361754461,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.072153677255816,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.18528306055567434,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.6662678894700513,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.3486270173656547,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.8523386090583007,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.0357142857142857,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.022142137799944228,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.03449460100913426,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.02456870108458431,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.41112360345527676,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.9679617323616552,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.16637373927920596,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.2390517709193154,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.31999969482421875,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 3.309999465942383,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -10.421340471820729,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 3.2178253743372913,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 3.884532172461917,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 17.679513177711748,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 2.498381223399093,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 29.547218654098526,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.4826629629827366,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 30.140170455669658,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -11.19951559062361,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 3.4791733677453367,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 4.139917441697836,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 19.748019698271055,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 2.7403353106986614,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 33.43719227485655,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.0880232597449861,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 32.03201541299205,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.2909999847412088,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.8469999790191629,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.1076000022888195,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.3635999870300317,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.019650001525882033,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.05035000324249239,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -3.847552039147086,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 13.787011425852455,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -2.803735222614236,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 17.764094439373988,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.8747060979217292,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 17.83947434788956,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.060714449201311194,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.6557144437517439,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.09406263456298447,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.3326491726311502,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.5130009484437767,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 10.843173847131672,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.3299999237060547,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.7000007629394531,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -5.473877819761109,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.327793461611936,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.3617955547405636,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 5.632530783060141,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.5782359403316413,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 12.396925015093618,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -3.319284611681251,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 8.68446340679214,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -6.25205293856399,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.5891414550199814,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.6171808239764829,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 7.701037303619452,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.8201900276312095,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 16.286898635851642,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -3.6400806555458978,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 12.69334244186665,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.18150005340576314,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.5820000648498542,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.05420001983642919,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.1656000518798848,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.011400003433227113,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.03950000762939254,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -2.763382752331033,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 5.649877365179101,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -2.1015359761081385,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 8.159034980322954,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.6655855469196013,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 8.09555818463047,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.04928575243268685,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.3357142039707728,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.12356271472021252,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.1206409443862944,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.5277773975835518,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 3.0088094569324597,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -3.0699996948242188,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 7.950004577636719,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -6.574957776892321,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.8269462395429139,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.9185797375067306,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 5.626503434938157,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.7748079235144729,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 19.182759740809672,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -6.078745340265865,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 6.58118595791435,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -7.353132895695203,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.5655982461348685,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.6631944682708113,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 7.695009955497468,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.0167620108140412,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 23.072733361567696,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -6.3995413841305115,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 10.590064992988857,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.2405002593994112,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 4.11800041198731,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.3752000427246003,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.4950001525878776,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.026749992370596942,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.08460002899168728,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -4.577738880042427,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 3.661006799643606,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -3.807022369247594,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 6.830405928277926,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -3.1349604577713084,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 7.95381660087211,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.47857175554547915,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.82928466796875,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.13305782837306346,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.9759931130671635,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -2.779034725174667,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 6.737848511426658,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.39150238037109375,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 2.0999984741210938,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.5497847149165791,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 3.8388186872962304,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 3.9350147102450106,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 5.9116746442499535,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -5.540508355957474,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -8.118845154792453,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 6.9429706869824415,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 20.90213319713401,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.327959833719461,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 4.100166680704276,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 4.19039997948093,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 7.980181164809264,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -5.176335233203188,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -4.946691049957074,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 7.24754766656622,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 26.390540954207097,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.6815750122070199,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.872499465942383,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.5313699340820364,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 2.4033999633789165,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.21914249420166243,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.9456500053405676,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.28387213130964817,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 4.801387211335761,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.0699309549265354,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.5930673509408031,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.8648919813556617,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.1522715480151149,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.5290636335100452,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.5314276559012283,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.5096236065887272,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.639440985071035,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.34463238171634814,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.8485902309228308,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 4.6300048828125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -11.25,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 3.552152523603669,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.393251760250247,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.2917337070800343,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -5.841049619265226,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.815091655412214,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -9.525657494216079,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 4.791939090974495,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -10.472103807370125,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 2.773977404800787,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.6545997536582924,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.5471189763159532,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -3.7725430987059156,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 2.0570457427117805,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -5.6356838734580545,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 4.471143047109848,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -6.463224772295618,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.627500152587885,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -6.444999694824219,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.03113952636721251,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.6743170166015773,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.10447380065917855,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.5871227264404126,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 2.8108597328886376,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.289790472132647,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 2.1040256566932865,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -4.782298531378382,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 2.2159517126696837,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -5.814844074238312,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.12835039411272398,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.40642874581473176,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.13676885823845764,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.3514963516967047,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.9352970976857833,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -4.70239079655992,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.26131716911396463,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.0788271899054932,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 13.8699951171875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -10.34002685546875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 5.568869770025708,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 2.973497001868042,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 2.8380097803006548,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.8445404405091903,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.8688228730846967,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -5.965240142902095,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.527076891733259,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -6.018318768990749,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 4.790694651222827,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 3.234844995276087,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 3.093395049536574,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.22396608005011975,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 2.110776960384264,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.0752665221440703,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.2062808478686122,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.009439733916241,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.415499877929733,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.672998046874909,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.673599853515725,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 3.9068994140625364,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.3201446533203125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.5103463745117551,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 2.6936963358586086,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.0798154515776046,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 2.5686832871721466,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.8029880451258204,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 3.0858081206897907,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.784582443479234,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.22428458077566837,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.9400002615792413,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.024060522747055835,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.4137100682417585,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 2.5522117592489124,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.9026638371901772,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.6528933494446337,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.0778497453582786,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 5.05999755859375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.410003662109375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.13678785332726928,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.45014408748538237,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.4368585212984333,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 2.676484364965237,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.11011577622059843,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -4.791751852071946,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.6578625840389716,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.0336284417780668,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.9149629721301511,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.7114920808934277,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.6922437905343526,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 4.7449908855245475,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.3520698635201658,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.9017782313139211,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.3370665401743249,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 5.042507476852576,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.28000030517577557,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.0764991760253793,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.22760009765625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.420799865722671,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.05785003662109034,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.1602001190185547,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 2.100157738655184,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.528362381733094,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 2.08048071918846,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.39440369411714027,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 2.054092364505733,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.0581838819764933,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.0121427263532361,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.480712890625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.07354660871228713,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.6167410666299382,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.8195539664237597,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.0336284417780668,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.5053725780527077,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.07734347970188615,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.040008544921875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -40.54998779296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.6765234757218463,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.8204051853025751,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.7139710656397948,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -6.859591947130749,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.018891024173495197,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -13.491329100533942,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.41858619725534396,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -7.508157177367435,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.10165164308103547,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.5590571918945297,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.45858579640387553,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -4.791085426571438,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.26084511147306344,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -9.601355479775918,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.7393822411199906,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -3.499278142292926,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -3.3824996948242188,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -13.619998168945358,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.3561285400390375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -5.475871582031232,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.2466467285156,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.0782229614257517,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.1906002423533906,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -8.478358582638311,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.642264774828206,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -10.528795747733266,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.36558003274515016,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -11.634066135521913,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.6128583635602673,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.936431884765625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.23339697133080417,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.0698072918515122,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.2985403661984627,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -6.61704150581205,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.4419279460795391,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.1748235392187656,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 14.300048828125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.84002685546875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 3.7000178104611647,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 4.001474069220534,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 3.914629830063654,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 10.803073277984709,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 2.2696293775066554,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.1034609479561599,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.9194749788063348,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.6859218479070783,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 2.921842691658283,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 4.2628220626285795,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 4.170015099299573,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 12.871579798544019,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 2.5115834648062236,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 3.9934345687141857,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.598678934941689,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 3.3229571871674306,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -5.8924987792968295,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -29.010501098632744,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.2490161132813,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 6.749482421875086,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.011863403320262478,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.20916931152351026,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 2.8777461046236343,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 3.8722760551638924,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.9593704397344318,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.8108730599579168,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 2.2636381180650034,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.165625851143969,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.7214268275669653,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.57928466796875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.20550409501608868,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.4208629369508472,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.8390216353408775,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.10802953053111963,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.23331684933720698,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.0571800995273524,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 3.5900001525878906,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -5.829998016357422,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 15.760670490734553,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.777697949413203,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.6547180384345985,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -5.666407294735176,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.2049352741620112,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -10.732501589339659,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 5.626145018049911,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -8.524670882457276,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 14.982495371931671,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.5163499560051577,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.3993327691986792,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -3.5979007741758657,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.4468893614615794,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -6.842527968581635,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 5.305348974185264,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -4.515791847382765,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.8989999771118136,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -8.049500083923334,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.6501999664306624,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -3.2893999481201206,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.23745000839232944,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.9001000404357882,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 7.712150178026491,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.12843204826423,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 5.130600252807113,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -4.383073515871452,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 4.093714678169718,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -5.771783199358332,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.6871425083705356,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.25692858014787934,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -2.2068357662942404,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.7125391577601636,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 3.332405124590416,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -5.4116753315613835,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.19953609530042693,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.3861463764068246,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 21.50994873046875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -73.6600341796875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 8.361754421672341,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.19264484259939874,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.17290453704667996,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -11.579161108042612,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 3.4365802185798096,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -5.4178994690800675,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 4.32699695249209,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -12.653491573332843,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 7.58357930286946,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.06870315080864664,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.08248073218923935,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -9.510654587483302,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 3.678534305879378,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.5279258483220435,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 4.006200908627443,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -8.644612538258336,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -9.514776611328102,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -42.75692443847652,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.103735351562591,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -4.7547180175781705,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 2.4630795288086347,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 13.87727767944341,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 3.2227385950848184,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -3.53051711020016,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 2.303248381929068,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -7.093766600051522,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 2.49730584004484,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -12.12542243690946,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.11285400390625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 3.3658561731099255,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.16766947518976494,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.8361344365276997,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.9604092116909726,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -6.713349778225375,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.3365143783601613,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.06243883184084309,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.3199996948242188,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.8800010681152344,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 6.369837534384737,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.681603683707622,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.541802878273379,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -11.568273673947981,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 4.930865661318329,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.3874808275912507,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 4.506884687359914,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.7585726544087086,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 5.591662415581855,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.4202556902995767,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.2864176090374597,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -9.499767153388671,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 5.172819748617897,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.5024927931667733,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 4.1860886434952675,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.2503063806658,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.5940000534057646,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.876000022888185,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.1327999877929713,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.6388000488281307,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 3.669678223890605,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.32326603799218745,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 2.5722706799309663,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -4.147385854272789,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.04750006539480989,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.20142854963030166,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.2755932061737463,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.7448765801774657,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 2.0748187943817484,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -4.526880095044849,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.2685608071968,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.5233531111180156,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 11.729995727539062,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 27.410003662109375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 8.783686273266056,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.8361667302949405,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.8990316186682232,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 10.686224592045734,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 4.801448822898346,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 9.235554442450299,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 5.0450479077768335,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 8.08060267164916,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 8.005511154463175,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.0975147237029859,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.1544168879041425,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 12.754731112605045,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 5.043402910197913,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 13.125528063208325,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 4.724251863912187,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 12.089481706723667,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.8584999084472713,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -3.2399986267089957,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.378750305175771,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.6639541625976335,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.2958123779296784,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.5954315948486055,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 5.652137088495368,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 13.646762680930959,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 5.003508725523654,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 12.294629797215507,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 4.238139572301513,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 9.65896212083178,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.11399187360491148,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 3.8024270193917395,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.393535722507556,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.9621704815160772,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 3.992945702603599,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 9.33049413428305,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.14601120985354143,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.7946211809996454,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 2.2899932861328125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -12.980010986328125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 4.261333553780878,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.3869467625073675,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.3557647553016352,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -9.03396773671844,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.674368313224516,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -10.042981949246732,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 2.0522475691993165,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -11.709942101878202,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 3.4831584349779954,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.1255987690993221,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.1003794860657159,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -6.965461216159129,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.9163224005240842,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -6.153008328488706,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.7314515253346703,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -7.701063066803693,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.2745002746582088,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -4.315999603271507,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.0666027832031375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.09345245361328125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.15706707000731512,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.9177513504028241,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.8388311172439096,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -4.639032278660361,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.2416873015511536,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -6.80533999760744,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.255427702863443,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -8.264376808513884,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.2350006103515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.6178567068917413,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.17180720077189093,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.5184666380205156,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.133660042640006,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -6.4257480130337274,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.5218489403019271,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.2509632064916094,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.5699996948242188,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.529998779296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 3.108424773919327,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.2058348429920374,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.1888637190976659,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.596164908994003,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.3928875065765567,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -6.242396991311483,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -6.192182542859445,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -5.253240966641659,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 2.3302496551164453,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.4671828364000827,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.4442489883335852,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.527658388434693,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.1509334192769902,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.352423370553458,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -6.512978586724092,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.244361931567152,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.14650001525879475,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.3444995880126953,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.07885818481445028,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.5045520019531153,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.09958374023437244,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.5450494575500429,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.0619909412482698,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -4.324607676667136,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.0037096747960161,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -3.1787386489522396,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.1738018407255524,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -3.7240147625176903,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.030714307512555772,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.07357134137834809,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.06559210991778786,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.16057770828298734,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.8140527308646561,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.716642661791946,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.6620487323760192,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.046110440134419894,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.37000274658203125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.30999755859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -2.5008959333800873,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.3929026069651398,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.40471499935936794,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 2.0571550644914005,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.9421937032628502,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 2.4254723186530436,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.006595018129075,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.5471204019835483,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -3.279071052182969,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.1315546135570944,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.14932973012344775,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 4.125661585050711,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.700239615963282,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 6.315445939411069,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.3273910619937213,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 5.555999437058057,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.15900001525878338,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.804499816894527,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.01649360656737997,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.052488555908205115,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.01703901290893839,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.07571243286133011,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.9606881854365312,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.8813535574593745,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.6320210524565884,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 2.4393160857270613,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.7266844748797352,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 2.3028746939662836,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.013928277151925239,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.0357142857142857,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.01576788684197683,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.033168837431684306,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.6340714599594399,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 2.244934861143488,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.3424456059155224,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.14956293372984797,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.6100006103515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 3.4000091552734375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.43125854520520424,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.3736945972445005,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.37767814017894974,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.3533192858997678,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.0777469193500635,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.5639003431127776,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.1632193854929191,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.1296933195066856,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.209433664008086,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.6350425906525459,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.6330634094148695,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 3.4218258064590783,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.31970100664963086,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 4.4538739638708025,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.8424233416282725,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 5.138572354581193,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.012999725341813928,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.009999084472667619,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.14400390624999204,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.1013088989257653,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.028705825805673157,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.14721885681152003,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.9658397296778753,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 2.0291155647659154,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.0305012881028142,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 2.6327149836808172,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.9162731242726485,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.8864959803085668,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.020714896065848087,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.30785805838448654,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.02771093190825802,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.15024381437776335,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.865544861856371,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.827862943461211,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.05127052920198416,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.4198355369111365,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.5800018310546875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 4.8400115966796875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.16815119512004761,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.25841175584355724,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.26622844991548433,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 3.0571205109158894,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.16229481395177814,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 5.1829354760469135,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -2.1783385316044956,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.1962899611374542,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.9463263139229294,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.002936237564488131,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.010843180679565023,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 5.125627031475199,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.07965927334778833,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 9.072909096804938,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -2.4991345754691423,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 2.8125890739370547,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.8465003967285156,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 4.0995010375976335,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.19972106933593636,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.068718872070292,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.15093772888184276,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.7109009552002021,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.8258672450260685,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.3390180304045698,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.46072550838707205,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 2.1594053108809907,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.47892833142906355,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 2.5511497027396395,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.1542859758649553,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.11571502685546875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.0782685517161017,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.01892913052468126,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.3137349739675277,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.7095606915517028,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.33802191216147226,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.2688840334231798,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.8800048828125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.7999954223632812,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -3.6466386383803506,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.1489357025320723,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.197450718733073,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 2.749158131152818,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -3.3396315817552313,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 2.2655600377852636,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -2.0126774311310935,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 2.0233081303026923,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -4.424813757183232,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.887587709124027,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.9420654494971537,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 4.817664651712128,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -3.097677494455663,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 6.155533658543289,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -2.33347347499574,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 6.0321871653772,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.35749969482421307,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.995999526977542,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.0414276123046875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.323105773925775,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.04195972442627749,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.21965938568115462,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -2.596649784075522,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.2876178537857266,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -2.276630914914479,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.7337467133687667,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -2.30139525059898,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.8771330595229507,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.0035716465541295594,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.10499954223632812,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.03916862796071441,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.08532002722019105,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -2.069806060677326,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.086096156577887,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.24189246024169786,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.4911219977815028,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.8300018310546875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.8800048828125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -3.111874223221922,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.7439186749150348,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.7848544171617409,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.6717075252688174,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.9881220326490645,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.750386525322777,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.5382336926727738,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.3802939911574321,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -3.890049342024804,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.4825706815069895,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.5294691479258211,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 3.7402140458281274,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.7461679453494963,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 3.139587095435248,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.85902973653742,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 4.389173026231941,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.28050003051758665,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.6285003662109432,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.014200439453119884,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.08515823364257358,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.02107208251952386,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.14887157440185206,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.9817618121267246,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.18355741230331457,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.7205623744676926,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.7385706703505477,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.7022023264859234,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.762599924748831,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.008929116385323788,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.30499976021902886,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.004121864585317603,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.23710959711043733,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.6940012178034083,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.5719551804967757,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.24942125236234114,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.5703591993181449,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.1800003051757812,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.1399993896484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.8165792696028129,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.4369273774855529,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.3908702393275796,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 3.9326945997919864,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.0246907321207601,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.066510519577446,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.5897013306030328,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.328899595641187,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.03840415079993109,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.6982753708935983,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.646255508563499,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 6.001201120351297,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.2666448194203275,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.8234631011805789,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.2689052867383861,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.6799794394333212,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.5104999542236328,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.427000045776367,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.21022064208983693,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.9684582519531233,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.06344795227050781,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.3562417602539085,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.5416334588989828,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.1401603856556859,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.2447943094660125,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.1232663356675836,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.1020963152213117,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.6150077181016247,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.05071422031947548,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.09071404593331489,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.07187712051468775,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.12495956671218433,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.0283227060355458,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.864923215379898,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.5778972251385759,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.8172006668379184,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.25,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.5699996948242188,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.1250838857639556,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.2775265061276242,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.3019739129527919,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.9859140645209097,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -3.766171111084814,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.4165630961052065,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.5387290347783624,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 4.10632047901347,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.9032590045668374,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.0161785127195788,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.046588643716872,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.0825924560384004,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -3.524217023785246,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.4734105246528193,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.2179329909137162,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 8.115199514087978,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.11299991607666016,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.8034997940063491,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.010309371948238777,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.0012046813964872172,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.004585819244390166,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.02479112625122326,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.8689967832797851,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.617279726993325,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.6260280869157642,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.371161285295619,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.5810439453759586,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.245618129447179,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.013928822108677408,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.0242854527064732,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.02408846351789018,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.07481647630809873,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.568355266444287,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 2.0592925078481095,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.12308058249484632,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.44335930967235987,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.029998779296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.2299995422363281,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.019980416619326,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.9098644114363452,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.9355910378082699,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 2.7566378008600845,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.04964258629332,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 3.5921834016020338,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.3461881760884031,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 4.457696949557222,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.7981555354222079,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.1712124048443906,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.1909763070441897,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 4.825144321419395,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.8076884989937518,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 7.4821570223600595,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.025392132223757,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 8.46657598463173,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.12849998474121094,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.5749999999999957,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.02563262939452926,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.1512200927734355,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.012264766693114382,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.0684302520751956,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.24441525224672134,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.5253793211174704,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.13267445914144638,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 3.25180813745668,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.04086469326298747,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 2.7152283936322186,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.012857437133789062,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.010000228881835938,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.030447112453031,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.06507522345656858,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.06669154878824468,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 2.734463748300797,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.22255343108685466,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.0006324808152470274,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.0799980163574219,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.8100013732910156,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -3.775654498012271,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.7908023147104055,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -2.892668185621572,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.49072501976672456,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -2.673181744088726,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.2928077173831367,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -2.653937076612578,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.6310003314803265,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -4.553829616815152,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.52945432130236,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -2.637282916385652,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 2.5592315403260346,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -2.431227656789158,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 4.1827813381411625,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -2.9747331204772243,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.377878703594182,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.1430000305175767,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.9029998779296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.014891128540043042,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.015172500610347583,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.022636280059813885,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.11419643402099666,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -2.4107841280180953,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.23969055433867847,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -2.0914404654450713,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.5613788514879712,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -2.1742028483269893,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.3654165232311222,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.04571424211774555,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.12357112339564735,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.11458497531097978,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.21578495595302938,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -2.0122937454883916,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.0652328599983774,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.5133667012037493,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.25493544803945634,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 10.21002197265625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -39.4599609375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 4.722547309519543,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.0119441272202323,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.9218633908776086,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -9.198733313080275,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.7917264309721972,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -9.959907335937167,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 3.8291210109512086,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -11.232616040597254,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 3.9443721907166607,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.7505961338121869,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.6664781216416884,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -7.130226792520966,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 2.0336805182717654,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -6.069933715179143,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 3.508324967086562,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -7.223737005522747,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -5.698999023437409,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -22.257501220703034,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.5655993652343341,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.4380004882812045,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.5906500244141171,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 3.556599731445317,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 2.751235686906705,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -3.2359546320606785,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.8761598622218596,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -6.495132509287583,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.8501290636821266,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -8.316082082277742,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.6142839704241077,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.6935686383928577,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.2026316491336395,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.5914597504718806,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.6106675468412703,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -6.224950215765393,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.011640729849072828,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.016413757606683843,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.7600021362304688,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -9.1199951171875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 3.0375173672399614,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.39571067981187813,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.3607346512523488,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -12.694555348192493,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.5194026292927081,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -13.881189003886007,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.468574057324945,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -16.97818124454188,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 2.2593422484370795,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.6570586732199235,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.6161199204882681,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -10.626048827633182,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.27744854199314073,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -9.991215383127983,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.7893701011895913,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -12.969302209467372,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.42499999999999716,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.7645000457763729,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.004200134277340339,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.3246002197265625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.021842193603518467,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.1048260879516647,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.0676316011685287,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -7.68822980495405,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.7067594659697409,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -8.844049972236368,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.783438822295146,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -9.836471727040408,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.0692858014787947,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.29928643362862717,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.09098784113227287,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.5192836101208749,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.6745381632924818,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -8.094430873702807,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.4035275355916502,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.024594847274254872,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -2.0399932861328125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -8.489990234375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 3.951954610275255,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.3135401314779083,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.271180599093947,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -4.224783722286529,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.6413567961341302,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -10.345182702772295,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -7.490373678728222,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -5.925638427458345,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 3.1737794914723736,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.5748881248859536,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.5265658683298664,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.1562772017272187,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.3994027088345629,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -6.455209082014269,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -7.811169722592869,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.9167593923838382,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.1529998779296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 3.2134994506835994,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.12039276123047671,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.1506588745117199,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.3144862365722645,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.7362275695800804,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.1085388301864674,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -5.971477031100559,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.128227933020065,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -5.0617786896626775,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.4090528025149318,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -6.199116323383926,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.05571310860770051,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.03642926897321441,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -8.131881094319837e-05,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.1338130872166281,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.9957987308673921,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -4.1442888846432995,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.9852703871990205,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.18684114104214955,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -3.920013427734375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -23.760009765625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 4.468953795822805,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.615491037872797,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -2.488577023068883,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -12.041486689755466,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.18559668998483492,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -9.145929584243817,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -6.569882292136364,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -13.37433868244101,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 3.6907786770199236,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.3541430444647515,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -2.2331917538329638,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -9.972980169196155,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.05635739731473244,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -5.255955963485793,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -6.89067833600101,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -9.365459647366503,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.3175003051758267,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 3.7179992675780795,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.4720001220703125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.5313995361328239,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.29259994506838893,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.9455499267578489,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.92087503206294,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -7.071408042206784,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.8650782396984025,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -5.548117224175197,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.0561523506091408,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -6.470238490158553,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.3164280482700885,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.1578630719866077,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.04879411797537747,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.47086795685257776,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.8978912337488829,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -5.442303929727233,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.2560922626256079,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.28895062545896577,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.4900054931640625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 9.949996948242188,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.661232009411484,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.1478155740002105,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.1949036832552107,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 4.790983314646802,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.07797400081481776,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 5.269711562562107,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.46430248620512415,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 2.279543724921794,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -2.439407128214366,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.4091635674082559,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.45028895249113,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 6.859489835206111,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.3199280881143851,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 9.159685183320132,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.1435064423404775,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 6.288422759996301,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.39550018310546875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.2190017700195312,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.3391949462890409,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.851657104492176,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.13494560241699105,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.6629866790771644,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.5206708052116316,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 4.209791868816959,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.8557592725564778,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 5.921987992415101,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.7081145095303896,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 4.619294917876383,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.11285727364676301,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.9864273071289062,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.036367390949011646,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.3657004205889003,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.589105413907042,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 3.9339432622633055,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.19609308656255164,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.3562080405592085,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.3400001525878906,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.9300003051757812,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.8883214568700346,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.0709348071972435,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.0268333905744775,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -5.542161688959357,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.15792019282470093,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -6.6075128329851065,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.637027462787044,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -10.70342475137851,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.1101463380671528,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.8095868137891982,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.7714481213385582,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -3.473655168400047,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.3998742801242683,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.7175392122270816,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.31623141892239737,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -6.694545716304001,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.16599998474121236,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.5814999580383322,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.05080001831054659,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.30359996795654354,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.026299991607665163,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.10629998207092228,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.6282291202421533,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.16105756732664,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.2246270859806785,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.0131042512472774,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.122221706768256,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.5568785328064276,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.031357220241001627,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.0755714688982283,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.1380666142463678,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.32902780919240904,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.9753303116320957,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.6678149423199446,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.144256650650616,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.42751806513961454,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.850006103515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.29999542236328125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -3.5414220064050816,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.946618882836503,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.9616176859809311,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -2.362085634342126,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.7347258916089894,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.07213660347782369,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.8940096588534008,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 1.6800531369883243,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -4.319597125207963,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.6852708894284576,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.7062324167450118,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.29357911378281587,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.492771804309422,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 3.9621102242358486,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.214805702718047,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 5.688932172062833,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.14049987792968466,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.6480003356933537,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.02913238525390227,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.20919204711913153,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.030969009399413494,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.16681583404540845,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.4048200298697022,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.5206271906282423,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.1428215362693006,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.7120475270028459,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.2533041147632096,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.1812667926497813,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.012499128069196397,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.13142885480608268,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.0046737881580125595,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.17332776418043916,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.09694253802013,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.38714750240089657,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.5337200191772847,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.008139620599784791,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.42999267578125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -15.480010986328125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_1d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 4.192459418357353,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.016693639220521916,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_5d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.015047252370536057,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -13.999582985539716,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_20d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.21362763617906033,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -14.140729916777572,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_60d_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -1.9481198726592819,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -18.852464809337324,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_1d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 3.414284299554471,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.24465435418752346,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_5d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.24033801686538325,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -11.931076464980405,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_20d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.4555817234786277,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -10.250756296019546,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_60d_pp",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -2.268915916523928,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -14.843585774262815,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma20",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.7514999389648267,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -1.495500183105463,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma50",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.059800109863260786,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.15760009765625682,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma200",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.15889999389648324,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.8753000640869288,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma20_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 1.279457538796846,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -8.396160767771333,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma50_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.9028352552392649,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -9.504118859915444,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma200_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.9138542252368431,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -12.121536675205324,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_sma",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.35428619384765625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.3721433367047995,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.2600536265495035,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.5177380126853501,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.drawdown_from_63d_high_pct",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.8176526278070746,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -8.8512842588782,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.volume_vs_previous20_ratio",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.2571203039009383,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.520116046764394,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS2.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.03000000000000025,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.08999999999999986,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLH0A0HYM2.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.009999999999999787,
        "unit": "percentage_points"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.13000000000000034,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLC0A0CM.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.0,
        "unit": "percentage_points"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.039999999999999925,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS10.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.03000000000000025,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.08999999999999986,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DFII10.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.020000000000000018,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.040000000000000036,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.T10YIE.value",
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.009999999999999787,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.050000000000000266,
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
    "available_prior_observations": 12,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.3200000000000003,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 3.3099999999999987,
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
  },
  {
    "id": "latest.TNX.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  }
]
```

## 判断依据 · 反弹是否可靠？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 反弹是否可靠？ |
| 事实指标引用 | ["prices.SPY.distance_sma20_pct", "prices.QQQ.distance_sma20_pct", "prices.SMH.distance_sma20_pct"] |
| 推断与解释 | 盘前改善，联合门槛和常规回踩尚未完成。 |
| 反证与缺口 | SMH略低门槛、AI部分公司逆势走弱。 |
| 确认条件 | SPY755.72、QQQ690.49、SMH522.49同时收复并守回踩，形成更高低点；RSP219.51以上且相对SPY不持续转弱。VWAP取得后作为额外确认。 |
| 失效条件 | QQQ跌回683.45、SMH511.63且反抽不回，SPY失751.60则显著降级；单个盘前越线不触发趋势反转。 |
| 观察期限 | 11月4日常规开盘后30–60分钟、收盘与后续1–3交易日 |
| 条件式指导 | 先验证开盘回踩和参与面，再以收盘及次日延续提高置信度；未知风险预算不推精确最优仓位。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相比早报新增选举结果、盘前行情及融资文件；完整交易日未变。 |

## 判断依据 · 优先观察板块？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 优先观察板块？ |
| 事实指标引用 | ["prices.XLI.return_5d_pct", "prices.ITA.return_5d_pct", "prices.XLF.return_1d_pct"] |
| 推断与解释 | 金融医疗加入盘前候选，工业军工维持观察；不沿用昨收排名直接下单。 |
| 反证与缺口 | 盘前ETF稀疏，真实广度与申赎缺失。 |
| 确认条件 | 金融守57.20并形成常规更高低点，医疗与工业持续强于SPY且不回吐开盘区间；次日延续后再评估增加风险。 |
| 失效条件 | 冲高跌破实际开盘区间且反抽不回，或行业持续跑输SPY；XLF重新失57.20则撤销盘前改善信号。 |
| 观察期限 | 11月4日常规开盘后30–60分钟、收盘与后续1–3交易日 |
| 条件式指导 | 先验证开盘回踩和参与面，再以收盘及次日延续提高置信度；未知风险预算不推精确最优仓位。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相比早报新增选举结果、盘前行情及融资文件；完整交易日未变。 |

## 判断依据 · AI需求和回报？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | AI需求和回报？ |
| 事实指标引用 | ["prices.SMH.return_1d_pct", "prices.MU.return_1d_pct"] |
| 推断与解释 | AMD需求证据仍强，现金占用、稀释与政策风险使价格分化。 |
| 反证与缺口 | 融资仍能完成，不构成行业全面断贷。 |
| 确认条件 | AMD守财报后新形成的常规支撑；MU收回861.59、DRAM守46.96，SMH越522.49并守回踩；SNDK先重获昨收1126.52。 |
| 失效条件 | 利好后跌破开盘区间且反抽不回，SMH失511.63；MU失845.25或DRAM47.18先减弱，829.24/46.29是更深层失效。 |
| 观察期限 | 11月4日常规开盘后30–60分钟、收盘与后续1–3交易日 |
| 条件式指导 | 先验证开盘回踩和参与面，再以收盘及次日延续提高置信度；未知风险预算不推精确最优仓位。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相比早报新增选举结果、盘前行情及融资文件；完整交易日未变。 |

## 判断依据 · 融资压力消除了吗？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 融资压力消除了吗？ |
| 事实指标引用 | ["prices.IGV.return_5d_pct", "macro.DFII10.value"] |
| 推断与解释 | Oracle股债融资、Meta欧元债表明资金可得，但价格与现金回报还需检验。 |
| 反证与缺口 | 四家公司估值桥不足，不作精确公司间比较。 |
| 确认条件 | ORCL回到126.19、VRT235.97、PLTR178.34、IGV103.33上并形成常规更高低点；融资落地后现金回报预期不再恶化。 |
| 失效条件 | 大盘上涨但个股持续创新低或反抽无力；政策传闻转为正式限制，或融资/经营预期再恶化。 |
| 观察期限 | 11月4日常规开盘后30–60分钟、收盘与后续1–3交易日 |
| 条件式指导 | 先验证开盘回踩和参与面，再以收盘及次日延续提高置信度；未知风险预算不推精确最优仓位。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相比早报新增选举结果、盘前行情及融资文件；完整交易日未变。 |

## 判断依据 · 恐慌还是过热？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 恐慌还是过热？ |
| 事实指标引用 | ["latest.VIX.value", "macro.BAMLH0A0HYM2.value", "macro.GPRD.value"] |
| 推断与解释 | 恐慌缓和中的分化修复，未见全面过热证据；黄金走强显示仍有避险。 |
| 反证与缺口 | 信用和GPR滞后、波动可因数据与政策再升。 |
| 确认条件 | SPY755.72、QQQ690.49、SMH522.49同时收复并守回踩，形成更高低点；RSP219.51以上且相对SPY不持续转弱。VWAP取得后作为额外确认。 |
| 失效条件 | QQQ跌回683.45、SMH511.63且反抽不回，SPY失751.60则显著降级；单个盘前越线不触发趋势反转。 |
| 观察期限 | 11月4日常规开盘后30–60分钟、收盘与后续1–3交易日 |
| 条件式指导 | 先验证开盘回踩和参与面，再以收盘及次日延续提高置信度；未知风险预算不推精确最优仓位。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相比早报新增选举结果、盘前行情及融资文件；完整交易日未变。 |

## 选举后政策重估与广度修复 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | AP等媒体判定民主党赢得两院，尚非各州正式认证或新法生效。 |
| 事实：市场反应 | 最新盘前大盘、金融、医疗回升，早先下跌标题已落后于报价。 |
| 推断：解释 | 推断：不确定性缓和与板块重估并存，不能只归因单一事件。 |
| 受益篮子 | ["金融、医疗、工业观察篮子"] |
| 受损篮子 | ["依赖未兑现政策优惠者"] |
| 反证 | 行政否决权仍在，政策细节与常规广度未确认。 |
| 下一催化剂 | 今晚常规时段承接、财政部安排与ISM |
| 证据 | ["https://apnews.com/article/ef6199e25927a9ac9f4c18eae0e497cd", "https://ca.investing.com/news/stock-market-news/us-stock-index-futures-steady-as-democrats-seize-congress-4928584"] |

## AI需求与股价分化 · 减弱

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | AMD指引支持需求，QCOM今晚盘后报告。 |
| 事实：市场反应 | AMD盘前仍涨但回吐部分盘后涨幅；MU/SNDK、ORCL/VRT相对弱。 |
| 推断：解释 | 推断：买盘在区分需求兑现、融资负担与政策暴露。 |
| 受益篮子 | ["现金回收可验证的芯片公司"] |
| 受损篮子 | ["估值高且融资/建设周期长者"] |
| 反证 | 单个盘前价格可能被低流动性扭曲，不能据此判定长期需求终结。 |
| 下一催化剂 | QCOM盘后、NVDA11月17日 |
| 证据 | ["https://newsroom.amd.com/news/amd-reports-third-quarter-2026-earnings/", "https://investor.qualcomm.com/news-events/press-releases/news-details/2026/Qualcomm-Schedules-Fourth-Quarter-and-Fiscal-2026-Earnings-Release-and-Conference-Call/default.aspx"] |

## 融资开放不等于资本成本无忧 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | Oracle股票发行新文件，Meta欧元初步文件。 |
| 事实：市场反应 | ORCL低于昨收，META高于昨收。 |
| 推断：解释 | 股权稀释、利息与现金回报要分公司看。 |
| 受益篮子 | ["现金回报足以覆盖投入者"] |
| 受损篮子 | ["融资规模扩大但回报延后者"] |
| 反证 | 融资可得是反对“信用市场全面冻结”的证据。 |
| 下一催化剂 | 发行最终条款、实际结算、现金流披露 |
| 证据 | ["https://www.sec.gov/Archives/edgar/data/1341439/000119312526445847/d181425d424b5.htm", "https://www.sec.gov/Archives/edgar/data/1326801/000119312526445646/d186765dfwp.htm", "https://www.sec.gov/Archives/edgar/data/1326801/000119312526446110/d44678d424b5.htm"] |

## 黄金走强与油价回落并存 · 新增

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 选举落定报道与伊朗触雷说法同时出现。 |
| 事实：市场反应 | GLD涨、WTI/Brent回落、VIX下降。 |
| 推断：解释 | 推断：不能用一个战争或恐慌指数解释多种资产。 |
| 受益篮子 | ["黄金及避险需求相关观察篮子"] |
| 受损篮子 | ["供应冲击押注过满者"] |
| 反证 | 金涨也可能受美元影响；触雷尚缺独立核验。 |
| 下一催化剂 | 真实航运、油价和利率反应 |
| 证据 | ["https://www.iranintl.com/en/202611045349"] |

## tc 报价（供应商时戳不等于成交时戳）

| 标的 | 价格 USD | 变化% | 观测时间 | 供应商时间 | 抓取时间 | 质量 |
| --- | --- | --- | --- | --- | --- | --- |
| AAPL | 335.12 | 0.97 | 2026-11-04T12:04:06+00:00 | 2026-11-04T12:04:06+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| AMD | 502.15 | 3.77 | 2026-11-04T12:04:07+00:00 | 2026-11-04T12:04:07+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| AMZN | 258.20 | 3.00 | 2026-11-04T12:03:40+00:00 | 2026-11-04T12:03:40+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| AVGO | 334.63 | 0.75 | 2026-11-04T12:03:36+00:00 | 2026-11-04T12:03:36+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| BABA | 103.95 | 3.58 | 2026-11-04T12:03:31+00:00 | 2026-11-04T12:03:31+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| CAT | 616.12 | -1.25 | 2026-11-04T12:03:29+00:00 | 2026-11-04T12:03:29+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| CEG | 253.30 | -3.83 | 2026-11-04T12:03:48+00:00 | 2026-11-04T12:03:48+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| COIN | 147.30 | 1.27 | 2026-11-04T12:03:09+00:00 | 2026-11-04T12:03:09+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| CVX | 224.60 | -0.30 | 2026-11-04T12:03:55+00:00 | 2026-11-04T12:03:55+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| DRAM | 47.65 | 0.02 | 2026-11-04T12:04:03+00:00 | 2026-11-04T12:04:03+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| GEV | 880.29 | -4.13 | 2026-11-04T12:03:18+00:00 | 2026-11-04T12:03:18+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| GLD | 370.22 | 3.05 | 2026-11-04T12:03:44+00:00 | 2026-11-04T12:03:44+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| GLW | 125.00 | -0.90 | 2026-11-04T12:01:48+00:00 | 2026-11-04T12:01:48+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| GOOGL | 282.02 | 0.71 | 2026-11-04T12:03:52+00:00 | 2026-11-04T12:03:52+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| IGV | 103.20 | 0.53 | 2026-11-04T12:02:20+00:00 | 2026-11-04T12:02:20+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| INTC | 59.63 | -1.52 | 2026-11-04T12:04:01+00:00 | 2026-11-04T12:04:01+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| IWM | 283.75 | 1.42 | 2026-11-04T12:03:56+00:00 | 2026-11-04T12:03:56+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| LITE | 673.51 | -0.98 | 2026-11-04T12:03:24+00:00 | 2026-11-04T12:03:24+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| LLY | 1,439.09 | 2.11 | 2026-11-04T12:03:56+00:00 | 2026-11-04T12:03:56+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| META | 629.68 | 1.39 | 2026-11-04T12:03:42+00:00 | 2026-11-04T12:03:42+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| MRVL | 170.80 | -0.68 | 2026-11-04T12:03:57+00:00 | 2026-11-04T12:03:57+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| MSFT | 532.23 | 2.16 | 2026-11-04T12:03:43+00:00 | 2026-11-04T12:03:43+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| MU | 851.99 | -0.36 | 2026-11-04T12:04:00+00:00 | 2026-11-04T12:04:00+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| NOW | 111.63 | 2.27 | 2026-11-04T12:03:56+00:00 | 2026-11-04T12:03:56+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| NVDA | 207.90 | 0.59 | 2026-11-04T12:03:52+00:00 | 2026-11-04T12:03:52+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| NXPI | 260.57 | -0.84 | 2026-11-04T09:01:27+00:00 | 2026-11-04T09:01:27+00:00 | 2026-11-04T12:04:10.895142+00:00 | stale |
| ORCL | 122.71 | -2.76 | 2026-11-04T12:04:02+00:00 | 2026-11-04T12:04:02+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| PLTR | 170.77 | -2.64 | 2026-11-04T12:04:01+00:00 | 2026-11-04T12:04:01+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| QQQ | 690.59 | 0.77 | 2026-11-04T12:03:56+00:00 | 2026-11-04T12:03:56+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| RSP | 221.79 | 1.15 | 2026-11-04T11:43:00+00:00 | 2026-11-04T11:43:00+00:00 | 2026-11-04T12:04:10.895142+00:00 | stale |
| SMH | 522.01 | 0.67 | 2026-11-04T12:03:23+00:00 | 2026-11-04T12:03:23+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| SNDK | 1,116.00 | -0.93 | 2026-11-04T12:04:04+00:00 | 2026-11-04T12:04:04+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| SPY | 762.45 | 1.07 | 2026-11-04T12:03:41+00:00 | 2026-11-04T12:03:41+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| STX | 598.50 | -1.30 | 2026-11-04T12:03:34+00:00 | 2026-11-04T12:03:34+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| TLT | 81.46 | 0.43 | 2026-11-04T12:01:34+00:00 | 2026-11-04T12:01:34+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| VRT | 223.96 | -5.09 | 2026-11-04T12:04:00+00:00 | 2026-11-04T12:04:00+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| XLE | 66.40 | -0.42 | 2026-11-04T12:00:14+00:00 | 2026-11-04T12:00:14+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| XLF | 58.05 | 1.50 | 2026-11-04T12:02:47+00:00 | 2026-11-04T12:02:47+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| XLI | 171.52 | 0.12 | 2026-11-04T11:39:00+00:00 | 2026-11-04T11:39:00+00:00 | 2026-11-04T12:04:10.895142+00:00 | stale |
| XLV | 186.89 | 1.56 | 2026-11-04T12:03:24+00:00 | 2026-11-04T12:03:24+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |
| XOM | 176.40 | -0.60 | 2026-11-04T12:04:00+00:00 | 2026-11-04T12:04:00+00:00 | 2026-11-04T12:04:10.895142+00:00 | ok |

## 核心行情与风险代理

| 标的 | 价格/指数 | 单位 | 观测日 | 1日% | 5日% | 20日% | 质量 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 754.35 | USD_per_share | 2026-11-03 | 0.30 | -1.99 | -3.18 | ok |
| QQQ | 685.28 | USD_per_share | 2026-11-03 | 0.62 | -4.99 | -9.79 | ok |
| IWM | 279.79 | USD_per_share | 2026-11-03 | 0.23 | -0.14 | -0.55 | ok |
| RSP | 219.26 | USD_per_share | 2026-11-03 | -0.33 | 0.80 | 3.26 | ok |
| GLD | 359.26 | USD_per_share | 2026-11-03 | -0.66 | -3.50 | -6.02 | ok |
| GC=F | 3,940.40 | USD_per_troy_ounce | 2026-11-03 | -0.74 | -3.29 | -5.89 | ok |
| CL=F | 96.09 | USD_per_barrel | 2026-11-03 | -0.38 | -3.81 | 7.44 | ok |
| BZ=F | 103.60 | USD_per_barrel | 2026-11-03 | -1.12 | -9.03 | 3.00 | ok |
| TLT | 81.11 | USD_per_share | 2026-11-03 | -0.76 | -0.64 | 4.96 | ok |
| UUP | 29.01 | USD_per_share | 2026-11-03 | 0.17 | -0.38 | 0.38 | ok |
| HYG | 76.98 | USD_per_share | 2026-11-03 | 0.12 | -0.80 | -0.38 | ok |
| LQD | 103.72 | USD_per_share | 2026-11-03 | 0.01 | -0.56 | 1.55 | ok |
| ^VIX | 20.83 | index | 2026-11-03 | -1.51 | 18.89 | 38.77 | ok |
| ^VIX3M | 21.27 | index | 2026-11-03 | -1.53 | 8.69 | 20.58 | ok |
| ^VVIX | 107.40 | index | 2026-11-03 | -2.78 | 7.99 | 30.04 | ok |
| ^MOVE | 99.97 | index | 2026-11-03 | -0.39 | 2.15 | -12.00 | ok |
| NVDA | 206.69 | USD_per_share | 2026-11-03 | 2.29 | -5.16 | -13.61 | ok |
| MSFT | 520.99 | USD_per_share | 2026-11-03 | 2.74 | -1.95 | -1.57 | ok |
| AMZN | 250.69 | USD_per_share | 2026-11-03 | 2.06 | -0.95 | -2.19 | ok |
| GOOGL | 280.03 | USD_per_share | 2026-11-03 | 0.37 | -12.65 | -19.46 | ok |
| META | 621.03 | USD_per_share | 2026-11-03 | 2.36 | 0.14 | -15.95 | ok |
| CRWV | 53.74 | USD_per_share | 2026-11-03 | 7.16 | -9.79 | -41.41 | ok |
| MU | 855.10 | USD_per_share | 2026-11-03 | 2.58 | -7.93 | -18.20 | ok |
| DRAM | 47.64 | USD_per_share | 2026-11-03 | 2.85 | -5.70 | -19.96 | ok |
| VRT | 235.97 | USD_per_share | 2026-11-03 | 5.23 | 13.14 | -6.78 | ok |

## 跨资产风险解释

完成日仍是11月3日，不能把与早报相同的收盘数字说成新的一天。VIX昨收20.83已获本次Cboe CSV核验，与VIX3M21.27的同日比值0.979未倒挂；VVIX107.40、MOVE99.97仍是昨收。最新VIX为4日11:48:46UTC的18.19，不能与昨日VIX3M拼成实时期限结构。20:03北京附近GLD370.22、TLT81.46，高于昨收359.26和81.11；黄金涨约3.05%、长债约0.43%，与大盘上涨同时出现，符合选举后不确定性缓和和避险需求并存，而非单一恐慌或全面过热。连续期货WTI95.13、Brent102.03、黄金4050.80，观测约11:54UTC，存在延迟与换月口径；美元指数101.349。10年收益率备用值仍是3日4.952%，不是当前利率。FRED最新2年4.59%、10年4.91%、实际10年2.62%均截至2日，HY343bp、IG94bp；金融压力仍10月23日−0.5837，GPR仍2日97.67、7日均137.64。媒体报道伊朗方面声称油轮触雷，独立船舶损毁与运量未核验；油价反而回落，不能由标题直接推出能源必涨。联储12月加25bp合约77.5%，较早报升3个百分点，与当下股涨/油跌并非同一个窗口；预测定价不是实际政策或客观概率。CNN418、CME超时，均缺失。

## 宏观与地缘风险指标

| 指标 | 数值 | 单位 | 观测日 | 20次观测变化 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- | --- |
| DGS2 | 4.59 | percent | 2026-11-02 | -0.24 | lagged | https://fred.stlouisfed.org/series/DGS2 |
| BAMLH0A0HYM2 | 3.43 | percentage_points | 2026-11-02 | 0.31 | lagged | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| BAMLC0A0CM | 0.94 | percentage_points | 2026-11-02 | 0.10 | lagged | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| DGS10 | 4.91 | percent | 2026-11-02 | -0.37 | lagged | https://fred.stlouisfed.org/series/DGS10 |
| DFII10 | 2.62 | percent | 2026-11-02 | -0.30 | lagged | https://fred.stlouisfed.org/series/DFII10 |
| T10YIE | 2.30 | percent | 2026-11-03 | -0.06 | ok | https://fred.stlouisfed.org/series/T10YIE |
| STLFSI4 | -0.58 | index | 2026-10-23 | 0.28 | lagged | https://fred.stlouisfed.org/series/STLFSI4 |
| CBOE_VIX | 20.83 | index | 2026-11-03 | 5.82 | ok | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| GPRD | 97.67 | index | 2026-11-02 | -213.94 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_ACT | 113.60 | index | 2026-11-02 | -291.60 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_THREAT | 94.75 | index | 2026-11-02 | -209.43 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_MA7 | 137.64 | index | 2026-11-02 | -46.66 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_MA30 | 164.04 | index | 2026-11-02 | -2.33 | lagged | https://www.matteoiacoviello.com/gpr.htm |

## CNN Fear & Greed

缺失：CNN 无可核验数据，不使用替代指数

## 19 板块与主题 ETF：价格量能证据

| 标的 | 板块 | 1日% | 5日% | 20日% | 相对SPY 1日pp | 相对SPY 5日pp | 相对SPY 20日pp | 成交量/前20日 | 观测日 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLK | 科技 | 1.31 | -6.85 | -12.62 | 1.02 | -4.86 | -9.44 | 1.12 | 2026-11-03 |
| XLE | 能源 | -0.85 | -2.24 | 4.60 | -1.15 | -0.25 | 7.77 | 0.94 | 2026-11-03 |
| XLF | 金融 | -0.64 | 2.34 | 5.89 | -0.94 | 4.33 | 9.06 | 0.92 | 2026-11-03 |
| XLI | 工业 | 0.95 | 2.02 | -0.15 | 0.65 | 4.01 | 3.02 | 1.26 | 2026-11-03 |
| XLV | 医疗 | -0.31 | 2.70 | 10.13 | -0.61 | 4.69 | 13.31 | 1.17 | 2026-11-03 |
| XLP | 必需消费 | -2.07 | 2.07 | 8.74 | -2.37 | 4.05 | 11.92 | 1.41 | 2026-11-03 |
| XLY | 可选消费 | -0.70 | 1.63 | 5.02 | -1.00 | 3.62 | 8.20 | 1.39 | 2026-11-03 |
| XLC | 通信 | 1.18 | -2.07 | -9.14 | 0.88 | -0.08 | -5.97 | 1.91 | 2026-11-03 |
| XLU | 公用事业 | -0.57 | 1.33 | 5.49 | -0.87 | 3.32 | 8.67 | 0.92 | 2026-11-03 |
| XLRE | 房地产 | 0.07 | 2.90 | 6.25 | -0.23 | 4.89 | 9.43 | 0.90 | 2026-11-03 |
| XLB | 材料 | -2.01 | 1.56 | 5.75 | -2.31 | 3.55 | 8.93 | 1.28 | 2026-11-03 |
| SMH | 半导体 | 2.01 | -7.07 | -18.02 | 1.71 | -5.08 | -14.85 | 0.92 | 2026-11-03 |
| IGV | 软件 | 0.75 | -8.16 | -7.65 | 0.45 | -6.17 | -4.47 | 0.98 | 2026-11-03 |
| XOP | 油气开采 | -1.05 | -4.24 | 1.62 | -1.35 | -2.26 | 4.80 | 1.23 | 2026-11-03 |
| OIH | 油服 | -1.01 | -5.81 | -1.62 | -1.31 | -3.82 | 1.55 | 1.01 | 2026-11-03 |
| ITA | 航空与国防 | 0.69 | 4.82 | 3.80 | 0.39 | 6.81 | 6.97 | 1.38 | 2026-11-03 |
| ARKX | 航天主题 | 1.15 | -3.02 | -9.99 | 0.85 | -1.03 | -6.82 | 0.54 | 2026-11-03 |
| KRE | 区域银行 | -1.15 | 0.41 | 4.01 | -1.45 | 2.40 | 7.19 | 0.80 | 2026-11-03 |
| SKYY | 云计算 | 0.93 | -9.03 | -8.79 | 0.63 | -7.04 | -5.61 | 0.79 | 2026-11-03 |

## 资金证据分层

19ETF完整日线重查，端点仍11月2日至3日；排名并未因本次生成新报告而产生新收盘。XLK+1.31%/5日-6.85%；SMH+2.01%/5日-7.07%；IGV+0.75%/5日-8.16%；SKYY+0.93%/5日-9.03%；XLI+0.95%/5日+2.02%；ITA+0.69%/5日+4.82%；XLF-0.64%/5日+2.34%；XLP-2.07%/5日+2.07%；XLE-0.85%/5日-2.24%；XLV-0.31%/5日+2.70%。昨收RSP−0.33%而SPY+0.30%，SPY量约20日均0.81倍，说明常规广度尚未确认。今晚增量是盘前XLF58.05、XLV186.89、IWM283.75与RSP221.79向上，RSP11:43UTC、XLI11:39UTC时点较稀疏，不能据此计算同步上涨家数。金融回到早报57.20观察位上，医疗值得加入观察；工业军工的5日相对强势仍是候选而非自动买点。AI内部AMD约502.16仍高于昨收483.90，但低于早报盘后520.54；MU851.99、SNDK1116.00、ORCL122.71与VRT223.96均低于昨收，不能把SMH或QQQ上涨写成整个产业链净流入。ICI再次核验仍为截至10月28日一周：全部ETF净发行459.06亿美元、国内股265.90亿、债券142.34亿、商品−18.89亿，非今晨黄金或金融的即时资金流。19ETF当期发行人净申赎及拆分桥缺失，机构持仓滞后，价格量能不识别“主力”。

## 最近可核验 ETF 申赎窗口

| 标的 | 金额 USD million | 起始日 | 结束日 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- |

## Polymarket 搜索覆盖与限制

2026-11-04T12:09:34.976443+00:00：基础全领域采集+15组主动检索（AI融资/破产、Oracle评级、Fed/通胀/衰退、银行、油气战争、Apple中国、IPO、选举与财报）。Oracle和QCOM已逐条核验规则；前者低量，后者极宽价差，均降置信度。AMD等已结束事件退出未来列表。CPI/Meta/Anthropic/Congress等结果有截断；OPEC返回OPEN噪声，不称全市场覆盖。

## Polymarket · 值得警惕的信号

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["AI bubble burst in 2026?", "期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。", "https://polymarket.com/event/ai-bubble-burst-by"] | [8.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.00399999999999999, "volume24h_usd": 744.3793850000001, "liquidity_usd": 25156.53923, "quality_flags": ["volume24h_under_1000_or_unknown"], "retrieved_at": "2026-11-04T12:04:11.221977+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["同规则当前价格、价差和成交量见合约卡；独立事实未核验时保留观察，不把定价当客观概率。", "AI估值与融资风险"] | ["同规则价格持续上行并有经营/信用证据", "现金流和信用改善"] | [null, null] |
| ["Military action against Saudi Oil Pipeline (East-West) by November 30?", "11月30日23:59利雅得时间前，合格空袭或地对地导弹（含指定单向攻击无人机）直接命中沙特东西输油管或泵站则Yes；不要求已证明显著损害。拦截残骸、小型短程弹药、地面入侵、炮火、网络攻击或未执行威胁不算。官方沙特信息与可信报道共识，冲突可等待三完整日。不同期限不拼接。", "https://polymarket.com/event/military-action-against-saudi-oil-pipeline-east-west-byptptpt"] | [34.0, {"status": "comparable", "change_pp": -4.499999999999998}] | {"spread": 0.019999999999999962, "volume24h_usd": 41602.28463999999, "liquidity_usd": 30061.031, "quality_flags": [], "retrieved_at": "2026-11-04T12:04:00.035029+00:00", "contract_end_at": "2026-11-30T20:59:00+00:00"} | ["同规则当前价格、价差和成交量见合约卡；独立事实未核验时保留观察，不把定价当客观概率。", "沙特管线供应尾部风险，不能将所有中东威胁视为已命中"] | ["按规则核验官方事实，再验证资产价格和信用传导", "传闻、广义风险或股价变化不满足专门结算条件"] | [null, null] |
| ["Major CEX insolvent in 2026?", "2026年12月31日23:59ET前Binance/Coinbase/Bybit/OKX/Kraken任一被正式宣布资不抵债或申请/拟申请任一种破产程序则Yes；按官方代表或可信报道共识。被盗、暂停提款或偿付证明延期本身不是触发。", "https://polymarket.com/event/major-cex-insolvent-in-2026"] | [3.05, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.015, "volume24h_usd": 1.59, "liquidity_usd": 23158.6853, "quality_flags": ["volume24h_under_1000_or_unknown"], "retrieved_at": "2026-11-04T12:04:04.696513+00:00", "contract_end_at": "2027-01-01T05:00:00+00:00"} | ["同规则当前价格、价差和成交量见合约卡；独立事实未核验时保留观察，不把定价当客观概率。", "五家加密平台任一破产的专门合约，安全事故本身不触发"] | ["按规则核验官方事实，再验证资产价格和信用传导", "传闻、广义风险或股价变化不满足专门结算条件"] | [null, null] |
| ["Oracle downgraded to junk by Moody's or S&P by December 31, 2026?", "2026年12月31日美东23:59前，Moody’s或S&P正式将Oracle长期主体或高级无担保债评级降至Ba1/BB+或更低才算Yes；负面展望或观察名单不算。低成交量与宽价差，仅作低置信度观察。", "https://polymarket.com/event/oracle-downgraded-to-junk-by-moodys-or-sp-by"] | [16.5, {"status": "no_baseline"}] | {"spread": 0.04999999999999999, "volume24h_usd": 61.101112, "liquidity_usd": 377.5537, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"], "retrieved_at": "2026-11-04T12:04:00.023864+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["主动检索新增Oracle评级风险；16.5%报价、低成交和5个百分点价差仅为弱信号。", "融资成本与AI建设资本约束"] | ["评级机构正式降级与信用价格共同恶化", "仅负面展望不符合结算；融资及现金流改善"] | [null, null] |

## Polymarket · 有参考价值的事件

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Strait of Hormuz traffic returns to normal by December 31?", "期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。", "https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31"] | [10.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.009999999999999995, "volume24h_usd": 198140.79750999997, "liquidity_usd": 355166.3411, "quality_flags": [], "retrieved_at": "2026-11-04T12:04:11.221977+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["同规则当前价格、价差和成交量见合约卡；独立事实未核验时保留观察，不把定价当客观概率。", "IMF七日平均船舶到达不少于60，不能由单日放行新闻替代。"] | ["官方Portwatch连续数据达到定义。", "只出现局部绕行或有限通航。"] | [null, null] |
| ["Will Anthropic IPO by December 31, 2026?", "Anthropic股份在2026年12月31日23:59美东前于公开证券交易所挂牌并开始交易才为Yes；仅提交S-1不算。被已上市公司收购则No。官方文件/公司与交易所公告优先，可信报道共识可辅助。", "https://polymarket.com/event/anthropic-ipo-by"] | [90.60000000000001, {"status": "comparable", "change_pp": -1.3000000000000012}] | {"spread": 0.006000000000000005, "volume24h_usd": 26043.665719999997, "liquidity_usd": 32557.63907, "quality_flags": [], "retrieved_at": "2026-11-04T12:04:03.289116+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["同规则当前价格、价差和成交量见合约卡；独立事实未核验时保留观察，不把定价当客观概率。", "AI一级市场融资窗口与公开估值参照；不等于云供应商利润"] | ["官方招股文件、定价及交易所首日交易依次核验", "仅保密/公开申报、尚未挂牌交易；不以媒体时刻替代官方"] | [null, null] |
| ["Will Apple purchase memory CXMT chips in 2026?", "2026年12月31日23:59ET前Apple官方宣布使用/购买/采购CXMT存储器即可Yes，不要求同期交付；经确认达成采购或供货协议也可。官方信息优先、可信报道共识辅助。不等同HBM已量产或全球利润率下降。", "https://polymarket.com/event/will-apple-purchase-memory-cxmt-chips-in-2026-20260630171913147"] | [11.0, {"status": "comparable", "change_pp": 2.0000000000000004}] | {"spread": 0.01999999999999999, "volume24h_usd": 980.198902, "liquidity_usd": 1502.0685, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"], "retrieved_at": "2026-11-04T12:04:03.364195+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["同规则当前价格、价差和成交量见合约卡；独立事实未核验时保留观察，不把定价当客观概率。", "Apple采购/协议可能改变存储供应链，不证明HBM良率或AI利润已崩塌"] | ["公司官方采购/协议与量产、价格资料分别验证", "传闻或审批申请尚非已采购；没有交付不一定阻止本合约Yes"] | [null, null] |

## Polymarket · 将要发生的事件及概率

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Will Qualcomm (QCOM) beat quarterly earnings?", "QCOM下一季首次发布的non-GAAP EPS按美分取整须严格高于固定门槛2.20美元；不是动态市场预期。未披露时依规则依次采用SeekingAlpha及GAAP口径，45天未发布为No；30个百分点买卖价差，不能解读为精确胜率。", "https://polymarket.com/event/qcom-quarterly-earnings-nongaap-eps-11-04-2026-2pt20"] | [81.0, {"status": "no_baseline"}] | {"spread": 0.29999999999999993, "volume24h_usd": 784.915398, "liquidity_usd": 133.2311, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"], "retrieved_at": "2026-11-04T12:04:00.044767+00:00", "contract_end_at": "2026-11-04T22:00:00+00:00"} | ["官方今晚盘后财报已核验，但30个百分点价差使81%报价缺乏精度，仅作事件提醒。", "手机/汽车/AI业务指引影响半导体相对强弱"] | ["官方首次EPS严格高于2.20美元且经营指引和股价承接一致", "固定EPS胜出仍可能股价下跌；不以该合约推股票收益"] | ["2026-11-04T16:45:00-05:00", "https://investor.qualcomm.com/news-events/press-releases/news-details/2026/Qualcomm-Schedules-Fourth-Quarter-and-Fiscal-2026-Earnings-Release-and-Conference-Call/default.aspx"] |

## Will the Fed increase interest rates by 25 bps after the December 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 770450 / 3215008 |
| Yes 概率 % | 77.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [5.0, 1.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 3.0000000000000027} |
| 24h成交量 / 流动性 USD | [382563.182792, 369573.9881] |
| 价差 pp | 1.00 |
| 到期 | 2026-12-09T23:59:00+00:00 |
| 结算规则摘要 | 以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。 |
| 规则指纹 | 933a10a15eeec0ff1de30468fa20540301ed243f75cc3572d42946192f81a123 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-04T11:59:57.787118Z |
| 抓取时间 | 2026-11-04T12:04:11.221977+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-december-20260729232808632 |

## Strait of Hormuz traffic returns to normal by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 455875 / 2176270 |
| Yes 概率 % | 10.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-1.0, -1.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [198140.79750999997, 355166.3411] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。 |
| 规则指纹 | b0c8ba27f4437b0d8ab819ae170bec118166232e39cdcaefb95bd352d29073d4 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-04T12:01:58.370457Z |
| 抓取时间 | 2026-11-04T12:04:11.221977+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31 |

## Tesla and SpaceX merger officially announced by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 192962 / 2252540 |
| Yes 概率 % | 10.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [1.0, -3.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.5000000000000004} |
| 24h成交量 / 流动性 USD | [2312.677827, 20189.6822] |
| 价差 pp | 2.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59纽约时间前，Tesla或SpaceX正式宣布双方合并或一方收购另一方的控制权即Yes；无需在期限内完成交易。控制权通常为过半权益或等效治理权；少数股权投资及仅讨论不算。以公司公告或可信报道共识核验；旧URL中的june-30不是本合约期限。 |
| 规则指纹 | 909906ae3b6db7e473468713ea6a1e1e4cf4c931fe247c7d3d576e7986513008 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-04T11:57:57.756111Z |
| 抓取时间 | 2026-11-04T12:04:11.221977+00:00 |
| 来源 | https://polymarket.com/event/tesla-and-spacex-merger-officially-announced-by-june-30 |

## AI bubble burst in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 691340 |
| Yes 概率 % | 8.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.65, 0.6] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [744.3793850000001, 25156.53923] |
| 价差 pp | 0.40 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | fc153b2136a8dfbadcd169dce1add40690acb1748566b99716fe7ae8fcb07330 |
| 质量 | ["volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-04T12:01:58.370457Z |
| 抓取时间 | 2026-11-04T12:04:11.221977+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## AI bubble burst by June 30, 2027?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 4838928 |
| Yes 概率 % | 22.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.5, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.5000000000000004} |
| 24h成交量 / 流动性 USD | [118.433261, 9083.5768] |
| 价差 pp | 1.00 |
| 到期 | 2027-07-01T03:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | bd0420587e08487fffa5050e7fd9b79ffff909a9f843d3f620207ee859462505 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-04T12:01:58.370457Z |
| 抓取时间 | 2026-11-04T12:04:11.221977+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## Oracle downgraded to junk by Moody's or S&P by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1219847 / 5939428 |
| Yes 概率 % | 16.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.5, -3.5] |
| 与上一快照可比变化 | {"status": "no_baseline"} |
| 24h成交量 / 流动性 USD | [61.101112, 377.5537] |
| 价差 pp | 5.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日美东23:59前，Moody’s或S&P正式将Oracle长期主体或高级无担保债评级降至Ba1/BB+或更低才算Yes；负面展望或观察名单不算。低成交量与宽价差，仅作低置信度观察。 |
| 规则指纹 | cb29bc6ea2fb2a6cd1d97dc489f0163f0b47e0cb2d31a9cbb3fe5dda90eb10c4 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-04T12:01:58.370457Z |
| 抓取时间 | 2026-11-04T12:04:00.023864+00:00 |
| 来源 | https://polymarket.com/event/oracle-downgraded-to-junk-by-moodys-or-sp-by |

## Will Qualcomm (QCOM) beat quarterly earnings?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1262792 / 6281121 |
| Yes 概率 % | 81.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [19.0, 7.0] |
| 与上一快照可比变化 | {"status": "no_baseline"} |
| 24h成交量 / 流动性 USD | [784.915398, 133.2311] |
| 价差 pp | 30.00 |
| 到期 | 2026-11-04T22:00:00+00:00 |
| 结算规则摘要 | QCOM下一季首次发布的non-GAAP EPS按美分取整须严格高于固定门槛2.20美元；不是动态市场预期。未披露时依规则依次采用SeekingAlpha及GAAP口径，45天未发布为No；30个百分点买卖价差，不能解读为精确胜率。 |
| 规则指纹 | 9b8e681d4367279cdfa8d0c021a644fc50f2e259ff43429fa26686475d94576c |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"] |
| 元数据更新（不是成交时间） | 2026-11-04T12:01:58.370457Z |
| 抓取时间 | 2026-11-04T12:04:00.044767+00:00 |
| 来源 | https://polymarket.com/event/qcom-quarterly-earnings-nongaap-eps-11-04-2026-2pt20 |

## Military action against Saudi Oil Pipeline (East-West) by November 30?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1147445 / 5401796 |
| Yes 概率 % | 34.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-4.5, -18.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -4.499999999999998} |
| 24h成交量 / 流动性 USD | [41602.28463999999, 30061.031] |
| 价差 pp | 2.00 |
| 到期 | 2026-11-30T20:59:00+00:00 |
| 结算规则摘要 | 11月30日23:59利雅得时间前，合格空袭或地对地导弹（含指定单向攻击无人机）直接命中沙特东西输油管或泵站则Yes；不要求已证明显著损害。拦截残骸、小型短程弹药、地面入侵、炮火、网络攻击或未执行威胁不算。官方沙特信息与可信报道共识，冲突可等待三完整日。不同期限不拼接。 |
| 规则指纹 | de6f019a1972387984a02c6a8e7cef39e331ff99c1895cf1bba902450d550441 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-04T12:01:58.370457Z |
| 抓取时间 | 2026-11-04T12:04:00.035029+00:00 |
| 来源 | https://polymarket.com/event/military-action-against-saudi-oil-pipeline-east-west-byptptpt |

## Will Anthropic IPO by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 549019 / 2413330 |
| Yes 概率 % | 90.60 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-1.95, -4.65] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -1.3000000000000012} |
| 24h成交量 / 流动性 USD | [26043.665719999997, 32557.63907] |
| 价差 pp | 0.60 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | Anthropic股份在2026年12月31日23:59美东前于公开证券交易所挂牌并开始交易才为Yes；仅提交S-1不算。被已上市公司收购则No。官方文件/公司与交易所公告优先，可信报道共识可辅助。 |
| 规则指纹 | 91cad6e5770d0b925976d3fbba5e8c61a7f0561a5ee40474d459b9851b8bf4e0 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-04T12:03:58.416488Z |
| 抓取时间 | 2026-11-04T12:04:03.289116+00:00 |
| 来源 | https://polymarket.com/event/anthropic-ipo-by |

## Will Apple purchase memory CXMT chips in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 652109 / 2745561 |
| Yes 概率 % | 11.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [0.5, -4.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 2.0000000000000004} |
| 24h成交量 / 流动性 USD | [980.198902, 1502.0685] |
| 价差 pp | 2.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59ET前Apple官方宣布使用/购买/采购CXMT存储器即可Yes，不要求同期交付；经确认达成采购或供货协议也可。官方信息优先、可信报道共识辅助。不等同HBM已量产或全球利润率下降。 |
| 规则指纹 | f9ba1bef2cbca87ceaec660e27ab85bc0edd5723bc3e5e58937caf9155b3e790 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-04T11:55:57.28558Z |
| 抓取时间 | 2026-11-04T12:04:03.364195+00:00 |
| 来源 | https://polymarket.com/event/will-apple-purchase-memory-cxmt-chips-in-2026-20260630171913147 |

## Major CEX insolvent in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 199777 / 1343533 |
| Yes 概率 % | 3.05 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [0.1, 0.1] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [1.59, 23158.6853] |
| 价差 pp | 1.50 |
| 到期 | 2027-01-01T05:00:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59ET前Binance/Coinbase/Bybit/OKX/Kraken任一被正式宣布资不抵债或申请/拟申请任一种破产程序则Yes；按官方代表或可信报道共识。被盗、暂停提款或偿付证明延期本身不是触发。 |
| 规则指纹 | 60d4965584f04350506eafe348b3b70153b2fd33101cc7cd02976facea6531d8 |
| 质量 | ["volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-04T11:59:57.787118Z |
| 抓取时间 | 2026-11-04T12:04:04.696513+00:00 |
| 来源 | https://polymarket.com/event/major-cex-insolvent-in-2026 |

## AI 压力：合约、经营与估值分开

三层分开。第一，2026专门泡沫合约8.5%未变，2027年6月版22.5%较早报降0.5个百分点；各自结算规则不同，不是AI股普跌概率。新增Oracle年末垃圾级评级合约16.5%，24小时成交仅约61美元、买卖14/19、价差5个百分点；2027年6月版价差51个百分点不纳入重点。QCOM固定EPS门槛合约81%但买卖66/96，价差30个百分点，不代表81%赚钱机会。第二，AMD官方收入指引170亿美元±3%与本季FCF5.54亿美元的分化仍成立；公司FCF不是模型FCFF。今日新10-Q单独核验租赁与采购承诺，强需求不能掩盖资本占用。Oracle4日424B5明确发行86,206,897股、每股116美元，总额约100亿美元，与另100亿美元债券并行；这是条款核验，未证明资金已结算到账。Meta最新美元定价文件与欧元初步文件显示融资窗口仍开，初步欧元金额/票息空白不猜测最终成本。Google马来西亚150亿美元投资为Reuters援引公司声明，需与未来两年支出窗口区分。Texas数据中心审批/税惠消息目前主要为社交转述，未核验生效法律；选举结果不能直接等同全国禁建。H100日期表3日2.96美元/GPU小时，FAQ与标题仍有口径冲突；单型号不足以定义算力经济性。第三，五家定期披露列表刷新，最新仍NVDA8月26、MSFT10月28、AMZN10月30、GOOGL10月29、META10月22；这不表示没有其他融资文件（META今日有）。NVDA复用核验底稿并更新价格；其余四家FCFF/净债务/租赁/稀释桥不全，明确unavailable，不强凑阈值。五年情景与反推是经营假设，不是客观泡沫概率。

## NVDA · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | scenario_analysis |
| 财务底稿 | TTM 至 2026-07-26；最新 10-Q / filed 2026-08-26 |
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001045810.json", "checked_at": "2026-11-04T12:05:13.061676+00:00", "latest_filing_date": "2026-08-26"} |
| 观测财务数据 | {"ttm_revenue_million": 302970, "revenue_quarters": [{"end": "2025-10-26", "value": 57006000000, "filed": "2025-11-19", "duration_days": 91}, {"end": "2026-01-25", "value": 68127000000, "filed": "2026-02-25", "duration_days": 91}, {"end": "2026-04-26", "value": 81615000000, "filed": "2026-05-20", "duration_days": 91}, {"end": "2026-07-26", "value": 96221000000, "filed": "2026-08-26", "duration_days": 91}], "cash_million": 22443.0, "liquid_investments_million": 34143.0, "debt_million": 33366.0, "finance_lease_million": 0, "diluted_shares_million": 24285.0, "latest_operating_income_million": 63734.0, "observed_end": "2026-07-26", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "Revenues", "latest_reported_revenue_million": 96221.0, "income_statement_window": "最近单季度", "ttm_bridge_note": "采用同版 FY2026全年 + FY2027半年 - FY2026半年；与四季逐项求和差1百万为披露舍入差。"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json", "https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。10-Q Note14 表明融资租赁费用不重大；模型按不重大近似零，不将其称为精确零负债。未确认担保仅作为压力情景，非已到期净债务。市场化股权42783和非市场化股权51157不作为类现金；非经营资产加回为0的保守假设。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | 无 |
| 价格 USD | 206.69 |
| 基期输入 USD million / million shares | {"revenue": 302970, "net_debt": -23220.0, "diluted_shares": 24285.0, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.2810998436251383, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## NVDA · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 98.77 | -52.21 | 14.00 | 60.00 | 12.00 | 68.42 |
| 基准 | 154.12 | -25.44 | 20.00 | 65.00 | 11.00 | 74.20 |
| 乐观 | 242.58 | 17.36 | 26.00 | 70.00 | 10.00 | 79.05 |

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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0000789019.json", "checked_at": "2026-11-04T12:05:17.346838+00:00", "latest_filing_date": "2026-10-28"} |
| 观测财务数据 | {"revenue_million": 92279, "operating_income_million": 45915, "operating_cashflow_million": 58000, "cash_capex_million": 39367, "cfo_less_cash_capex_million": 18633, "diluted_shares_million": 7446, "unit": "USD million; shares million", "observed_end": "2026-09-30", "published_at": null} |
| 来源 | ["https://www.microsoft.com/en-us/Investor/earnings/FY-2027-Q1/press-release-webcast", "https://www.sec.gov/Archives/edgar/data/789019/000119312526439794/d799291dfwp.htm"] |
| 口径 | 单季CFO减现金capex不等于FCFF；融资租赁新增/负债、优先权益、TTM及稀释桥须完整后重算；不假设缺失项为零。 |
| 主观假设说明 | 缺失 |
| 权益桥额外假设 | 无 |
| 缺失原因 | 本次新增30日FWP，29日已定价250亿美元债券、11月4日预定结算；新财报完整TTM/租赁/净债务桥仍缺，不沿用旧精确DCF。 |

## AMZN · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | unavailable |
| 财务底稿 | FY2026 Q3 ended 2026-09-30 |
| 披露检查 | {"checked_at": "2026-11-04T12:05:19.982342+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001018724.json", "latest_filing_date": "2026-10-30"} |
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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001652044.json", "checked_at": "2026-11-04T12:05:22.636270+00:00", "latest_filing_date": "2026-10-29"} |
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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001326801.json", "checked_at": "2026-11-04T12:05:26.440553+00:00", "latest_filing_date": "2026-10-22"} |
| 观测财务数据 | {"revenue_million": 64601, "operating_cashflow_million": 32790, "reported_capex_including_finance_lease_principal_million": 34910, "company_defined_fcf_million": -2120, "diluted_shares_million": 2573, "reported_operating_income_million": 12988, "legal_charge_million": 9900, "observed_end": "2026-09-30", "published_at": "2026-10-21T16:01:00-04:00", "unit": "USD million; shares million", "noncancelable_commitments_million": 454520, "leases_not_commenced_million": 355730, "contingent_cloud_capacity_max_million": 14720, "restricted_cash_reclassified_million": 10800, "commitments_due_2026_million": 45850, "commitments_due_2027_million": 121410} |
| 来源 | ["https://www.prnewswire.com/news-releases/meta-reports-third-quarter-2026-results-302915964.html", "https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm", "https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Announces-Launch-of-Offering-of-Depositary-Shares-Representing-Series-A-Mandatory-Convertible-Preferred-Stock-and-Offering-of-Class-A-Common-Stock-in-Connection-with-Forward-Sale-Agreements/default.aspx", "https://www.prnewswire.com/news-releases/meta-announces-pricing-of-offering-of-depositary-shares-representing-series-a-mandatory-convertible-preferred-stock-and-offering-of-class-a-common-stock-in-connection-with-forward-sale-agreements-302920247.html"] |
| 口径 | 公司FCF扣除融资租赁本金，不能直接代替模型FCFF；融资租赁负债/新增资产未齐，不假设零。法律费用不全归AI经营。 |
| 主观假设说明 | 缺失 |
| 权益桥额外假设 | 无 |
| 缺失原因 | 22日10-Q已核验，本次无新增定期财报。27日普通股625美元定价、优先票息6.5%已核验；完整融资租赁负债/新增资产、优先权益/远期发行与现金到账桥未齐，不用不同承诺简单充当现有债务，暂停精确FCFF反推。 |

## 大盘修复先看回踩质量

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 选举后开盘承接、ISM服务业、QCOM盘后财报 |
| 关联标的 | ["SPY", "QQQ", "SMH", "RSP"] |
| 确认条件 | SPY755.72、QQQ690.49、SMH522.49同时收复并守回踩，形成更高低点；RSP219.51以上且相对SPY不持续转弱。VWAP取得后作为额外确认。 |
| 失效条件 | QQQ跌回683.45、SMH511.63且反抽不回，SPY失751.60则显著降级；单个盘前越线不触发趋势反转。 |
| 观察期限 | 11月4日常规开盘后30–60分钟、收盘与后续1–3交易日 |
| 反证 | 目前只有异步盘前值，未核验开盘区间、VWAP和全成分广度。 |
| 状态 | 盘前部分满足，等待常规确认 |

## 金融医疗工业先验证参与面

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 选举后开盘承接、ISM服务业、QCOM盘后财报 |
| 关联标的 | ["XLF", "XLV", "XLI", "ITA"] |
| 确认条件 | 金融守57.20并形成常规更高低点，医疗与工业持续强于SPY且不回吐开盘区间；次日延续后再评估增加风险。 |
| 失效条件 | 冲高跌破实际开盘区间且反抽不回，或行业持续跑输SPY；XLF重新失57.20则撤销盘前改善信号。 |
| 观察期限 | 11月4日常规开盘后30–60分钟、收盘与后续1–3交易日 |
| 反证 | 没有即时净申赎，个别权重财报可能掩盖行业广度。 |
| 状态 | 盘前部分满足，等待常规确认 |

## 芯片分化，不追盘前跳升

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 选举后开盘承接、ISM服务业、QCOM盘后财报 |
| 关联标的 | ["AMD", "MU", "SNDK", "DRAM"] |
| 确认条件 | AMD守财报后新形成的常规支撑；MU收回861.59、DRAM守46.96，SMH越522.49并守回踩；SNDK先重获昨收1126.52。 |
| 失效条件 | 利好后跌破开盘区间且反抽不回，SMH失511.63；MU失845.25或DRAM47.18先减弱，829.24/46.29是更深层失效。 |
| 观察期限 | 11月4日常规开盘后30–60分钟、收盘与后续1–3交易日 |
| 反证 | AMD上涨不能证明存储利润相同，盘前回吐说明好财报未必是好买点。 |
| 状态 | 盘前部分满足，等待常规确认 |

## AI基建和软件等待相对强弱修复

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 选举后开盘承接、ISM服务业、QCOM盘后财报 |
| 关联标的 | ["ORCL", "VRT", "PLTR", "IGV"] |
| 确认条件 | ORCL回到126.19、VRT235.97、PLTR178.34、IGV103.33上并形成常规更高低点；融资落地后现金回报预期不再恶化。 |
| 失效条件 | 大盘上涨但个股持续创新低或反抽无力；政策传闻转为正式限制，或融资/经营预期再恶化。 |
| 观察期限 | 11月4日常规开盘后30–60分钟、收盘与后续1–3交易日 |
| 反证 | 分化可能只是盘前噪声，不能以单个低价判长期崩盘。 |
| 状态 | 盘前部分满足，等待常规确认 |

## 黄金和能源分开交易逻辑

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 选举后开盘承接、ISM服务业、QCOM盘后财报 |
| 关联标的 | ["GLD", "XLE"] |
| 确认条件 | 黄金守盘前涨幅并有美元/实际利率配合，避免直接追高；能源须XLE收67.23、同月份油价稳定且供给损失核验。 |
| 失效条件 | 黄金冲高回落失新形成支撑且美元反升；XLE继续低于67.23，油股弱于大盘则供应冲击交易不确认。 |
| 观察期限 | 11月4日常规开盘后30–60分钟、收盘与后续1–3交易日 |
| 反证 | 避险需求不保证金价一直涨，战争标题也不保证能源股受益。 |
| 状态 | 盘前部分满足，等待常规确认 |

## 跨期比较与上期剧本复核

基线为本日07:15早报，完成交易日相同；相同收盘行情不重复解释为今日上涨。盘前SPY762.45越755.72，QQQ690.59仅略越690.49，SMH522.01仍略低522.49；联合确认尚未完成。RSP221.79越219.51、XLF58.05越57.20是新增参与面线索，但报价异步、尚未开盘。AMD从早报盘后520.54回到约502.16，MU由871.71回到约851.99；因此“强财报自动带动全AI链”假设减弱，分化观察强化。黄金从昨收359.26至盘前370.22，而VIX降至18.19，不能机械贴恐慌/过热标签。同规则Polymarket：2176270 +0.00个百分点；3215008 +3.00个百分点；691340 +0.00个百分点；2252540 +0.50个百分点；4838928 -0.50个百分点；5401796 -4.50个百分点；2413330 -1.30个百分点；2745561 +2.00个百分点；1343533 +0.00个百分点。旧参议院市场562793已不在当前活跃结果中，不把缺失当0%，媒体结果与合约最终裁决分开。

## 可计算的跨期变化

```json
[
  {
    "mode": "daily",
    "baseline": "reports/daily/2026-11-03/20261103T232406.152751Z/evidence.json",
    "baseline_cutoff": "2026-11-03T23:23:52.704958+00:00",
    "close_change_pct": {
      "SPY": 0.0,
      "QQQ": 0.0,
      "IWM": 0.0,
      "RSP": 0.0,
      "GLD": 0.0,
      "GC=F": -0.010153940301893538,
      "CL=F": -0.6513698044470773,
      "BZ=F": -0.6711453088734332,
      "TLT": 0.0,
      "UUP": 0.0,
      "HYG": 0.0,
      "LQD": 0.0,
      "^VIX": 0.0,
      "^VIX3M": 0.0,
      "^VVIX": 0.0,
      "^MOVE": -0.00019842338880859955,
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
      "AAPL": {
        "change_pct": 0.9701717384754449,
        "from_observed_at": "2026-11-03T23:17:09+00:00",
        "to_observed_at": "2026-11-04T12:04:06+00:00"
      },
      "AMD": {
        "change_pct": -3.53190917124524,
        "from_observed_at": "2026-11-03T23:17:29+00:00",
        "to_observed_at": "2026-11-04T12:04:07+00:00"
      },
      "AMZN": {
        "change_pct": 2.9957317802864036,
        "from_observed_at": "2026-11-03T23:17:09+00:00",
        "to_observed_at": "2026-11-04T12:03:40+00:00"
      },
      "AVGO": {
        "change_pct": 0.7527173094872497,
        "from_observed_at": "2026-11-03T23:17:09+00:00",
        "to_observed_at": "2026-11-04T12:03:36+00:00"
      },
      "BABA": {
        "change_pct": 3.084093613645389,
        "from_observed_at": "2026-11-03T23:17:27+00:00",
        "to_observed_at": "2026-11-04T12:03:31+00:00"
      },
      "CAT": {
        "change_pct": -1.8917197452229306,
        "from_observed_at": "2026-11-03T23:16:23+00:00",
        "to_observed_at": "2026-11-04T12:03:29+00:00"
      },
      "CEG": {
        "change_pct": -3.78910632880044,
        "from_observed_at": "2026-11-03T23:13:24+00:00",
        "to_observed_at": "2026-11-04T12:03:48+00:00"
      },
      "DRAM": {
        "change_pct": -2.0554984583761593,
        "from_observed_at": "2026-11-03T23:16:57+00:00",
        "to_observed_at": "2026-11-04T12:04:03+00:00"
      },
      "GEV": {
        "change_pct": -4.999728043388729,
        "from_observed_at": "2026-11-03T23:15:14+00:00",
        "to_observed_at": "2026-11-04T12:03:18+00:00"
      },
      "GLD": {
        "change_pct": 2.836032332435212,
        "from_observed_at": "2026-11-03T23:11:39+00:00",
        "to_observed_at": "2026-11-04T12:03:44+00:00"
      },
      "GLW": {
        "change_pct": -2.8598072738576397,
        "from_observed_at": "2026-11-03T23:16:44+00:00",
        "to_observed_at": "2026-11-04T12:01:48+00:00"
      },
      "GOOGL": {
        "change_pct": 0.5956839664704727,
        "from_observed_at": "2026-11-03T23:17:26+00:00",
        "to_observed_at": "2026-11-04T12:03:52+00:00"
      },
      "INTC": {
        "change_pct": -3.1393762183235863,
        "from_observed_at": "2026-11-03T23:17:36+00:00",
        "to_observed_at": "2026-11-04T12:04:01+00:00"
      },
      "IWM": {
        "change_pct": 1.444353079975702,
        "from_observed_at": "2026-11-03T23:17:03+00:00",
        "to_observed_at": "2026-11-04T12:03:56+00:00"
      },
      "LITE": {
        "change_pct": -2.3190717911530156,
        "from_observed_at": "2026-11-03T23:16:29+00:00",
        "to_observed_at": "2026-11-04T12:03:24+00:00"
      },
      "LLY": {
        "change_pct": 2.251669745630225,
        "from_observed_at": "2026-11-03T23:17:30+00:00",
        "to_observed_at": "2026-11-04T12:03:56+00:00"
      },
      "META": {
        "change_pct": 1.3928473664718277,
        "from_observed_at": "2026-11-03T23:17:09+00:00",
        "to_observed_at": "2026-11-04T12:03:42+00:00"
      },
      "MRVL": {
        "change_pct": -1.7826336975273138,
        "from_observed_at": "2026-11-03T23:16:42+00:00",
        "to_observed_at": "2026-11-04T12:03:57+00:00"
      },
      "MSFT": {
        "change_pct": 2.383425669436745,
        "from_observed_at": "2026-11-03T23:17:15+00:00",
        "to_observed_at": "2026-11-04T12:03:43+00:00"
      },
      "MU": {
        "change_pct": -2.263274380190128,
        "from_observed_at": "2026-11-03T23:17:36+00:00",
        "to_observed_at": "2026-11-04T12:04:00+00:00"
      },
      "NOW": {
        "change_pct": 2.5099173553718934,
        "from_observed_at": "2026-11-03T23:16:35+00:00",
        "to_observed_at": "2026-11-04T12:03:56+00:00"
      },
      "NVDA": {
        "change_pct": -1.023565817662464,
        "from_observed_at": "2026-11-03T23:17:27+00:00",
        "to_observed_at": "2026-11-04T12:03:52+00:00"
      },
      "ORCL": {
        "change_pct": -3.8234971392742345,
        "from_observed_at": "2026-11-03T23:17:03+00:00",
        "to_observed_at": "2026-11-04T12:04:02+00:00"
      },
      "PLTR": {
        "change_pct": -2.6416761687571233,
        "from_observed_at": "2026-11-03T23:17:09+00:00",
        "to_observed_at": "2026-11-04T12:04:01+00:00"
      },
      "QQQ": {
        "change_pct": 0.1987754272946285,
        "from_observed_at": "2026-11-03T23:17:28+00:00",
        "to_observed_at": "2026-11-04T12:03:56+00:00"
      },
      "SMH": {
        "change_pct": 0.673069505515711,
        "from_observed_at": "2026-11-03T23:17:09+00:00",
        "to_observed_at": "2026-11-04T12:03:23+00:00"
      },
      "SNDK": {
        "change_pct": -2.723057076113111,
        "from_observed_at": "2026-11-03T23:17:40+00:00",
        "to_observed_at": "2026-11-04T12:04:04+00:00"
      },
      "SPY": {
        "change_pct": 0.7678684711355466,
        "from_observed_at": "2026-11-03T23:17:17+00:00",
        "to_observed_at": "2026-11-04T12:03:41+00:00"
      },
      "STX": {
        "change_pct": -1.2995151555130424,
        "from_observed_at": "2026-11-03T23:17:09+00:00",
        "to_observed_at": "2026-11-04T12:03:34+00:00"
      },
      "TLT": {
        "change_pct": 0.605162405829307,
        "from_observed_at": "2026-11-03T23:15:34+00:00",
        "to_observed_at": "2026-11-04T12:01:34+00:00"
      },
      "VRT": {
        "change_pct": -7.362865315053535,
        "from_observed_at": "2026-11-03T23:17:29+00:00",
        "to_observed_at": "2026-11-04T12:04:00+00:00"
      }
    },
    "macro_change": {
      "DGS2": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-11-02"
      },
      "BAMLH0A0HYM2": {
        "change": 0.0,
        "unit": "percentage_points",
        "observation_date": "2026-11-02"
      },
      "BAMLC0A0CM": {
        "change": 0.0,
        "unit": "percentage_points",
        "observation_date": "2026-11-02"
      },
      "DGS10": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-11-02"
      },
      "DFII10": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-11-02"
      },
      "T10YIE": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-11-03"
      },
      "STLFSI4": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-23"
      },
      "CBOE_VIX": {
        "change": -0.3200000000000003,
        "unit": "index",
        "observation_date": "2026-11-03"
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
      "3215008": {
        "status": "comparable",
        "change_pp": 3.0000000000000027
      },
      "2176270": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "2252540": {
        "status": "comparable",
        "change_pp": 0.5000000000000004
      },
      "691340": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "4838928": {
        "status": "comparable",
        "change_pp": -0.5000000000000004
      },
      "5401796": {
        "status": "comparable",
        "change_pp": -4.499999999999998
      },
      "2413330": {
        "status": "comparable",
        "change_pp": -1.3000000000000012
      },
      "2745561": {
        "status": "comparable",
        "change_pp": 2.0000000000000004
      },
      "1343533": {
        "status": "comparable",
        "change_pp": 0.0
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
    "event": "ISM服务业",
    "date": "2026-11-04T10:00:00-05:00",
    "source": "https://www.ismworld.org/supply-management-news-and-reports/reports/rob-report-calendar/"
  },
  {
    "event": "财政部季度再融资详细安排",
    "date": "2026-11-04 America/New_York",
    "source": "https://home.treasury.gov/news/press-releases/sb0675/"
  },
  {
    "event": "微软原250亿美元债券计划结算，非新增同额发行",
    "date": "2026-11-04 America/New_York",
    "source": "https://www.sec.gov/Archives/edgar/data/789019/000119312526442618/d150456d424b2.htm"
  },
  {
    "event": "Lumentum财报；分钟未本次核验",
    "date": "2026-11-05 America/New_York",
    "source": "https://www.investor.lumentum.com/overview/default.aspx"
  },
  {
    "event": "10月就业报告",
    "date": "2026-11-06T08:30:00-05:00",
    "source": "https://www.bls.gov/schedule/2026/11_sched.htm"
  },
  {
    "event": "10月CPI",
    "date": "2026-11-10T08:30:00-05:00",
    "source": "https://www.bls.gov/schedule/2026/11_sched.htm"
  },
  {
    "event": "NVDA财报电话会",
    "date": "2026-11-17T17:00:00-05:00",
    "source": "https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/default.aspx"
  },
  {
    "event": "Oracle100亿美元债券计划结算，未核验完成",
    "date": "2026-11-04 America/New_York",
    "source": "https://www.sec.gov/Archives/edgar/data/1341439/000119312526443918/d87441dfwp.htm"
  },
  {
    "event": "QCOM财报盘后发布；电话会16:45美东/次日05:45北京",
    "date": "2026-11-04T16:45:00-05:00",
    "source": "https://investor.qualcomm.com/news-events/press-releases/news-details/2026/Qualcomm-Schedules-Fourth-Quarter-and-Fiscal-2026-Earnings-Release-and-Conference-Call/default.aspx"
  }
]
```

## 新闻事件去重与时间

| 事件 | 摘要 | 发生时间（未知留空） | 各来源发布时间 / 抓取时间 |
| --- | --- | --- | --- |
| election | AP等媒体判定民主党赢得两院；认证及具体政策落地仍是后续事项。 | 缺失 | [{"source": "https://apnews.com/article/ef6199e25927a9ac9f4c18eae0e497cd", "published_at": null, "retrieved_at": "2026-11-04T12:09:34.976443+00:00"}] |
| oracle-equity | 新424B5明确约8621万股、每股116美元、总额约100亿美元股票发行，与100亿美元债券并行。 | 缺失 | [{"source": "https://www.sec.gov/Archives/edgar/data/1341439/000119312526445847/d181425d424b5.htm", "published_at": null, "retrieved_at": "2026-11-04T12:09:34.976443+00:00"}] |
| meta-funding | 美元债定价文件及欧元初步文件已核验；后者空白项不是最终票息。 | 缺失 | [{"source": "https://www.sec.gov/Archives/edgar/data/1326801/000119312526446110/d44678d424b5.htm", "published_at": null, "retrieved_at": "2026-11-04T12:09:34.976443+00:00"}] |
| amd-cash | AMD新10-Q补充资本占用线索；收入增长与FCF回收分开观察。 | 缺失 | [{"source": "https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm", "published_at": null, "retrieved_at": "2026-11-04T12:09:34.976443+00:00"}] |
| apple-china | AFP报道中国开发者试用已启动，不能等同12月公众版本已发布。 | 缺失 | [{"source": "https://www.afp.com/en/apple-ai-tools-come-china-after-two-year-delay", "published_at": null, "retrieved_at": "2026-11-04T12:09:34.976443+00:00"}] |
| iran-mines | 伊朗方面声称油轮触雷，多源报道转述同一声明，未独立确认损毁。 | 缺失 | [{"source": "https://www.iranintl.com/en/202611045349", "published_at": null, "retrieved_at": "2026-11-04T12:09:34.976443+00:00"}] |
| qcom | 官方确认4日盘后财报及16:45美东电话会；固定EPS预测合约流动性差。 | 2026-11-04T16:45:00-05:00 | [{"source": "https://investor.qualcomm.com/news-events/press-releases/news-details/2026/Qualcomm-Schedules-Fourth-Quarter-and-Fiscal-2026-Earnings-Release-and-Conference-Call/default.aspx", "published_at": null, "retrieved_at": "2026-11-04T12:09:34.976443+00:00"}] |

## 覆盖范围与数据缺口

```json
[
  "CNN418，CME超时；不以tc温度或加密恐贪替代。",
  "tc报价时间为请求时间且仍昨收，使用公开分钟时间核验的独立报价包；部分ETF报价稀疏，非同步篮子。",
  "今晚尚未常规开盘，VWAP、开盘区间和回踩尚不存在；全成分广度未取到，不伪造可靠反弹确认。",
  "FRED利率信用截至2日、金融压力10月23日、GPR2日；不是当前无风险证明。",
  "ICI仍10月28日宽口径净发行，缺19ETF当期申赎与拆分桥；不称主力净流入。",
  "NVDA复用底稿且租赁近似；其余四家完整FCFF桥缺失。已刷新五家定期披露列表并额外检查META融资文件。",
  "两组tc新闻均50条且截断；关键事件补官方/财经核验仍非新闻全覆盖。Texas数据中心限制尚未核验正式政策，Google扩建援引Reuters，CVS拆分仍待官方正文。",
  "伊朗触雷是单方声明，多家转述并非独立损失核验；AP选举结果页面全文受限，使用可检索摘要并以媒体判定表述，不冒充州认证。",
  "Polymarket多项搜索截断，Oracle低成交、QCOM价差极宽；旧参院合约退出活跃结果，不把缺失当零或擅自声称已裁决。",
  "H100日期表与FAQ口径不一致；连续期货可能延迟/换月，不制造避险或战争统一指数。",
  "tc缓存CPI/NVDA日期与官方不同，采用BLS11月10日、NVDA11月17日；不把计划结算写成已完成。",
  "原始采集存在请求失败，见采集质量记录",
  "MSFT 估值: 本次新增30日FWP，29日已定价250亿美元债券、11月4日预定结算；新财报完整TTM/租赁/净债务桥仍缺，不沿用旧精确DCF。",
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
  "tc 报价质量 stale: NXPI, RSP, XLI；不作为新成交证据",
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
  "指标缺失/历史不足: prices.^VIX.volume_vs_previous20_ratio, prices.^VIX3M.volume_vs_previous20_ratio, prices.^VVIX.volume_vs_previous20_ratio, prices.^MOVE.volume_vs_previous20_ratio, prices.DRAM.sma200, prices.DRAM.distance_sma200_pct, quotes.NXPI.value, quotes.RSP.value, quotes.XLI.value"
]
```

## 来源、时间与核验记录

```json
[
  {
    "url": "https://www.afp.com/en/apple-ai-tools-come-china-after-two-year-delay",
    "checked_at": "2026-11-04T12:09:34.976443+00:00",
    "note": "AFP报道中国开发者试用已启动，不能等同12月公众版本已发布。"
  },
  {
    "url": "https://www.sec.gov/Archives/edgar/data/1326801/000119312526446110/d44678d424b5.htm",
    "checked_at": "2026-11-04T12:09:34.976443+00:00",
    "note": "美元债定价文件及欧元初步文件已核验；后者空白项不是最终票息。"
  },
  {
    "url": "https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/",
    "checked_at": "2026-11-04T12:04:13.857906+00:00",
    "note": "本次公开资料复核；计划、条款、观测日与已发生事实分开"
  },
  {
    "url": "https://investor.nvidia.com/events-and-presentations/events-and-presentations/default.aspx",
    "checked_at": "2026-11-04T12:04:14.442244+00:00",
    "note": "本次公开资料复核；计划、条款、观测日与已发生事实分开"
  },
  {
    "url": "https://www.sec.gov/Archives/edgar/data/1321655/000132165526000045/a2026q3ex991pressrelease.htm",
    "checked_at": "2026-11-04T12:04:15.080125+00:00",
    "note": "本次公开资料复核；计划、条款、观测日与已发生事实分开"
  },
  {
    "url": "https://www.bls.gov/schedule/2026/11_sched.htm",
    "checked_at": "2026-11-04T12:09:34.976443+00:00",
    "note": "官方事件日历/既有公告；非已完成证明"
  },
  {
    "url": "https://www.sec.gov/Archives/edgar/data/1326801/000119312526445646/d186765dfwp.htm",
    "checked_at": "2026-11-04T12:06:14.336833+00:00",
    "note": "本次公开资料复核；计划、条款、观测日与已发生事实分开"
  },
  {
    "url": "https://www.ici.org/research/stats/etf_flows",
    "checked_at": "2026-11-04T12:04:12.942317+00:00",
    "note": "本次公开资料复核；计划、条款、观测日与已发生事实分开"
  },
  {
    "url": "https://www.rba.gov.au/media-releases/2026/mr-26-30.html",
    "checked_at": "2026-11-04T12:04:23.530524+00:00",
    "note": "本次公开资料复核；计划、条款、观测日与已发生事实分开"
  },
  {
    "url": "https://www.sec.gov/Archives/edgar/data/1341439/000119312526445847/d181425d424b5.htm",
    "checked_at": "2026-11-04T12:09:34.976443+00:00",
    "note": "新424B5明确约8621万股、每股116美元、总额约100亿美元股票发行，与100亿美元债券并行。"
  },
  {
    "url": "https://investors.cvshealth.com/overview/default.aspx",
    "checked_at": "2026-11-04T12:04:57.583621+00:00",
    "note": "本次公开资料复核；计划、条款、观测日与已发生事实分开"
  },
  {
    "url": "https://finance.yahoo.com/technology/articles/meta-starts-debut-euro-bond-082229966.html",
    "checked_at": "2026-11-04T12:05:46.580537+00:00",
    "note": "本次公开资料复核；计划、条款、观测日与已发生事实分开"
  },
  {
    "url": "https://www.rba.gov.au/news/",
    "checked_at": "2026-11-04T12:04:13.007053+00:00",
    "note": "本次公开资料复核；计划、条款、观测日与已发生事实分开"
  },
  {
    "url": "https://www.iranintl.com/en/202611045349",
    "checked_at": "2026-11-04T12:09:34.976443+00:00",
    "note": "伊朗方面声称油轮触雷，多源报道转述同一声明，未独立确认损毁。"
  },
  {
    "url": "https://www.sec.gov/Archives/edgar/data/1341439/000119312526443918/d87441dfwp.htm",
    "checked_at": "2026-11-04T12:09:34.976443+00:00",
    "note": "官方事件日历/既有公告；非已完成证明"
  },
  {
    "url": "https://newsroom.amd.com/news/amd-reports-third-quarter-2026-earnings/",
    "checked_at": "2026-11-04T12:04:22.623037+00:00",
    "note": "本次公开资料复核；计划、条款、观测日与已发生事实分开"
  },
  {
    "url": "https://www.apple.com/newsroom/2026/11/apple-reports-fourth-quarter-results/",
    "checked_at": "2026-11-04T12:04:14.163557+00:00",
    "note": "本次公开资料复核；计划、条款、观测日与已发生事实分开"
  },
  {
    "url": "https://investor.qualcomm.com/news-events/press-releases/news-details/2026/Qualcomm-Schedules-Fourth-Quarter-and-Fiscal-2026-Earnings-Release-and-Conference-Call/default.aspx",
    "checked_at": "2026-11-04T12:09:34.976443+00:00",
    "note": "官方事件日历/既有公告；非已完成证明"
  },
  {
    "url": "https://www.bls.gov/news.release/jolts.htm",
    "checked_at": "2026-11-04T12:04:22.762918+00:00",
    "note": "本次公开资料复核；计划、条款、观测日与已发生事实分开"
  },
  {
    "url": "https://finance.yahoo.com/technology/ai/articles/nvidia-orders-data-center-clients-080911859.html",
    "checked_at": "2026-11-04T12:04:24.051171+00:00",
    "note": "本次公开资料复核；计划、条款、观测日与已发生事实分开"
  },
  {
    "url": "https://home.treasury.gov/policy-issues/financing-the-government/quarterly-refunding/most-recent-quarterly-refunding-documents/",
    "checked_at": "2026-11-04T12:05:06.216567+00:00",
    "note": "本次公开资料复核；计划、条款、观测日与已发生事实分开"
  },
  {
    "url": "https://www.silicondata.com/products/silicon-index/h100",
    "checked_at": "2026-11-04T12:04:12.874553+00:00",
    "note": "本次公开资料复核；计划、条款、观测日与已发生事实分开"
  },
  {
    "url": "https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm",
    "checked_at": "2026-11-04T12:09:34.976443+00:00",
    "note": "AMD新10-Q补充资本占用线索；收入增长与FCF回收分开观察。"
  },
  {
    "url": "https://apnews.com/article/ef6199e25927a9ac9f4c18eae0e497cd",
    "checked_at": "2026-11-04T12:09:34.976443+00:00",
    "note": "AP等媒体判定民主党赢得两院；认证及具体政策落地仍是后续事项。"
  },
  {
    "url": "https://www.ismworld.org/supply-management-news-and-reports/reports/rob-report-calendar/",
    "checked_at": "2026-11-04T12:09:34.976443+00:00",
    "note": "官方事件日历/既有公告；非已完成证明"
  },
  {
    "url": "https://home.treasury.gov/news/press-releases/sb0675/",
    "checked_at": "2026-11-04T12:09:34.976443+00:00",
    "note": "官方事件日历/既有公告；非已完成证明"
  },
  {
    "url": "https://www.sec.gov/Archives/edgar/data/789019/000119312526442618/d150456d424b2.htm",
    "checked_at": "2026-11-04T12:09:34.976443+00:00",
    "note": "官方事件日历/既有公告；非已完成证明"
  },
  {
    "url": "https://www.investor.lumentum.com/overview/default.aspx",
    "checked_at": "2026-11-04T12:09:34.976443+00:00",
    "note": "官方事件日历/既有公告；非已完成证明"
  },
  {
    "url": "https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/default.aspx",
    "checked_at": "2026-11-04T12:09:34.976443+00:00",
    "note": "官方事件日历/既有公告；非已完成证明"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AAPL",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AMD",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AMZN",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AVGO",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/BABA",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CAT",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CEG",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/COIN",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CVX",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/DRAM",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GEV",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GLD",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GLW",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GOOGL",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/IGV",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/INTC",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/IWM",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/LITE",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/LLY",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/META",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/MRVL",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/MSFT",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/MU",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NOW",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NVDA",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NXPI",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/ORCL",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/PLTR",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/QQQ",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/RSP",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SMH",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SNDK",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SPY",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/STX",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/TLT",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/VRT",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLE",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLF",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLI",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLV",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XOM",
    "checked_at": "2026-11-04T12:04:10.895142+00:00",
    "note": "公开分钟指示，实际时间来自行情而非请求时间"
  },
  {
    "url": "https://ca.investing.com/news/stock-market-news/us-stock-index-futures-steady-as-democrats-seize-congress-4928584",
    "checked_at": "2026-11-04T12:09:34.976443+00:00",
    "note": "可检索Reuters摘要：股指期货扭转早期跌势；价格以实际分钟数据为准"
  },
  {
    "url": "https://new.streetinsider.com/Reuters/Google%2Bto%2Binvest%2B%2415%2Bbillion%2Bin%2BMalaysia%2Bin%2B2027%2Band%2B2028/27284476.html",
    "checked_at": "2026-11-04T12:09:34.976443+00:00",
    "note": "可检索Reuters摘要援引公司2027–2028投资计划；正文403"
  }
]
```

## 付费信源建议（未订阅）

```json
[]
```
