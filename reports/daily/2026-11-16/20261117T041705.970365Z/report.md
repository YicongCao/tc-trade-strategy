# 每日交易总结 · 2026-11-16

## 一分钟读懂 · Agent 摘要

### 当前判断

当前偏风险收缩，昨晚反弹框架的失效条件已在收盘触发；仍缺全面流动性恐慌的证据。早报延至北京时间中午采集，主体为纽约16日收盘。

### 与上次相比

SPY收739.95、QQQ661.75，跌破昨晚观察线747.89/671.71；SMH跌5.11%、MU跌7.62%，弱势扩大。

### 最重要的信号

- 19个行业/主题ETF仅2涨，VIX升至22.91；涨少跌多，反弹尚不可靠。
- 2年/10年美债降至4.83%/5.12%，但股票未止跌，说明利率回落本身不够。
- 新远程算力出口限制叠加NVDA财报，AI进入经营与融资兑现检验。

### 接下来观察

- 宽基先收复SPY747.89–749.82、QQQ671.71–672.15，再看回踩与收盘；跌破738.07/660.48且反抽失败则继续防守。
- 优先观察XLP/XLV/XLF，芯片等待SMH473.33及板块广度修复。
- 北京18日05:20左右NVDA结果、06:00电话会；不凭盘后第一跳确认反转。

### 不要忽略

CNN当前值缺失；信用数据滞后，缺当期ETF申赎与逐分钟承接证据。以上是条件剧本，不是已确认买点。

## 研究结论

11月17日早报补发：宽基失守、芯片领跌，反弹确认失败；等待财报后的回踩与广度验证。

## 时点与口径

| 项目 | 内容 |
| --- | --- |
| 模式 | 每日交易总结 |
| 常规交易窗口 | 2026-11-16 → 2026-11-16（纽约交易日） |
| 截止·纽约 | 2026-11-16T23:16:39.595176-05:00 |
| 截止·北京 | 2026-11-17T12:16:39.595176+08:00 |
| 实际生成时间 | 2026-11-17T04:16:40.091883+00:00 |
| 市场阶段 | 休市 |
| 下一交易日 | 2026-11-17 |
| 运行重点 | 全市场 |
| 上一版本 | reports/daily/2026-11-13/20261116T120823.536214Z/evidence.json |
| 质量 | partial |
| Daily 北京时间计划时段 | 2026-11-17T07:15:00+08:00 |

## 采集、补查与剩余缺口

