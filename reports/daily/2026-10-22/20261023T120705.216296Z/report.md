# 每日交易总结 · 2026-10-22

## 一分钟读懂 · Agent 摘要

### 当前判断

盘前只是分化修复，反弹仍脆弱；科技估值压力尚在，新增警惕偏向能源与通胀。

### 与上次相比

较早报，WDC和BE收复部分盘后跌幅，但仍低于昨日收盘；油价触105美元合约由38%升至53%，AI严重下行专门合约由9.45%降至8.9%，并非所有风险都在同向升温。

### 最重要的信号

- 约纽约08:02，SPY−0.24%、QQQ−0.06%、SMH+0.55%；META−0.48%，WDC−2.59%、BE−3.42%。均相对昨日常规收盘。
- VIX盘前约19.54；昨日同日VIX19.03低于VIX3M20.12，尚无完整系统性恐慌证据。
- H100租金仍为22日2.88美元/小时；需求尚强与股票估值下修可以同时发生。

### 接下来观察

- 21:30北京开盘后，QQQ/SMH先守701.90/520.53，再看常规VWAP回踩、相对SPY及参与面；未满足前仅观察。
- 22:00北京发布密歇根终值：重点是通胀预期与债券/成长股反应。PMI日程仍有一级来源核验缺口。
- 若油价风险和信用压力同步上升、反抽破前低，继续以降低方向风险为先；若回踩守住并持续收复均线，才逐级提高反弹可信度。

### 不要忽略

CNN、当前板块净申赎缺失，信用截至21日；Brent不同来源不一致，未据此判断涨跌。盘前不是已完成的反转。

## 研究结论

北京时间10月23日晚间：仍是科技估值降温与结构性避险，盘前半导体仅小幅修复，尚未确认可靠反弹。相较早报更显著的是油价触及高位的合约预期上升，而AI严重下行合约回落；两条风险线应分开。今晚先验证开盘承接，再观察消费者通胀预期，避免把第一波反抽当趋势反转。

## 时点与口径

| 项目 | 内容 |
| --- | --- |
| 模式 | 每日交易总结 |
| 常规交易窗口 | 2026-10-22 → 2026-10-22（纽约交易日） |
| 截止·纽约 | 2026-10-23T08:07:01.886830-04:00 |
| 截止·北京 | 2026-10-23T20:07:01.886830+08:00 |
| 实际生成时间 | 2026-10-23T12:07:01.971675+00:00 |
| 市场阶段 | 盘前 |
| 下一交易日 | 2026-10-23 |
| 运行重点 | 全市场 |
| 上一版本 | reports/daily/2026-10-22/20261022T232116.893782Z/evidence.json |
| 质量 | partial |
| Daily 北京时间计划时段 | 2026-10-23T20:00:00+08:00 |

## 采集、补查与剩余缺口