| 目标 | 补查结果 | 来源 | 观测 / 抓取时间 | 说明 |
| --- | --- | --- | --- | --- |
| 1219851 | 已校验接入 | https://gamma-api.polymarket.com/events/1219851 | 2026-11-17T04:07:31.020247+00:00 / 2026-11-17T04:07:31.020247+00:00 | Gamma snapshot; metadata update is not last trade time |

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
| polymarket.query.ceasefire | truncated | 按主题或事件ID补查；不能声称全市场覆盖 | 降低相关判断可信度；保留缺口 |
| polymarket.query.inflation | truncated | 按主题或事件ID补查；不能声称全市场覆盖 | 降低相关判断可信度；保留缺口 |
| cnn | missing | 核验 CNN Fear & Greed 原值及更新时间 | 降低相关判断可信度；保留缺口 |
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
| prices.SPY.relative_spy_20d_pp | 0.00 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_60d_pp | 0.00 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SPY/history/ |
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
| prices.QQQ.value | 661.75 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_1d_pct | -2.67 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_5d_pct | -2.59 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_20d_pct | -7.88 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_60d_pct | -7.15 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_1d_pp | -0.76 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_5d_pp | -0.90 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_20d_pp | -4.42 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_60d_pp | -4.02 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma20 | 692.62 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma50 | 716.59 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma200 | 681.41 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma20_pct | -4.46 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma50_pct | -7.65 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma200_pct | -2.89 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_sma | 19.23 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_pct | 2.91 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.drawdown_from_63d_high_pct | -12.89 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.volume_vs_previous20_ratio | 0.87 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.IWM.value | 272.94 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_1d_pct | -1.66 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_5d_pct | -3.39 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_20d_pct | 0.61 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_60d_pct | -8.77 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_1d_pp | 0.25 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_5d_pp | -1.69 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_20d_pp | 4.07 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_60d_pp | -5.64 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IWM/history/ |
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
| prices.RSP.relative_spy_20d_pp | 6.05 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_60d_pp | 2.26 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/RSP/history/ |
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
| prices.GLD.relative_spy_20d_pp | -3.59 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_60d_pp | -13.51 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GLD/history/ |
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
| prices.GC=F.value | 3,873.00 | USD_per_troy_ounce | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_1d_pct | -0.34 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_5d_pct | -5.87 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_20d_pct | -6.90 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_60d_pct | -17.25 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_1d_pp | 1.57 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_5d_pp | -4.18 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_20d_pp | -3.44 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_60d_pp | -14.13 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma20 | 4,020.85 | USD_per_troy_ounce | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma50 | 4,169.44 | USD_per_troy_ounce | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma200 | 4,467.88 | USD_per_troy_ounce | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma20_pct | -3.68 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma50_pct | -7.11 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma200_pct | -13.31 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_sma | 95.59 | USD_per_troy_ounce | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_pct | 2.47 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.drawdown_from_63d_high_pct | -17.56 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.volume_vs_previous20_ratio | 0.12 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.CL=F.value | 84.96 | USD_per_barrel | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_1d_pct | -4.07 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_5d_pct | -2.18 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_20d_pct | -18.04 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_60d_pct | -2.41 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_1d_pp | -2.15 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_5d_pp | -0.48 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_20d_pp | -14.58 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_60d_pp | 0.71 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma20 | 94.80 | USD_per_barrel | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma50 | 95.24 | USD_per_barrel | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma200 | 87.88 | USD_per_barrel | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma20_pct | -10.38 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma50_pct | -10.79 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma200_pct | -3.32 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_sma | 4.60 | USD_per_barrel | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_pct | 5.42 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.drawdown_from_63d_high_pct | -19.72 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.volume_vs_previous20_ratio | 0.03 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.BZ=F.value | 91.59 | USD_per_barrel | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_1d_pct | -4.43 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_5d_pct | -1.06 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_20d_pct | -16.39 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_60d_pct | -2.97 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_1d_pp | -2.52 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_5d_pp | 0.63 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_20d_pp | -12.93 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_60d_pp | 0.16 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma20 | 104.23 | USD_per_barrel | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma50 | 104.17 | USD_per_barrel | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma200 | 94.10 | USD_per_barrel | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma20_pct | -12.13 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma50_pct | -12.07 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma200_pct | -2.67 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_sma | 5.59 | USD_per_barrel | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_pct | 6.10 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.drawdown_from_63d_high_pct | -22.14 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.volume_vs_previous20_ratio | 0.03 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.TLT.value | 79.38 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_1d_pct | 0.00 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_5d_pct | -3.15 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_20d_pct | 0.32 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_60d_pct | -2.08 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_1d_pp | 1.91 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_5d_pp | -1.46 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_20d_pp | 3.78 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_60d_pp | 1.04 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/TLT/history/ |
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
| prices.UUP.relative_spy_20d_pp | 5.39 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_60d_pp | 9.08 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/UUP/history/ |
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
| prices.HYG.relative_spy_20d_pp | 3.85 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_60d_pp | 0.97 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/HYG/history/ |
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
| prices.LQD.relative_spy_20d_pp | 3.77 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_60d_pp | 1.38 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/LQD/history/ |
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
| prices.^VIX.relative_spy_20d_pp | 27.70 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_60d_pp | 47.38 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
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
| prices.^VIX3M.relative_spy_20d_pp | 20.91 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_60d_pp | 27.56 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
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
| prices.^VVIX.relative_spy_20d_pp | 10.29 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_60d_pp | 35.54 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
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
| prices.^MOVE.return_5d_pct | 9.18 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_20d_pct | 0.18 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_60d_pct | 42.13 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_1d_pp | 4.43 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_5d_pp | 8.54 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_20d_pp | 3.23 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_60d_pp | 45.68 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma20 | 97.96 | index | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma50 | 94.88 | index | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma200 | 79.45 | index | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma20_pct | 3.39 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma50_pct | 6.75 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma200_pct | 27.48 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_sma | 5.13 | index | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_pct | 5.07 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.drawdown_from_63d_high_pct | -10.84 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-16 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.NVDA.value | 156.14 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_1d_pct | -4.12 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_5d_pct | -12.61 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_20d_pct | -28.08 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_60d_pct | -27.20 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_1d_pp | -2.21 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_5d_pp | -10.92 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_20d_pp | -24.61 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_60d_pp | -24.08 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma20 | 195.64 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma50 | 213.15 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma200 | 203.75 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma20_pct | -20.19 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma50_pct | -26.75 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma200_pct | -23.37 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_sma | 11.33 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_pct | 7.26 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.drawdown_from_63d_high_pct | -34.73 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.volume_vs_previous20_ratio | 1.59 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.MSFT.value | 517.99 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_1d_pct | -1.12 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_5d_pct | -4.99 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_20d_pct | -2.91 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_60d_pct | 7.19 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_1d_pp | 0.79 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_5d_pp | -3.29 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_20d_pp | 0.55 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_60d_pp | 10.32 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
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
| prices.AMZN.relative_spy_20d_pp | 1.67 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_60d_pp | 2.79 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
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
| prices.GOOGL.relative_spy_20d_pp | -14.11 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_60d_pp | -14.54 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
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
| prices.META.relative_spy_20d_pp | -7.74 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_60d_pp | 17.13 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/META/history/ |
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
| prices.CRWV.relative_spy_20d_pp | -14.93 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_60d_pp | -40.10 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
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
| prices.MU.relative_spy_20d_pp | -17.08 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_60d_pp | -22.49 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MU/history/ |
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
| prices.DRAM.relative_spy_20d_pp | -15.28 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_60d_pp | -28.79 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
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
| prices.VRT.value | 188.67 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_1d_pct | -6.63 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_5d_pct | -5.89 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_20d_pct | -8.45 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_60d_pct | -27.96 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_1d_pp | -4.72 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_5d_pp | -4.19 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_20d_pp | -4.99 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_60d_pp | -24.83 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma20 | 208.11 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma50 | 229.47 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma200 | 271.50 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma20_pct | -9.34 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma50_pct | -17.78 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma200_pct | -30.51 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_sma | 20.94 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_pct | 11.10 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.drawdown_from_63d_high_pct | -35.11 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.volume_vs_previous20_ratio | 0.85 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/VRT/history/ |
| prices.XLK.value | 164.76 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_1d_pct | -3.24 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_5d_pct | -3.58 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_20d_pct | -11.40 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_60d_pct | -10.01 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_1d_pp | -1.33 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_5d_pp | -1.89 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_20d_pp | -7.94 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_60d_pp | -6.89 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLK/history/ |
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
| prices.XLE.relative_spy_20d_pp | -2.60 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_60d_pp | 3.80 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLE/history/ |
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
| prices.XLF.relative_spy_20d_pp | 9.13 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_60d_pp | 4.70 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLF/history/ |
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
| prices.XLI.relative_spy_20d_pp | 2.85 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_60d_pp | -4.72 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLI/history/ |
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
| prices.XLV.relative_spy_20d_pp | 10.42 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_60d_pp | 11.13 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLV/history/ |
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
| prices.XLP.relative_spy_20d_pp | 9.64 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_60d_pp | 11.52 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLP/history/ |
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
| prices.XLY.relative_spy_20d_pp | 6.69 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_60d_pp | 3.46 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLY/history/ |
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
| prices.XLC.relative_spy_20d_pp | 0.49 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_60d_pp | -0.67 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLC/history/ |
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
| prices.XLU.relative_spy_20d_pp | 10.13 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_60d_pp | 7.04 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLU/history/ |
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
| prices.XLRE.relative_spy_20d_pp | 9.65 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_60d_pp | 2.11 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
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
| prices.XLB.relative_spy_20d_pp | 4.48 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_60d_pp | -0.30 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLB/history/ |
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
| prices.SMH.relative_spy_20d_pp | -12.32 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_60d_pp | -14.45 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SMH/history/ |
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
| prices.IGV.value | 99.00 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_1d_pct | -2.16 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_5d_pct | -2.42 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_20d_pct | -6.59 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_60d_pct | -4.23 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_1d_pp | -0.25 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_5d_pp | -0.73 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_20d_pp | -3.13 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_60d_pp | -1.10 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma20 | 104.70 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma50 | 106.01 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma200 | 94.21 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma20_pct | -5.45 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma50_pct | -6.61 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma200_pct | 5.08 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_sma | 3.20 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_pct | 3.23 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.drawdown_from_63d_high_pct | -12.13 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.volume_vs_previous20_ratio | 0.80 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IGV/history/ |
| prices.XOP.value | 179.98 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_1d_pct | -2.61 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_5d_pct | 3.35 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_20d_pct | -9.77 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_60d_pct | -4.67 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_1d_pp | -0.70 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_5d_pp | 5.04 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_20d_pp | -6.31 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_60d_pp | -1.54 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XOP/history/ |
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
| prices.OIH.relative_spy_20d_pp | -2.77 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_60d_pp | -9.92 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/OIH/history/ |
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
| prices.ITA.relative_spy_20d_pp | 4.18 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_60d_pp | -8.61 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ITA/history/ |
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
| prices.ARKX.relative_spy_20d_pp | -3.13 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_60d_pp | -12.51 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
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
| prices.KRE.value | 72.19 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_1d_pct | -0.76 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_5d_pct | -1.72 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_20d_pct | 4.23 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_60d_pct | -3.02 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_1d_pp | 1.16 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_5d_pp | -0.02 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_20d_pp | 7.69 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_60d_pp | 0.11 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma20 | 72.53 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma50 | 71.58 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma200 | 70.66 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma20_pct | -0.47 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma50_pct | 0.85 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma200_pct | 2.17 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_sma | 1.57 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_pct | 2.17 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.drawdown_from_63d_high_pct | -3.55 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.volume_vs_previous20_ratio | 1.18 | ratio | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/KRE/history/ |
| prices.SKYY.value | 149.30 | USD_per_share | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_1d_pct | -2.10 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_5d_pct | -0.94 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_20d_pct | -7.31 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_60d_pct | -7.40 | percent | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_1d_pp | -0.19 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_5d_pp | 0.76 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_20d_pp | -3.85 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_60d_pp | -4.27 | pp | 2026-11-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
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
    "id": "prices.SPY.relative_spy_20d_pp",
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
    "id": "prices.SPY.relative_spy_60d_pp",
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
        "change": 0.2667138671874909,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.5920529174803733,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 7.255194702148401,
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
        "change": -2.01428512988846,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.971822578669813,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -4.691542943512572,
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
    "id": "prices.QQQ.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -18.1400146484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -17.5999755859375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -56.6099853515625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.4648942669586495,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -6.211748012606133,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -3.8740539472781332,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -6.216685948417977,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.335227846591781,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.1195477411329202,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.6665886862764614,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.0587515258575158,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -4.7636683590956626,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.8820762151037016,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.1707927969030747,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -12.24601644116251,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.08341379074628952,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.9338047973408656,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.5393396293137407,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.9291944287435414,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.5641826717994292,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.3187615948402343,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.3687616411842907,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.25438126160301,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.209960433497227,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.5901475211035012,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.14910552761842055,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -5.1345819004317566,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.8304992675781477,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -11.686499023437477,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -48.74550170898442,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.129232177734366,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.432070312500059,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -9.658247070312541,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.20995056152344205,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.3225051879883267,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 7.220093383789049,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.2195263341626363,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.9135693963059803,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.3538474858391218,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.3821590932096672,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.004184010049614,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -6.566749724958919,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.69287863777975,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.7767464388355867,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -9.436762345470285,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.6242893763950867,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.6171482631138367,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 8.474304199218748,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.16936624511125187,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.3133388757336655,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.4087082390352088,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.387912393665925,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.3168228165404425,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -7.452016343210965,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.04110324254328768,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.231054338331939,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.15984015093525938,
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
    "id": "prices.IWM.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.28438877491129233,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.8513308658250285,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 8.172972585092941,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.04071926735248432,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.2910730391429102,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 4.928947741546898,
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
        "change": 0.07519912719726562,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.4321054840087868,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.8776644897461097,
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
        "change": -1.678302473858173,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.5931954691533208,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.06499641773789477,
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
    "id": "prices.RSP.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 1.5868512848809084,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.8529360377996777,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 4.806547767684389,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.6502186708249647,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.10076193443810944,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 5.95061897815703,
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
        "change": 0.11595588684082259,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.615233078002916,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.361009445190433,
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
        "change": -1.1324109593226384,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.2876102968523817,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.480950551378446,
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
    "id": "prices.GLD.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 2.2026664460007557,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -6.1666342248651755,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.1973517026467979,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.058993593329294214,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -10.848786472760107,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -11.619175675627169,
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
        "change": -13.300048828125,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -241.5,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -287.10009765625,
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
        "change": -0.36796711599292875,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.3140344869208787,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.16003108096771523,
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
        "change": -1.241155010495187,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -9.519725252338562,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -5.141666575897785,
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
        "change": 0.1494985176268342,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -5.085307235383629,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.796239484114004,
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
        "change": -2.2675466237458988,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -9.979509916817564,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -19.447873084795233,
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
        "change": 1.1803409417120103,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.963908728344389,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.494745398932108,
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
        "change": 3.0463365091792483,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -7.748680077546211,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -4.942452722190471,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 2.4473255627190054,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.889677499638134,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.7574684414844319,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.02438207025430117,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -9.65961159229607,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -12.336438544064478,
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
        "change": -14.355004882812409,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -56.05999755859375,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -182.07000732421875,
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
        "change": -12.072001953125437,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -52.67399902343732,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -200.18199707031272,
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
        "change": -4.3605004882811045,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -29.284500732421293,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -71.90750610351552,
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
        "change": 0.013062796665141985,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.599105099338585,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.658269859713702,
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
        "change": -0.049894520943272624,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.5610097711689335,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.3148614551793294,
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
        "change": -0.21287148550143264,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.805570252251602,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -4.951038012159525,
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
        "change": -2.6714041573660694,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 7.014299665178569,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 23.835763113839292,
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
        "change": -0.0602921577565283,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.31534742753414857,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.7432977104735601,
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
        "change": -0.28311229471409405,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -5.140704373120151,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -6.111373613021552,
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
        "change": -1.2027761983796987,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.9595906882335772,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.8021574619017767,
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
        "change": -3.5999984741210938,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.8899993896484375,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -18.70000457763672,
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
        "change": -3.862198934107919,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.3167767446203946,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -6.283755062308294,
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
        "change": 0.3230137964661095,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 7.786514419335777,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -12.758633694589072,
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
        "change": -5.368409350927271,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -10.689632237703337,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -26.266941606982584,
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
        "change": -3.2432740863182152,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -7.812609514082225,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -18.479764758840567,
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
        "change": -2.3138908764029797,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 4.594719959885662,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -3.9490407443439013,
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
        "change": 4.610505316140545,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 9.55755959412813,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -12.559419840881759,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.0705823058350994,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -10.494002501957842,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -23.713233681384146,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.9513453923180148,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -7.49271118956073,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -11.368330218109813,
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
        "change": -0.9350002288818331,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.872000503540036,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.4644996643066435,
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
        "change": -0.13040008544921022,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.2988003540039017,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.744599609375001,
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
        "change": 0.09875000000000966,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.5898499870300355,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.4537499999999994,
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
        "change": -2.885161065573449,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.7003001618029696,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -21.442192583746923,
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
        "change": -3.652901179612945,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.699305743861025,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -24.090066950230938,
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
        "change": -4.210053834026395,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.8186311016380916,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -26.10583509952398,
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
        "change": 0.03214263916015625,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.3057136535644531,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.6635714939662387,
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
        "change": 0.25645705663419704,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.23414092313374457,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.6171741056675981,
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
        "change": -3.4016804420622364,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.7858824123102686,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -17.669851888965393,
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
        "change": -0.8833193434973236,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.9782183106546762,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.3436381177163944,
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
        "change": -4.25,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.9800033569335938,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -17.960006713867188,
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
        "change": -4.455343258888322,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.4137763354212352,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -4.152299200254939,
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
        "change": 1.4637173950098115,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 10.58589025674691,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -3.7778382053959225,
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
        "change": -3.632645632681932,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.1922818053722004,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -25.573145288636468,
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
        "change": -5.163047023070555,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -7.5416600417741675,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -16.16129874141874,
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
        "change": -2.9070352011833833,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 5.691719550686503,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.817584882290546,
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
        "change": 5.751208914684247,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 12.356935431539261,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -3.578624351688608,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.3348185875897602,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.9966520696267054,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -23.01943736303803,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.8711183290703546,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -7.221761717252672,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -9.049864200687985,
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
        "change": -0.8980003356933537,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.4790004730224524,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.08299942016601847,
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
        "change": -0.09380004882812898,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.1013999938964929,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 5.232999877929686,
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
        "change": 0.10449996948241846,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.622699966430659,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.9469499969482484,
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
        "change": -3.291961896880224,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.9282090220154817,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -17.314057655579873,
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
        "change": -3.9971744911343485,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.8543706417937003,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -22.803998756867617,
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
        "change": -4.629743407885057,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.6967887217593458,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -24.183211490656333,
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
        "change": 0.07285690307617188,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.09642846243722136,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.7364273071289058,
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
        "change": 0.3466333760542808,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.03956324654166554,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.585520533496065,
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
        "change": -3.6127167817496364,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.8330528408858733,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -21.861656246027938,
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
        "change": -0.8989458846565154,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.9992564344509824,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.8964994795267829,
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
    "id": "prices.TLT.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 3.0372291766372017,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.494208116562737,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 5.342889252344063,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 2.6367870016477446,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.451180272520659,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 8.442953831495835,
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
        "change": -0.04314117431640341,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.4283923339843767,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.5403306579589753,
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
        "change": -0.022301635742181247,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.44648513793944744,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.6892775344848587,
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
        "change": 0.05377173897536114,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.6851376914428404,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.5697061559022387,
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
        "change": 0.025882420755862334,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.587732741322457,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.6976029828928203,
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
        "change": 0.0,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.7118686668657577,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.8008358178770214,
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
    "id": "prices.UUP.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 2.2233274519161244,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.6759237982158517,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.658896233486519,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 2.544865601418767,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 3.2103138651024548,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 11.591695460569596,
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
        "change": -0.3294553549675783,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.35941270174215667,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.5630454136109075,
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
    "id": "prices.HYG.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 2.0623680212493167,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.3007400974298413,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 4.860300086566916,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 1.962473339032622,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.03951437722066187,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 6.548389127119847,
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
        "change": -0.03342437744140625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.493464050292971,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.9874623107910168,
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
        "change": -0.0023395538330106547,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.3951014328002884,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.4118492126464872,
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
        "change": -0.22911792510360574,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.3723445914662782,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.1302887448143895,
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
        "change": -0.26801353621969115,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.4991612047816396,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.3951606764663884,
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
    "id": "prices.LQD.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 2.7925696376303377,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.5347575143433994,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 4.541291130124659,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 2.412097984010597,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.89585933033548,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 7.2752246279632065,
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
        "change": -0.03647888183593295,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.48021331787109034,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.8605935668945222,
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
        "change": -0.017653465270996094,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.4733256530761736,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.6717213058471714,
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
        "change": 0.025553682675438782,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.3427718944891032,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.7478758702099242,
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
        "change": 0.0068746087269255796,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.3310729092272378,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.5433491258839518,
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
    "id": "prices.^VIX.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 29.990332104498794,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -6.530063380070203,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.7864099255642465,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 18.583822121204427,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 13.899726449333969,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 52.57791859316716,
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
    "id": "prices.^VIX3M.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 19.161436739098747,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.3590542930470342,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 11.5956053537124,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 18.539676208375653,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 11.80541332057393,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 35.98072872233931,
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
    "id": "prices.^VVIX.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 16.749150148337513,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -7.524195355584395,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -15.290029131594872,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 21.71494737214338,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 20.212640531275774,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 33.36625478623261,
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
        "change": 2.492401123046875,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": 8.512405395507812,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": 0.182403564453125,
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
        "change": 2.1571857644890446,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": 7.782325616701047,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": 3.879157844055736,
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
        "change": 8.28733408018605,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": 16.59098748496819,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": 8.778596302817878,
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
        "change": 3.7905243595412697,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": 8.055295369284408,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": -32.4619280040154,
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
        "change": 10.375657236402596,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": 13.444421113745513,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": 9.644872297711004,
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
        "change": 3.7054938221939837,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": 10.00626392534154,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": 4.68416861925538,
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
        "change": 10.568981295793357,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": 13.25383792780982,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": 6.764859254939694,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_20d_pp",
    "available_prior_observations": 20,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 4.586169265609574,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": 6.115327246536683,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": -29.075427695582256,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_60d_pp",
    "available_prior_observations": 20,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 12.461609805840808,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": 12.411401136385763,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": 15.563992410015182,
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
        "change": 0.009120178222659092,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": -1.2648792266845703,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": -1.7868782043456974,
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
        "change": 0.43144805908202954,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": 2.0634481811523386,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": 9.785847930908204,
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
        "change": 0.21926200866698764,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": 0.9742120361328119,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": 3.697462005615236,
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
        "change": 2.534847533085416,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": 9.896600466108207,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": 2.034933487777124,
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
        "change": 2.151349638007405,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": 6.798281716078458,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": -12.062967176602381,
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
        "change": 2.7930560357694034,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": 9.264910869169384,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": -5.98191150205718,
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
        "change": 0.020778656005859375,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": 0.07720783778599305,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": -0.32493482317243316,
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
        "change": -0.1068448979666643,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": -0.38186373717014366,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": -0.3305442139444317,
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
        "change": 2.194015102574731,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-06",
        "to": "2026-11-16",
        "change": 7.493314709372111,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-16",
        "to": "2026-11-16",
        "change": 0.16056652016125383,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -6.7100067138671875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -22.529998779296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -60.94999694824219,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.1106144784322374,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.14989343700252444,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -5.502693934380731,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.13662141031454134,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.0340694034859599,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -8.531537874585016,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -4.1278444696499115,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -7.021649464021564,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -23.55044464176308,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.3827001423787024,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -6.641925919705706,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -32.27363714909395,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.5623064207272983,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 4.427836652267792,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -3.1679796164163383,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 4.424112929988976,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.7369757713063905,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -8.332324020877703,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.8300174245577416,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -6.826019728276069,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -20.996736716164644,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.09077144837850426,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -6.322027595184213,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -25.162202608363195,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.0474998474121264,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -13.523500061035179,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -32.021498870849626,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.4792504882812523,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -5.847731323242186,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -9.678004455566423,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.17271896362305483,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.6006591033935536,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.9354911804199162,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.1530254328242613,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -5.611357671451989,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -15.546616610267861,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.6214248964699713,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -8.33166268046477,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -24.171081363287563,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.2255975813576434,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -10.800043934605997,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -30.40594449519758,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.3235713413783472,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.54356929234096,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 5.58857182094029,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.4976411603889872,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.338506273831719,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 4.611328688610616,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.804717672546161,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -9.417320791668612,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -25.476507084423947,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.2635446022547725,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.3139224493609536,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.648619083812888,
        "unit": "ratio"
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
    "id": "prices.MSFT.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.3641855771682412,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.459936289790822,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -6.718676577924576,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.602163829753966,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.744671521891318,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -25.735337794867434,
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
        "change": 0.4520631408691429,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.6867805480957259,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 6.649572753906284,
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
        "change": -1.457704265901441,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -6.64110374051117,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -5.374578230267481,
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
    "id": "prices.AMZN.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -6.156996286173788,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.446497926265025,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.7848020085634455,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.566500177955509,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.6499025695108855,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -6.300215285899792,
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
    "id": "prices.GOOGL.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.1090409257076494,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.9355494625870584,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -11.972983753351206,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.2504662668041764,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.7045758891429923,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -18.267969738774894,
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
        "change": -0.2681182861328466,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.0889399719238781,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.783750457763688,
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
        "change": -3.496417960022356,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.0370289424353025,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -17.059045726061782,
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
    "id": "prices.META.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.6306466888848856,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.6663753016311755,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -3.818205024158137,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.3597581676843333,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 5.502988896573536,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.4977304610468423,
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
        "change": -0.4412509155272346,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.4904629516601062,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.7194863891601244,
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
        "change": -2.3556261317109084,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.1355805506280023,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -12.24758053845073,
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
    "id": "prices.CRWV.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.637264646279057,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 20.77891940401495,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 12.619706134712972,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.1206454696390935,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 10.56610582010127,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -21.14057170066955,
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
    "id": "prices.MU.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -6.804724012150555,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 5.51502577720775,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -4.681004667734447,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.217839293421047,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.7609666741392438,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -16.776900782117334,
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
        "change": 1.5222201538085756,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 8.742124328613272,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 46.217359771728525,
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
        "change": -7.93255313357677,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.944606717121734,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -31.8028032269402,
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
    "id": "prices.DRAM.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -7.729244549087822,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 5.097171935196256,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 5.324310942255517,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.262226311668428,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.486619192371759,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -15.651907554680815,
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
    "id": "prices.VRT.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -13.400009155273438,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -11.800003051757812,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -17.410003662109375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.0204213247857825,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -16.261688236733484,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -6.466658709829232,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -16.39147723395905,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 4.714082385245012,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 8.01757377724871,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -6.340827645807534,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 7.799315851276946,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 9.402416258942226,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -4.335313065978696,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 3.801919612071437,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.0514831879601765,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.4721132670808434,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -11.983745021468218,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -4.131944391864839,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -12.103985714284615,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 6.485127560037363,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 8.216787630956023,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -4.043000600715362,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 7.994945587022441,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 11.956124184540663,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.0433843719784974,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 4.1218179365929295,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 8.162917728690928,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.8705001831054631,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.312999725341797,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -31.85249862670898,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.8358248901367062,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -6.386325378417951,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -24.635951232910145,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.013093185424850162,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.2814161682128997,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.077360382080087,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -6.0343825728001566,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.7142136280429057,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 4.778504309309916,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -5.140696271523172,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.776769921714685,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.1199846615849047,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -4.939118219239848,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.422823700502157,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -7.2827071585898295,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.28607177734375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.4514312744140625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 10.427784511021207,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.87742878392854,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.377180239976937,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 5.997528651134322,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -4.608635707216756,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.352073130547115,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.9083138658437804,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.21671123420041916,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.026913851673232014,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.1599973705874672,
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
    "id": "prices.XLK.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.9132927218409748,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.7714864521140576,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -4.284115861304416,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.8295393892166611,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.2682512003478461,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -8.757720843508476,
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
    "id": "prices.XLE.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 1.0424373147803316,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.29941416121790354,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -12.057723369723107,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.46163792832437656,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.3501830060548605,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -6.61132039144181,
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
        "change": 0.06816047668456804,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.36464042663574503,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.8985040283203105,
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
        "change": -2.2795240235147016,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.312985691874725,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -10.7845795324639,
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
    "id": "prices.XLF.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 2.2727282209451634,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.5215692771883162,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 9.722935026082602,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.46555245451788085,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.8353507691152848,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 10.561267141571197,
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
        "change": 0.02692876815796552,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.1440944862365754,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.3520298194885285,
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
        "change": -0.9860917190320109,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.06322941463372445,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 5.134187404978485,
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
    "id": "prices.XLI.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 1.077868553955319,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.2626082606595581,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.883170161383187,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.30566077243117107,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.6764325505747468,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 7.767376598698316,
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
        "change": 0.00764801025388806,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.12614761352537585,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.5590048217773358,
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
        "change": -1.8098429498030422,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.9405763339744864,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.9033029601691056,
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
    "id": "prices.XLV.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 2.3905310669719473,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.342203758115179,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 5.5876629784409335,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.32996304850051317,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.628491215191811,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 6.657577760535749,
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
    "id": "prices.XLP.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 3.080004456990893,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.3006971583415563,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.276670386905023,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 1.735670226165709,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.4451674856085805,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 11.16385131985611,
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
        "change": 0.05334243774414915,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.2620676803588964,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.0349322128295881,
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
        "change": 0.22750735300083136,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.6949154000558408,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 5.115484562963423,
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
    "id": "prices.XLY.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.1651629771452061,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.36534406657576,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.790556603729667,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.4321534617968692,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.9522720666747313,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.5960044271215565,
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
        "change": -0.011356811523441479,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.02373249053955817,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.3691440582275334,
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
        "change": -1.5800070876158756,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.4636954664542188,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.5247235107429664,
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
    "id": "prices.XLC.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.8050504222702926,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.8951395594911871,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.6444192163824773,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.02903358062897876,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.1604391059443775,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.5905520227513117,
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
        "change": -0.06087612152100519,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.23259288787842536,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.060179824829106,
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
        "change": -1.6197432610228208,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.28364042948377755,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.9998689977806179,
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
    "id": "prices.XLU.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 4.6354670468556565,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.6801742606369565,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 7.505222302122183,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 4.850149316343433,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 4.681698930930622,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 21.019611553528417,
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
        "change": 0.008771514892579546,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.03865335464477937,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.117687416076663,
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
        "change": 0.16223832577673125,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.6640370973810983,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 6.036158540548309,
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
    "id": "prices.XLRE.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 3.247403059675114,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.10141373210466043,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 10.905353407526365,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 2.023497024609844,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.13340197616795724,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 14.647647385031927,
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
    "id": "prices.XLB.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.7457705776574901,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -5.863049163964828,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.079845912059319,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.2280086901342524,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.3289846840634745,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.834913089158798,
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
        "change": 0.014123744964599894,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.07920091629028292,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.4251508903503449,
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
        "change": -1.5204764119375103,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.0477686141212823,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.17896913303248052,
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
    "id": "prices.SMH.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.6585101120610197,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.9397740968244417,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -5.24752629692048,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.79800244611258,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.17801250723288398,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -8.199845965170228,
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
    "id": "prices.IGV.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.19000244140625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.4599990844726562,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -6.989997863769531,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.9079693625365879,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -4.773473064522649,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -3.7456179598389205,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -4.7607703076251395,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.992801679707279,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.3291751905534674,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.575989226717724,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.229626544618612,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -5.530832753392101,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -3.5210277979224496,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.710237727158404,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -24.69808917724804,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.3596613048316488,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.4955298492573812,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.410903641874528,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.4732787879507039,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.22175650491492727,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.5283890442607815,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.2781621816255528,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.4252562803641067,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -2.9771248277936646,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.2290991039222492,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.3903394026369091,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -17.586654636517288,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.3494998931884794,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.7179996490478544,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -3.5274997711181726,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.1113999938964838,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.5379998779296926,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.041000213623050286,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.04353466033936115,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.14039642333983693,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.48772174835204396,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.7700977664110717,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.7851644734998553,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -3.3767138170062827,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.9657108097651639,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.8373190556831505,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -6.632638152654868,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.3742429436927504,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.771906888383091,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -8.005014846539883,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.06571469988141754,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.14071437290736588,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.39071491786411805,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.13491299868619366,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.21707791734317006,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.5818517918981749,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.9437316739123531,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.1833665789041454,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -6.203956667584432,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.23493572777231775,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.11442105093889032,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.024344731323097113,
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
    "id": "prices.XOP.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.3021592778084239,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.7906820296006991,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -15.184711975963182,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.3526272110237825,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.2173332904103717,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -12.615703164086113,
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
        "change": 0.20767326354979332,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.129175949096691,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 5.9875269699096805,
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
        "change": -2.9285635651393083,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.717999500028778,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -15.490447357241077,
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
    "id": "prices.OIH.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.1940126556435624,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.2033814156946487,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.770966396376338,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.0189423478570756,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.6910756122060402,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -4.266197538203541,
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
    "id": "prices.ITA.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.4034346964328579,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -3.4457841451120306,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 7.147999505598213,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.14849701574093288,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 3.577973349071671,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 8.761810912145451,
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
        "change": -0.03757923126219964,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.15096622467041243,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -153.8609831237793,
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
        "change": -2.275787186186772,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.3456533476575165,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 1.5723374291177539,
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
    "id": "prices.ARKX.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.103113307034854,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.9506797400407052,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 4.683703057424626,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.1078060308518225,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.463780489095024,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -7.40813917881561,
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
    "id": "prices.KRE.value",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.5499954223632812,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.2599945068359375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.9300003051757812,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_1d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.0594776948481432,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.487413420699458,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.03173480497090653,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_5d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -2.463369018728323,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.3356726027836663,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.2841695009319976,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_20d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.03332933258146653,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.361857392654331,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 8.022623886179058,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_60d_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.9350801185822433,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.194524484248628,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 5.005199546617666,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_1d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.4888303628567958,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.7905297945658094,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.366449122935299,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_5d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 1.8241225009461126,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.4353725720086854,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -1.0849556472246835,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 2.3311563776736373,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.166227656908836,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 10.576331811777495,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 1.3568485754179571,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 2.5144228087701226,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 12.11663408734842,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma20",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.14650001525878054,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.8534996032714872,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 2.602499771118161,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma50",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.05307449340820369,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.09942886352538949,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.9692437744140676,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma200",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.02280172348022802,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.13771497726439463,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.6004489135742119,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma20_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.9612888380508,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -2.943103727418861,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.4857671016204379,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma50_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.6930317858567792,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.6178279360191894,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 5.385571023441815,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma200_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.8116149362922265,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -1.9862095451550266,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 3.306590036696888,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_sma",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.02642876761300217,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.08000074114118294,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.2978564671107702,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.05272486621277617,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": -0.07172966797318958,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.3383442958644045,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 1.2633060245237027,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.666256591283799,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 7.073492520966518,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.volume_vs_previous20_ratio",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": 0.6466594107592906,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 0.29945463485547585,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": 0.5417723631741603,
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
    "id": "prices.SKYY.relative_spy_20d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -1.230058170601922,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 5.519436155880763,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -0.5206756470273355,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_60d_pp",
    "available_prior_observations": 21,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-13",
        "to": "2026-11-16",
        "change": -0.7789674782919582,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-09",
        "to": "2026-11-16",
        "change": 1.7689627591154782,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 20,
        "from": "2026-10-19",
        "to": "2026-11-16",
        "change": -22.355216772190325,
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
| 事实指标引用 | ["prices.QQQ.sma200", "prices.SPY.value", "prices.QQQ.value", "prices.RSP.return_1d_pct", "observed.SPY.low", "observed.QQQ.low"] |
| 推断与解释 | 推断：收盘已触发昨晚框架失效；先修复位置、后回踩及广度，不能把超跌反抽当趋势反转。 |
| 反证与缺口 | 仍可能出现空头回补；没有本轮分钟数据证明常规VWAP或回踩。 |
| 确认条件 | SPY先收复747.89–749.82，QQQ671.71–672.15；回踩形成更高低点且收盘站稳，RSP/IWM同步改善、涨跌家数扩散。进一步看SPY20日757.69、QQQ200日681.41；第一段反抽只是修复。 |
| 失效条件 | SPY跌破16日低738.07、QQQ660.48且反抽失败，或突破后又收回区间下方 |
| 观察期限 | 11月17–20日；财报后按实际新信息复核 |
| 条件式指导 | 按确认、失效和事件风险分批评估；无法承受财报跳空则等待事件落地，不依据低价本身升级。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相对昨晚新增16日完整收盘；前期观察支撑已失守，今日条件已更新。 |

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
| 判断变化原因 | 相对昨晚新增16日完整收盘；前期观察支撑已失守，今日条件已更新。 |

## 判断依据 · 哪些板块优先观察

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 哪些板块优先观察 |
| 事实指标引用 | ["prices.XLF.relative_spy_20d_pp", "prices.XLV.relative_spy_20d_pp", "prices.XLP.sma20"] |
| 推断与解释 | 推断：防御/金融相对强，但只有少数绝对上涨；排序不等于买点或资金净流入。 |
| 反证与缺口 | XLP收盘低于开盘，XLV/XLF仍下跌；相对抗跌不自动成为买点。 |
| 确认条件 | XLP92.38、XLV187.60、XLF57.89是16日低点参考；回踩守住后再突破各自16日高93.48/191.33/58.81，且收盘维持相对领先。支撑不是保证，按实际波动修订。 |
| 失效条件 | 关键低点破位且无法收复、相对强度反转；金融另看信用扩散。 |
| 观察期限 | 11月17–20日；财报后按实际新信息复核 |
| 条件式指导 | 按确认、失效和事件风险分批评估；无法承受财报跳空则等待事件落地，不依据低价本身升级。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相对昨晚新增16日完整收盘；前期观察支撑已失守，今日条件已更新。 |

## 判断依据 · 是否为全面恐慌或过热

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 是否为全面恐慌或过热 |
| 事实指标引用 | ["prices.^VIX.value", "prices.^VIX3M.value", "macro.BAMLH0A0HYM2.value", "observed.Treasury10Y.value"] |
| 推断与解释 | 推断：风险收缩加重；曲线接近平坦，信用资料滞后，无法断言系统性恐慌。 |
| 反证与缺口 | 债券利率回落、黄金未上涨、金融压力指标滞后；CNN新值缺失。 |
| 确认条件 | VIX/短期期限结构、当期信用利差与市场广度持续同步恶化才升级风险判断。 |
| 失效条件 | 价格收复、广度扩散且信用与波动同步稳定，撤销恐慌升级假设。 |
| 观察期限 | 11月17–20日并随新信用数据更新 |
| 条件式指导 | 同时观察股、债、波动与信用；不把单一阈值机械转换成仓位。 |
| 主观置信等级 | medium |
| 判断变化原因 | VIX由19.30升22.91，美债16日小幅回落；新增完整收盘证据。 |