| 目标 | 补查结果 | 来源 | 观测 / 抓取时间 | 说明 |
| --- | --- | --- | --- | --- |

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
| prices.SPY.value | 763.96 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_1d_pct | -1.18 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_5d_pct | -1.01 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_20d_pct | -0.42 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_60d_pct | 4.99 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_1d_pp | 0.00 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_5d_pp | 0.00 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_20d_pp | 0.00 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_60d_pp | 0.00 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma20 | 770.72 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma50 | 767.22 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma200 | 723.62 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma20_pct | -0.88 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma50_pct | -0.42 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma200_pct | 5.57 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_sma | 7.30 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_pct | 0.96 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.drawdown_from_63d_high_pct | -1.94 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.volume_vs_previous20_ratio | 1.34 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SPY/history/ |
| prices.QQQ.value | 704.47 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_1d_pct | -2.86 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_5d_pct | -3.23 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_20d_pct | -4.94 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_60d_pct | 6.57 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_1d_pp | -1.68 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_5d_pp | -2.22 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_20d_pp | -4.52 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_60d_pp | 1.58 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma20 | 737.24 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma50 | 725.98 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma200 | 675.69 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma20_pct | -4.44 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma50_pct | -2.96 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma200_pct | 4.26 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_sma | 12.04 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_pct | 1.71 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.drawdown_from_63d_high_pct | -7.27 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.volume_vs_previous20_ratio | 1.83 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.IWM.value | 276.67 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_1d_pct | 0.07 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_5d_pct | 0.58 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_20d_pct | -1.77 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_60d_pct | -3.87 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_1d_pp | 1.25 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_5d_pp | 1.59 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_20d_pp | -1.35 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_60d_pp | -8.86 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma20 | 277.50 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma50 | 286.63 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma200 | 277.06 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma20_pct | -0.30 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma50_pct | -3.47 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma200_pct | -0.14 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_sma | 3.75 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_pct | 1.36 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.drawdown_from_63d_high_pct | -9.08 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.volume_vs_previous20_ratio | 1.00 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IWM/history/ |
| prices.RSP.value | 218.22 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_1d_pct | 0.73 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_5d_pct | 1.50 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_20d_pct | 3.79 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_60d_pct | 1.53 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_1d_pp | 1.91 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_5d_pp | 2.51 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_20d_pp | 4.21 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_60d_pp | -3.46 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma20 | 212.39 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma50 | 215.05 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma200 | 205.83 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma20_pct | 2.74 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma50_pct | 1.47 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma200_pct | 6.02 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_sma | 2.08 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_pct | 0.95 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.drawdown_from_63d_high_pct | -1.67 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.volume_vs_previous20_ratio | 1.60 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/RSP/history/ |
| prices.GLD.value | 369.00 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_1d_pct | -2.63 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_5d_pct | -3.58 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_20d_pct | -5.79 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_60d_pct | -0.56 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_1d_pp | -1.44 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_5d_pp | -2.57 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_20d_pp | -5.37 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_60d_pp | -5.55 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma20 | 380.43 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma50 | 395.15 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma200 | 414.42 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma20_pct | -3.01 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma50_pct | -6.62 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma200_pct | -10.96 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_sma | 5.18 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_pct | 1.40 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.drawdown_from_63d_high_pct | -13.80 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.volume_vs_previous20_ratio | 2.23 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GC=F.value | 4,060.40 | USD_per_troy_ounce | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_1d_pct | -2.16 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_5d_pct | -2.63 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_20d_pct | -5.53 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_60d_pct | 0.60 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_1d_pp | -0.98 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_5d_pp | -1.62 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_20d_pp | -5.11 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_60d_pp | -4.39 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma20 | 4,170.93 | USD_per_troy_ounce | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma50 | 4,350.12 | USD_per_troy_ounce | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma200 | 4,535.17 | USD_per_troy_ounce | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma20_pct | -2.65 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma50_pct | -6.66 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma200_pct | -10.47 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_sma | 70.26 | USD_per_troy_ounce | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_pct | 1.73 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.drawdown_from_63d_high_pct | -13.57 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.volume_vs_previous20_ratio | 1.01 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.CL=F.value | 99.47 | USD_per_barrel | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_1d_pct | 2.39 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_5d_pct | 1.53 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_20d_pct | 5.14 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_60d_pct | 17.77 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_1d_pp | 3.57 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_5d_pp | 2.55 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_20d_pp | 5.56 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_60d_pp | 12.78 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma20 | 94.19 | USD_per_barrel | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma50 | 92.49 | USD_per_barrel | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma200 | 85.05 | USD_per_barrel | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma20_pct | 5.61 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma50_pct | 7.55 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma200_pct | 16.95 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_sma | 4.24 | USD_per_barrel | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_pct | 4.27 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.drawdown_from_63d_high_pct | -6.01 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.volume_vs_previous20_ratio | 1.17 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.BZ=F.value | 113.17 | USD_per_barrel | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_1d_pct | 4.00 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_5d_pct | 6.84 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_20d_pct | 6.16 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_60d_pct | 24.72 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_1d_pp | 5.18 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_5d_pp | 7.86 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_20d_pp | 6.58 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_60d_pp | 19.73 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma20 | 105.24 | USD_per_barrel | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma50 | 100.24 | USD_per_barrel | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma200 | 90.89 | USD_per_barrel | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma20_pct | 7.53 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma50_pct | 12.90 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma200_pct | 24.51 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_sma | 3.92 | USD_per_barrel | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_pct | 3.46 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.drawdown_from_63d_high_pct | 0.00 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.volume_vs_previous20_ratio | 1.02 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.TLT.value | 81.74 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_1d_pct | 1.87 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_5d_pct | 2.21 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_20d_pct | 3.34 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_60d_pct | -0.16 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_1d_pp | 3.05 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_5d_pp | 3.23 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_20d_pp | 3.76 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_60d_pp | -5.15 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma20 | 78.61 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma50 | 80.28 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma200 | 83.33 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma20_pct | 3.98 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma50_pct | 1.82 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma200_pct | -1.90 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_sma | 0.85 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_pct | 1.04 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.drawdown_from_63d_high_pct | -1.81 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.volume_vs_previous20_ratio | 1.30 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/TLT/history/ |
| prices.UUP.value | 28.90 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_1d_pct | -0.07 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_5d_pct | -0.34 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_20d_pct | 0.73 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_60d_pct | 1.69 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_1d_pp | 1.11 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_5d_pp | 0.67 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_20d_pp | 1.15 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_60d_pp | -3.30 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma20 | 28.93 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma50 | 28.47 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma200 | 27.87 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma20_pct | -0.09 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma50_pct | 1.52 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma200_pct | 3.68 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_sma | 0.13 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_pct | 0.44 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.drawdown_from_63d_high_pct | -0.79 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.volume_vs_previous20_ratio | 1.02 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/UUP/history/ |
| prices.HYG.value | 77.10 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_1d_pct | 0.16 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_5d_pct | -0.04 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_20d_pct | -0.57 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_60d_pct | -1.26 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_1d_pp | 1.34 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_5d_pp | 0.98 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_20d_pp | -0.15 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_60d_pp | -6.24 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma20 | 77.06 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma50 | 77.99 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma200 | 77.89 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma20_pct | 0.06 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma50_pct | -1.14 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma200_pct | -1.02 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_sma | 0.28 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_pct | 0.37 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.drawdown_from_63d_high_pct | -2.57 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.volume_vs_previous20_ratio | 0.72 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/HYG/history/ |
| prices.LQD.value | 104.28 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_1d_pct | 1.04 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_5d_pct | 0.75 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_20d_pct | 1.53 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_60d_pct | -0.56 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_1d_pp | 2.22 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_5d_pp | 1.77 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_20d_pp | 1.95 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_60d_pp | -5.55 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma20 | 102.58 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma50 | 103.91 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma200 | 105.93 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma20_pct | 1.66 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma50_pct | 0.36 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma200_pct | -1.55 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_sma | 0.64 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_pct | 0.61 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.drawdown_from_63d_high_pct | -1.58 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.volume_vs_previous20_ratio | 1.22 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/LQD/history/ |
| prices.^VIX.value | 19.03 | index | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_1d_pct | 14.09 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_5d_pct | 15.61 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_20d_pct | 21.44 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_60d_pct | 11.35 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_1d_pp | 15.27 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_5d_pp | 16.63 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_20d_pp | 21.86 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_60d_pp | 8.09 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma20 | 16.31 | index | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma50 | 15.83 | index | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma200 | 18.18 | index | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma20_pct | 16.70 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma50_pct | 20.21 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma200_pct | 4.65 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_sma | 1.84 | index | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_pct | 9.67 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.drawdown_from_63d_high_pct | -7.89 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-22 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX3M.value | 20.12 | index | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_1d_pct | 7.48 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_5d_pct | 8.82 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_20d_pct | 9.17 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_60d_pct | -6.42 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_1d_pp | 8.66 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_5d_pp | 9.83 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_20d_pp | 9.59 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_60d_pp | -11.41 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma20 | 18.48 | index | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma50 | 18.45 | index | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma200 | 20.47 | index | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma20_pct | 8.90 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma50_pct | 9.06 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma200_pct | -1.70 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_sma | 1.03 | index | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_pct | 5.09 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.drawdown_from_63d_high_pct | -6.42 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-22 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VVIX.value | 107.94 | index | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_1d_pct | 14.16 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_5d_pct | 16.60 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_20d_pct | 19.18 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_60d_pct | -1.40 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_1d_pp | 15.34 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_5d_pp | 17.62 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_20d_pp | 19.60 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_60d_pp | -6.39 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma20 | 91.78 | index | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma50 | 90.17 | index | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma200 | 98.59 | index | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma20_pct | 17.60 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma50_pct | 19.70 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma200_pct | 9.48 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_sma | 9.13 | index | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_pct | 8.46 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.drawdown_from_63d_high_pct | -1.79 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-22 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^MOVE.value | 106.84 | index | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_1d_pct | 11.36 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_5d_pct | 4.24 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_20d_pct | 11.93 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_60d_pct | 40.41 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_1d_pp | 12.54 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_5d_pp | 5.26 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_20d_pp | 12.43 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_60d_pp | 37.04 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma20 | 103.25 | index | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma50 | 87.17 | index | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma200 | 76.50 | index | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma20_pct | 3.48 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma50_pct | 22.56 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma200_pct | 39.65 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_sma | 5.59 | index | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_pct | 5.23 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.drawdown_from_63d_high_pct | -5.95 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-22 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.NVDA.value | 212.21 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_1d_pct | -4.40 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_5d_pct | -2.31 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_20d_pct | -5.51 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_60d_pct | 11.81 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_1d_pp | -3.22 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_5d_pp | -1.30 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_20d_pp | -5.09 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_60d_pp | 6.82 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma20 | 226.25 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma50 | 222.68 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma200 | 203.25 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma20_pct | -6.20 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma50_pct | -4.70 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma200_pct | 4.41 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_sma | 6.15 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_pct | 2.90 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.drawdown_from_63d_high_pct | -11.30 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.volume_vs_previous20_ratio | 1.21 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.MSFT.value | 521.08 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_1d_pct | -2.23 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_5d_pct | -3.40 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_20d_pct | 4.65 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_60d_pct | 33.68 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_1d_pp | -1.05 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_5d_pp | -2.39 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_20d_pp | 5.07 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_60d_pp | 28.69 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma20 | 526.29 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma50 | 507.78 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma200 | 435.15 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma20_pct | -0.99 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma50_pct | 2.62 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma200_pct | 19.75 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_sma | 11.38 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_pct | 2.18 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.drawdown_from_63d_high_pct | -4.12 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.volume_vs_previous20_ratio | 1.00 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.AMZN.value | 250.38 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_1d_pct | -4.57 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_5d_pct | -1.72 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_20d_pct | 0.40 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_60d_pct | 10.47 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_1d_pp | -3.39 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_5d_pp | -0.70 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_20d_pp | 0.82 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_60d_pp | 5.48 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma20 | 254.51 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma50 | 255.99 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma200 | 243.26 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma20_pct | -1.62 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma50_pct | -2.19 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma200_pct | 2.93 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_sma | 7.11 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_pct | 2.84 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.drawdown_from_63d_high_pct | -11.84 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.volume_vs_previous20_ratio | 1.37 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.GOOGL.value | 324.22 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_1d_pct | -3.15 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_5d_pct | -7.16 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_20d_pct | -5.30 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_60d_pct | -3.65 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_1d_pp | -1.97 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_5d_pp | -6.14 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_20d_pp | -4.88 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_60d_pp | -8.64 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma20 | 344.27 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma50 | 343.40 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma200 | 340.99 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma20_pct | -5.82 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma50_pct | -5.58 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma200_pct | -4.92 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_sma | 8.48 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_pct | 2.62 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.drawdown_from_63d_high_pct | -14.09 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.volume_vs_previous20_ratio | 1.16 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.META.value | 648.85 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_1d_pct | -6.98 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_5d_pct | -11.93 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_20d_pct | -16.56 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_60d_pct | 10.89 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_1d_pp | -5.80 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_5d_pp | -10.91 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_20d_pp | -16.14 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_60d_pp | 5.90 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma20 | 723.10 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma50 | 662.61 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma200 | 631.68 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma20_pct | -10.27 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma50_pct | -2.08 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma200_pct | 2.72 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_sma | 25.57 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_pct | 3.94 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.drawdown_from_63d_high_pct | -16.56 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.volume_vs_previous20_ratio | 2.07 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/META/history/ |
| prices.CRWV.value | 55.60 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_1d_pct | -10.06 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_5d_pct | -20.22 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_20d_pct | -38.31 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_60d_pct | -8.58 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_1d_pp | -8.88 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_5d_pp | -19.20 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_20d_pp | -37.89 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_60d_pp | -13.57 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma20 | 77.54 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma50 | 84.31 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma200 | 92.11 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma20_pct | -28.29 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma50_pct | -34.05 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma200_pct | -39.64 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_sma | 6.56 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_pct | 11.81 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.drawdown_from_63d_high_pct | -48.39 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.volume_vs_previous20_ratio | 1.68 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.MU.value | 856.49 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_1d_pct | -6.26 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_5d_pct | -8.03 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_20d_pct | -20.72 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_60d_pct | 15.92 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_1d_pp | -5.08 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_5d_pp | -7.01 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_20d_pp | -20.30 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_60d_pp | 10.93 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma20 | 996.83 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma50 | 984.04 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma200 | 729.20 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma20_pct | -14.08 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma50_pct | -12.96 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma200_pct | 17.46 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_sma | 49.17 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_pct | 5.74 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.drawdown_from_63d_high_pct | -21.94 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.volume_vs_previous20_ratio | 1.21 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MU/history/ |
| prices.DRAM.value | 45.68 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_1d_pct | -7.08 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_5d_pct | -7.40 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_20d_pct | -24.77 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_60d_pct | 1.85 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_1d_pp | -5.90 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_5d_pp | -6.38 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_20d_pp | -24.35 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_60d_pp | -3.14 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma20 | 55.34 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma50 | 56.82 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma200 | 缺失 | USD_per_share | 2026-10-22 | unavailable | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma20_pct | -17.45 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma50_pct | -19.61 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma200_pct | 缺失 | percent | 2026-10-22 | unavailable | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_sma | 2.62 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_pct | 5.74 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.drawdown_from_63d_high_pct | -28.20 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.volume_vs_previous20_ratio | 1.55 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.VRT.value | 195.59 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_1d_pct | -7.81 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_5d_pct | -8.92 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_20d_pct | -20.26 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_60d_pct | -12.29 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_1d_pp | -6.62 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_5d_pp | -7.91 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_20d_pp | -19.85 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_60d_pp | -17.28 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma20 | 233.15 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma50 | 249.53 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma200 | 268.86 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma20_pct | -16.11 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma50_pct | -21.62 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma200_pct | -27.25 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_sma | 11.72 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_pct | 5.99 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.drawdown_from_63d_high_pct | -33.42 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.volume_vs_previous20_ratio | 1.63 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/VRT/history/ |
| prices.XLK.value | 182.34 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_1d_pct | -3.29 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_5d_pct | -3.62 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_20d_pct | -6.35 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_60d_pct | 9.60 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_1d_pp | -2.11 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_5d_pp | -2.61 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_20d_pp | -5.93 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_60d_pp | 4.61 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma20 | 193.88 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma50 | 189.68 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma200 | 168.00 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma20_pct | -5.95 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma50_pct | -3.87 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma200_pct | 8.53 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_sma | 4.04 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_pct | 2.21 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.drawdown_from_63d_high_pct | -9.73 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.volume_vs_previous20_ratio | 1.43 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLE.value | 67.57 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_1d_pct | -0.87 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_5d_pct | 1.52 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_20d_pct | 7.94 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_60d_pct | 15.89 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_1d_pp | 0.32 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_5d_pp | 2.53 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_20d_pp | 8.36 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_60d_pp | 10.90 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma20 | 65.04 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma50 | 63.98 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma200 | 57.45 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma20_pct | 3.90 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma50_pct | 5.62 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma200_pct | 17.61 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_sma | 1.44 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_pct | 2.13 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.drawdown_from_63d_high_pct | -0.98 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.volume_vs_previous20_ratio | 1.31 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLF.value | 56.65 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_1d_pct | 1.09 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_5d_pct | 2.50 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_20d_pct | 3.89 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_60d_pct | 0.30 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_1d_pp | 2.27 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_5d_pp | 3.51 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_20d_pp | 4.31 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_60d_pp | -4.69 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma20 | 54.63 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma50 | 56.02 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma200 | 53.35 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma20_pct | 3.69 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma50_pct | 1.13 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma200_pct | 6.18 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_sma | 0.70 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_pct | 1.24 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.drawdown_from_63d_high_pct | -2.92 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.volume_vs_previous20_ratio | 0.90 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLI.value | 166.73 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_1d_pct | -0.94 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_5d_pct | -0.69 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_20d_pct | -1.24 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_60d_pct | -5.37 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_1d_pp | 0.24 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_5d_pp | 0.32 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_20d_pp | -0.82 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_60d_pp | -10.36 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma20 | 168.51 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma50 | 172.41 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma200 | 172.37 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma20_pct | -1.05 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma50_pct | -3.30 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma200_pct | -3.27 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_sma | 2.61 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_pct | 1.56 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.drawdown_from_63d_high_pct | -10.37 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.volume_vs_previous20_ratio | 1.45 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLV.value | 181.30 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_1d_pct | 1.32 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_5d_pct | 2.32 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_20d_pct | 6.73 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_60d_pct | 9.48 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_1d_pp | 2.50 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_5d_pp | 3.33 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_20d_pp | 7.15 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_60d_pp | 4.49 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma20 | 172.05 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma50 | 170.56 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma200 | 156.92 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma20_pct | 5.38 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma50_pct | 6.30 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma200_pct | 15.54 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_sma | 3.12 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_pct | 1.72 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.drawdown_from_63d_high_pct | 0.00 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.volume_vs_previous20_ratio | 1.19 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLP.value | 89.99 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_1d_pct | 3.31 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_5d_pct | 3.82 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_20d_pct | 10.15 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_60d_pct | 3.69 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_1d_pp | 4.49 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_5d_pp | 4.83 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_20d_pp | 10.57 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_60d_pp | -1.30 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma20 | 84.00 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma50 | 84.05 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma200 | 83.28 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma20_pct | 7.13 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma50_pct | 7.07 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma200_pct | 8.05 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_sma | 1.30 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_pct | 1.45 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.drawdown_from_63d_high_pct | 0.00 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.volume_vs_previous20_ratio | 1.78 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLY.value | 115.01 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_1d_pct | -0.45 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_5d_pct | 1.41 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_20d_pct | 4.25 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_60d_pct | 3.27 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_1d_pp | 0.73 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_5d_pp | 2.43 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_20d_pp | 4.67 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_60d_pp | -1.72 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma20 | 111.85 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma50 | 113.41 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma200 | 115.38 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma20_pct | 2.83 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma50_pct | 1.41 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma200_pct | -0.32 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_sma | 1.50 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_pct | 1.30 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.drawdown_from_63d_high_pct | -3.84 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.volume_vs_previous20_ratio | 1.15 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLC.value | 107.42 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_1d_pct | -1.42 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_5d_pct | -4.46 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_20d_pct | -5.76 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_60d_pct | -1.59 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_1d_pp | -0.24 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_5d_pp | -3.45 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_20d_pp | -5.34 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_60d_pp | -6.57 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma20 | 110.89 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma50 | 111.55 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma200 | 112.75 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma20_pct | -3.13 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma50_pct | -3.70 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma200_pct | -4.73 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_sma | 1.66 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_pct | 1.55 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.drawdown_from_63d_high_pct | -6.39 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.volume_vs_previous20_ratio | 0.94 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLU.value | 42.87 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_1d_pct | 2.07 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_5d_pct | 2.93 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_20d_pct | 8.92 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_60d_pct | -3.84 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_1d_pp | 3.25 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_5d_pp | 3.94 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_20d_pp | 9.34 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_60d_pp | -8.83 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma20 | 40.97 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma50 | 41.73 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma200 | 43.77 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma20_pct | 4.64 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma50_pct | 2.72 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma200_pct | -2.05 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_sma | 0.70 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_pct | 1.63 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.drawdown_from_63d_high_pct | -5.46 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.volume_vs_previous20_ratio | 0.82 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLRE.value | 42.52 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_1d_pct | 1.09 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_5d_pct | 1.26 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_20d_pct | 2.09 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_60d_pct | -6.71 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_1d_pp | 2.27 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_5d_pp | 2.28 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_20d_pp | 2.51 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_60d_pp | -11.70 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma20 | 41.47 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma50 | 42.73 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma200 | 42.68 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma20_pct | 2.52 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma50_pct | -0.50 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma200_pct | -0.38 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_sma | 0.62 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_pct | 1.47 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.drawdown_from_63d_high_pct | -6.81 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.volume_vs_previous20_ratio | 1.42 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLB.value | 51.69 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_1d_pct | 0.72 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_5d_pct | 2.23 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_20d_pct | 4.05 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_60d_pct | 0.36 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_1d_pp | 1.90 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_5d_pp | 3.25 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_20d_pp | 4.47 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_60d_pp | -4.63 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma20 | 49.84 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma50 | 50.91 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma200 | 50.59 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma20_pct | 3.70 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma50_pct | 1.53 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma200_pct | 2.17 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_sma | 0.70 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_pct | 1.36 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.drawdown_from_63d_high_pct | -3.25 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.volume_vs_previous20_ratio | 0.83 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLB/history/ |
| prices.SMH.value | 523.35 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_1d_pct | -5.99 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_5d_pct | -6.35 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_20d_pct | -12.85 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_60d_pct | 3.79 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_1d_pp | -4.81 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_5d_pp | -5.34 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_20d_pp | -12.43 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_60d_pp | -1.20 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma20 | 589.51 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma50 | 576.33 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma200 | 514.73 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma20_pct | -11.22 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma50_pct | -9.19 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma200_pct | 1.68 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_sma | 18.07 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_pct | 3.45 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.drawdown_from_63d_high_pct | -17.44 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.volume_vs_previous20_ratio | 1.96 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SMH/history/ |
| prices.IGV.value | 108.72 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_1d_pct | -0.09 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_5d_pct | -0.80 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_20d_pct | 1.47 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_60d_pct | 17.70 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_1d_pp | 1.09 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_5d_pp | 0.21 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_20d_pp | 1.88 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_60d_pp | 12.71 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma20 | 108.35 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma50 | 106.21 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma200 | 93.79 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma20_pct | 0.34 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma50_pct | 2.36 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma200_pct | 15.92 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_sma | 2.83 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_pct | 2.61 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.drawdown_from_63d_high_pct | -3.51 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.volume_vs_previous20_ratio | 1.21 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IGV/history/ |
| prices.XOP.value | 196.87 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_1d_pct | -1.08 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_5d_pct | 1.02 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_20d_pct | 6.97 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_60d_pct | 14.89 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_1d_pp | 0.10 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_5d_pp | 2.03 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_20d_pp | 7.39 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_60d_pp | 9.90 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma20 | 191.03 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma50 | 189.14 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma200 | 167.31 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma20_pct | 3.06 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma50_pct | 4.09 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma200_pct | 17.67 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_sma | 4.90 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_pct | 2.49 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.drawdown_from_63d_high_pct | -1.75 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.volume_vs_previous20_ratio | 1.58 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XOP/history/ |
| prices.OIH.value | 377.00 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_1d_pct | -4.21 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_5d_pct | 0.11 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_20d_pct | -4.36 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_60d_pct | 2.46 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_1d_pp | -3.03 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_5d_pp | 1.12 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_20d_pp | -3.94 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_60d_pp | -2.53 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma20 | 385.48 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma50 | 402.69 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma200 | 394.95 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma20_pct | -2.20 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma50_pct | -6.38 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma200_pct | -4.54 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_sma | 11.13 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_pct | 2.95 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.drawdown_from_63d_high_pct | -13.65 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.volume_vs_previous20_ratio | 2.34 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/OIH/history/ |
| prices.ITA.value | 204.48 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_1d_pct | -0.64 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_5d_pct | -1.18 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_20d_pct | -3.89 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_60d_pct | -13.35 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_1d_pp | 0.54 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_5d_pp | -0.16 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_20d_pp | -3.47 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_60d_pp | -18.34 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma20 | 207.01 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma50 | 219.45 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma200 | 229.34 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma20_pct | -1.22 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma50_pct | -6.82 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma200_pct | -10.84 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_sma | 3.75 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_pct | 1.84 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.drawdown_from_63d_high_pct | -19.15 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.volume_vs_previous20_ratio | 1.00 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ARKX.value | 29.63 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_1d_pct | -3.01 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_5d_pct | -2.95 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_20d_pct | -9.58 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_60d_pct | 0.37 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_1d_pp | -1.83 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_5d_pp | -1.93 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_20d_pp | -9.16 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_60d_pp | -4.62 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma20 | 31.53 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma50 | 32.21 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma200 | 32.58 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma20_pct | -6.04 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma50_pct | -8.01 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma200_pct | -9.04 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_sma | 0.74 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_pct | 2.49 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.drawdown_from_63d_high_pct | -15.00 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.volume_vs_previous20_ratio | 1.10 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.KRE.value | 72.41 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_1d_pct | 2.53 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_5d_pct | 3.81 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_20d_pct | 2.07 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_60d_pct | -4.41 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_1d_pp | 3.72 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_5d_pp | 4.83 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_20d_pp | 2.49 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_60d_pp | -9.40 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma20 | 69.98 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma50 | 72.25 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma200 | 70.15 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma20_pct | 3.47 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma50_pct | 0.22 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma200_pct | 3.22 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_sma | 1.30 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_pct | 1.79 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.drawdown_from_63d_high_pct | -6.55 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.volume_vs_previous20_ratio | 1.16 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/KRE/history/ |
| prices.SKYY.value | 164.32 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_1d_pct | -1.39 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_5d_pct | -1.38 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_20d_pct | -1.55 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_60d_pct | 18.59 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_1d_pp | -0.21 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_5d_pp | -0.37 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_20d_pp | -1.13 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_60d_pp | 13.60 | pp | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma20 | 166.71 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma50 | 164.20 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma200 | 135.34 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma20_pct | -1.43 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma50_pct | 0.07 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma200_pct | 21.41 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_sma | 4.56 | USD_per_share | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_pct | 2.77 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.drawdown_from_63d_high_pct | -6.04 | percent | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.volume_vs_previous20_ratio | 0.59 | ratio | 2026-10-22 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SKYY/history/ |
| macro.DGS2.value | 4.81 | percent | 2026-10-21 | lagged | source_series_v1:DGS2 | https://fred.stlouisfed.org/series/DGS2 |
| macro.BAMLH0A0HYM2.value | 3.27 | percentage_points | 2026-10-21 | lagged | source_series_v1:BAMLH0A0HYM2 | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| macro.BAMLC0A0CM.value | 0.88 | percentage_points | 2026-10-21 | lagged | source_series_v1:BAMLC0A0CM | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| macro.DGS10.value | 5.13 | percent | 2026-10-21 | lagged | source_series_v1:DGS10 | https://fred.stlouisfed.org/series/DGS10 |
| macro.DFII10.value | 2.76 | percent | 2026-10-21 | lagged | source_series_v1:DFII10 | https://fred.stlouisfed.org/series/DFII10 |
| macro.T10YIE.value | 2.32 | percent | 2026-10-22 | ok | source_series_v1:T10YIE | https://fred.stlouisfed.org/series/T10YIE |
| macro.STLFSI4.value | -0.63 | index | 2026-10-16 | lagged | source_series_v1:STLFSI4 | https://fred.stlouisfed.org/series/STLFSI4 |
| macro.CBOE_VIX.value | 19.03 | index | 2026-10-22 | ok | source_series_v1:CBOE_VIX | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| macro.GPRD.value | 248.66 | index | 2026-10-19 | lagged | source_series_v1:GPRD | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_ACT.value | 230.19 | index | 2026-10-19 | lagged | source_series_v1:GPRD_ACT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_THREAT.value | 310.16 | index | 2026-10-19 | lagged | source_series_v1:GPRD_THREAT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA7.value | 177.92 | index | 2026-10-19 | lagged | source_series_v1:GPRD_MA7 | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA30.value | 176.01 | index | 2026-10-19 | lagged | source_series_v1:GPRD_MA30 | https://www.matteoiacoviello.com/gpr.htm |
| quotes.MSFT.value | 521.08 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.AMZN.value | 250.38 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.GOOGL.value | 324.22 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.SPY.value | 762.12 | USD_per_share | 2026-10-23T12:02:10+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SPY |
| quotes.QQQ.value | 704.08 | USD_per_share | 2026-10-23T12:01:53+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| quotes.SMH.value | 526.21 | USD_per_share | 2026-10-23T12:01:11+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SMH |
| quotes.META.value | 645.75 | USD_per_share | 2026-10-23T12:02:16+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/META |
| quotes.NVDA.value | 212.78 | USD_per_share | 2026-10-23T12:02:15+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| quotes.WDC.value | 345.00 | USD_per_share | 2026-10-23T12:02:19+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/WDC |
| quotes.BE.value | 210.32 | USD_per_share | 2026-10-23T12:02:19+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/BE |
| external.premarket.WTI | 100.75 | USD_per_barrel | 2026-10-23T11:53:15+00:00 | lagged | 延迟分钟样本；期货连续合约可能换月；不是即时可成交价 | https://query1.finance.yahoo.com/v8/finance/chart/CL=F |
| external.premarket.gold | 4,039.70 | USD_per_troy_ounce | 2026-10-23T11:53:12+00:00 | lagged | 延迟分钟样本；期货连续合约可能换月；不是即时可成交价 | https://query1.finance.yahoo.com/v8/finance/chart/GC=F |
| external.premarket.VIX | 19.54 | index | 2026-10-23T11:48:16+00:00 | lagged | 延迟分钟样本；期货连续合约可能换月；不是即时可成交价 | https://query1.finance.yahoo.com/v8/finance/chart/^VIX |