## AI政策、治理与现金流兑现 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 新远程算力限制与NVDA财报临近 |
| 事实：市场反应 | NVDA−4.12%、SMH−5.11%、MU−7.62% |
| 推断：解释 | 推断：投资者提高风险折价；无法将当日跌幅精确归因单一新闻 |
| 受益篮子 | ["现金流稳健且能验证需求的软件/云公司，条件观察"] |
| 受损篮子 | ["半导体、算力融资、高杠杆主题"] |
| 反证 | H100租价仍高，需求崩塌未验证 |
| 下一催化剂 | 17日NVDA结果、订单回款与指引 |
| 证据 | ["https://www.bis.gov/press-release/bis-issues-rule-addressing-remote-access-american-super-intelligence-technology", "https://www.bis.gov/media/documents/rin-0694-ak50.pdf", "https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/default.aspx", "https://www.silicondata.com/products/silicon-index/h100"] |

## 利率下降没有换来股市止跌 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 财政部曲线回落；Warsh讨论AI经济情景 |
| 事实：市场反应 | 2年4.83%、10年5.12%，QQQ仍跌2.67% |
| 推断：解释 | 推断：折现率只是变量之一，盈利和风险溢价仍主导 |
| 受益篮子 | ["高质量现金流，待价格确认"] |
| 受损篮子 | ["长久期高预期股票"] |
| 反证 | 单日共振不构成因果识别 |
| 下一催化剂 | 进口价格、FOMC纪要 |
| 证据 | ["https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value_month=202611&type=daily_treasury_yield_curve", "https://www.federalreserve.gov/newsevents/speech/warsh20261116a.htm", "https://www.federalreserve.gov/newsevents/2026-November.htm"] |

## 防御相对占优，绝对承接有限 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 19ETF中仅必需消费和公用事业上涨 |
| 事实：市场反应 | XLP+0.27%、XLU+0.18%，XLV/XLF仍跌 |
| 推断：解释 | 推断：避险偏好比全面风险回归更明显 |
| 受益篮子 | ["XLP", "XLV", "XLF", "XLU"] |
| 受损篮子 | ["SMH", "XLK", "ARKX"] |
| 反证 | 相对收益不等于净申赎，XLP开盘后也回落 |
| 下一催化剂 | 下一交易日回踩和收盘 |
| 证据 | ["https://finance.yahoo.com/quote/XLP/", "https://www.ici.org/research/stats/etf_flows"] |

## 油价与航运风险分化 · 待核验

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | Reuters较新窗口显示过境减少 |
| 事实：市场反应 | WTI/Brent同源日线继续下跌，能源ETF落后 |
| 推断：解释 | 推断：供需预期、美元及合约因素可能抵消地缘溢价，不能只选利多故事 |
| 受益篮子 | ["运输/消费者仅为油价下降条件受益"] |
| 受损篮子 | ["XLE", "XOP", "OIH"] |
| 反证 | 停火合约上涨不等于实际运输恢复 |
| 下一催化剂 | 可核验过境量、供应与指定合约价格 |
| 证据 | ["https://www.gulf-times.com/article/731298/shopping/shipping-slows-through-strait-of-hormuz-after-tanker-attacks/amp", "https://www.matteoiacoviello.com/gpr.htm"] |

## AI融资市场接受度 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | Anthropic拟上市临近 |
| 事实：市场反应 | 首日市值<1.25万亿档33.25%，较昨晚+8.60pp |
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

## 核心行情与风险代理

| 标的 | 价格/指数 | 单位 | 观测日 | 1日% | 5日% | 20日% | 质量 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 739.95 | USD_per_share | 2026-11-16 | -1.91 | -1.69 | -3.46 | ok |
| QQQ | 661.75 | USD_per_share | 2026-11-16 | -2.67 | -2.59 | -7.88 | ok |
| IWM | 272.94 | USD_per_share | 2026-11-16 | -1.66 | -3.39 | 0.61 | ok |
| RSP | 218.93 | USD_per_share | 2026-11-16 | -1.01 | -0.91 | 2.59 | ok |
| GLD | 352.93 | USD_per_share | 2026-11-16 | -0.71 | -7.01 | -7.05 | ok |
| GC=F | 3,873.00 | USD_per_troy_ounce | 2026-11-16 | -0.34 | -5.87 | -6.90 | ok |
| CL=F | 84.96 | USD_per_barrel | 2026-11-16 | -4.07 | -2.18 | -18.04 | ok |
| BZ=F | 91.59 | USD_per_barrel | 2026-11-16 | -4.43 | -1.06 | -16.39 | ok |
| TLT | 79.38 | USD_per_share | 2026-11-16 | 0.00 | -3.15 | 0.32 | ok |
| UUP | 29.56 | USD_per_share | 2026-11-16 | 0.20 | 2.04 | 1.93 | ok |
| HYG | 76.73 | USD_per_share | 2026-11-16 | -0.27 | -1.01 | 0.39 | ok |
| LQD | 102.80 | USD_per_share | 2026-11-16 | -0.01 | -1.79 | 0.31 | ok |
| ^VIX | 22.91 | index | 2026-11-16 | 18.70 | 15.01 | 24.24 | ok |
| ^VIX3M | 23.02 | index | 2026-11-16 | 11.64 | 10.41 | 17.45 | ok |
| ^VVIX | 114.23 | index | 2026-11-16 | 12.51 | 16.05 | 6.83 | ok |
| ^MOVE | 101.28 | index | 2026-11-16 | 2.52 | 9.18 | 0.18 | ok |
| NVDA | 156.14 | USD_per_share | 2026-11-16 | -4.12 | -12.61 | -28.08 | ok |
| MSFT | 517.99 | USD_per_share | 2026-11-16 | -1.12 | -4.99 | -2.91 | ok |
| AMZN | 257.75 | USD_per_share | 2026-11-16 | -3.34 | -3.44 | -1.79 | ok |
| GOOGL | 283.72 | USD_per_share | 2026-11-16 | -4.07 | -1.54 | -17.57 | ok |
| META | 626.41 | USD_per_share | 2026-11-16 | -2.38 | -2.33 | -11.20 | ok |
| CRWV | 49.88 | USD_per_share | 2026-11-16 | -6.12 | 1.84 | -18.39 | ok |
| MU | 719.02 | USD_per_share | 2026-11-16 | -7.62 | -1.93 | -20.54 | ok |
| DRAM | 39.27 | USD_per_share | 2026-11-16 | -7.38 | -6.01 | -18.75 | ok |
| VRT | 188.67 | USD_per_share | 2026-11-16 | -6.63 | -5.89 | -8.45 | ok |

## 跨资产风险解释

判断：风险偏好收缩，半导体压力向宽基扩散；不属于过热，暂不称全面流动性恐慌。16日VIX22.91、VIX3M23.02，同日比值约0.995，曲线接近平坦但未倒挂；VVIX114.23、MOVE101.28同步上升。VIX高低没有一条能机械划分恐慌的通用线。CNN API返回418，官方页面抓取受限，本轮没有可核验新值，不沿用昨晚39冒充当前。
[财政部16日曲线](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value_month=202611&type=daily_treasury_yield_curve)显示2年4.83%、10年5.12%，比13日分别下降5/3bp；FRED对应序列仍停在13日，面板保留各自时点。利率回落而股价仍跌，反证了“只等利率降就能反弹”。FRED实际10年2.91%、HY323bp、IG89bp为13日；金融压力−0.4918为6日，不能据其滞后低值否认当前风险。
同源16日日线黄金期货3873、WTI84.96、Brent91.59分别约−0.34%、−4.07%、−4.43%；期货是连续合约供应商日线，不是交易所正式结算，不能用异常低的合约成交量证明需求崩溃。GLD−0.71%、TLT持平、UUP+0.20%，未出现黄金与长债一致大涨的传统避险组合。GPR已更新到16日189.55，7日均值145.08，反映报纸报道密度而非损失或战争概率。
[Reuters/Kpler报道](https://www.gulf-times.com/article/731298/shopping/shipping-slows-through-strait-of-hormuz-after-tanker-attacks/amp)称周末过境减少，星期六5艘商品船、星期日未登记，比较上周末31艘；跟踪覆盖与补报可能影响计数。此前“接近战前水平”的概括不能抹去这个较新窗口。伊朗22日合约72.5%上升，与Hormuz恢复正常合约4.5%并不矛盾：前者专门行动/停火定义不等于海峡通行。油价下降也不能独自证明航运安全改善。

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

缺失：本轮CNN API 418，官方页面抓取受限；旧39为16日早晨值，不作为当前读数。

## 19 板块与主题 ETF：价格量能证据

| 标的 | 板块 | 1日% | 5日% | 20日% | 相对SPY 1日pp | 相对SPY 5日pp | 相对SPY 20日pp | 成交量/前20日 | 观测日 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLK | 科技 | -3.24 | -3.58 | -11.40 | -1.33 | -1.89 | -7.94 | 1.05 | 2026-11-16 |
| XLE | 能源 | -1.96 | 2.83 | -6.06 | -0.04 | 4.52 | -2.60 | 0.86 | 2026-11-16 |
| XLF | 金融 | -0.85 | 0.33 | 5.67 | 1.06 | 2.02 | 9.13 | 1.17 | 2026-11-16 |
| XLI | 工业 | -1.85 | -1.91 | -0.61 | 0.06 | -0.22 | 2.85 | 1.04 | 2026-11-16 |
| XLV | 医疗 | -0.51 | -0.24 | 6.96 | 1.40 | 1.45 | 10.42 | 0.87 | 2026-11-16 |
| XLP | 必需消费 | 0.27 | 1.88 | 6.18 | 2.18 | 3.57 | 9.64 | 1.01 | 2026-11-16 |
| XLY | 可选消费 | -1.53 | -2.36 | 3.22 | 0.39 | -0.67 | 6.69 | 0.98 | 2026-11-16 |
| XLC | 通信 | -1.72 | -0.50 | -2.97 | 0.19 | 1.19 | 0.49 | 0.78 | 2026-11-16 |
| XLU | 公用事业 | 0.18 | 0.75 | 6.67 | 2.09 | 2.45 | 10.13 | 0.73 | 2026-11-16 |
| XLRE | 房地产 | -0.27 | -0.87 | 6.19 | 1.64 | 0.82 | 9.65 | 0.78 | 2026-11-16 |
| XLB | 材料 | -1.46 | -2.78 | 1.02 | 0.46 | -1.08 | 4.48 | 1.16 | 2026-11-16 |
| SMH | 半导体 | -5.11 | -5.23 | -15.78 | -3.19 | -3.54 | -12.32 | 0.85 | 2026-11-16 |
| IGV | 软件 | -2.16 | -2.42 | -6.59 | -0.25 | -0.73 | -3.13 | 0.80 | 2026-11-16 |
| XOP | 油气开采 | -2.61 | 3.35 | -9.77 | -0.70 | 5.04 | -6.31 | 0.63 | 2026-11-16 |
| OIH | 油服 | -3.84 | 0.16 | -6.23 | -1.93 | 1.85 | -2.77 | 0.74 | 2026-11-16 |
| ITA | 航空与国防 | -2.46 | -2.68 | 0.72 | -0.55 | -0.99 | 4.18 | 0.72 | 2026-11-16 |
| ARKX | 航天主题 | -4.00 | -6.59 | -6.59 | -2.09 | -4.90 | -3.13 | 0.34 | 2026-11-16 |
| KRE | 区域银行 | -0.76 | -1.72 | 4.23 | 1.16 | -0.02 | 7.69 | 1.18 | 2026-11-16 |
| SKYY | 云计算 | -2.10 | -0.94 | -7.31 | -0.19 | 0.76 | -3.85 | 0.77 | 2026-11-16 |

## 资金证据分层

16日19个行业/主题ETF仅XLP、XLU上涨，2涨17跌；这是本仓库固定篮子广度，不是全市场上涨家数。XLP+0.27%、XLU+0.18%，XLV−0.51%、XLF−0.85%相对抗跌；SMH−5.11%、ARKX−4.00%、OIH−3.84%、XLK−3.24%落后。RSP−1.01%、IWM−1.66%均跌，不能把跌得少写成全面承接。20个同端点交易日相对SPY：XLV+10.42pp、XLU+10.13pp、XLP+9.64pp、XLF+9.13pp，SMH−12.32pp、XLK−7.94pp；防御/金融优先观察，能源、工业、软件、航天仍需修复。
[Reuters收盘报道](https://www.marketscreener.com/news/wall-street-slumps-on-ai-jitters-ahead-of-nvidia-results-anthropic-ipo-ce785edfdd8ef425)给出NYSE跌涨比3.45:1，Nasdaq上涨1131、下跌3697；来源为新闻所引市场统计，非本轮自行逐股审计。SPY成交量约前20日均量1.47倍，NVDA1.59倍，但SMH仅0.85倍、QQQ0.87倍，不能称所有板块都放量恐慌。
资金证据分层：[VanEck](https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/overview/)16日SMH净值461.74、净资产611.3亿美元；单点且金额四舍五入，没有连续精确份额及拆分核验，无法反推可靠当日申赎。[ICI](https://www.ici.org/research/stats/etf_flows)仍为截至11月4日一周，美国股票ETF净发行308.68亿美元、债券138.89亿美元、商品1.29亿美元。此滞后窗口不能解释16日资金去向；当期细分申赎及滞后机构持仓未核验，以上轮动只代表价格量能。

## 最近可核验 ETF 申赎窗口

| 标的 | 金额 USD million | 起始日 | 结束日 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- |
| US_DOMESTIC_EQUITY_ETFS | 30868 | 2026-10-29 | 2026-11-04 | public_report | https://www.ici.org/research/stats/etf_flows |
| US_BOND_ETFS | 13889 | 2026-10-29 | 2026-11-04 | public_report | https://www.ici.org/research/stats/etf_flows |
| US_COMMODITY_ETFS | 129 | 2026-10-29 | 2026-11-04 | public_report | https://www.ici.org/research/stats/etf_flows |

## Polymarket 搜索覆盖与限制

17日04:07UTC起重采固定清单并主动搜索17组：Fed/衰退、AI、NVDA、AMD、CRWV、伊朗/俄乌、Hormuz、油价、关税、政府、银行、航天、数据中心及故障等。独立搜索每词最多10事件，部分hasMore=true；固定采集也存在分页截断，非全量市场/新闻库。补入事件ID并核对15份已跟踪规则，全部hash不变。最显著新增参考是Anthropic较低估值档上升；新增发现无额外高质量且规则已审计合约，不强行扩表。未来7/30天催化剂单列；IPO具体时分未知，upcoming_events为空。

## Polymarket · 值得警惕的信号

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["AI bubble burst in 2026?", "期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。", "https://polymarket.com/event/ai-bubble-burst-by"] | [7.75, {"status": "comparable", "change_pp": 0.050000000000000044}] | {"spread": 0.0010000000000000009, "volume24h_usd": 4102.681727, "liquidity_usd": 190014.09858, "quality_flags": [], "retrieved_at": "2026-11-17T04:08:13.188609+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["多条件AI合约与实际融资分开", "AI估值/融资"] | ["多个实际阈值与信用持续恶化共同出现", "需求、回款与融资恢复且阈值未满足"] | [null, null] |
| ["CoreWeave downgraded by Moody's or S&P by December 31, 2026?", "2026年12月31日23:59ET前，Moody’s或S&P正式下调CoreWeave长期主体/企业家族或高级无担保债信用评级则Yes；仅负面展望/观察名单不算，不要求降至某统一评级档。成交很薄，不视为客观违约概率。", "https://polymarket.com/event/coreweave-downgraded-by-moodys-or-sp-by"] | [25.0, {"status": "comparable", "change_pp": -2.500000000000002}] | {"spread": 0.04000000000000001, "volume24h_usd": 50.106663999999995, "liquidity_usd": 437.2914, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"], "retrieved_at": "2026-11-17T04:07:31.020247+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["25%，较昨晚−2.5pp；价差4pp、24h50.11美元，不能证明信用改善", "算力融资成本"] | ["正式评级行动及实际融资成本共同转坏", "仅展望变化或评级不变；薄盘口不足确认"] | [null, null] |
| ["US x Iran Effective Ceasefire by November 22?", "须完成连续14个伊朗标准时间日，美国未实施合资格命中伊朗陆地及内水的空袭或地对地导弹行动，首日在创建后至11月22日范围内；最后合资格行动次日为首日，无行动则创建日。第14日后再留3个日历日报道窗口。拦截碎片、海域/领空、网络、地面入侵和部分小型袭击不算。不是双边全面停火；期限不同于15日档，首次基线。", "https://polymarket.com/event/us-x-iran-effective-ceasefire-begins-by-2-week-pause-20261108"] | [72.5, {"status": "comparable", "change_pp": 13.0}] | {"spread": 0.030000000000000027, "volume24h_usd": 6519.000959, "liquidity_usd": 65196.799, "quality_flags": [], "retrieved_at": "2026-11-17T04:08:13.188609+00:00", "contract_end_at": "2026-11-22T20:29:00+00:00"} | ["22日专门合约72.5%，较昨晚+13pp；海峡通行仍须另查", "原油、运输及风险溢价"] | ["按正式规则核验命中行动及完整观察窗，另查实际航运", "出现合资格行动，或把海上袭击错误等同此结算条件"] | [null, null] |

## Polymarket · 有参考价值的事件

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Strait of Hormuz traffic returns to normal by December 31?", "期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。", "https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31"] | [4.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.010000000000000002, "volume24h_usd": 20984.675375, "liquidity_usd": 259177.7465, "quality_flags": [], "retrieved_at": "2026-11-17T04:08:13.188609+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["实际通行量与外交表态分开", "油运/能源"] | ["Portwatch量持续改善并满足规则", "航运事件持续且量未恢复"] | [null, null] |
| ["Russia x Ukraine energy ceasefire agreement by November 30, 2026?", "11月30日23:59基辅时间前，双方同意相互暂停至少一类明确能源设施打击；双方官宣或可信报道共识确认。第三方单方声称、谈判或单一设施暂停不算。正式协议可先于实际生效；不同于15日截止档，首次基线。", "https://polymarket.com/event/russia-x-ukraine-energy-ceasefire-agreement-by"] | [4.5, {"status": "comparable", "change_pp": -1.0000000000000002}] | {"spread": 0.010000000000000002, "volume24h_usd": 5995.942236, "liquidity_usd": 154524.1629, "quality_flags": [], "retrieved_at": "2026-11-17T04:08:13.188609+00:00", "contract_end_at": "2026-11-30T21:59:00+00:00"} | ["能源30日档4.5%，较昨晚−1pp；不跨已过期合约", "能源供给/风险溢价"] | ["双方确认合格能源设施互停安排", "仅换囚或第三方声称"] | [null, null] |
| ["Russia x Ukraine ceasefire agreement by December 31, 2026?", "2026年末23:59ET前，双方官宣或可信共识确认相互暂停直接交战，包含明确生效日的全面暂停；仅限定目标/地点的局部能源安排不算。达成协议可先于实际生效，单方暂停不算。", "https://polymarket.com/event/russia-x-ukraine-ceasefire-agreement-by"] | [11.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.009999999999999995, "volume24h_usd": 1232.156294, "liquidity_usd": 104896.4191, "quality_flags": [], "retrieved_at": "2026-11-17T04:08:13.188609+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["全年全面停火协议与能源局部暂停定义不同", "军工/欧洲风险偏好"] | ["双边明确全面暂停及生效日", "仅局部或单方暂停"] | [null, null] |
| ["Will WTI Crude Oil (WTI) hit (HIGH) $110 in November?", "11月规定Pyth时段内，ICE Europe WTI活跃月CLL最终1分钟High达到110美元即Yes，不取整，末三个交易日换月。仅因系统/数据故障无法核验时使用ICE官方日高低；正常Pyth收市不属于故障，不计该时段后价格。结构变动依Pyth调整价。规则与11月14日建立的新基线一致，不跨此前规则变更比较；Yahoo连续WTI不能直接裁决。", "https://polymarket.com/event/what-price-will-wti-hit-in-november-2026"] | [2.75, {"status": "comparable", "change_pp": -1.4000000000000001}] | {"spread": 0.009000000000000001, "volume24h_usd": 5473.038371, "liquidity_usd": 38078.48155, "quality_flags": [], "retrieved_at": "2026-11-17T04:08:13.188609+00:00", "contract_end_at": "2026-12-01T04:59:59.999000+00:00"} | ["月内WTI高点合约；不直接用Yahoo裁决", "通胀与油气"] | ["指定Pyth/ICE价格和实际供应压力同向", "供应改善且指定价格未触发"] | [null, null] |
| ["New NVIDIA CEO named by December 31, 2026?", "2026年12月31日23:59纽约时间前，英伟达正式宣布黄仁勋的CEO继任者即满足；实际就任可以更晚，临时CEO不计。以公司公开声明为主要来源，可参照可信报道共识。与离任宣布合约不同。", "https://polymarket.com/event/new-nvidia-ceo-named-by-december-31-2026"] | [20.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.009999999999999981, "volume24h_usd": 4647.183337, "liquidity_usd": 83430.6989, "quality_flags": [], "retrieved_at": "2026-11-17T04:08:13.188609+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["临时CEO已经任命，但本合约只计正式永久继任者宣布", "管理连续性、客户信任与估值风险溢价"] | ["公司正式公告永久CEO且符合截止要求", "只有临时任命或到期无永久继任宣布"] | [null, null] |
| ["Will the Fed increase interest rates by 50+ bps after the December 2026 meeting?", "衡量12月8–9日该次FOMC前后联邦基金目标区间上限上调至少50bp；非标准变化向上取整到最近25bp对应档。按正式声明，若下一次会议结束仍无声明则按不变档处理。不是全年累计加息幅度。", "https://polymarket.com/event/fed-decision-in-december-20260729232808632"] | [5.1499999999999995, {"status": "comparable", "change_pp": -3.8}] | {"spread": 0.0010000000000000009, "volume24h_usd": 297592.82797499996, "liquidity_usd": 437424.25449, "quality_flags": [], "retrieved_at": "2026-11-17T04:08:13.188609+00:00", "contract_end_at": "2026-12-09T23:59:00+00:00"} | ["官方日历确认12月8–9日FOMC；仅确认日期，本轮不猜公告时分", "利率与长久期估值"] | ["官方政策及融资/利率同步趋紧", "数据转弱与实际政策不符"] | [null, null] |
| ["Will the Fed increase interest rates by 25 bps after the December 2026 meeting?", "以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。", "https://polymarket.com/event/fed-decision-in-december-20260729232808632"] | [91.5, {"status": "comparable", "change_pp": 4.0000000000000036}] | {"spread": 0.010000000000000009, "volume24h_usd": 154415.233366, "liquidity_usd": 549682.1717, "quality_flags": [], "retrieved_at": "2026-11-17T04:08:13.188609+00:00", "contract_end_at": "2026-12-09T23:59:00+00:00"} | ["官方日历确认12月8–9日FOMC；仅确认日期，本轮不猜公告时分", "利率和估值"] | ["以正式目标区间变动匹配专门档位", "实际政策与对应档不符"] | [null, null] |
| ["SpaceX Starship fully reusable before 2027?", "2026年12月31日23:59ET之前SpaceX、Musk或正式代表宣布Starship上面级完全可复用即Yes；不要求Super Heavy可复用，也不要求已经实际复飞。捕获画面不自动替代正式声明及平台裁决。当前价差13个百分点，24h成交缺失，低质量。", "https://polymarket.com/event/spacex-starship-fully-reusable-before-2027"] | [30.5, {"status": "comparable", "change_pp": 0.5000000000000004}] | {"spread": 0.10999999999999999, "volume24h_usd": 40.6, "liquidity_usd": 2827.4556, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"], "retrieved_at": "2026-11-17T04:08:13.188609+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["30.5%，价差11pp、24h40.60美元，质量不足以支持高置信预测", "可能影响航天叙事；不能直接推导上市供应商利润或Tesla合并"] | ["结算须SpaceX/Musk正式宣布上面级完全可复用；投资判断另需工程/订单证据及后续相对强势，规则不要求实际复飞。", "公告不满足专门定义，或上市标的无业务受益且价格确认失败"] | [null, null] |
| ["Will Anthropic's market cap be less than $1.25T at market close on IPO day?", "按Anthropic IPO首个交易日正式收盘价乘在外股数确定市值；边界归入较高区间，以主要交易所正式上市页优先。缩短/中断日取正式收盘，若无则下一交易日正式收盘；至2027年12月31日23:59ET无IPO则No IPO档。当前档位分别小于1.25万亿、1.25万亿至小于1.5万亿美元；元数据截止并非上市日期。", "https://polymarket.com/event/anthropic-ipo-closing-market-cap-higher-strikes"] | [33.25, {"status": "comparable", "change_pp": 8.600000000000001}] | {"spread": 0.0010000000000000009, "volume24h_usd": 331125.439613, "liquidity_usd": 93773.79028, "quality_flags": [], "retrieved_at": "2026-11-17T04:08:13.188609+00:00", "contract_end_at": "2028-01-01T04:59:00+00:00"} | ["低于1.25万亿档33.25%，1.25–1.5万亿39.95%；需实际发行/交易核验，不等于完整估值分布", "AI融资风险偏好和关联企业承诺"] | ["正式上市及首日官方收盘/股份数，承诺按条件完成", "延期、未完成融资或首日规模不支持叙事"] | [null, null] |
| ["Will Anthropic's market cap be between $1.25T and $1.5T at market close on IPO day?", "按Anthropic IPO首个交易日正式收盘价乘在外股数确定市值；边界归入较高区间，以主要交易所正式上市页优先。缩短/中断日取正式收盘，若无则下一交易日正式收盘；至2027年12月31日23:59ET无IPO则No IPO档。当前档位分别小于1.25万亿、1.25万亿至小于1.5万亿美元；元数据截止并非上市日期。", "https://polymarket.com/event/anthropic-ipo-closing-market-cap-higher-strikes"] | [39.95, {"status": "comparable", "change_pp": -2.4499999999999966}] | {"spread": 0.0010000000000000009, "volume24h_usd": 93732.21923699998, "liquidity_usd": 49045.15179, "quality_flags": [], "retrieved_at": "2026-11-17T04:08:13.188609+00:00", "contract_end_at": "2028-01-01T04:59:00+00:00"} | ["低于1.25万亿档33.25%，1.25–1.5万亿39.95%；需实际发行/交易核验，不等于完整估值分布", "AI融资风险偏好和关联企业承诺"] | ["正式上市及首日官方收盘/股份数，承诺按条件完成", "延期、未完成融资或首日规模不支持叙事"] | [null, null] |

## Polymarket · 将要发生的事件及概率

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |

## 将要发生的事件及概率 · 本次无合格合约

本次未纳入合格合约，不代表相关风险或事件不存在。见搜索覆盖与限制。

## Will Anthropic's market cap be less than $1.25T at market close on IPO day?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 548858 / 2412744 |
| Yes 概率 % | 33.25 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [11.3, 15.25] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 8.600000000000001} |
| 24h成交量 / 流动性 USD | [331125.439613, 93773.79028] |
| 价差 pp | 0.10 |
| 到期 | 2028-01-01T04:59:00+00:00 |
| 结算规则摘要 | 按Anthropic IPO首个交易日正式收盘价乘在外股数确定市值；边界归入较高区间，以主要交易所正式上市页优先。缩短/中断日取正式收盘，若无则下一交易日正式收盘；至2027年12月31日23:59ET无IPO则No IPO档。当前档位分别小于1.25万亿、1.25万亿至小于1.5万亿美元；元数据截止并非上市日期。 |
| 规则指纹 | 33fa2aa35789c12e9a89f5398066c46fb0549dd1e70a1dbd7a8a329d96258d60 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-17T04:06:57.6983Z |
| 抓取时间 | 2026-11-17T04:08:13.188609+00:00 |
| 来源 | https://polymarket.com/event/anthropic-ipo-closing-market-cap-higher-strikes |

## Will the Fed increase interest rates by 50+ bps after the December 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 770450 / 3215009 |
| Yes 概率 % | 5.15 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-3.5, 4.6] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -3.8} |
| 24h成交量 / 流动性 USD | [297592.82797499996, 437424.25449] |
| 价差 pp | 0.10 |
| 到期 | 2026-12-09T23:59:00+00:00 |
| 结算规则摘要 | 衡量12月8–9日该次FOMC前后联邦基金目标区间上限上调至少50bp；非标准变化向上取整到最近25bp对应档。按正式声明，若下一次会议结束仍无声明则按不变档处理。不是全年累计加息幅度。 |
| 规则指纹 | a05ecc7aefe678e9936425027277135b8c37cdaf659af595020eb1668ec48e58 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-17T04:04:57.363799Z |
| 抓取时间 | 2026-11-17T04:08:13.188609+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-december-20260729232808632 |

## Will the Fed increase interest rates by 25 bps after the December 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 770450 / 3215008 |
| Yes 概率 % | 91.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [4.0, 12.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 4.0000000000000036} |
| 24h成交量 / 流动性 USD | [154415.233366, 549682.1717] |
| 价差 pp | 1.00 |
| 到期 | 2026-12-09T23:59:00+00:00 |
| 结算规则摘要 | 以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。 |
| 规则指纹 | 933a10a15eeec0ff1de30468fa20540301ed243f75cc3572d42946192f81a123 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-17T04:04:57.363799Z |
| 抓取时间 | 2026-11-17T04:08:13.188609+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-december-20260729232808632 |

## Will Anthropic's market cap be between $1.25T and $1.5T at market close on IPO day?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 548858 / 2412745 |
| Yes 概率 % | 39.95 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-4.2, 8.6] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -2.4499999999999966} |
| 24h成交量 / 流动性 USD | [93732.21923699998, 49045.15179] |
| 价差 pp | 0.10 |
| 到期 | 2028-01-01T04:59:00+00:00 |
| 结算规则摘要 | 按Anthropic IPO首个交易日正式收盘价乘在外股数确定市值；边界归入较高区间，以主要交易所正式上市页优先。缩短/中断日取正式收盘，若无则下一交易日正式收盘；至2027年12月31日23:59ET无IPO则No IPO档。当前档位分别小于1.25万亿、1.25万亿至小于1.5万亿美元；元数据截止并非上市日期。 |
| 规则指纹 | 615259a7206c78ca706da6d0de3e855413e1933333789449adf38e0aabdfed46 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-17T04:06:57.6983Z |
| 抓取时间 | 2026-11-17T04:08:13.188609+00:00 |
| 来源 | https://polymarket.com/event/anthropic-ipo-closing-market-cap-higher-strikes |

## Strait of Hormuz traffic returns to normal by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 455875 / 2176270 |
| Yes 概率 % | 4.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, -5.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [20984.675375, 259177.7465] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。 |
| 规则指纹 | b0c8ba27f4437b0d8ab819ae170bec118166232e39cdcaefb95bd352d29073d4 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-17T04:06:57.6983Z |
| 抓取时间 | 2026-11-17T04:08:13.188609+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31 |

## US x Iran Effective Ceasefire by November 22?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1337182 / 6831495 |
| Yes 概率 % | 72.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [16.0, 13.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 13.0} |
| 24h成交量 / 流动性 USD | [6519.000959, 65196.799] |
| 价差 pp | 3.00 |
| 到期 | 2026-11-22T20:29:00+00:00 |
| 结算规则摘要 | 须完成连续14个伊朗标准时间日，美国未实施合资格命中伊朗陆地及内水的空袭或地对地导弹行动，首日在创建后至11月22日范围内；最后合资格行动次日为首日，无行动则创建日。第14日后再留3个日历日报道窗口。拦截碎片、海域/领空、网络、地面入侵和部分小型袭击不算。不是双边全面停火；期限不同于15日档，首次基线。 |
| 规则指纹 | 78780fef798e8d3d9f3bb09d7cf3b6ef6c296271b6a12297a43b7d1800e94f75 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-17T04:06:57.6983Z |
| 抓取时间 | 2026-11-17T04:08:13.188609+00:00 |
| 来源 | https://polymarket.com/event/us-x-iran-effective-ceasefire-begins-by-2-week-pause-20261108 |

## Russia x Ukraine energy ceasefire agreement by November 30, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1360126 / 6947942 |
| Yes 概率 % | 4.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-1.0, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -1.0000000000000002} |
| 24h成交量 / 流动性 USD | [5995.942236, 154524.1629] |
| 价差 pp | 1.00 |
| 到期 | 2026-11-30T21:59:00+00:00 |
| 结算规则摘要 | 11月30日23:59基辅时间前，双方同意相互暂停至少一类明确能源设施打击；双方官宣或可信报道共识确认。第三方单方声称、谈判或单一设施暂停不算。正式协议可先于实际生效；不同于15日截止档，首次基线。 |
| 规则指纹 | 4d97d360ed855920071504ae11e5ea8f81585c041447e5901a083ae049db5223 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-17T04:06:57.6983Z |
| 抓取时间 | 2026-11-17T04:08:13.188609+00:00 |
| 来源 | https://polymarket.com/event/russia-x-ukraine-energy-ceasefire-agreement-by |

## Tesla and SpaceX merger officially announced by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 192962 / 2252540 |
| Yes 概率 % | 27.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, 18.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [5755.974306999999, 19138.852] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59纽约时间前，Tesla或SpaceX正式宣布双方合并或一方收购另一方的控制权即Yes；无需在期限内完成交易。控制权通常为过半权益或等效治理权；少数股权投资及仅讨论不算。以公司公告或可信报道共识核验；旧URL中的june-30不是本合约期限。 |
| 规则指纹 | 909906ae3b6db7e473468713ea6a1e1e4cf4c931fe247c7d3d576e7986513008 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-17T04:06:57.6983Z |
| 抓取时间 | 2026-11-17T04:08:13.188609+00:00 |
| 来源 | https://polymarket.com/event/tesla-and-spacex-merger-officially-announced-by-june-30 |

## Will WTI Crude Oil (WTI) hit (HIGH) $110 in November?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1250301 / 6172751 |
| Yes 概率 % | 2.75 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.9, -6.75] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -1.4000000000000001} |
| 24h成交量 / 流动性 USD | [5473.038371, 38078.48155] |
| 价差 pp | 0.90 |
| 到期 | 2026-12-01T04:59:59.999000+00:00 |
| 结算规则摘要 | 11月规定Pyth时段内，ICE Europe WTI活跃月CLL最终1分钟High达到110美元即Yes，不取整，末三个交易日换月。仅因系统/数据故障无法核验时使用ICE官方日高低；正常Pyth收市不属于故障，不计该时段后价格。结构变动依Pyth调整价。规则与11月14日建立的新基线一致，不跨此前规则变更比较；Yahoo连续WTI不能直接裁决。 |
| 规则指纹 | 33ad0c642348432662de13f0d7c28f03c826ab7031226c102e452236917b6b7c |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-17T04:06:57.6983Z |
| 抓取时间 | 2026-11-17T04:08:13.188609+00:00 |
| 来源 | https://polymarket.com/event/what-price-will-wti-hit-in-november-2026 |