## 指标历史比较（不同日期观测，非连续交易日）

```json
[
  {
    "id": "prices.SPY.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -9.1300048828125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.706304177423723,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.468008016047595,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.1073891005603742,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.38010904460459294,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.16099853515629547,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.13232910156250455,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.3875564575195085,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.1636587518234487,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.1726376976615716,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.3189558774517218,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.2328578404017856,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.04140959487419538,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.171880600200037,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.5741257654957713,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -20.73004150390625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -3.913389615651186,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.7177083140196623,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.7826707299543068,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.9012108296822863,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.207085438227463,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.2497002979720673,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.675281629393932,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.2813198742868792,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.8315002441406705,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.3695349121093159,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.41583007812505457,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.5680804448867,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.8046416623433656,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -3.1340922946144767,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.7707170758928577,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.15511376083257034,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.7288579412834473,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.9192076984484934,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.19000244140625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.1851079954635404,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.305020340626717,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.15799012450689043,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.6377124184381082,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.5211961819601827,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.1629876754208781,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.2653792250672646,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.2576033738335148,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.24949951171873863,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.5050286865234739,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.11157752990720837,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.15796546295926417,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.23594640930562072,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.028374095240835118,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.12571498325892838,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.04640199846511872,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.06244015858958285,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.3923179064267709,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.5800018310546875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.36797662913850004,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.6476421574435509,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.2634309064881943,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.6427138941111585,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.074280806562223,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.8203658586040441,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.370820007048568,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.2626048495065652,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.3980003356933537,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.04064147949219432,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.1177413177490223,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.5524112174508877,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.7537432221012663,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.7073727390629836,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.0642852783203125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.022724520556382855,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.7119185912802695,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.6475351289735958,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -9.95001220703125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.9699182805657864,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -4.369605638598328,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.247236987445589,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -3.1541324228814283,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.2636141031420633,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.9015976225507334,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.1398478868852155,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -3.534241467486021,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.1345001220703352,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.7184002685546602,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.2208999633788835,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.3192742029749636,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.3439886355771318,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.352221111860098,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.24928501674107206,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.1026066451643457,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.324389010392668,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.3327244731044146,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -89.60009765625,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.337667913308661,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -3.6554939311677748,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.6285646328307646,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.1587606675734117,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.6313637358849378,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.1874859151201798,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.5211755322703908,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.5388697121780046,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -11.8800048828125,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -8.142001953125146,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.1785009765626455,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.8656098178850389,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.8814937149086557,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.9317367290314298,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.5928257533482224,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.07574297803203645,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.9072779041551797,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.07999207453961832,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.3199996948242188,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 6.9464632676428435,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.6352933185681087,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.2776156741947311,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -4.79955401923764,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 8.652767445066566,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.8327146974794863,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.8297734263656436,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -5.179663063842231,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.24300003051757812,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.32400009155273324,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.2117000007629457,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.19642354240539,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.1391578985556103,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.4427596532322635,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.1735719953264514,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.28052572983714885,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.1921947034715394,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.16590138705761603,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 4.349998474121094,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 3.9698506109109966,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 4.242485979315225,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.5947384973200132,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -4.689993640217029,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 5.67615478833472,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 5.71049399536282,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.702127597880387,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -5.07010268482162,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.3284999847412138,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.48379989624024233,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.262349987030035,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 3.809486275743401,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 3.813141782081342,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 4.4394113447898,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.0035711015973771687,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.1351313491721129,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.946660212770245,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.208526291508901,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.5,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.7321141828912978,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.5020841845564394,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 3.207471955553376,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 3.449254389339751,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 3.438418360315021,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.9700922006040344,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 4.314861056113751,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 3.0691453447351584,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.13192901611328978,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.005430908203123863,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.012990455627445385,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.7365881844551234,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.861785516884884,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.8151470989063667,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.04571424211774544,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.03759771242505605,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.8018872569003586,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.584147897189995,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.020000457763671875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.13836361302214106,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.34198688538391586,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.21045083579653845,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.4993061832613277,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.567940564401582,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.8099949014315109,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.8969382647638358,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.11919713865673476,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.010499954223632812,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.013999977111815554,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.008699998855593805,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.10544609415737982,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.12024047161882656,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.10415026005154981,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.0014286041259765625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.004633885849170405,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.06865931458936991,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.45888059344991305,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.1199951171875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.039359921635573336,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.2602266944148446,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.42166760375934587,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.37713682491672396,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.6669442557881498,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.2077813216327504,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.52905670431972,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.0029722196878694263,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.02224960327149006,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.03450775146484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.001445770263671875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.18456137469340383,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.1975281439767107,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.1558836367336669,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.005713871547154026,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.007992965813643282,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.15163856031296108,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.16592451178230394,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.0699996948242188,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.0464110758806489,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.217877412505052,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.757577162716395,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.5823111316936034,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.752715253304372,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.685885428552647,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.864966263276769,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.2022020870890104,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.07865829467773722,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.018847503662101417,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.011818809509264838,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.9658790816359897,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.0477998662449584,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.0210126156124044,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.029285430908203125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.022061607955592755,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.009858987681489,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.29822164406606066,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.3500003814697266,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 17.728241041408843,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 16.739882092846393,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 11.560827394955476,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 30.615947391706058,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 19.434545218832568,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 18.207890108893984,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 12.66821649551585,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 33.601870351856775,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.16800003051757884,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.08800001144409109,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.017900004386902424,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 13.346224056721478,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 14.255166466629763,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 12.833100936924701,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.18142856870378776,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.27400113398290316,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 11.374638910097035,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.4000015258789062,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 8.900444279565079,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 9.188128965796551,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 5.801537013224322,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.6784131245807119,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 10.606748456988802,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 10.656136981844146,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 6.9089261137846965,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.0585221691853057,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.08450002670288015,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.031800003051756676,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.009850006103516051,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 7.111886785206888,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 7.413451388322323,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 6.7958844651020645,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.11500004359654015,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.23332206980991188,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 6.511635004087935,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 13.389999389648438,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 16.838090231401114,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 16.497771722164046,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 12.4629581331696,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.6222533814373117,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 18.54439440882484,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 17.965779738211637,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 13.570347233729976,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.242144336832718,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.868500137329093,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.3888000488281165,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.09465000152587777,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 13.604664870937324,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 14.395175497199865,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 13.488878394469094,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.8728566850934705,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.2743193293532489,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 12.182693970980672,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 10.899993896484375,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 17.024972390682603,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 7.393916566033065,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -10.190275895388014,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 16.154150780776487,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 18.731276568106328,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 8.861924582080661,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -9.726347835273522,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 17.64007852224327,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.5694999694824219,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.5783999633789136,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.21064998626708586,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 10.041898321506338,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 11.768572743787198,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 13.90146012495508,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.5628569466727118,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.007607173442036874,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 9.595065178603392,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -9.759994506835938,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -6.937755844897464,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.613665294333012,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -3.9382850324053753,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.9869143637622813,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -5.231451667473741,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.1456572782854169,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.8308959318450015,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.3670234083668733,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.618499755859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.23259033203123636,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.12703559875487258,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -4.046392309047763,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -4.279040531867128,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -4.870247885354085,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.2635716029575894,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.24627349575897517,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -4.079582963859619,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.37040790610504837,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -11.8699951171875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.43028520440588,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -3.264871412860726,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.8151224006218714,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.0683941239233405,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.7239810269821567,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.796863396813131,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.7077333000614976,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.4485031685279317,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.157501220703125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.5915057373046579,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.22793258666990823,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.4786453821161514,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.46001383968093,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.7919990904099237,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.25714111328125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.096889572749157,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.184192630520277,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.34792299146794803,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -11.989990234375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -4.470876282624847,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -4.982010378227885,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -4.854347387843805,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -3.1790697040752214,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.764572105201124,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -3.5140023621802907,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -3.7469582872834306,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -3.5591787486798134,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.04999999999998295,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.33799987792966135,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.04725006103515739,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -4.7312004362078275,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -4.548620814442883,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -4.949818001386674,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.6457138061523438,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.37596941245017135,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -4.221530419747265,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.5098033455001112,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -10.540008544921875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.5263365117093475,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -3.4538276257322527,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -4.3897775197631494,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -4.026658429459551,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.1799676657143756,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.9858196096846576,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -3.282388419202775,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -4.406767474064145,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.9069992065429346,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.3819866943359216,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.05245147705079489,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.8060479723938547,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.961029503170254,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -3.1060978293268593,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.373572213309151,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.19397868210185498,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.792740225793299,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.04669301015424199,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -48.6700439453125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -7.448598505323501,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -6.501049690330884,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -10.296383293796872,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -6.750702433147326,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -5.742294327899778,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -5.033041674283289,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -9.188994193236498,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -7.1308114777519185,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -6.43700256347654,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.4091296386718568,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.05036865234376364,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -5.879614165108837,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -7.569496729630654,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -7.696039007238498,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 3.0128566196986597,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.706904583585453,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -6.259087985237098,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.6128869005959543,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -6.220001220703125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -9.56251479629968,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -14.198048142324305,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -9.450566800775249,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.4400556158641429,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -7.856210618875959,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -12.730040126276712,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -8.343177700214877,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.820164660468734,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.7264999389648494,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.0426000976562477,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.11170001983641953,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -6.285383223110742,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -6.481953703361466,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -6.6711642953191514,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.2907142639160156,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.6582082268971092,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -5.773694446193296,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.054141851619037284,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -57.17999267578125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -8.22240589971619,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -7.976608443293854,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -5.975164384783504,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 4.548033376309247,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -6.516101722292467,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -6.508600427246257,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -4.8677752842231286,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 4.167924331704653,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -11.19349975585942,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.0931323242188,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.5665596008300327,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -4.718396697827476,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -5.707723700774247,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -8.284020317331375,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.0311183970953337,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.5815610931527022,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -5.211364553707195,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.41976456000737694,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -3.479999542236328,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -10.09652477417462,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -5.444624975366997,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -4.187849071976256,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.0591574039352514,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -8.390220596750897,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -3.976616959319401,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -3.0804599714158805,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.4392664485398443,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.75200004577637,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.1823999786376902,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -5.0976005272598925,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -5.847735005357723,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.17571449279785156,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.7641134000712926,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -5.469977366648827,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.8148742371678085,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -16.55999755859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -12.025681138633981,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -4.1291090702386235,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -5.541129705343685,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 8.992669072486969,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -10.319376961210258,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.661101054191028,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -4.43374060478331,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 8.612560027882378,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.4855003356933594,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.8539862060546852,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.1038049316405818,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -6.142855833764138,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -6.00949452152253,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -6.189830069213986,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.7378561837332587,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.8157178646617256,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -5.637101037596494,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.3567549556638232,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -6.1999969482421875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -4.9601201395890975,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.6282115511905735,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.8719314737669315,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.7326857603485504,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -3.253815962165374,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.1602035351429785,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.7645423732065568,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.1127948049531433,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.6185005187988111,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.1259973144531159,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.181085243225084,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.8886403798905618,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -3.202668639529993,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -3.8115060792365725,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.2471422467912947,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.20390319253250855,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -3.069305419921875,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.27221394435067636,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.5900039672851562,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.1451547785555016,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.7337457583373563,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.3440177582982216,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -3.2050795414917843,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.5611493988682215,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.2017537743849513,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.23662865773784603,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -3.5851885860963755,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.2485000610351591,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.13801246643065923,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.11408493041992074,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.309182085588323,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.1525408420503425,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.2630202440710327,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.0999998365129744,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.16516987290804264,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.8646013859247237,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.4888707094430097,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.6100006103515625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.5142097682644398,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.2911328972758698,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.137498343513399,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.6648041068650485,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.220513945688163,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.1768751187717252,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.2448874440737727,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.2846950622604556,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.1060001373291044,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.021314620971679688,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.004657649993895063,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.9171496734105666,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.126977733114165,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.134134921177754,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.021428516932896158,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.024746477203256623,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.0453543417035527,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.1343473611342717,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.5800018310546875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.8440175553874782,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.4512302911310337,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.1915312176989259,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.155099290254414,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.13771337796375516,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.016777724916561265,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.9158578828614483,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.7749902456498212,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.1050003051757642,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.37303558349611876,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.02996208190918992,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.8754543198728815,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.705645998293547,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.9335928808497429,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.0842851911272322,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.06474837298869729,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.8494173590992808,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.4617939796241437,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.3600006103515625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.8082591218568034,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.543180192379511,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.7215711988422857,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.083998579137103,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 3.5145632992805265,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.924827823668084,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.8289602994026595,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.70388953453251,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.5715003967285099,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.2700436401367199,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.12573127746583168,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.0250796787480754,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.2172935748236746,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.4125521574894755,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.12357112339564713,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.04639184682473285,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.48938096261215147,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.1841821724568915,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.8799972534179688,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 4.035505477064594,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.5985578602954806,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 4.469335392097219,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.97251532698255,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 5.741809654488317,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 4.066565876343075,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 5.576724492657593,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.592406282377957,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.41450004577636435,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.10931777954101562,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.06992107391357649,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.9142229854438817,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 3.291709661415121,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 3.3702005693295733,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.1621426173618863,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.1383219985274402,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.7293440337873935,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.7311973743965154,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.5199966430664062,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.4760696094073813,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.2035397378078914,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.1590289530799538,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.33546880216215325,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.2302345680163418,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.7355317217602964,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.9483601474804209,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.04464024244243969,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.23450012207031534,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.05241836547851619,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.026559753417970455,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.6819302434950769,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.4114434890657437,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.42762068137135456,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.022142682756696397,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.013293062586858806,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.43479217760664657,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.23165310412319917,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.5500030517578125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.31523302905223094,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.7952346598875573,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.5742564114453304,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.2744165456765932,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.3910711483714921,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.3272266438399623,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.4668673108849566,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.6545255902811853,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.32849998474119957,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.049755401611335515,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.044250602722172516,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.107537582163165,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.3459298397040742,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.3368353868372873,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.07500021798270073,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.09085010308478392,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.3507651867170516,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.5370286871673204,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.8699989318847656,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.7848956347338074,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.258027339260238,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 3.2573011656558135,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 3.2139060133301145,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 3.4911998121575305,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 3.726035355307833,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 4.364690266216188,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.8337969687255207,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.17549991607666016,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.013000030517581251,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.004186897277833168,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.6825274321612405,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.11595686825663,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.9786113656454778,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.025000163487025717,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.025770097290692906,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 3.1390852959771944,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.31591920907559146,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.45999908447265625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.8487458975393167,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.1116218975675265,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.5630173580496454,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.1095744352530579,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 3.55505007496304,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.3563861184800685,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.6704064586100196,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.7294653906484658,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.04349994659423828,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.031972808837885225,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.013887271881102947,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.0026587087373473,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.1500097103283369,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.045698560782049,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.0014283316476003671,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.019451607997624132,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.008196181970944,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.5589024473546805,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.3699989318847656,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.5452857948972545,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.0869650361310157,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.97747157976913,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.8606742714945557,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.2515899723209776,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.3810429799165793,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 3.084860680329504,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.4805652268899623,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.10049991607665731,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.012982788085935226,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.02396125793456605,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.5342948301105821,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.7524543033281539,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.6832864950486295,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.009285790579659614,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.008320442312591547,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.6925688002514585,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.15206151384650501,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -33.35003662109375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -7.883195729972781,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -4.927003676327146,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -5.416346298827801,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.323102911615659,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -6.1768915525490575,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -3.458995660279551,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -4.308957198267427,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.703211956220252,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -3.8585021972655795,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.229600830078084,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.67864990234375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -5.043145284025453,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -5.580977033758016,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -6.621961258059628,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.2664271763392847,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.43437231163001977,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -5.261087764102935,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.9532910417079057,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.09999847412109375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.8594043505722468,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.8897710472580709,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.7991842528958237,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.8655877085458137,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.15310017314852375,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.42176303121047587,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.906573353456198,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.2456967531504048,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.07849998474121378,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.11279998779296818,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.01909835815429517,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.16509961061037526,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.20306896196113922,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.13025129536774394,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.021427699497767794,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.017295935549736186,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.088753417720977,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.049290201744972784,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.1500091552734375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.5654273507056384,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.41950994009412046,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.9970084791974383,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -5.212957695747722,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.1408768267180847,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.8875179561417155,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.8896193786370628,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -5.593066740352313,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.6409996032714673,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.3799844360351585,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.36468212127684296,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.4762384749001933,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.3485830605516336,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.5448711099303338,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.287143162318638,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.17117448689825032,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.0729659162004745,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.8563925468780094,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -16.579986572265625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -6.470389720409919,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.8255351057106637,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -3.837562136874084,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -3.523903654373828,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -4.764085542986196,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.3575270896630687,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.73017303631371,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -3.9040126989784207,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.8600006103515625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.7247998046875068,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.3333500671386673,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -4.073818145983655,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -3.9417361005125717,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -4.282212552372988,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.3007158551897309,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.4548262427325138,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -3.7976973480714484,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.4219347943988263,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.30999755859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.46193967143779435,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.9381059687953783,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.09122001645963662,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.5488929621568683,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.2443645059859287,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.4700979527477833,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.0161690841007376,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.1687839175522754,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.41399993896484943,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.9369729614257665,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.1257655334472929,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.43440420234890365,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.19825900969562316,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.5220303497219483,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.1100006103515625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.06513815714461635,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.5179354421934512,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.26466384245679375,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.9200000762939453,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -4.573954674651115,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -3.029823843502999,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -3.0928076642477436,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.43804944289447256,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.867650497227392,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.561815827455404,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.985418563687369,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.057940398289879624,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.15700006484985352,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.10119998931885021,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.013850011825567776,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.4375205641140156,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.5592216473201095,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.7843251561559743,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.01821422576904297,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.13467877265919403,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.639128112983313,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.44393646896677397,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.7900009155273438,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.5346939194419438,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.7788984424306866,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 1.7311615314088868,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 3.1036811629925447,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 4.240998096865667,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.246906458478281,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.838550631969261,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.7235721183879527,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.07350006103516193,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.09063552856446222,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.03166622161865007,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.451638821576574,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.600027708214625,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.506268833781089,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.05928530011858246,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.038593577536486956,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.3100165271940583,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.19518048765247142,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.30999755859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_1d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -3.400512259735844,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_5d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.971648910469915,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_20d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.008585265839379,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_60d_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.242715130978354,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_1d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.6942080823121208,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_5d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.50364089442232,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_20d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.09880383472099519,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_60d_pp",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -2.622824175582945,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma20",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.1294998168945085,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma50",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.035200195312512506,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma200",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.16955001831055938,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma20_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.3080598054069248,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma50_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.4285399081386263,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma200_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.8612506962197628,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_sma",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.038572038922991325,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.061595126444043746,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.drawdown_from_63d_high_pct",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -1.3208288447912775,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.volume_vs_previous20_ratio",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.05395780986625298,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS2.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.019999999999999574,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLH0A0HYM2.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.06000000000000005,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLC0A0CM.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.010000000000000009,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS10.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.009999999999999787,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DFII10.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.010000000000000231,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.T10YIE.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.050000000000000266,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.STLFSI4.value",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-09",
        "to": "2026-10-16",
        "change": 0.08779999999999999,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.CBOE_VIX.value",
    "available_prior_observations": 4,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 2.3500000000000014,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.GPRD.value",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-13",
        "to": "2026-10-19",
        "change": -93.74026489257812,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.GPRD_ACT.value",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-13",
        "to": "2026-10-19",
        "change": -214.35792541503906,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.GPRD_THREAT.value",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-13",
        "to": "2026-10-19",
        "change": -7.66876220703125,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.GPRD_MA7.value",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-13",
        "to": "2026-10-19",
        "change": -8.659194946289062,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.GPRD_MA30.value",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-13",
        "to": "2026-10-19",
        "change": -1.8906707763671875,
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
| 事实指标引用 | ["macro.BAMLH0A0HYM2.value", "macro.DGS10.value", "prices.^VIX.value"] |
| 推断与解释 | 结构性避险、成长估值降温；尚不足以认定系统性恐慌。 |
| 反证与缺口 | 信用数据截至21日，最新冲击可能尚未反映；盘前VIX不与昨日VIX3M计算当前期限结构。 |
| 确认条件 | 波动、信用和市场广度同步恶化才提高恐慌判断。 |
| 失效条件 | 地缘缓和且成长价格、现金回收持续改善。 |
| 观察期限 | 下一交易日至两周 |
| 条件式指导 | 观察多指标，不依赖单一情绪读数。 |
| 主观置信等级 | medium |
| 判断变化原因 | 较早报收盘窗口未变；盘前半导体弱修复，能源合约显著上升，AI合约下降；官方VIX补齐昨日。 |

## 判断依据 · 反弹是否可靠？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 反弹是否可靠？ |
| 事实指标引用 | ["prices.QQQ.distance_sma20_pct", "prices.SMH.distance_sma20_pct", "prices.SPY.distance_sma20_pct"] |
| 推断与解释 | 盘前SMH小幅回升、QQQ近持平，只能认定价格修复尝试；不能验证今晚尚未发生的常规VWAP。 |
| 反证与缺口 | 急跌可能形成短期修复；无完整分钟路径，不能虚构VWAP失败。 |
| 确认条件 | 常规回踩守住并连续两次收盘收复20日线。 |
| 失效条件 | 下一开盘守不住前低、反抽受压，或收盘再创新低。 |
| 观察期限 | 1–5个交易日 |
| 条件式指导 | 从价格承接到收盘趋势逐级确认，不跳步。 |
| 主观置信等级 | medium |
| 判断变化原因 | 较早报收盘窗口未变；盘前半导体弱修复，能源合约显著上升，AI合约下降；官方VIX补齐昨日。 |

## 判断依据 · 轮动是否等于资金流入？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 轮动是否等于资金流入？ |
| 事实指标引用 | ["prices.SMH.relative_spy_5d_pp", "prices.RSP.relative_spy_5d_pp", "prices.IGV.return_1d_pct"] |
| 推断与解释 | 防御、金融、等权强于科技；19ETF价量是相对偏好证据，不能证明主力净流入。 |
| 反证与缺口 | 当期份额/申赎缺失。 |
| 确认条件 | 相对强弱延续、发行人净申赎和盈利互相支持。 |
| 失效条件 | 领涨迅速消失、财报不支持。 |
| 观察期限 | 1–2周 |
| 条件式指导 | 保留资金数据的真实窗口，不把上涨称主力净流入。 |
| 主观置信等级 | medium |
| 判断变化原因 | 较早报收盘窗口未变；盘前半导体弱修复，能源合约显著上升，AI合约下降；官方VIX补齐昨日。 |

## 判断依据 · AI支出增长是利好吗？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | AI支出增长是利好吗？ |
| 事实指标引用 | ["prices.NVDA.return_1d_pct", "prices.SMH.distance_sma20_pct", "prices.CRWV.distance_sma20_pct"] |
| 推断与解释 | 需求仍强与估值下修并存；回收现金和融资成本决定高预期能否兑现。 |
| 反证与缺口 | H100租金上升、WDC/BE收入增长。 |
| 确认条件 | 收入、利润和企业自由现金流可持续改善，价格承接配合。 |
| 失效条件 | 融资收紧或资本开支增速长期高于现金创造，订单开始下修。 |
| 观察期限 | 下一季度并每日观察价格风险 |
| 条件式指导 | 区分观测、管理层指引和估值假设；META暂停精确估值。 |
| 主观置信等级 | medium |
| 判断变化原因 | 较早报收盘窗口未变；盘前半导体弱修复，能源合约显著上升，AI合约下降；官方VIX补齐昨日。 |

## AI增长与现金回收的冲突 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | META最新Q3 10-Q的大额多年采购、未开始租赁及附条件采购承诺延续此前核验；LRCX官方季度收入82.19亿美元、下一季指引86亿美元±4亿美元。 |
| 事实：市场反应 | 昨收META−6.98%、NVDA−4.40%、SMH−5.99%；今盘前NVDA约+0.27%、SMH+0.55%，META仍−0.48%。 |
| 推断：解释 | 推断：市场在重新定价投资回收与增长预期，不能从股价跌幅直接推出客户需求崩塌；LRCX指引低于市场预期是新闻说法，本次未取得完整一致预期，不定量声称落差。 |
| 受益篮子 | ["现金回收强、预期较低的公司观察"] |
| 受损篮子 | ["高估值AI硬件", "依赖融资扩张的算力链"] |
| 反证 | H100带日期租金上升；设备公司仍报告增长。 |
| 下一催化剂 | 今晚常规开盘承接及下周FOMC、云厂商财报；官方披露列表本次已重新检查。 |
| 证据 | ["https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm", "https://investor.lamresearch.com/2026-10-21-Lam-Research-Corporation-Reports-Financial-Results-for-the-Quarter-Ended-September-27,-2026", "https://www.silicondata.com/products/silicon-index/h100"] |

## 防御与等权相对占优 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 10月22日19个板块及主题ETF收盘窗口已更新。 |
| 事实：市场反应 | XLP+3.31%、XLV+1.32%、XLF+1.09%、RSP+0.73%；XLK−3.29%、SMH−5.99%。 |
| 推断：解释 | 推断：抛售集中于成长及科技权重，尚不能称所有资产一起被抛售；上涨不证明主力净流入。 |
| 受益篮子 | ["XLP", "XLV", "XLF", "RSP观察"] |
| 受损篮子 | ["SMH", "XLK"] |
| 反证 | 防御资产也可能估值过高；一天领先可能反转。 |
| 下一催化剂 | 下一交易日相对收益是否延续；等待带明确窗口的份额及申赎证据。 |
| 证据 | ["https://finance.yahoo.com/quote/RSP/history/", "https://www.ici.org/research/stats/etf_flows"] |

## 油价压力与避险分化 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | WTI盘前连续报价100.75，油价105美元触价合约53%；Brent分钟报价与AP新闻报价不一致，保留冲突。 |
| 事实：市场反应 | 昨日TLT上涨、GLD下跌；今晚VIX盘前约19.54，油价风险合约较早报上升15个百分点。 |
| 推断：解释 | 推断：供给风险和通胀担忧是需独立跟踪的风险线。触价合约不是月末油价预报，也不能用Yahoo报价代为结算。 |
| 受益篮子 | ["能源供给链观察", "高质量债券观察"] |
| 受损篮子 | ["能源成本敏感行业", "长久期成长"] |
| 反证 | 美伊专门停火合约77.5%，但月底通航正常仅0.35%；两者定义不同，停火不等于航道恢复。 |
| 下一催化剂 | 实际供应及通航数据；下周FOMC。 |
| 证据 | ["https://polymarket.com/event/us-iran-ceasefire-continues-throughptptpt", "https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-october-31-20260810151043583", "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm"] |

## 财报后的跌幅收窄仍需常规买盘确认 · 减弱

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | WDC Q1FY27收入43.81亿美元、同比+55%，Q2收入指引中点51亿美元；BE Q3收入12.358亿美元、同比+138.1%，全年收入指引提高到44–46亿美元。 |
| 事实：市场反应 | UTC12:02附近WDC345、BE210.32，分别比昨日常规收盘低2.59%和3.42%；相较早报盘后335.80/204.88有所修复。 |
| 推断：解释 | 推断：最初抛压缓解，但尚未消化财报后损失。强经营增长与低于预期的股票反应可共存；没有完整一致预期和电话会证据，不单因果归因。 |
| 受益篮子 | ["现金兑现及估值可验证的候选"] |
| 受损篮子 | ["高预期数据中心供电与存储链"] |
| 反证 | 两家公司收入及指引仍增长；盘后交易稀薄。WDC是HDD链证据，不能当作SNDK的NAND或MU的HBM财报。 |
| 下一催化剂 | 今晚开盘成交后能否持续收复昨日收盘，及回踩是否守住。 |
| 证据 | ["https://investor.wdc.com/node/28921/pdf", "https://www.bloomenergy.com/news/bloom-energy-reports-record-third-quarter-2026-financial-results-and-raises-full-year-2026-guidance/"] |

## 航天重组仍属于事件观察 · 待核验

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | Tesla/SpaceX年底正式控制权交易公告专门合约18.5%，较早报不变。 |
| 事实：市场反应 | 尚无本次独立核验的正式合并公告；不以赔率变化替代交易事实。 |
| 推断：解释 | 仅作为潜在事件溢价观察，不转换为行业盈利预测。 |
| 受益篮子 | ["航天事件篮子观察"] |
| 受损篮子 | ["传闻追价"] |
| 反证 | 传闻、谈判或少数股权投资不满足结算定义。 |
| 下一催化剂 | 正式公司公告，日期未定。 |
| 证据 | ["https://polymarket.com/event/tesla-and-spacex-merger-officially-announced-by-june-30"] |

## 工业AI继续兑现产品，盈利兑现仍待验证 · 新增

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | Siemens 10月22日官方公告与NVIDIA推进芯片设计、AI工厂基础设施及工业软件应用；本次通过官方正文核验。 |
| 事实：市场反应 | NVDA昨日下跌、今盘前小涨，尚无可分离的公告异常收益证据。 |
| 推断：解释 | 推断：是AI应用仍在扩张的反证，但产品效率指标不等于新增收入或自由现金流。 |
| 受益篮子 | ["工业软件与自动化观察", "NVDA生态观察"] |
| 受损篮子 | ["若定价竞争或资本投入侵蚀回报的供应商"] |
| 反证 | 市场尚未持续奖励增长；订单金额和利润贡献未量化。 |
| 下一催化剂 | 后续实际客户部署与财报收入兑现，日期未定。 |
| 证据 | ["https://press.siemens.com/global/nl/node/7478"] |

## tc 报价（供应商时戳不等于成交时戳）

| 标的 | 价格 USD | 变化% | 观测时间 | 供应商时间 | 抓取时间 | 质量 |
| --- | --- | --- | --- | --- | --- | --- |
| MSFT | 521.08 | -2.23 | 缺失 | 缺失 | 2026-10-23T12:02:27.163806+00:00 | unverified_trade_timestamp |
| AMZN | 250.38 | -4.57 | 缺失 | 缺失 | 2026-10-23T12:02:27.163806+00:00 | unverified_trade_timestamp |
| GOOGL | 324.22 | -3.15 | 缺失 | 缺失 | 2026-10-23T12:02:27.163806+00:00 | unverified_trade_timestamp |
| SPY | 762.12 | -0.24 | 2026-10-23T12:02:10+00:00 | 2026-10-23T12:02:10+00:00 | 2026-10-23T12:02:27.163806+00:00 | ok |
| QQQ | 704.08 | -0.06 | 2026-10-23T12:01:53+00:00 | 2026-10-23T12:01:53+00:00 | 2026-10-23T12:02:27.163806+00:00 | ok |
| SMH | 526.21 | 0.55 | 2026-10-23T12:01:11+00:00 | 2026-10-23T12:01:11+00:00 | 2026-10-23T12:02:27.163806+00:00 | ok |
| META | 645.75 | -0.48 | 2026-10-23T12:02:16+00:00 | 2026-10-23T12:02:16+00:00 | 2026-10-23T12:02:27.163806+00:00 | ok |
| NVDA | 212.78 | 0.27 | 2026-10-23T12:02:15+00:00 | 2026-10-23T12:02:15+00:00 | 2026-10-23T12:02:27.163806+00:00 | ok |
| WDC | 345.00 | -2.59 | 2026-10-23T12:02:19+00:00 | 2026-10-23T12:02:19+00:00 | 2026-10-23T12:02:27.163806+00:00 | ok |
| BE | 210.32 | -3.42 | 2026-10-23T12:02:19+00:00 | 2026-10-23T12:02:19+00:00 | 2026-10-23T12:02:27.163806+00:00 | ok |

## 核心行情与风险代理

| 标的 | 价格/指数 | 单位 | 观测日 | 1日% | 5日% | 20日% | 质量 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 763.96 | USD_per_share | 2026-10-22 | -1.18 | -1.01 | -0.42 | ok |
| QQQ | 704.47 | USD_per_share | 2026-10-22 | -2.86 | -3.23 | -4.94 | ok |
| IWM | 276.67 | USD_per_share | 2026-10-22 | 0.07 | 0.58 | -1.77 | ok |
| RSP | 218.22 | USD_per_share | 2026-10-22 | 0.73 | 1.50 | 3.79 | ok |
| GLD | 369.00 | USD_per_share | 2026-10-22 | -2.63 | -3.58 | -5.79 | ok |
| GC=F | 4,060.40 | USD_per_troy_ounce | 2026-10-22 | -2.16 | -2.63 | -5.53 | ok |
| CL=F | 99.47 | USD_per_barrel | 2026-10-22 | 2.39 | 1.53 | 5.14 | ok |
| BZ=F | 113.17 | USD_per_barrel | 2026-10-22 | 4.00 | 6.84 | 6.16 | ok |
| TLT | 81.74 | USD_per_share | 2026-10-22 | 1.87 | 2.21 | 3.34 | ok |
| UUP | 28.90 | USD_per_share | 2026-10-22 | -0.07 | -0.34 | 0.73 | ok |
| HYG | 77.10 | USD_per_share | 2026-10-22 | 0.16 | -0.04 | -0.57 | ok |
| LQD | 104.28 | USD_per_share | 2026-10-22 | 1.04 | 0.75 | 1.53 | ok |
| ^VIX | 19.03 | index | 2026-10-22 | 14.09 | 15.61 | 21.44 | ok |
| ^VIX3M | 20.12 | index | 2026-10-22 | 7.48 | 8.82 | 9.17 | ok |
| ^VVIX | 107.94 | index | 2026-10-22 | 14.16 | 16.60 | 19.18 | ok |
| ^MOVE | 106.84 | index | 2026-10-22 | 11.36 | 4.24 | 11.93 | ok |
| NVDA | 212.21 | USD_per_share | 2026-10-22 | -4.40 | -2.31 | -5.51 | ok |
| MSFT | 521.08 | USD_per_share | 2026-10-22 | -2.23 | -3.40 | 4.65 | ok |
| AMZN | 250.38 | USD_per_share | 2026-10-22 | -4.57 | -1.72 | 0.40 | ok |
| GOOGL | 324.22 | USD_per_share | 2026-10-22 | -3.15 | -7.16 | -5.30 | ok |
| META | 648.85 | USD_per_share | 2026-10-22 | -6.98 | -11.93 | -16.56 | ok |
| CRWV | 55.60 | USD_per_share | 2026-10-22 | -10.06 | -20.22 | -38.31 | ok |
| MU | 856.49 | USD_per_share | 2026-10-22 | -6.26 | -8.03 | -20.72 | ok |
| DRAM | 45.68 | USD_per_share | 2026-10-22 | -7.08 | -7.40 | -24.77 | ok |
| VRT | 195.59 | USD_per_share | 2026-10-22 | -7.81 | -8.92 | -20.26 | ok |

## 跨资产风险解释

维持结构性避险、未确认系统性恐慌。昨日Cboe官方VIX已更新至22日19.03，与Yahoo一致；同日VIX3M20.12，近月低于三个月，只是波动率指数期限关系。今11:48UTC VIX19.54，不能和昨日VIX3M拼接成当前期限曲线。MOVE106.84仍为22日。盘前WTI连续合约100.75、黄金连续报价4039.70（11:53UTC），是延迟分钟样本，换月口径须留意。Brent Yahoo11:52UTC109.83，而AP盘前报道114.92，时点/合约差异未解决；不据其差值判断油价已回落，也不覆盖历史序列。ICE/CME公开页面未返回可核验同交割实时报价。FRED2年4.81%、10年5.13%、实际10年2.76%、HY327bp、IG88bp仍截至21日；Yahoo TNX22日4.953是不同时间口径，不拼成长序列。STLFSI−0.6328截至16日、GPR248.66截至19日。Fed9月16日官方加息25bp至3.75–4%，下次决定尚未发生。密歇根官网目前仍是10月初值：一年通胀预期4.7%、长期3.5%；终值今晚10ET才发布，不能提前宣称改善。CNN不可得，无统一自造恐慌或战争指数。

## 宏观与地缘风险指标

| 指标 | 数值 | 单位 | 观测日 | 20次观测变化 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- | --- |
| DGS2 | 4.81 | percent | 2026-10-21 | 0.10 | lagged | https://fred.stlouisfed.org/series/DGS2 |
| BAMLH0A0HYM2 | 3.27 | percentage_points | 2026-10-21 | 0.54 | lagged | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| BAMLC0A0CM | 0.88 | percentage_points | 2026-10-21 | 0.11 | lagged | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| DGS10 | 5.13 | percent | 2026-10-21 | 0.17 | lagged | https://fred.stlouisfed.org/series/DGS10 |
| DFII10 | 2.76 | percent | 2026-10-21 | 0.13 | lagged | https://fred.stlouisfed.org/series/DFII10 |
| T10YIE | 2.32 | percent | 2026-10-22 | -0.03 | ok | https://fred.stlouisfed.org/series/T10YIE |
| STLFSI4 | -0.63 | index | 2026-10-16 | 0.04 | lagged | https://fred.stlouisfed.org/series/STLFSI4 |
| CBOE_VIX | 19.03 | index | 2026-10-22 | 3.36 | ok | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| GPRD | 248.66 | index | 2026-10-19 | 50.22 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_ACT | 230.19 | index | 2026-10-19 | 1.92 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_THREAT | 310.16 | index | 2026-10-19 | 119.76 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_MA7 | 177.92 | index | 2026-10-19 | -5.90 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_MA30 | 176.01 | index | 2026-10-19 | 14.79 | lagged | https://www.matteoiacoviello.com/gpr.htm |

## CNN Fear & Greed

缺失：CNN 无可核验数据，不使用替代指数

## 19 板块与主题 ETF：价格量能证据

| 标的 | 板块 | 1日% | 5日% | 20日% | 相对SPY 1日pp | 相对SPY 5日pp | 相对SPY 20日pp | 成交量/前20日 | 观测日 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLK | 科技 | -3.29 | -3.62 | -6.35 | -2.11 | -2.61 | -5.93 | 1.43 | 2026-10-22 |
| XLE | 能源 | -0.87 | 1.52 | 7.94 | 0.32 | 2.53 | 8.36 | 1.31 | 2026-10-22 |
| XLF | 金融 | 1.09 | 2.50 | 3.89 | 2.27 | 3.51 | 4.31 | 0.90 | 2026-10-22 |
| XLI | 工业 | -0.94 | -0.69 | -1.24 | 0.24 | 0.32 | -0.82 | 1.45 | 2026-10-22 |
| XLV | 医疗 | 1.32 | 2.32 | 6.73 | 2.50 | 3.33 | 7.15 | 1.19 | 2026-10-22 |
| XLP | 必需消费 | 3.31 | 3.82 | 10.15 | 4.49 | 4.83 | 10.57 | 1.78 | 2026-10-22 |
| XLY | 可选消费 | -0.45 | 1.41 | 4.25 | 0.73 | 2.43 | 4.67 | 1.15 | 2026-10-22 |
| XLC | 通信 | -1.42 | -4.46 | -5.76 | -0.24 | -3.45 | -5.34 | 0.94 | 2026-10-22 |
| XLU | 公用事业 | 2.07 | 2.93 | 8.92 | 3.25 | 3.94 | 9.34 | 0.82 | 2026-10-22 |
| XLRE | 房地产 | 1.09 | 1.26 | 2.09 | 2.27 | 2.28 | 2.51 | 1.42 | 2026-10-22 |
| XLB | 材料 | 0.72 | 2.23 | 4.05 | 1.90 | 3.25 | 4.47 | 0.83 | 2026-10-22 |
| SMH | 半导体 | -5.99 | -6.35 | -12.85 | -4.81 | -5.34 | -12.43 | 1.96 | 2026-10-22 |
| IGV | 软件 | -0.09 | -0.80 | 1.47 | 1.09 | 0.21 | 1.88 | 1.21 | 2026-10-22 |
| XOP | 油气开采 | -1.08 | 1.02 | 6.97 | 0.10 | 2.03 | 7.39 | 1.58 | 2026-10-22 |
| OIH | 油服 | -4.21 | 0.11 | -4.36 | -3.03 | 1.12 | -3.94 | 2.34 | 2026-10-22 |
| ITA | 航空与国防 | -0.64 | -1.18 | -3.89 | 0.54 | -0.16 | -3.47 | 1.00 | 2026-10-22 |
| ARKX | 航天主题 | -3.01 | -2.95 | -9.58 | -1.83 | -1.93 | -9.16 | 1.10 | 2026-10-22 |
| KRE | 区域银行 | 2.53 | 3.81 | 2.07 | 3.72 | 4.83 | 2.49 | 1.16 | 2026-10-22 |
| SKYY | 云计算 | -1.39 | -1.38 | -1.55 | -0.21 | -0.37 | -1.13 | 0.59 | 2026-10-22 |

## 资金证据分层

19ETF统一截至10月22日，展示同端点1/5/20/60日强弱。SMH五日相对SPY−5.34个百分点，XLP+4.83、XLV+3.33、XLF+3.51、RSP+2.51个百分点，体现防御和非科技相对占优；QQQ/SMH当日成交约前20日均量1.84/1.97倍。价量不等于净申赎或主力身份。发行人SPY/SMH页面已更新至22日，SPY份额1061.18百万、NAV763.79，SMH NAV523.14，但仍未取得连续份额和拆分桥；ICI最新可核验仍截至14日ETF净发行532.62亿美元、国内股票296.70亿美元，不能当作22日资金去向。保留前期明确日期的个体ETF资金报告作为滞后对照，不使用其解释今日净流入。机构13F本就滞后，当前机构实际买卖无法取得。 相较早报收盘窗口相同，19ETF收盘轮动不是又发生一次资金变化；今盘前仅半导体相对修复，不能推断整日轮动。

## 最近可核验 ETF 申赎窗口

| 标的 | 金额 USD million | 起始日 | 结束日 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- |
| XLK | 1,496.06 | 2026-10-05 | 2026-10-09 | public_report | https://www.etf.com/sections/weekly-etf-flows/etf-inflows-top-41b-investors-pile-brazil-long-bonds |
| TLT | 1,207.29 | 2026-10-05 | 2026-10-09 | public_report | https://www.etf.com/sections/weekly-etf-flows/etf-inflows-top-41b-investors-pile-brazil-long-bonds |
| SMH | -1,665.50 | 2026-10-05 | 2026-10-09 | public_report | https://www.etf.com/sections/weekly-etf-flows/etf-inflows-top-41b-investors-pile-brazil-long-bonds |
| DRAM | -694.28 | 2026-10-05 | 2026-10-09 | public_report | https://www.etf.com/sections/weekly-etf-flows/etf-inflows-top-41b-investors-pile-brazil-long-bonds |
| IYW | -830.57 | 2026-10-05 | 2026-10-09 | public_report | https://www.etf.com/sections/weekly-etf-flows/etf-inflows-top-41b-investors-pile-brazil-long-bonds |
| IWM | 2,224.18 | 2026-10-15 | 2026-10-15 | public_report | https://www.etf.com/sections/daily-etf-flows/etf-fund-flows-small-cap-focused-iwm-nets-22-billion |
| SOXL | 1,362.77 | 2026-10-15 | 2026-10-15 | public_report | https://www.etf.com/sections/daily-etf-flows/etf-fund-flows-small-cap-focused-iwm-nets-22-billion |
| IGV | 446.52 | 2026-10-15 | 2026-10-15 | public_report | https://www.etf.com/sections/daily-etf-flows/etf-fund-flows-small-cap-focused-iwm-nets-22-billion |
| SOXX | 363.61 | 2026-10-15 | 2026-10-15 | public_report | https://www.etf.com/sections/daily-etf-flows/etf-fund-flows-small-cap-focused-iwm-nets-22-billion |
| SMH | -508.48 | 2026-10-15 | 2026-10-15 | public_report | https://www.etf.com/sections/daily-etf-flows/etf-fund-flows-small-cap-focused-iwm-nets-22-billion |
| TLT | -1640 | 2026-10-15 | 2026-10-15 | public_report | https://www.etf.com/sections/daily-etf-flows/etf-fund-flows-small-cap-focused-iwm-nets-22-billion |
| SOXL | 1,710.51 | 2026-10-14 | 2026-10-14 | public_report | https://www.etf.com/sections/daily-etf-flows/etf-fund-flows-semiconductors-leveraged-etfs-dominate |
| SMH | 617.69 | 2026-10-14 | 2026-10-14 | public_report | https://www.etf.com/sections/daily-etf-flows/etf-fund-flows-semiconductors-leveraged-etfs-dominate |
| QQQ | -4,275.63 | 2026-10-14 | 2026-10-14 | public_report | https://www.etf.com/sections/daily-etf-flows/etf-fund-flows-semiconductors-leveraged-etfs-dominate |
| SPY | -1,400.14 | 2026-10-14 | 2026-10-14 | public_report | https://www.etf.com/sections/daily-etf-flows/etf-fund-flows-semiconductors-leveraged-etfs-dominate |
| XLF | -726.36 | 2026-10-14 | 2026-10-14 | public_report | https://www.etf.com/sections/daily-etf-flows/etf-fund-flows-semiconductors-leveraged-etfs-dominate |
| DRAM | -481.66 | 2026-10-14 | 2026-10-14 | public_report | https://www.etf.com/sections/daily-etf-flows/etf-fund-flows-semiconductors-leveraged-etfs-dominate |

## Polymarket 搜索覆盖与限制

2026-10-23T12:07:01.436538+00:00刷新1552候选、25主题搜索和跟踪ID；补搜Fed/AI/战争/能源/关税/政府停摆/金融/工业/软件/航天及临近事件。训练暂停页面盘口宽、成交稀薄，不引用平台AI摘要为事实；过期停摆合约不采用。九个高相关规则hash与早报一致。两页截断保留覆盖缺口，不代表找遍全市场。

## Polymarket · 值得警惕的信号

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["AI bubble burst in 2026?", "期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。", "https://polymarket.com/event/ai-bubble-burst-by"] | [8.9, {"status": "comparable", "change_pp": -0.5500000000000005}] | {"spread": 0.0040000000000000036, "volume24h_usd": 3903.024744, "liquidity_usd": 37576.99574, "quality_flags": [], "retrieved_at": "2026-10-23T12:02:36.451288+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["年底AI合约较早报回落；保留尾部风险观察而非声称警报升级。", "AI估值与融资风险"] | ["同规则价格持续上行并有经营/信用证据", "现金流和信用改善"] | [null, null] |
| ["Will WTI Crude Oil (WTI) hit (HIGH) $105 in October?", "10月交易时段内，Pyth的ICE WTI活跃月合约1分钟最终高价达到105美元即Yes；按规则提前3个交易时段换月，数据不可用时可依ICE日高低。不是月末价格，也不能以Yahoo CL=F直接结算。", "https://polymarket.com/event/what-price-will-wti-hit-in-october-2026"] | [53.0, {"status": "comparable", "change_pp": 15.000000000000002}] | {"spread": 0.040000000000000036, "volume24h_usd": 11371.049671, "liquidity_usd": 33270.6752, "quality_flags": [], "retrieved_at": "2026-10-23T12:02:36.451288+00:00", "contract_end_at": "2026-11-01T03:59:59.999000+00:00"} | ["较早报+15个百分点，大于当前4个百分点价差；能源成本传导值得警惕，仍需实物/同交割市场证据。", "能源成本→利率→成长估值"] | ["供应中断与可核验油价共同走强", "通行恢复及供应增加"] | [null, null] |

## Polymarket · 有参考价值的事件

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Strait of Hormuz traffic returns to normal by October 31?", "10月31日前IMF Portwatch海峡船舶通行7日均值任一天达到60才为Yes；非宣布开放。末日数据等待14日，有窗口内修订和明显数据错误处理。", "https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-october-31-20260810151043583"] | [0.35000000000000003, {"status": "comparable", "change_pp": -0.45000000000000007}] | {"spread": 0.001, "volume24h_usd": 115860.650046, "liquidity_usd": 244553.77016, "quality_flags": [], "retrieved_at": "2026-10-23T12:02:36.451288+00:00", "contract_end_at": "2026-11-01T03:59:00+00:00"} | ["Strait of Hormuz traffic returns to normal by October 31?；专门规则解释，变化须结合价差和经营证据。", "航运恢复速度影响供给风险溢价"] | ["IMF同口径船舶通行7日均值回升", "只有口头提议、无实际通航"] | [null, null] |
| ["Strait of Hormuz traffic returns to normal by December 31?", "期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。", "https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31"] | [11.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.009999999999999995, "volume24h_usd": 35581.737457, "liquidity_usd": 604511.6587, "quality_flags": [], "retrieved_at": "2026-10-23T12:02:36.451288+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["Strait of Hormuz traffic returns to normal by December 31?；专门规则解释，变化须结合价差和经营证据。", "能源中期风险"] | ["实际船舶数据支持改善", "封锁和袭击持续"] | [null, null] |
| ["US x Iran ceasefire continues through October 31?", "截至10月31日伊朗标准时间23:59，美国未对伊朗领土及内水实施规则列明的直接命中空袭或地对地打击才为Yes。海域/空域、拦截碎片、小型打击、网络战等不计；争议信息允许三日核验。不是所有交战方全面停火，也不等于海峡畅通。", "https://polymarket.com/event/us-iran-ceasefire-continues-throughptptpt"] | [77.5, {"status": "comparable", "change_pp": 1.0000000000000009}] | {"spread": 0.010000000000000009, "volume24h_usd": 173888.050894, "liquidity_usd": 264269.077, "quality_flags": [], "retrieved_at": "2026-10-23T12:02:36.451288+00:00", "contract_end_at": "2026-10-31T23:59:00+00:00"} | ["US x Iran ceasefire continues through October 31?；专门规则解释，变化须结合价差和经营证据。", "定义差异解释与通航低概率并存"] | ["可信报道符合专门规则", "其他交战行动不能自动当本合约失效"] | [null, null] |
| ["Will the Fed increase interest rates by 25 bps after the December 2026 meeting?", "以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。", "https://polymarket.com/event/fed-decision-in-december-20260729232808632"] | [72.5, {"status": "comparable", "change_pp": 1.5000000000000013}] | {"spread": 0.010000000000000009, "volume24h_usd": 99700.339061, "liquidity_usd": 101372.909, "quality_flags": [], "retrieved_at": "2026-10-23T12:02:36.451288+00:00", "contract_end_at": "2026-12-09T23:59:00+00:00"} | ["Will the Fed increase interest rates by 25 bps after the December 2026 meeting?；专门规则解释，变化须结合价差和经营证据。", "贴现率影响长久期资产"] | ["后续通胀及官方政策支持", "通胀缓解及政策转向"] | [null, null] |
| ["Tesla and SpaceX merger officially announced by December 31?", "2026年12月31日23:59纽约时间前，Tesla或SpaceX正式宣布双方合并或一方收购另一方的控制权即Yes；无需在期限内完成交易。控制权通常为过半权益或等效治理权；少数股权投资及仅讨论不算。以公司公告或可信报道共识核验；旧URL中的june-30不是本合约期限。", "https://polymarket.com/event/tesla-and-spacex-merger-officially-announced-by-june-30"] | [18.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.010000000000000009, "volume24h_usd": 2212.70253, "liquidity_usd": 31519.7757, "quality_flags": [], "retrieved_at": "2026-10-23T12:02:36.451288+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["Tesla and SpaceX merger officially announced by December 31?；专门规则解释，变化须结合价差和经营证据。", "航天/汽车事件溢价与融资结构"] | ["正式公告符合控制权转移要求，并核验资产价格反应", "仅委员会讨论、少数股权投资或传闻"] | [null, null] |

## Polymarket · 将要发生的事件及概率

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Will there be no change in Fed interest rates after the October 2026 meeting?", "以10月27–28日FOMC前后联邦基金目标区间上限不变结算；非25bp标准变动向上取整至25bp档；若下一会议期限仍无声明按不变档结算。", "https://polymarket.com/event/fed-decision-in-october-20260617190323537"] | [93.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.009999999999999898, "volume24h_usd": 1254333.9245760003, "liquidity_usd": 989042.4812, "quality_flags": [], "retrieved_at": "2026-10-23T12:02:36.451288+00:00", "contract_end_at": "2026-10-29T03:59:00+00:00"} | ["Will there be no change in Fed interest rates after the October 2026 meeting?；专门规则解释，变化须结合价差和经营证据。", "政策上限变化影响折现率"] | ["官方声明发布后核验", "会前预期不是实际决定"] | ["2026-10-28T14:00:00-04:00", "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm"] |

## Will there be no change in Fed interest rates after the October 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 606422 / 2589812 |
| Yes 概率 % | 93.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [4.0, 7.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [1254333.9245760003, 989042.4812] |
| 价差 pp | 1.00 |
| 到期 | 2026-10-29T03:59:00+00:00 |
| 结算规则摘要 | 以10月27–28日FOMC前后联邦基金目标区间上限不变结算；非25bp标准变动向上取整至25bp档；若下一会议期限仍无声明按不变档结算。 |
| 规则指纹 | fbc973610971c579003bb7db1464373da28fb0d8484ae204350268d22f83fb7e |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-23T11:58:04.918728Z |
| 抓取时间 | 2026-10-23T12:02:36.451288+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-october-20260617190323537 |

## US x Iran ceasefire continues through October 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1038648 / 4641065 |
| Yes 概率 % | 77.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [4.0, -4.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 1.0000000000000009} |
| 24h成交量 / 流动性 USD | [173888.050894, 264269.077] |
| 价差 pp | 1.00 |
| 到期 | 2026-10-31T23:59:00+00:00 |
| 结算规则摘要 | 截至10月31日伊朗标准时间23:59，美国未对伊朗领土及内水实施规则列明的直接命中空袭或地对地打击才为Yes。海域/空域、拦截碎片、小型打击、网络战等不计；争议信息允许三日核验。不是所有交战方全面停火，也不等于海峡畅通。 |
| 规则指纹 | 4ad99c00bba55951472643794eca27dab0743ff8891a0f80509306b4b3c87506 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-23T12:00:05.491429Z |
| 抓取时间 | 2026-10-23T12:02:36.451288+00:00 |
| 来源 | https://polymarket.com/event/us-iran-ceasefire-continues-throughptptpt |

## Strait of Hormuz traffic returns to normal by October 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 830253 / 3501950 |
| Yes 概率 % | 0.35 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.55, -0.2] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.45000000000000007} |
| 24h成交量 / 流动性 USD | [115860.650046, 244553.77016] |
| 价差 pp | 0.10 |
| 到期 | 2026-11-01T03:59:00+00:00 |
| 结算规则摘要 | 10月31日前IMF Portwatch海峡船舶通行7日均值任一天达到60才为Yes；非宣布开放。末日数据等待14日，有窗口内修订和明显数据错误处理。 |
| 规则指纹 | be893052d9d9b648fb6ffa8b901ed6d9775d1cd3d1be9f830e1dcf5d0f046390 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-23T12:00:05.491429Z |
| 抓取时间 | 2026-10-23T12:02:36.451288+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-october-31-20260810151043583 |

## Will the Fed increase interest rates by 25 bps after the December 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 770450 / 3215008 |
| Yes 概率 % | 72.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-6.0, -6.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 1.5000000000000013} |
| 24h成交量 / 流动性 USD | [99700.339061, 101372.909] |
| 价差 pp | 1.00 |
| 到期 | 2026-12-09T23:59:00+00:00 |
| 结算规则摘要 | 以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。 |
| 规则指纹 | 933a10a15eeec0ff1de30468fa20540301ed243f75cc3572d42946192f81a123 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-23T12:00:05.491429Z |
| 抓取时间 | 2026-10-23T12:02:36.451288+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-december-20260729232808632 |

## Strait of Hormuz traffic returns to normal by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 455875 / 2176270 |
| Yes 概率 % | 11.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [35581.737457, 604511.6587] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。 |
| 规则指纹 | b0c8ba27f4437b0d8ab819ae170bec118166232e39cdcaefb95bd352d29073d4 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-23T12:00:05.491429Z |
| 抓取时间 | 2026-10-23T12:02:36.451288+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31 |

## Will WTI Crude Oil (WTI) hit (HIGH) $105 in October?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1078055 / 4951227 |
| Yes 概率 % | 53.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [12.0, 20.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 15.000000000000002} |
| 24h成交量 / 流动性 USD | [11371.049671, 33270.6752] |
| 价差 pp | 4.00 |
| 到期 | 2026-11-01T03:59:59.999000+00:00 |
| 结算规则摘要 | 10月交易时段内，Pyth的ICE WTI活跃月合约1分钟最终高价达到105美元即Yes；按规则提前3个交易时段换月，数据不可用时可依ICE日高低。不是月末价格，也不能以Yahoo CL=F直接结算。 |
| 规则指纹 | 0c455b139d74a669b793323a95aea1e08486656281c457348bd488137e37ae8a |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-23T12:00:05.491429Z |
| 抓取时间 | 2026-10-23T12:02:36.451288+00:00 |
| 来源 | https://polymarket.com/event/what-price-will-wti-hit-in-october-2026 |

## AI bubble burst in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 691340 |
| Yes 概率 % | 8.90 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.45, 2.15] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.5500000000000005} |
| 24h成交量 / 流动性 USD | [3903.024744, 37576.99574] |
| 价差 pp | 0.40 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | fc153b2136a8dfbadcd169dce1add40690acb1748566b99716fe7ae8fcb07330 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-23T12:00:05.491429Z |
| 抓取时间 | 2026-10-23T12:02:36.451288+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## Tesla and SpaceX merger officially announced by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 192962 / 2252540 |
| Yes 概率 % | 18.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [2.5, -6.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [2212.70253, 31519.7757] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59纽约时间前，Tesla或SpaceX正式宣布双方合并或一方收购另一方的控制权即Yes；无需在期限内完成交易。控制权通常为过半权益或等效治理权；少数股权投资及仅讨论不算。以公司公告或可信报道共识核验；旧URL中的june-30不是本合约期限。 |
| 规则指纹 | 909906ae3b6db7e473468713ea6a1e1e4cf4c931fe247c7d3d576e7986513008 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-23T12:02:05.75822Z |
| 抓取时间 | 2026-10-23T12:02:36.451288+00:00 |
| 来源 | https://polymarket.com/event/tesla-and-spacex-merger-officially-announced-by-june-30 |

## AI bubble burst by June 30, 2027?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 4838928 |
| Yes 概率 % | 20.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [0.5, 2.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [2.43, 9518.1912] |
| 价差 pp | 1.00 |
| 到期 | 2027-07-01T03:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | bd0420587e08487fffa5050e7fd9b79ffff909a9f843d3f620207ee859462505 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-10-23T11:58:04.918728Z |
| 抓取时间 | 2026-10-23T12:02:36.451288+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## AI 压力：合约、经营与估值分开

三层分开：一、年底专门AI严重下行合约8.9%，较早报9.45%下降0.55个百分点，现价差0.4个百分点；不是产业客观崩溃概率。2027年6月底20.5%不变，但24h成交仅2.43美元、流动性不足1万美元，不赋予有效新增信息。二、H100最新仍是22日2.88美元/GPU小时、7日+10.3%；Siemens/NVIDIA官方工业AI落地、WDC/BE业绩增长属于需求尚强反证。META多年混合性质支出承诺不能算作当年资本开支或全部债务，现金回收与融资成本仍是检验重点；未经原始来源核验的CDS线索不使用。三、本次SEC五家公司披露列表核验与早报相同：NVDA 8月26日、MSFT7月29日、AMZN7月31日、GOOGL7月23日、META10月22日。前四家复用已核验FCFF底稿，当前完整收盘窗口亦相同；META租赁资产新增与净债务缺口继续阻止精确估值。公司整体情景不是AI单项价值，情景权重不是概率。

## NVDA · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | scenario_analysis |
| 财务底稿 | TTM 至 2026-07-26；最新 10-Q / filed 2026-08-26 |
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001045810.json", "checked_at": "2026-10-23T12:03:41.400519+00:00", "latest_filing_date": "2026-08-26"} |
| 观测财务数据 | {"ttm_revenue_million": 302970, "revenue_quarters": [{"end": "2025-10-26", "value": 57006000000, "filed": "2025-11-19", "duration_days": 91}, {"end": "2026-01-25", "value": 68127000000, "filed": "2026-02-25", "duration_days": 91}, {"end": "2026-04-26", "value": 81615000000, "filed": "2026-05-20", "duration_days": 91}, {"end": "2026-07-26", "value": 96221000000, "filed": "2026-08-26", "duration_days": 91}], "cash_million": 22443.0, "liquid_investments_million": 34143.0, "debt_million": 33366.0, "finance_lease_million": 0, "diluted_shares_million": 24285.0, "latest_operating_income_million": 63734.0, "observed_end": "2026-07-26", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "Revenues", "latest_reported_revenue_million": 96221.0, "income_statement_window": "最近单季度", "ttm_bridge_note": "采用同版 FY2026全年 + FY2027半年 - FY2026半年；与四季逐项求和差1百万为披露舍入差。"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json", "https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。10-Q Note14 表明融资租赁费用不重大；模型按不重大近似零，不将其称为精确零负债。未确认担保仅作为压力情景，非已到期净债务。市场化股权42783和非市场化股权51157不作为类现金；非经营资产加回为0的保守假设。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | 无 |
| 价格 USD | 212.21 |
| 基期输入 USD million / million shares | {"revenue": 302970, "net_debt": -23220.0, "diluted_shares": 24285.0, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.28856748660883513, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## NVDA · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 98.77 | -53.46 | 14.00 | 60.00 | 12.00 | 68.42 |
| 基准 | 154.12 | -27.38 | 20.00 | 65.00 | 11.00 | 74.20 |
| 乐观 | 242.58 | 14.31 | 26.00 | 70.00 | 10.00 | 79.05 |

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
| 状态 | scenario_analysis |
| 财务底稿 | TTM 至 2026-06-30；最新 10-K / filed 2026-07-29 |
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0000789019.json", "checked_at": "2026-10-23T12:03:44.479293+00:00", "latest_filing_date": "2026-07-29"} |
| 观测财务数据 | {"ttm_revenue_million": 331839.0, "revenue_quarters": [{"end": "2025-09-30", "value": 77673000000, "filed": "2025-10-29", "duration_days": 92}, {"end": "2025-12-31", "value": 81273000000, "filed": "2026-01-28", "duration_days": 92}, {"end": "2026-03-31", "value": 82886000000, "filed": "2026-04-29", "duration_days": 90}, {"end": "2026-06-30", "value": 90007000000, "filed": "2026-07-29", "duration_days": 91}], "cash_million": 20935.0, "liquid_investments_million": 55908.0, "debt_million": 40294.0, "finance_lease_million": 66594.0, "diluted_shares_million": 7453.0, "latest_operating_income_million": 155237.0, "observed_end": "2026-06-30", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "RevenueFromContractWithCustomerExcludingAssessedTax", "latest_reported_revenue_million": 331839.0, "income_statement_window": "FY2026 全年"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0000789019.json", "https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。融资租赁66594计入债务；资本开支假设涵盖新增租赁，现金支出115948加融资租赁资产新增24608为本年经济资本开支140556。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | 无 |
| 价格 USD | 521.08 |
| 基期输入 USD million / million shares | {"revenue": 331839.0, "net_debt": 30045.0, "diluted_shares": 7453.0, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.3118469138671366, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## MSFT · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 143.02 | -72.55 | 8.00 | 42.00 | 10.50 | 76.13 |
| 基准 | 266.55 | -48.85 | 14.00 | 47.00 | 9.50 | 81.05 |
| 乐观 | 484.83 | -6.96 | 20.00 | 52.00 | 8.50 | 84.97 |

## MSFT · 可复算假设

| 情景 | 假设（比例以小数表示） |
| --- | --- |
| 悲观 | {"growth": 0.08000000000000002, "start_margin": 0.4678081840892722, "operating_margin": 0.42, "tax_rate": 0.2, "da_ratio": 0.15, "capex_ratio": 0.265, "working_capital_ratio": 0.04, "wacc": 0.105, "terminal_growth": 0.025, "dilution": 0, "start_capex_ratio": 0.4235668501893991} |
| 基准 | {"growth": 0.14, "start_margin": 0.4678081840892722, "operating_margin": 0.47, "tax_rate": 0.2, "da_ratio": 0.15, "capex_ratio": 0.25, "working_capital_ratio": 0.04, "wacc": 0.095, "terminal_growth": 0.025, "dilution": 0, "start_capex_ratio": 0.4235668501893991} |
| 乐观 | {"growth": 0.2, "start_margin": 0.4678081840892722, "operating_margin": 0.52, "tax_rate": 0.2, "da_ratio": 0.15, "capex_ratio": 0.235, "working_capital_ratio": 0.04, "wacc": 0.085, "terminal_growth": 0.025, "dilution": 0, "start_capex_ratio": 0.4235668501893991} |

## MSFT · 折现率与经营下修敏感性

| WACC% | 收入CAGR% | 每股 USD |
| --- | --- | --- |
| 7.50 | 14.00 | 387.27 |
| 7.50 | 9.00 | 312.25 |
| 9.50 | 14.00 | 266.55 |
| 9.50 | 9.00 | 215.63 |
| 11.50 | 14.00 | 199.99 |
| 11.50 | 9.00 | 162.30 |

## AMZN · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | scenario_analysis |
| 财务底稿 | TTM 至 2026-06-30；最新 10-Q / filed 2026-07-31 |
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001018724.json", "checked_at": "2026-10-23T12:03:47.390917+00:00", "latest_filing_date": "2026-07-31"} |
| 观测财务数据 | {"ttm_revenue_million": 775680.0, "revenue_quarters": [{"end": "2025-09-30", "value": 180169000000, "filed": "2025-10-31", "duration_days": 92}, {"end": "2025-12-31", "value": 213386000000, "filed": "2026-02-06", "duration_days": 92}, {"end": "2026-03-31", "value": 181519000000, "filed": "2026-04-30", "duration_days": 90}, {"end": "2026-06-30", "value": 200606000000, "filed": "2026-07-31", "duration_days": 91}], "cash_million": 78213.0, "liquid_investments_million": 44775.0, "debt_million": 133320.0, "finance_lease_million": 13451.0, "diluted_shares_million": 10903.0, "latest_operating_income_million": 27461.0, "observed_end": "2026-06-30", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "RevenueFromContractWithCustomerExcludingAssessedTax", "latest_reported_revenue_million": 200606.0, "income_statement_window": "最近单季度"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001018724.json", "https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。总长期债务132995（含当前部分）加短期借款325，融资租赁13451另加；未将其他长期负债全部误作有息债务。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | 无 |
| 价格 USD | 250.38 |
| 基期输入 USD million / million shares | {"revenue": 775680.0, "net_debt": 23783.0, "diluted_shares": 10903.0, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.39019090391543154, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## AMZN · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 11.53 | -95.39 | 6.00 | 12.00 | 11.00 | 84.01 |
| 基准 | 87.42 | -65.08 | 12.00 | 17.00 | 10.00 | 83.61 |
| 乐观 | 238.05 | -4.92 | 18.00 | 22.00 | 9.00 | 86.04 |

## AMZN · 可复算假设

| 情景 | 假设（比例以小数表示） |
| --- | --- |
| 悲观 | {"growth": 0.06, "start_margin": 0.1368902226254449, "operating_margin": 0.12000000000000001, "tax_rate": 0.23, "da_ratio": 0.12, "capex_ratio": 0.195, "working_capital_ratio": 0.02, "wacc": 0.11, "terminal_growth": 0.025, "dilution": 0, "start_capex_ratio": 0.23} |
| 基准 | {"growth": 0.12, "start_margin": 0.1368902226254449, "operating_margin": 0.17, "tax_rate": 0.23, "da_ratio": 0.12, "capex_ratio": 0.18, "working_capital_ratio": 0.02, "wacc": 0.1, "terminal_growth": 0.025, "dilution": 0, "start_capex_ratio": 0.23} |
| 乐观 | {"growth": 0.18, "start_margin": 0.1368902226254449, "operating_margin": 0.22000000000000003, "tax_rate": 0.23, "da_ratio": 0.12, "capex_ratio": 0.16499999999999998, "working_capital_ratio": 0.02, "wacc": 0.09000000000000001, "terminal_growth": 0.025, "dilution": 0, "start_capex_ratio": 0.23} |

## AMZN · 折现率与经营下修敏感性

| WACC% | 收入CAGR% | 每股 USD |
| --- | --- | --- |
| 8.00 | 12.00 | 125.55 |
| 8.00 | 7.00 | 100.46 |
| 10.00 | 12.00 | 87.42 |
| 10.00 | 7.00 | 70.07 |
| 12.00 | 12.00 | 65.58 |
| 12.00 | 7.00 | 52.65 |

## GOOGL · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | scenario_analysis |
| 财务底稿 | TTM 至 2026-06-30；最新 10-Q / filed 2026-07-23 |
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001652044.json", "checked_at": "2026-10-23T12:03:50.294117+00:00", "latest_filing_date": "2026-07-23"} |
| 观测财务数据 | {"ttm_revenue_million": 445867.0, "revenue_quarters": [{"end": "2025-09-30", "value": 102346000000, "filed": "2025-10-30", "duration_days": 92}, {"end": "2025-12-31", "value": 113829000000, "filed": "2026-02-05", "duration_days": 92}, {"end": "2026-03-31", "value": 109896000000, "filed": "2026-04-30", "duration_days": 90}, {"end": "2026-06-30", "value": 119796000000, "filed": "2026-07-23", "duration_days": 91}], "cash_million": 55911.0, "liquid_investments_million": 186563.0, "debt_million": 100164, "finance_lease_million": 2590.0, "diluted_shares_million": 12309.0, "latest_operating_income_million": 40770.0, "observed_end": "2026-06-30", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "Revenues", "latest_reported_revenue_million": 119796.0, "income_statement_window": "最近单季度"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001652044.json", "https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/goog-20260630.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。优先股按完全转换处理：季度稀释股数12309减已计入的16，再加合同最大转换股数54.45825；不再扣19000优先股本金。未来3年优先股息按年1203.125、10%折现约2991.99计入权益桥调整，此为保守假设；capped call 未赋值。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | {"preferred_coupon_pv_million": 2991.9938016528904, "discount_rate": 0.1, "years": 3} |
| 价格 USD | 324.22 |
| 基期输入 USD million / million shares | {"revenue": 445867.0, "net_debt": -136728.0061983471, "diluted_shares": 12347.45825, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.3783029567533228, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## GOOGL · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 66.88 | -79.37 | 7.00 | 31.00 | 11.00 | 79.41 |
| 基准 | 131.94 | -59.30 | 13.00 | 36.00 | 10.00 | 82.80 |
| 乐观 | 250.29 | -22.80 | 19.00 | 41.00 | 9.00 | 85.75 |

## GOOGL · 可复算假设

| 情景 | 假设（比例以小数表示） |
| --- | --- |
| 悲观 | {"growth": 0.07, "start_margin": 0.3403285585495342, "operating_margin": 0.31, "tax_rate": 0.2, "da_ratio": 0.09, "capex_ratio": 0.21500000000000002, "working_capital_ratio": 0.03, "wacc": 0.11, "terminal_growth": 0.025, "dilution": 0, "start_capex_ratio": 0.36} |
| 基准 | {"growth": 0.13, "start_margin": 0.3403285585495342, "operating_margin": 0.36, "tax_rate": 0.2, "da_ratio": 0.09, "capex_ratio": 0.2, "working_capital_ratio": 0.03, "wacc": 0.1, "terminal_growth": 0.025, "dilution": 0, "start_capex_ratio": 0.36} |
| 乐观 | {"growth": 0.19, "start_margin": 0.3403285585495342, "operating_margin": 0.41, "tax_rate": 0.2, "da_ratio": 0.09, "capex_ratio": 0.185, "working_capital_ratio": 0.03, "wacc": 0.09000000000000001, "terminal_growth": 0.025, "dilution": 0, "start_capex_ratio": 0.36} |

## GOOGL · 折现率与经营下修敏感性

| WACC% | 收入CAGR% | 每股 USD |
| --- | --- | --- |
| 8.00 | 13.00 | 182.92 |
| 8.00 | 8.00 | 149.41 |
| 10.00 | 13.00 | 131.94 |
| 10.00 | 8.00 | 108.70 |
| 12.00 | 13.00 | 102.73 |
| 12.00 | 8.00 | 85.34 |

## META · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | unavailable |
| 财务底稿 | 2026Q3 ended 2026-09-30 |
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001326801.json", "checked_at": "2026-10-23T12:03:53.098115+00:00", "latest_filing_date": "2026-10-22"} |
| 观测财务数据 | {"revenue_million": 64601, "operating_cashflow_million": 32790, "reported_capex_including_finance_lease_principal_million": 34910, "company_defined_fcf_million": -2120, "diluted_shares_million": 2573, "reported_operating_income_million": 12988, "legal_charge_million": 9900, "observed_end": "2026-09-30", "published_at": "2026-10-21T16:01:00-04:00", "unit": "USD million; shares million", "noncancelable_commitments_million": 454520, "leases_not_commenced_million": 355730, "contingent_cloud_capacity_max_million": 14720, "restricted_cash_reclassified_million": 10800, "commitments_due_2026_million": 45850, "commitments_due_2027_million": 121410} |
| 来源 | ["https://www.prnewswire.com/news-releases/meta-reports-third-quarter-2026-results-302915964.html", "https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm"] |
| 口径 | 公司FCF扣除融资租赁本金，不能直接代替模型FCFF；融资租赁负债/新增资产未齐，不假设零。法律费用不全归AI经营。 |
| 主观假设说明 | 缺失 |
| 权益桥额外假设 | 无 |
| 缺失原因 | 10月22日新10-Q已核验；多年承诺与受限资金已记录，但完整融资租赁负债及资产新增口径未齐，不将不同承诺简单当现有债务，暂停精确FCFF反推。 |

## 下跌后的修复是否值得相信

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 今晚开盘消化WDC/BE财报与密歇根消费者通胀预期 |
| 关联标的 | ["QQQ", "SMH", "NVDA", "META", "WDC", "BE"] |
| 确认条件 | 先守住22日QQQ/SMH低点701.90/520.53，开盘30分钟后收回当日常规VWAP、回踩不破且相对SPY转强；随后连续两次收盘站稳动态20日线。目前20日线QQQ737.24、SMH589.51，仅参考，非下单价。 今晚22:00北京调查发布后的二次回踩，比开盘第一根阳线更有参考价值；需用实际常规分钟数据计算VWAP。 |
| 失效条件 | 破前低后反抽仍受压、相对强弱继续恶化，或新指引/现金回收转弱；单次穿越不做唯一判断。 |
| 观察期限 | 下一交易日至5个交易日 |
| 反证 | WDC/BE仍低于昨日收盘，油价风险合约抬升；盘前低流动性不能证明反弹持续。 |
| 状态 | 盘前弱修复，常规时段确认待发生 |

## 供给冲击或信用扩散的风险剧本

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 可核验能源供应变化、FOMC与融资条件 |
| 关联标的 | ["XLE", "GLD", "QQQ", "TLT"] |
| 确认条件 | 油价专门合约53%相较早报上升15个百分点；只有同交割油价持续上涨，并伴随信用利差、波动与市场参与面恶化，才提高系统性风险判断。VIX25/HY400bp仅情景研究阈值，不是客观分界。 |
| 失效条件 | 实际通航改善、油价回落且成长现金回收和价格承接改善。 |
| 观察期限 | 1–10个交易日 |
| 反证 | 等权、防御上涨；最新滞后HY未扩大，近月VIX仍低于三个月，不能认定已系统性失控。 |
| 状态 | 风险观察，未全面确认 |

## 跨期比较与上期剧本复核

比较10月23日07:15早报：没有新完整交易日，收盘技术指标不变。盘前WDC/BE比早间盘后有修复，却仍低于22日常规收盘；QQQ近持平、SMH小涨，尚未满足开盘回踩或连续收盘确认。九合约rule_hash均一致：10月不变93.5%不变，12月+25bp71%→72.5%（+1.5个百分点），油价触105 38%→53%（+15，价差4），月底通航0.8%→0.35%（−0.45），停火76.5%→77.5%（+1），年底AI9.45%→8.9%（−0.55）。这些不同事件不可相加。Cboe官方VIX补齐22日19.03；H100未有新日读数。

## 可计算的跨期变化

```json
[
  {
    "mode": "daily",
    "baseline": "reports/daily/2026-10-22/20261022T232116.893782Z/evidence.json",
    "baseline_cutoff": "2026-10-22T23:21:14.008837+00:00",
    "close_change_pct": {
      "SPY": 0.0,
      "QQQ": 0.0,
      "IWM": 0.0,
      "RSP": 0.0,
      "GLD": 0.0,
      "GC=F": 0.5148976181966081,
      "CL=F": 0.47474870778092537,
      "BZ=F": 0.32800984678851286,
      "TLT": 0.0,
      "UUP": 0.0,
      "HYG": 0.0,
      "LQD": 0.0,
      "^VIX": 0.0,
      "^VIX3M": 0.0,
      "^VVIX": 0.0,
      "^MOVE": 0.0011211422797474668,
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
      "SPY": {
        "change_pct": -0.26304424639785884,
        "from_observed_at": "2026-10-22T23:13:11+00:00",
        "to_observed_at": "2026-10-23T12:02:10+00:00"
      },
      "QQQ": {
        "change_pct": 0.09951946316357763,
        "from_observed_at": "2026-10-22T23:15:15+00:00",
        "to_observed_at": "2026-10-23T12:01:53+00:00"
      },
      "SMH": {
        "change_pct": 0.7333187079256342,
        "from_observed_at": "2026-10-22T23:14:50+00:00",
        "to_observed_at": "2026-10-23T12:01:11+00:00"
      },
      "META": {
        "change_pct": -0.14072310023813817,
        "from_observed_at": "2026-10-22T23:15:12+00:00",
        "to_observed_at": "2026-10-23T12:02:16+00:00"
      },
      "NVDA": {
        "change_pct": -0.006532068461717611,
        "from_observed_at": "2026-10-22T23:15:11+00:00",
        "to_observed_at": "2026-10-23T12:02:15+00:00"
      },
      "WDC": {
        "change_pct": 2.739726027397249,
        "from_observed_at": "2026-10-22T23:15:17+00:00",
        "to_observed_at": "2026-10-23T12:02:19+00:00"
      },
      "BE": {
        "change_pct": 2.655212807497076,
        "from_observed_at": "2026-10-22T23:15:13+00:00",
        "to_observed_at": "2026-10-23T12:02:19+00:00"
      }
    },
    "macro_change": {
      "DGS2": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-10-21"
      },
      "BAMLH0A0HYM2": {
        "change": 0.0,
        "unit": "percentage_points",
        "observation_date": "2026-10-21"
      },
      "BAMLC0A0CM": {
        "change": 0.0,
        "unit": "percentage_points",
        "observation_date": "2026-10-21"
      },
      "DGS10": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-10-21"
      },
      "DFII10": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-10-21"
      },
      "T10YIE": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-10-22"
      },
      "STLFSI4": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-16"
      },
      "CBOE_VIX": {
        "change": 2.3500000000000014,
        "unit": "index",
        "observation_date": "2026-10-22"
      },
      "GPRD": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-19"
      },
      "GPRD_ACT": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-19"
      },
      "GPRD_THREAT": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-19"
      },
      "GPRD_MA7": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-19"
      },
      "GPRD_MA30": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-19"
      }
    },
    "event_probability_change": {
      "2589812": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "4641065": {
        "status": "comparable",
        "change_pp": 1.0000000000000009
      },
      "3501950": {
        "status": "comparable",
        "change_pp": -0.45000000000000007
      },
      "3215008": {
        "status": "comparable",
        "change_pp": 1.5000000000000013
      },
      "2176270": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "4951227": {
        "status": "comparable",
        "change_pp": 15.000000000000002
      },
      "691340": {
        "status": "comparable",
        "change_pp": -0.5500000000000005
      },
      "2252540": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "4838928": {
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
    "event": "美股常规开盘",
    "date": "2026-10-23T09:30:00-04:00",
    "source": "tc:get_trading_calendar"
  },
  {
    "event": "密歇根10月终值：关注消费者通胀预期；官方确认10ET",
    "date": "2026-10-23T10:00:00-04:00",
    "source": "https://www.sca.isr.umich.edu/"
  },
  {
    "event": "FOMC会议结束及政策决定",
    "date": "2026-10-28T14:00:00-04:00",
    "source": "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm"
  }
]
```

## 新闻事件去重与时间

| 事件 | 摘要 | 发生时间（未知留空） | 各来源发布时间 / 抓取时间 |
| --- | --- | --- | --- |
| oct22-close | 科技与存储领跌；以ETF收盘独立核验，指数与ETF跌幅分别展示。 | 2026-10-22T16:00:00-04:00 | [{"source": "https://www.cls.cn/detail/2512863", "published_at": "2026-10-22T20:01:03+00:00", "retrieved_at": "2026-10-23T12:07:01.436538+00:00"}] |
| wdc-q1 | WDC收入及指引增长，但盘后价格仍弱；HDD证据不等于NAND/HBM经营结果。 | 缺失 | [{"source": "https://investor.wdc.com/node/28921/pdf", "published_at": null, "retrieved_at": "2026-10-23T12:07:01.436538+00:00"}] |
| be-q3 | BE收入12.358亿美元、同比+138.1%，全年收入指引升至44–46亿美元；盘后价格低于收盘。 | 缺失 | [{"source": "https://www.bloomenergy.com/news/bloom-energy-reports-record-third-quarter-2026-financial-results-and-raises-full-year-2026-guidance/", "published_at": null, "retrieved_at": "2026-10-23T12:07:01.436538+00:00"}] |
| lrcx-guidance | 此前21日发布的收入82.19亿美元、下一季指引86亿美元±4亿美元，在22日交易消化。 | 缺失 | [{"source": "https://investor.lamresearch.com/2026-10-21-Lam-Research-Corporation-Reports-Financial-Results-for-the-Quarter-Ended-September-27,-2026", "published_at": null, "retrieved_at": "2026-10-23T12:07:01.436538+00:00"}] |
| siemens-industrial-ai | 10月22日Siemens官方公告与NVIDIA推进工业AI落地；未核验新增订单金额。 | 缺失 | [{"source": "https://press.siemens.com/global/nl/node/7478", "published_at": null, "retrieved_at": "2026-10-23T12:07:01.436538+00:00"}] |
| michigan-next | 官网仍为10月初值，终值将于23日10ET发布；本次未发生。 | 缺失 | [{"source": "https://www.sca.isr.umich.edu/", "published_at": null, "retrieved_at": "2026-10-23T12:07:01.436538+00:00"}] |
| oil-conflict | 盘前油价存在交割/时间口径冲突，WTI合约预期明显变化；不采用冲突Brent数值判断方向。 | 缺失 | [{"source": "https://apnews.com/article/7b47ef3b037bfba4e34f685329b9b963", "published_at": null, "retrieved_at": "2026-10-23T12:07:01.436538+00:00"}] |

## 覆盖范围与数据缺口

```json
[
  "CNN原接口418、官网受限；不使用替代情绪分数。",
  "FRED信用、名义/实际利率仍截至21日；GPR截至19日、STLFSI截至16日，不当实时。",
  "tc报价全部相同请求时戳且价格为昨日收盘，设为成交时戳未验证；当前由Yahoo分钟时间补充。",
  "广域新闻50条has_more，最早时点见本地原包；核心7标的high补查25条无has_more但仍非全市场覆盖。tc当前实际返回cls/twitter/financialjuice等平台，不能只按工具旧描述解释覆盖。",
  "Polymarket若干主题两页截断；AI2027合约24h成交仅2.43美元、流动性不足1万美元；完整订单簿不可得。",
  "当前19板块ETF连续份额、拆分桥及净申赎缺失；发行人单点/ICI截至14日窗口不能作为当前流量。",
  "Brent Yahoo109.83与AP114.92报价不一致；交割与时点未厘清，ICE动态页无可核验报价，不使用该差异判方向。",
  "PMI辅助日历显示今晚9:45ET，但一级日历403；不虚构发布结果。密歇根官方终值10ET已确认。",
  "常规开盘尚未来到，未提供今日常规VWAP；全市场成分广度、盈利修正一致预期及CME独立政策定价不可得。",
  "META融资租赁资产新增及净债务口径缺失，继续暂停精确估值；前四家底稿复用并本次重新检查最新披露。",
  "DRAM长历史不足；财报电话会细节未全量核对。",
  "原始采集存在请求失败，见采集质量记录",
  "META 估值: 10月22日新10-Q已核验；多年承诺与受限资金已记录，但完整融资租赁负债及资产新增口径未齐，不将不同承诺简单当现有债务，暂停精确FCFF反推。",
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
  "tc 报价质量 unverified_trade_timestamp: MSFT, AMZN, GOOGL；不作为新成交证据",
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
  "指标缺失/历史不足: prices.^VIX.volume_vs_previous20_ratio, prices.^VIX3M.volume_vs_previous20_ratio, prices.^VVIX.volume_vs_previous20_ratio, prices.^MOVE.volume_vs_previous20_ratio, prices.DRAM.sma200, prices.DRAM.distance_sma200_pct, quotes.MSFT.value, quotes.AMZN.value, quotes.GOOGL.value"
]
```

## 来源、时间与核验记录

```json
[
  {
    "url": "https://www.silicondata.com/products/silicon-index/h100",
    "checked_at": "2026-10-23T12:07:01.436538+00:00",
    "note": "仍为22日带日期读数"
  },
  {
    "url": "https://www.ici.org/research/stats/etf_flows",
    "checked_at": "2026-10-23T12:07:01.436538+00:00",
    "note": "最新窗口10月14日；不冒充22日流量"
  },
  {
    "url": "https://www.ssga.com/us/en/individual/etfs/state-street-spdr-sp-500-etf-trust-spy",
    "checked_at": "2026-10-23T12:07:01.436538+00:00",
    "note": "22日NAV/份额单点"
  },
  {
    "url": "https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/",
    "checked_at": "2026-10-23T12:07:01.436538+00:00",
    "note": "22日NAV/净资产单点"
  },
  {
    "url": "https://www.cnn.com/markets/fear-and-greed",
    "checked_at": "2026-10-23T12:07:01.436538+00:00",
    "note": "网页受限/接口418"
  },
  {
    "url": "https://press.siemens.com/global/nl/node/7478",
    "checked_at": "2026-10-23T12:07:01.436538+00:00",
    "note": "官方正文Requests200；新工业AI产品不等于营收"
  },
  {
    "url": "https://www.sca.isr.umich.edu/",
    "checked_at": "2026-10-23T12:07:01.436538+00:00",
    "note": "官方下一发布时点与现有初值"
  },
  {
    "url": "https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm",
    "checked_at": "2026-10-23T12:07:01.436538+00:00",
    "note": "9月16日官方政策决定"
  },
  {
    "url": "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm",
    "checked_at": "2026-10-23T12:07:01.436538+00:00",
    "note": "会议日期"
  },
  {
    "url": "https://investor.wdc.com/node/28921/pdf",
    "checked_at": "2026-10-23T12:07:01.436538+00:00",
    "note": "官方Q1FY27"
  },
  {
    "url": "https://www.bloomenergy.com/news/bloom-energy-reports-record-third-quarter-2026-financial-results-and-raises-full-year-2026-guidance/",
    "checked_at": "2026-10-23T12:07:01.436538+00:00",
    "note": "官方Q3FY26"
  },
  {
    "url": "https://www.ice.com/products/219/Brent-Crude-Futures/data",
    "checked_at": "2026-10-23T12:07:01.436538+00:00",
    "note": "未取得同交割实时值"
  },
  {
    "url": "https://www.cmegroup.com/markets/energy/crude-oil/light-sweet-crude.quotes.html",
    "checked_at": "2026-10-23T12:07:01.436538+00:00",
    "note": "公开页未返回可核验现价"
  },
  {
    "url": "https://www.kiplinger.com/investing/economy/this-weeks-economic-calendar",
    "checked_at": "2026-10-23T12:07:01.436538+00:00",
    "note": "辅助日历提示PMI9:45ET；一级来源403，未列为官方确认"
  },
  {
    "url": "https://polymarket.com/event/which-ai-labs-announce-a-training-pause-by-october-31",
    "checked_at": "2026-10-23T12:07:01.436538+00:00",
    "note": "新发现候选盘口宽/低成交，未纳入定量预警"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SPY",
    "checked_at": "2026-10-23T12:07:01.436538+00:00",
    "note": "实际分钟时点报价"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/QQQ",
    "checked_at": "2026-10-23T12:07:01.436538+00:00",
    "note": "实际分钟时点报价"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SMH",
    "checked_at": "2026-10-23T12:07:01.436538+00:00",
    "note": "实际分钟时点报价"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/META",
    "checked_at": "2026-10-23T12:07:01.436538+00:00",
    "note": "实际分钟时点报价"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NVDA",
    "checked_at": "2026-10-23T12:07:01.436538+00:00",
    "note": "实际分钟时点报价"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/WDC",
    "checked_at": "2026-10-23T12:07:01.436538+00:00",
    "note": "实际分钟时点报价"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/BE",
    "checked_at": "2026-10-23T12:07:01.436538+00:00",
    "note": "实际分钟时点报价"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0001045810.json",
    "checked_at": "2026-10-23T12:03:41.400519+00:00",
    "note": "最新披露列表，本次重新检查"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0000789019.json",
    "checked_at": "2026-10-23T12:03:44.479293+00:00",
    "note": "最新披露列表，本次重新检查"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0001018724.json",
    "checked_at": "2026-10-23T12:03:47.390917+00:00",
    "note": "最新披露列表，本次重新检查"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0001652044.json",
    "checked_at": "2026-10-23T12:03:50.294117+00:00",
    "note": "最新披露列表，本次重新检查"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0001326801.json",
    "checked_at": "2026-10-23T12:03:53.098115+00:00",
    "note": "最新披露列表，本次重新检查"
  }
]
```

## 付费信源建议（未订阅）

```json
[
  {
    "product": "Silicon Data历史序列",
    "gap": "补足同型号租金连续阈值及回收周期研究；未订阅。",
    "url": "https://www.silicondata.com/pricing",
    "checked_at": "2026-10-21T23:23:48.175382+00:00"
  }
]
```