## New NVIDIA CEO named by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1367877 / 6977205 |
| Yes 概率 % | 20.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [4647.183337, 83430.6989] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59纽约时间前，英伟达正式宣布黄仁勋的CEO继任者即满足；实际就任可以更晚，临时CEO不计。以公司公开声明为主要来源，可参照可信报道共识。与离任宣布合约不同。 |
| 规则指纹 | 09c6c6ee9faa8f03a8b6caf37ffb4757f33e53eedba525eae02360d329bf2d68 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-17T04:06:57.6983Z |
| 抓取时间 | 2026-11-17T04:08:13.188609+00:00 |
| 来源 | https://polymarket.com/event/new-nvidia-ceo-named-by-december-31-2026 |

## AI bubble burst by June 30, 2027?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 4838928 |
| Yes 概率 % | 18.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, -4.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [4185.652106, 94675.2613] |
| 价差 pp | 2.00 |
| 到期 | 2027-07-01T03:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | bd0420587e08487fffa5050e7fd9b79ffff909a9f843d3f620207ee859462505 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-17T04:04:57.363799Z |
| 抓取时间 | 2026-11-17T04:08:13.188609+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## AI bubble burst in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 691340 |
| Yes 概率 % | 7.75 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [0.3, 0.6] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.050000000000000044} |
| 24h成交量 / 流动性 USD | [4102.681727, 190014.09858] |
| 价差 pp | 0.10 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | fc153b2136a8dfbadcd169dce1add40690acb1748566b99716fe7ae8fcb07330 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-17T04:04:57.363799Z |
| 抓取时间 | 2026-11-17T04:08:13.188609+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## Russia x Ukraine ceasefire agreement by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 478472 / 2243897 |
| Yes 概率 % | 11.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, -3.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [1232.156294, 104896.4191] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年末23:59ET前，双方官宣或可信共识确认相互暂停直接交战，包含明确生效日的全面暂停；仅限定目标/地点的局部能源安排不算。达成协议可先于实际生效，单方暂停不算。 |
| 规则指纹 | 2ea22f9548269db3205e41396a99073a2d5788dc4fde17989e34c8051ae6b75b |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-17T04:06:57.6983Z |
| 抓取时间 | 2026-11-17T04:08:13.188609+00:00 |
| 来源 | https://polymarket.com/event/russia-x-ukraine-ceasefire-agreement-by |

## SpaceX Starship fully reusable before 2027?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 79056 / 676812 |
| Yes 概率 % | 30.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [0.5, 1.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.5000000000000004} |
| 24h成交量 / 流动性 USD | [40.6, 2827.4556] |
| 价差 pp | 11.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59ET之前SpaceX、Musk或正式代表宣布Starship上面级完全可复用即Yes；不要求Super Heavy可复用，也不要求已经实际复飞。捕获画面不自动替代正式声明及平台裁决。当前价差13个百分点，24h成交缺失，低质量。 |
| 规则指纹 | f9fb2d12d212bf90423007fe92524df34a8bd934a8f723520205802b8ad8d31a |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"] |
| 元数据更新（不是成交时间） | 2026-11-17T04:06:57.6983Z |
| 抓取时间 | 2026-11-17T04:08:13.188609+00:00 |
| 来源 | https://polymarket.com/event/spacex-starship-fully-reusable-before-2027 |

## CoreWeave downgraded by Moody's or S&P by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1219851 / 5939467 |
| Yes 概率 % | 25.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [5.5, 7.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -2.500000000000002} |
| 24h成交量 / 流动性 USD | [50.106663999999995, 437.2914] |
| 价差 pp | 4.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59ET前，Moody’s或S&P正式下调CoreWeave长期主体/企业家族或高级无担保债信用评级则Yes；仅负面展望/观察名单不算，不要求降至某统一评级档。成交很薄，不视为客观违约概率。 |
| 规则指纹 | 040e522db15913bd31de0e1a7f935727361429e7c42b3c1fc5286a0cf1b0fc42 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-17T04:06:57.6983Z |
| 抓取时间 | 2026-11-17T04:07:31.020247+00:00 |
| 来源 | https://polymarket.com/event/coreweave-downgraded-by-moodys-or-sp-by |

## AI 压力：合约、经营与估值分开

三层分开。第一层：AI泡沫2026年内合约7.75%、2027年6月档18%，按专门多条件与90日窗口结算，不是行业崩盘客观概率。CoreWeave降级合约25%，价差4pp、24h仅50.11美元，变化−2.5pp不足证明信用改善。H100日期表16日3.08美元/GPU小时，15日3.10，远高于合约连续5天≤1美元阈值；网页7日涨幅标题与日期表不一致，仅采日期表，未完成其他历史触发条件全审计。
第二层：[BIS新公告](https://www.bis.gov/press-release/bis-issues-rule-addressing-remote-access-american-super-intelligence-technology)及[规则展示稿](https://www.bis.gov/media/documents/rin-0694-ak50.pdf)涉及海外数据中心向特定受限主体远程供应算力，增加尽调要求。展示稿生效日仍是联邦公报发表日占位，不能声称全部条款已即时生效，也不能量化未经披露的收入损失。[Warsh官方讲话](https://www.federalreserve.gov/newsevents/speech/warsh20261116a.htm)列出生产率普惠、就业替代、投资回报失望三类情景，最后一种可能导致估值与就业下行；他明确这些是情景，不是预测或利率决定。NVDA−4.12%、CRWV−6.12%、MU−7.62%，显示风险溢价压力；政策影响、融资承诺与真实客户现金流须分别核验。
第三层：本轮SEC定期披露检查五家全部成功，最新财报日期仍NVDA8月26日、MSFT10月28日、AMZN10月30日、GOOGL10月29日、META10月22日。复用已核验底稿，以16日完整收盘更新公司整体五年FCFF情景和反推；没有把尚未发布的17日NVDA结果写成最新基本面。只有NVDA关键输入完整，其余四家保留无估值结论。WACC/终值/稀释均为模型假设，不给情景权重解释为概率，不把整体估值都归因AI。
[Anthropic SEC指示日程](https://www.sec.gov/Archives/edgar/data/2130357/000162828026073040/anthropicpbc-fwpxeeaprospea.htm)仍为预计18日定价、19日交易，可调整；低于1.25万亿首日市值档由24.65%升至33.25%，1.25–1.5万亿由42.4%降至39.95%。这表明这些分档报价变化，不能据两个分档推导整个分布或长期价值；私募承诺不等于到账。

## NVDA · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | scenario_analysis |
| 财务底稿 | TTM 至 2026-07-26；最新 10-Q / filed 2026-08-26 |
| 披露检查 | {"checked_at": "2026-11-17T04:09:49.178142+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001045810.json", "latest_filing_date": "2026-08-26"} |
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
| 披露检查 | {"checked_at": "2026-11-17T04:09:51.161475+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0000789019.json", "latest_filing_date": "2026-10-28"} |
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
| 披露检查 | {"checked_at": "2026-11-17T04:09:53.594072+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001018724.json", "latest_filing_date": "2026-10-30"} |
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
| 披露检查 | {"checked_at": "2026-11-17T04:09:55.982814+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001652044.json", "latest_filing_date": "2026-10-29"} |
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
| 披露检查 | {"checked_at": "2026-11-17T04:09:58.016577+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001326801.json", "latest_filing_date": "2026-10-22"} |
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
| 反证 | 仍可能出现空头回补；没有本轮分钟数据证明常规VWAP或回踩。 |
| 状态 | 昨晚747.89/671.71失效条件已收盘触发；升级条件未满足 |

## 芯片：等待经营证据与板块修复

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | NVDA17日财报、政策影响和现金回收披露 |
| 关联标的 | ["SMH", "NVDA", "MU"] |
| 确认条件 | SMH收复16日高473.33并回踩守稳；NVDA先158.39再163.20，MU先739.12再750.25；相对SPY转强、更多芯片同行跟随，财报后次日收盘承接才升级。 |
| 失效条件 | SMH460.64、NVDA155.01、MU716.38再失且反抽失败；或明确订单/回款/融资恶化。 |
| 观察期限 | 11月17–20日；财报后按实际新信息复核 |
| 反证 | H100价格高不等于股票见底；财报跳空可越过止损，杠杆ETF每日重置存在路径损耗。 |
| 状态 | 旧支撑已失守，保留观察，不以跌多或单根阳线建仓 |

## 防御与金融：优先观察但不追涨

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 相对强势能否转化为绝对上涨 |
| 关联标的 | ["XLP", "XLV", "XLF", "XLU"] |
| 确认条件 | XLP92.38、XLV187.60、XLF57.89是16日低点参考；回踩守住后再突破各自16日高93.48/191.33/58.81，且收盘维持相对领先。支撑不是保证，按实际波动修订。 |
| 失效条件 | 关键低点破位且无法收复、相对强度反转；金融另看信用扩散。 |
| 观察期限 | 11月17–20日；财报后按实际新信息复核 |
| 反证 | XLP收盘低于开盘，XLV/XLF仍下跌；相对抗跌不自动成为买点。 |
| 状态 | 观察优先级高于芯片；不等于确定净流入 |

## 能源：等待油价和价格同步

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 真实航运、供给及需求变化 |
| 关联标的 | ["XLE", "XOP", "OIH"] |
| 确认条件 | XLE/XOP/OIH先收复20日65.96/189.80/381.60并回踩守稳，油价与企业盈利预期同向支持。 |
| 失效条件 | 油价继续弱、突破失败或供给改善兑现。 |
| 观察期限 | 11月17–20日；财报后按实际新信息复核 |
| 反证 | 地缘风险高也可能伴随能源股下跌，不能用新闻单向定价。 |
| 状态 | 当前未确认 |

## 工业与航天：保留次级观察

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 官方工程与企业订单披露 |
| 关联标的 | ["XLI", "ARKX", "ITA"] |
| 确认条件 | XLI先收20日167.77、ARKX29.70、ITA70.16并保持相对SPY改善；航天还需实际订单映射。 |
| 失效条件 | 重新跌破修复区且反抽失败，或工程/订单归因不成立。 |
| 观察期限 | 11月17–20日；财报后按实际新信息复核 |
| 反证 | Starship合约价差11pp且24h40.60美元；不据此推导上市篮子上涨。 |
| 状态 | 当前未确认 |

## 跨期比较与上期剧本复核

与16日20:00晚报相比：现在新增16日完整收盘，不再只用盘前警报。SPY747.89、QQQ671.71、SMH473.26、NVDA158.39、MU750.25均收盘失守；修复确认失败。日线能确认破位收盘，不能重建分钟反抽顺序或VWAP。XLP/XLU绝对微涨，XLV/XLF相对抗跌但未全面承接。利率从13日到16日回落，新GPR数据更新；CNN由可核验旧值转为本轮缺失。以下15份合约均同ID、同rule_hash：Strait of Hormuz traffic returns to normal by December 31?：4.5%（较昨晚+0.00pp）；Will the Fed increase interest rates by 25 bps after the December 2026 meeting?：91.5%（较昨晚+4.00pp）；AI bubble burst in 2026?：7.75%（较昨晚+0.05pp）；AI bubble burst by June 30, 2027?：18%（较昨晚+0.00pp）；Tesla and SpaceX merger officially announced by December 31?：27.5%（较昨晚+0.00pp）；Will the Fed increase interest rates by 50+ bps after the December 2026 meeting?：5.15%（较昨晚-3.80pp）；CoreWeave downgraded by Moody's or S&P by December 31, 2026?：25%（较昨晚-2.50pp）；Russia x Ukraine ceasefire agreement by December 31, 2026?：11.5%（较昨晚+0.00pp）；New NVIDIA CEO named by December 31, 2026?：20.5%（较昨晚+0.00pp）；Will WTI Crude Oil (WTI) hit (HIGH) $110 in November?：2.75%（较昨晚-1.40pp）；SpaceX Starship fully reusable before 2027?：30.5%（较昨晚+0.50pp）；Will Anthropic's market cap be less than $1.25T at market close on IPO day?：33.25%（较昨晚+8.60pp）；Will Anthropic's market cap be between $1.25T and $1.5T at market close on IPO day?：39.95%（较昨晚-2.45pp）；US x Iran Effective Ceasefire by November 22?：72.5%（较昨晚+13.00pp）；Russia x Ukraine energy ceasefire agreement by November 30, 2026?：4.5%（较昨晚-1.00pp）。CRWV及Starship薄盘口变化低置信；伊朗22日72.5%是专门规则价格，不与已过15日档拼接。

## 可计算的跨期变化

```json
[
  {
    "mode": "daily",
    "baseline": "reports/daily/2026-11-13/20261116T120823.536214Z/evidence.json",
    "baseline_cutoff": "2026-11-16T12:07:57.618352+00:00",
    "close_change_pct": {
      "SPY": -1.9115265723043784,
      "QQQ": -2.6680807568290943,
      "IWM": -1.6574208985696837,
      "RSP": -1.0083247193896638,
      "GLD": -0.7089659430880024,
      "GC=F": -0.34222907806965575,
      "CL=F": -4.065039039481944,
      "BZ=F": -4.434474292983404,
      "TLT": 0.0,
      "UUP": 0.20338802014367996,
      "HYG": -0.27293875462582884,
      "LQD": -0.009721337489809745,
      "^VIX": 18.704667114284177,
      "^VIX3M": 11.639182933318937,
      "^VVIX": 12.508622801467407,
      "^MOVE": 2.5229285352249997,
      "NVDA": -4.120360124274091,
      "MSFT": -1.1243060612239009,
      "AMZN": -3.3413348607762794,
      "GOOGL": -4.074107664930038,
      "META": -2.3812166682883995,
      "CRWV": -6.117071211486225,
      "MU": -7.617784457777088,
      "DRAM": -7.382077725173741,
      "VRT": -6.631369658819919,
      "XLK": -3.2417220531082536,
      "XLE": -1.9550499933231102,
      "XLF": -0.8520790685065838,
      "XLI": -1.8485573763200036,
      "XLV": -0.513635789967315,
      "XLP": 0.270709262729496,
      "XLY": -1.5252556924927996,
      "XLC": -1.7204919537932017,
      "XLU": 0.1816485347283736,
      "XLRE": -0.2704506080087654,
      "XLB": -1.455099230699064,
      "SMH": -5.1052914439682855,
      "IGV": -2.1642478392807307,
      "XOP": -2.608229028475062,
      "OIH": -3.837031983203021,
      "ITA": -2.461197152361383,
      "ARKX": -4.004107131375656,
      "KRE": -0.7561114084624232,
      "SKYY": -2.1047744873758045
    },
    "quote_change_pct": {},
    "macro_change": {
      "DGS2": {
        "change": 0.019999999999999574,
        "unit": "percent",
        "observation_date": "2026-11-13"
      },
      "BAMLH0A0HYM2": {
        "change": 0.029999999999999805,
        "unit": "percentage_points",
        "observation_date": "2026-11-13"
      },
      "BAMLC0A0CM": {
        "change": 0.0,
        "unit": "percentage_points",
        "observation_date": "2026-11-13"
      },
      "DGS10": {
        "change": 0.05000000000000071,
        "unit": "percent",
        "observation_date": "2026-11-13"
      },
      "DFII10": {
        "change": 0.050000000000000266,
        "unit": "percent",
        "observation_date": "2026-11-13"
      },
      "T10YIE": {
        "change": -0.040000000000000036,
        "unit": "percent",
        "observation_date": "2026-11-16"
      },
      "STLFSI4": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-11-06"
      },
      "CBOE_VIX": {
        "change": 3.6099999999999994,
        "unit": "index",
        "observation_date": "2026-11-16"
      },
      "GPRD": {
        "change": 75.60165405273438,
        "unit": "index",
        "observation_date": "2026-11-16"
      },
      "GPRD_ACT": {
        "change": 86.13592529296875,
        "unit": "index",
        "observation_date": "2026-11-16"
      },
      "GPRD_THREAT": {
        "change": 86.85680389404297,
        "unit": "index",
        "observation_date": "2026-11-16"
      },
      "GPRD_MA7": {
        "change": -13.762054443359375,
        "unit": "index",
        "observation_date": "2026-11-16"
      },
      "GPRD_MA30": {
        "change": -33.277984619140625,
        "unit": "index",
        "observation_date": "2026-11-16"
      }
    },
    "event_probability_change": {
      "2412744": {
        "status": "comparable",
        "change_pp": 8.600000000000001
      },
      "3215009": {
        "status": "comparable",
        "change_pp": -3.8
      },
      "3215008": {
        "status": "comparable",
        "change_pp": 4.0000000000000036
      },
      "2412745": {
        "status": "comparable",
        "change_pp": -2.4499999999999966
      },
      "2176270": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "6831495": {
        "status": "comparable",
        "change_pp": 13.0
      },
      "6947942": {
        "status": "comparable",
        "change_pp": -1.0000000000000002
      },
      "2252540": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "6172751": {
        "status": "comparable",
        "change_pp": -1.4000000000000001
      },
      "6977205": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "4838928": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "691340": {
        "status": "comparable",
        "change_pp": 0.050000000000000044
      },
      "2243897": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "676812": {
        "status": "comparable",
        "change_pp": 0.5000000000000004
      },
      "5939467": {
        "status": "comparable",
        "change_pp": -2.500000000000002
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

## 覆盖范围与数据缺口

```json
[
  "本次晨报恢复后延至北京时间中午采集；未伪造07:15生成或已知信息。",
  "tc五个授权工具当前未加载，不能刷新tc日历/市场概览/新闻；使用显式标源的NYSE日历、Yahoo/Cboe及公开来源。",
  "CNN新值缺失，未使用tc温度或加密货币指数替代。",
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
  "Polymarket 查询 ceasefire 达到页数上限，存在遗漏",
  "Polymarket 查询 inflation 达到页数上限，存在遗漏",
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
  "polymarket.query.ceasefire: truncated",
  "polymarket.query.inflation: truncated",
  "cnn: missing",
  "request.38906ddc2d63: request_failed",
  "Polymarket 临近事件：本次未纳入合格合约，见搜索说明",
  "指标缺失/历史不足: prices.^VIX.volume_vs_previous20_ratio, prices.^VIX3M.volume_vs_previous20_ratio, prices.^VVIX.volume_vs_previous20_ratio, prices.^MOVE.volume_vs_previous20_ratio, prices.DRAM.sma200, prices.DRAM.distance_sma200_pct"
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
    "url": "https://data.sec.gov/submissions/CIK0001045810.json",
    "checked_at": "2026-11-17T04:09:49.178142+00:00",
    "note": "SEC最新定期披露检查成功；不等于FCFF输入完整。"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0000789019.json",
    "checked_at": "2026-11-17T04:09:51.161475+00:00",
    "note": "SEC最新定期披露检查成功；不等于FCFF输入完整。"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0001018724.json",
    "checked_at": "2026-11-17T04:09:53.594072+00:00",
    "note": "SEC最新定期披露检查成功；不等于FCFF输入完整。"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0001652044.json",
    "checked_at": "2026-11-17T04:09:55.982814+00:00",
    "note": "SEC最新定期披露检查成功；不等于FCFF输入完整。"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0001326801.json",
    "checked_at": "2026-11-17T04:09:58.016577+00:00",
    "note": "SEC最新定期披露检查成功；不等于FCFF输入完整。"
  }
]
```

## 付费信源建议（未订阅）

```json
[]
```
