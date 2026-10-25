# 每日交易总结 · 2026-10-23

## 一分钟读懂 · Agent 摘要

### 当前判断

初步缓和，反弹仍待确认。期货已开盘，但美股常规时段尚无新承接证据。

### 与上次相比

较昨晚，补核验SpaceX大额GPU融资消息；H100租金升至2.89美元。沙特管线风险合约反升、WTI触价合约下降，信号并不一致。

### 最重要的信号

- 23:08UTC延迟报价：12月ES/NQ约+0.29%/+0.47%、WTI约−0.98%；只是开周初步修复。
- AI需求和融资可得与现金回报不足可以同时成立，不能由融资额推出盈利。
- 周五SPY与等权仍下跌；VIX19.45和信用数据尚不能检验周末消息。

### 接下来观察

- 今晚QQQ709.30、SMH533.34收复并回踩守住，SPY/RSP同步，才增加反弹可信度；失守701.16/521.47则警惕。
- 软件/云优先看承接，能源防油价回落引发回吐；半导体等价格和指引共同确认。
- 27日STX、28日FOMC/微软、29日GDP/PCE及Amazon/Sandisk，重点看现金回报而非只看EPS。

### 不要忽略

现货价格仍至23日；期货约延迟10分钟。CNN、完整广度与当期板块净申赎缺失；预测报价不是客观概率。

## 研究结论

北京时间10月26日早报：期指小幅修复、油价回落提供初步缓和，尚不足确认反弹可靠。AI融资与需求证据增强，但现金回报未被证明；本周FOMC和科技财报是主要检验。

## 时点与口径

| 项目 | 内容 |
| --- | --- |
| 模式 | 每日交易总结 |
| 常规交易窗口 | 2026-10-23 → 2026-10-23（纽约交易日） |
| 截止·纽约 | 2026-10-25T19:20:31.284317-04:00 |
| 截止·北京 | 2026-10-26T07:20:31.284317+08:00 |
| 实际生成时间 | 2026-10-25T23:20:31.942212+00:00 |
| 市场阶段 | 休市 |
| 下一交易日 | 2026-10-26 |
| 运行重点 | 全市场 |
| 上一版本 | reports/daily/2026-10-23/20261025T120902.061174Z/evidence.json |
| 质量 | partial |
| Daily 北京时间计划时段 | 2026-10-26T07:15:00+08:00 |

## 采集、补查与剩余缺口

| 目标 | 补查结果 | 来源 | 观测 / 抓取时间 | 说明 |
| --- | --- | --- | --- | --- |
| 1147445 | 已校验接入 | https://gamma-api.polymarket.com/events/1147445 | 2026-10-25T23:14:34.458538+00:00 / 2026-10-25T23:14:34.458538+00:00 | Gamma retrieval snapshot, not last trade timestamp; settlement reviewed |

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
| prices.SPY.value | 759.97 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_1d_pct | -0.52 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_5d_pct | -0.43 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_20d_pct | -1.48 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_60d_pct | 2.72 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_1d_pp | 0.00 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_5d_pp | 0.00 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_20d_pp | 0.00 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_60d_pp | 0.00 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma20 | 770.15 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma50 | 766.90 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma200 | 724.00 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma20_pct | -1.32 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma50_pct | -0.90 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma200_pct | 4.97 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_sma | 7.18 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_pct | 0.94 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.drawdown_from_63d_high_pct | -2.45 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.volume_vs_previous20_ratio | 0.82 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SPY/history/ |
| prices.QQQ.value | 704.40 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_1d_pct | -0.01 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_5d_pct | -0.76 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_20d_pct | -5.39 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_60d_pct | 3.16 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_1d_pp | 0.51 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_5d_pp | -0.33 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_20d_pp | -3.91 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_60d_pp | 0.44 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma20 | 735.24 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma50 | 725.44 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma200 | 676.10 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma20_pct | -4.19 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma50_pct | -2.90 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma200_pct | 4.19 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_sma | 12.06 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_pct | 1.71 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.drawdown_from_63d_high_pct | -7.27 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.volume_vs_previous20_ratio | 0.82 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.IWM.value | 275.75 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_1d_pct | -0.33 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_5d_pct | 1.96 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_20d_pct | -2.21 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_60d_pct | -5.51 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_1d_pp | 0.19 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_5d_pp | 2.39 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_20d_pp | -0.73 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_60d_pp | -8.23 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma20 | 277.19 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma50 | 286.09 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma200 | 277.17 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma20_pct | -0.52 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma50_pct | -3.61 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma200_pct | -0.51 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_sma | 3.69 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_pct | 1.34 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.drawdown_from_63d_high_pct | -9.38 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.volume_vs_previous20_ratio | 0.81 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IWM/history/ |
| prices.RSP.value | 216.54 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_1d_pct | -0.77 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_5d_pct | 1.14 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_20d_pct | 2.57 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_60d_pct | 0.92 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_1d_pp | -0.25 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_5d_pp | 1.57 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_20d_pp | 4.05 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_60d_pp | -1.80 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma20 | 212.66 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma50 | 214.94 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma200 | 205.95 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma20_pct | 1.82 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma50_pct | 0.74 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma200_pct | 5.14 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_sma | 2.08 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_pct | 0.96 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.drawdown_from_63d_high_pct | -2.43 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.volume_vs_previous20_ratio | 0.73 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/RSP/history/ |
| prices.GLD.value | 366.61 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_1d_pct | -0.65 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_5d_pct | -4.03 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_20d_pct | -6.81 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_60d_pct | -2.80 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_1d_pp | -0.13 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_5d_pp | -3.60 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_20d_pp | -5.34 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_60d_pp | -5.52 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma20 | 379.09 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma50 | 394.50 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma200 | 414.21 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma20_pct | -3.29 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma50_pct | -7.07 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma200_pct | -11.49 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_sma | 5.33 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_pct | 1.45 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.drawdown_from_63d_high_pct | -14.36 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.volume_vs_previous20_ratio | 1.23 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GC=F.value | 4,007.90 | USD_per_troy_ounce | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_1d_pct | -1.29 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_5d_pct | -4.14 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_20d_pct | -7.25 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_60d_pct | -2.25 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_1d_pp | -0.77 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_5d_pp | -3.71 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_20d_pp | -5.77 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_60d_pp | -4.97 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma20 | 4,155.26 | USD_per_troy_ounce | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma50 | 4,341.87 | USD_per_troy_ounce | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma200 | 4,532.90 | USD_per_troy_ounce | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma20_pct | -3.55 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma50_pct | -7.69 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma200_pct | -11.58 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_sma | 71.89 | USD_per_troy_ounce | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_pct | 1.79 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.drawdown_from_63d_high_pct | -14.69 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.volume_vs_previous20_ratio | 1.42 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.CL=F.value | 103.27 | USD_per_barrel | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_1d_pct | 3.82 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_5d_pct | 1.83 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_20d_pct | 11.75 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_60d_pct | 23.54 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_1d_pp | 4.34 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_5d_pp | 2.26 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_20d_pp | 13.23 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_60d_pp | 20.82 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma20 | 94.73 | USD_per_barrel | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma50 | 92.93 | USD_per_barrel | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma200 | 85.29 | USD_per_barrel | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma20_pct | 9.02 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma50_pct | 11.13 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma200_pct | 21.09 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_sma | 4.38 | USD_per_barrel | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_pct | 4.24 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.drawdown_from_63d_high_pct | -2.42 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.volume_vs_previous20_ratio | 1.08 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.BZ=F.value | 116.72 | USD_per_barrel | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_1d_pct | 3.14 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_5d_pct | 6.24 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_20d_pct | 11.89 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_60d_pct | 31.10 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_1d_pp | 3.66 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_5d_pp | 6.67 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_20d_pp | 13.36 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_60d_pp | 28.38 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma20 | 105.86 | USD_per_barrel | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma50 | 100.83 | USD_per_barrel | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma200 | 91.17 | USD_per_barrel | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma20_pct | 10.25 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma50_pct | 15.76 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma200_pct | 28.02 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_sma | 3.98 | USD_per_barrel | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_pct | 3.41 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.drawdown_from_63d_high_pct | 0.00 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.volume_vs_previous20_ratio | 0.96 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.TLT.value | 81.34 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_1d_pct | -0.49 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_5d_pct | 1.61 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_20d_pct | 2.96 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_60d_pct | -0.59 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_1d_pp | 0.03 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_5d_pp | 2.04 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_20d_pp | 4.43 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_60d_pp | -3.31 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma20 | 78.73 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma50 | 80.26 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma200 | 83.31 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma20_pct | 3.32 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma50_pct | 1.34 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma200_pct | -2.36 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_sma | 0.83 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_pct | 1.02 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.drawdown_from_63d_high_pct | -2.29 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.volume_vs_previous20_ratio | 0.70 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/TLT/history/ |
| prices.UUP.value | 28.96 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_1d_pct | 0.21 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_5d_pct | 0.14 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_20d_pct | 1.19 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_60d_pct | 2.91 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_1d_pp | 0.73 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_5d_pp | 0.57 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_20d_pp | 2.66 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_60d_pp | 0.19 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma20 | 28.94 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma50 | 28.48 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma200 | 27.88 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma20_pct | 0.06 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma50_pct | 1.67 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma200_pct | 3.87 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_sma | 0.12 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_pct | 0.42 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.drawdown_from_63d_high_pct | -0.58 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.volume_vs_previous20_ratio | 0.64 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/UUP/history/ |
| prices.HYG.value | 77.05 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_1d_pct | -0.06 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_5d_pct | 0.25 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_20d_pct | -0.60 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_60d_pct | -1.60 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_1d_pp | 0.46 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_5d_pp | 0.68 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_20d_pp | 0.88 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_60d_pp | -4.32 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma20 | 77.03 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma50 | 77.95 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma200 | 77.89 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma20_pct | 0.02 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma50_pct | -1.15 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma200_pct | -1.08 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_sma | 0.28 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_pct | 0.37 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.drawdown_from_63d_high_pct | -2.63 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.volume_vs_previous20_ratio | 0.88 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/HYG/history/ |
| prices.LQD.value | 103.85 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_1d_pct | -0.41 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_5d_pct | 0.44 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_20d_pct | 1.05 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_60d_pct | -1.15 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_1d_pp | 0.11 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_5d_pp | 0.86 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_20d_pp | 2.53 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_60d_pp | -3.87 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma20 | 102.63 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma50 | 103.87 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma200 | 105.91 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma20_pct | 1.18 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma50_pct | -0.02 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma200_pct | -1.95 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_sma | 0.64 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_pct | 0.62 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.drawdown_from_63d_high_pct | -1.99 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.volume_vs_previous20_ratio | 0.82 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/LQD/history/ |
| prices.^VIX.value | 19.45 | index | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_1d_pct | 2.21 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_5d_pct | -2.70 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_20d_pct | 30.80 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_60d_pct | 21.64 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_1d_pp | 2.73 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_5d_pp | -2.27 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_20d_pp | 32.28 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_60d_pp | 19.65 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma20 | 16.54 | index | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma50 | 15.94 | index | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma200 | 18.21 | index | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma20_pct | 17.62 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma50_pct | 22.06 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma200_pct | 6.82 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_sma | 1.89 | index | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_pct | 9.72 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.drawdown_from_63d_high_pct | -5.86 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-23 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX3M.value | 20.48 | index | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_1d_pct | 1.79 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_5d_pct | -0.10 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_20d_pct | 14.22 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_60d_pct | 5.03 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_1d_pp | 2.31 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_5d_pp | 0.33 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_20d_pp | 15.70 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_60d_pp | 2.31 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma20 | 18.60 | index | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma50 | 18.49 | index | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma200 | 20.48 | index | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma20_pct | 10.09 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma50_pct | 10.79 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma200_pct | 0.01 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_sma | 1.09 | index | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_pct | 5.33 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.drawdown_from_63d_high_pct | -4.74 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-23 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VVIX.value | 109.70 | index | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_1d_pct | 1.63 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_5d_pct | -0.19 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_20d_pct | 24.89 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_60d_pct | 15.89 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_1d_pp | 2.15 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_5d_pp | 0.24 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_20d_pp | 26.36 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_60d_pp | 13.17 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma20 | 92.88 | index | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma50 | 90.58 | index | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma200 | 98.68 | index | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma20_pct | 18.11 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma50_pct | 21.11 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma200_pct | 11.16 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_sma | 9.50 | index | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_pct | 8.66 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.drawdown_from_63d_high_pct | -0.19 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-23 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^MOVE.value | 103.31 | index | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_1d_pct | -3.30 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_5d_pct | 2.19 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_20d_pct | -1.21 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_60d_pct | 39.27 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_1d_pp | -2.78 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_5d_pp | 2.62 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_20d_pp | -0.27 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_60d_pp | 34.83 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma20 | 103.18 | index | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma50 | 87.80 | index | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma200 | 76.69 | index | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma20_pct | 0.12 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma50_pct | 17.67 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma200_pct | 34.71 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_sma | 5.67 | index | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_pct | 5.49 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.drawdown_from_63d_high_pct | -9.06 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-23 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.NVDA.value | 210.96 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_1d_pct | -0.59 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_5d_pct | -1.48 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_20d_pct | -6.27 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_60d_pct | 8.28 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_1d_pp | -0.07 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_5d_pp | -1.05 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_20d_pp | -4.79 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_60d_pp | 5.56 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma20 | 225.54 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma50 | 222.39 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma200 | 203.36 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma20_pct | -6.47 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma50_pct | -5.14 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma200_pct | 3.74 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_sma | 5.98 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_pct | 2.83 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.drawdown_from_63d_high_pct | -11.82 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.volume_vs_previous20_ratio | 0.76 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.MSFT.value | 524.51 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_1d_pct | 0.66 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_5d_pct | -0.86 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_20d_pct | 1.62 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_60d_pct | 16.49 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_1d_pp | 1.18 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_5d_pp | -0.43 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_20d_pp | 3.09 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_60d_pp | 13.77 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma20 | 526.70 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma50 | 508.35 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma200 | 435.37 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma20_pct | -0.42 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma50_pct | 3.18 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma200_pct | 20.48 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_sma | 11.04 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_pct | 2.10 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.drawdown_from_63d_high_pct | -3.49 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.volume_vs_previous20_ratio | 0.64 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.AMZN.value | 248.00 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_1d_pct | -0.95 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_5d_pct | -0.80 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_20d_pct | -0.67 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_60d_pct | 5.31 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_1d_pp | -0.43 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_5d_pp | -0.37 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_20d_pp | 0.81 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_60d_pp | 2.59 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma20 | 254.43 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma50 | 255.65 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma200 | 243.29 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma20_pct | -2.53 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma50_pct | -2.99 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma200_pct | 1.93 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_sma | 7.08 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_pct | 2.86 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.drawdown_from_63d_high_pct | -12.68 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.volume_vs_previous20_ratio | 0.70 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.GOOGL.value | 320.21 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_1d_pct | -1.24 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_5d_pct | -5.98 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_20d_pct | -6.89 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_60d_pct | -3.97 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_1d_pp | -0.71 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_5d_pp | -5.55 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_20d_pp | -5.42 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_60d_pp | -6.69 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma20 | 343.08 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma50 | 342.88 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma200 | 340.99 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma20_pct | -6.67 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma50_pct | -6.61 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma200_pct | -6.09 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_sma | 8.39 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_pct | 2.62 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.drawdown_from_63d_high_pct | -15.16 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.volume_vs_previous20_ratio | 0.73 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.META.value | 642.62 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_1d_pct | -0.96 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_5d_pct | -9.40 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_20d_pct | -14.51 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_60d_pct | 19.31 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_1d_pp | -0.44 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_5d_pp | -8.97 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_20d_pp | -13.03 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_60d_pp | 16.59 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma20 | 717.65 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma50 | 663.58 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma200 | 631.66 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma20_pct | -10.45 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma50_pct | -3.16 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma200_pct | 1.74 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_sma | 25.28 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_pct | 3.93 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.drawdown_from_63d_high_pct | -17.36 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.volume_vs_previous20_ratio | 0.75 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/META/history/ |
| prices.CRWV.value | 54.24 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_1d_pct | -2.46 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_5d_pct | -11.65 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_20d_pct | -38.08 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_60d_pct | -26.61 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_1d_pp | -1.93 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_5d_pp | -11.23 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_20d_pp | -36.61 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_60d_pp | -29.33 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma20 | 75.87 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma50 | 83.27 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma200 | 92.00 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma20_pct | -28.51 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma50_pct | -34.87 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma200_pct | -41.05 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_sma | 6.45 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_pct | 11.89 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.drawdown_from_63d_high_pct | -49.66 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.volume_vs_previous20_ratio | 0.92 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.MU.value | 877.55 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_1d_pct | 2.46 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_5d_pct | -0.15 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_20d_pct | -18.90 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_60d_pct | 0.35 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_1d_pp | 2.98 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_5d_pp | 0.28 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_20d_pp | -17.43 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_60d_pp | -2.37 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma20 | 986.60 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma50 | 982.60 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma200 | 731.89 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma20_pct | -11.05 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma50_pct | -10.69 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma200_pct | 19.90 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_sma | 50.32 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_pct | 5.73 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.drawdown_from_63d_high_pct | -20.02 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.volume_vs_previous20_ratio | 0.79 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MU/history/ |
| prices.DRAM.value | 47.06 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_1d_pct | 3.02 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_5d_pct | 1.31 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_20d_pct | -23.99 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_60d_pct | -10.09 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_1d_pp | 3.54 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_5d_pp | 1.74 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_20d_pp | -22.51 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_60d_pp | -12.81 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma20 | 54.60 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma50 | 56.62 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma200 | 缺失 | USD_per_share | 2026-10-23 | unavailable | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma20_pct | -13.80 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma50_pct | -16.89 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma200_pct | 缺失 | percent | 2026-10-23 | unavailable | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_sma | 2.72 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_pct | 5.79 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.drawdown_from_63d_high_pct | -26.03 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.volume_vs_previous20_ratio | 0.82 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.VRT.value | 194.32 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_1d_pct | -0.65 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_5d_pct | -5.86 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_20d_pct | -23.28 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_60d_pct | -14.56 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_1d_pp | -0.13 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_5d_pp | -5.43 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_20d_pp | -21.80 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_60d_pp | -17.28 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma20 | 230.20 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma50 | 247.67 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma200 | 268.97 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma20_pct | -15.59 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma50_pct | -21.54 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma200_pct | -27.76 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_sma | 11.83 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_pct | 6.09 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.drawdown_from_63d_high_pct | -33.85 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.volume_vs_previous20_ratio | 1.37 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/VRT/history/ |
| prices.XLK.value | 183.23 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_1d_pct | 0.49 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_5d_pct | -0.13 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_20d_pct | -6.64 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_60d_pct | 4.39 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_1d_pp | 1.01 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_5d_pp | 0.30 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_20d_pp | -5.17 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_60d_pp | 1.67 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma20 | 193.23 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma50 | 189.53 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma200 | 168.19 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma20_pct | -5.17 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma50_pct | -3.33 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma200_pct | 8.94 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_sma | 4.14 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_pct | 2.26 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.drawdown_from_63d_high_pct | -9.29 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.volume_vs_previous20_ratio | 0.85 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLE.value | 69.33 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_1d_pct | 2.60 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_5d_pct | 1.60 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_20d_pct | 11.75 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_60d_pct | 18.29 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_1d_pp | 3.13 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_5d_pp | 2.03 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_20d_pp | 13.23 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_60d_pp | 15.57 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma20 | 65.40 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma50 | 64.15 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma200 | 57.58 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma20_pct | 6.01 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma50_pct | 8.08 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma200_pct | 20.41 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_sma | 1.47 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_pct | 2.12 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.drawdown_from_63d_high_pct | 0.00 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.volume_vs_previous20_ratio | 1.21 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLF.value | 55.90 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_1d_pct | -1.32 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_5d_pct | 0.68 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_20d_pct | 1.93 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_60d_pct | -1.58 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_1d_pp | -0.80 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_5d_pp | 1.11 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_20d_pp | 3.41 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_60d_pp | -4.30 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma20 | 54.69 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma50 | 55.98 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma200 | 53.36 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma20_pct | 2.22 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma50_pct | -0.13 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma200_pct | 4.76 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_sma | 0.71 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_pct | 1.28 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.drawdown_from_63d_high_pct | -4.20 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.volume_vs_previous20_ratio | 0.78 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLI.value | 164.62 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_1d_pct | -1.27 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_5d_pct | -1.87 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_20d_pct | -3.41 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_60d_pct | -7.47 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_1d_pp | -0.74 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_5d_pp | -1.44 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_20d_pp | -1.93 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_60d_pp | -10.19 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma20 | 168.21 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma50 | 172.00 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma200 | 172.41 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma20_pct | -2.14 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma50_pct | -4.29 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma200_pct | -4.52 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_sma | 2.68 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_pct | 1.63 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.drawdown_from_63d_high_pct | -11.50 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.volume_vs_previous20_ratio | 0.96 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLV.value | 179.28 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_1d_pct | -1.11 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_5d_pct | 1.45 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_20d_pct | 5.03 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_60d_pct | 10.06 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_1d_pp | -0.59 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_5d_pp | 1.88 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_20d_pp | 6.50 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_60d_pp | 7.34 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma20 | 172.48 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma50 | 170.79 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma200 | 157.02 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma20_pct | 3.94 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma50_pct | 4.97 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma200_pct | 14.17 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_sma | 3.14 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_pct | 1.75 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.drawdown_from_63d_high_pct | -1.11 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.volume_vs_previous20_ratio | 0.90 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLP.value | 88.26 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_1d_pct | -1.92 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_5d_pct | 0.73 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_20d_pct | 7.56 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_60d_pct | 3.94 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_1d_pp | -1.40 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_5d_pp | 1.16 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_20d_pp | 9.03 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_60d_pp | 1.22 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma20 | 84.31 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma50 | 84.10 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma200 | 83.35 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma20_pct | 4.68 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma50_pct | 4.94 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma200_pct | 5.89 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_sma | 1.37 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_pct | 1.55 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.drawdown_from_63d_high_pct | -1.92 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.volume_vs_previous20_ratio | 1.48 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLY.value | 113.10 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_1d_pct | -1.66 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_5d_pct | 0.57 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_20d_pct | 2.30 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_60d_pct | 0.85 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_1d_pp | -1.14 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_5d_pp | 1.00 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_20d_pp | 3.77 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_60d_pp | -1.87 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma20 | 111.97 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma50 | 113.31 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma200 | 115.35 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma20_pct | 1.00 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma50_pct | -0.18 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma200_pct | -1.95 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_sma | 1.56 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_pct | 1.38 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.drawdown_from_63d_high_pct | -5.43 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.volume_vs_previous20_ratio | 0.90 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLC.value | 105.51 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_1d_pct | -1.78 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_5d_pct | -4.36 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_20d_pct | -6.60 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_60d_pct | -0.68 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_1d_pp | -1.26 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_5d_pp | -3.93 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_20d_pp | -5.12 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_60d_pp | -3.40 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma20 | 110.52 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma50 | 111.42 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma200 | 112.70 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma20_pct | -4.53 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma50_pct | -5.30 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma200_pct | -6.38 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_sma | 1.69 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_pct | 1.60 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.drawdown_from_63d_high_pct | -8.05 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.volume_vs_previous20_ratio | 0.83 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLU.value | 42.56 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_1d_pct | -0.72 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_5d_pct | 0.83 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_20d_pct | 7.72 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_60d_pct | -4.00 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_1d_pp | -0.20 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_5d_pp | 1.26 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_20d_pp | 9.19 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_60d_pp | -6.72 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma20 | 41.12 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma50 | 41.71 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma200 | 43.77 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma20_pct | 3.50 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma50_pct | 2.04 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma200_pct | -2.78 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_sma | 0.69 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_pct | 1.62 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.drawdown_from_63d_high_pct | -5.82 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.volume_vs_previous20_ratio | 0.51 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLRE.value | 42.57 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_1d_pct | 0.12 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_5d_pct | 0.97 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_20d_pct | 2.43 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_60d_pct | -5.24 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_1d_pp | 0.64 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_5d_pp | 1.40 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_20d_pp | 3.91 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_60d_pp | -7.95 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma20 | 41.52 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma50 | 42.69 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma200 | 42.70 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma20_pct | 2.52 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma50_pct | -0.28 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma200_pct | -0.30 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_sma | 0.65 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_pct | 1.53 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.drawdown_from_63d_high_pct | -6.70 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.volume_vs_previous20_ratio | 1.22 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLB.value | 51.31 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_1d_pct | -0.74 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_5d_pct | 0.77 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_20d_pct | 3.03 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_60d_pct | -0.18 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_1d_pp | -0.21 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_5d_pp | 1.20 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_20d_pp | 4.51 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_60d_pp | -2.90 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma20 | 49.92 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma50 | 50.90 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma200 | 50.62 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma20_pct | 2.79 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma50_pct | 0.81 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma200_pct | 1.37 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_sma | 0.67 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_pct | 1.31 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.drawdown_from_63d_high_pct | -3.96 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.volume_vs_previous20_ratio | 0.72 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLB/history/ |
| prices.SMH.value | 527.20 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_1d_pct | 0.74 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_5d_pct | -2.33 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_20d_pct | -13.08 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_60d_pct | -2.17 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_1d_pp | 1.26 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_5d_pp | -1.90 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_20d_pp | -11.61 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_60d_pp | -4.89 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma20 | 585.55 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma50 | 575.09 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma200 | 515.44 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma20_pct | -9.96 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma50_pct | -8.33 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma200_pct | 2.28 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_sma | 18.37 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_pct | 3.48 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.drawdown_from_63d_high_pct | -16.83 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.volume_vs_previous20_ratio | 0.91 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SMH/history/ |
| prices.IGV.value | 110.59 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_1d_pct | 1.72 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_5d_pct | 5.99 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_20d_pct | 4.32 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_60d_pct | 18.52 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_1d_pp | 2.24 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_5d_pp | 6.42 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_20d_pp | 5.80 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_60d_pp | 15.80 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma20 | 108.58 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma50 | 106.30 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma200 | 93.81 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma20_pct | 1.85 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma50_pct | 4.04 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma200_pct | 17.89 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_sma | 2.91 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_pct | 2.63 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.drawdown_from_63d_high_pct | -1.85 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.volume_vs_previous20_ratio | 0.84 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IGV/history/ |
| prices.XOP.value | 201.69 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_1d_pct | 2.45 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_5d_pct | 0.65 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_20d_pct | 11.12 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_60d_pct | 15.80 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_1d_pp | 2.97 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_5d_pp | 1.08 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_20d_pp | 12.60 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_60d_pp | 13.08 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma20 | 192.04 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma50 | 189.60 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma200 | 167.71 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma20_pct | 5.02 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma50_pct | 6.38 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma200_pct | 20.26 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_sma | 4.90 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_pct | 2.43 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.drawdown_from_63d_high_pct | 0.00 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.volume_vs_previous20_ratio | 0.94 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XOP/history/ |
| prices.OIH.value | 397.36 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_1d_pct | 5.40 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_5d_pct | 3.97 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_20d_pct | 0.93 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_60d_pct | 5.73 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_1d_pp | 5.92 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_5d_pp | 4.40 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_20d_pp | 2.41 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_60d_pp | 3.01 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma20 | 385.67 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma50 | 402.42 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma200 | 395.41 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma20_pct | 3.03 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma50_pct | -1.26 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma200_pct | 0.49 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_sma | 11.56 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_pct | 2.91 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.drawdown_from_63d_high_pct | -8.98 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.volume_vs_previous20_ratio | 2.14 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/OIH/history/ |
| prices.ITA.value | 202.23 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_1d_pct | -1.10 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_5d_pct | -3.27 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_20d_pct | -5.42 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_60d_pct | -14.98 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_1d_pp | -0.58 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_5d_pp | -2.84 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_20d_pp | -3.94 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_60d_pp | -17.70 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma20 | 206.43 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma50 | 218.50 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma200 | 229.22 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma20_pct | -2.03 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma50_pct | -7.45 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma200_pct | -11.77 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_sma | 4.09 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_pct | 2.02 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.drawdown_from_63d_high_pct | -20.04 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.volume_vs_previous20_ratio | 1.00 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ARKX.value | 29.84 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_1d_pct | 0.71 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_5d_pct | -0.12 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_20d_pct | -8.73 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_60d_pct | -1.68 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_1d_pp | 1.23 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_5d_pp | 0.31 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_20d_pp | -7.26 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_60d_pp | -4.40 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma20 | 31.39 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma50 | 32.11 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma200 | 32.56 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma20_pct | -4.94 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma50_pct | -7.07 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma200_pct | -8.37 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_sma | 0.76 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_pct | 2.54 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.drawdown_from_63d_high_pct | -14.40 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.volume_vs_previous20_ratio | 0.55 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.KRE.value | 72.46 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_1d_pct | 0.07 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_5d_pct | 3.80 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_20d_pct | 1.27 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_60d_pct | -3.99 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_1d_pp | 0.59 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_5d_pp | 4.23 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_20d_pp | 2.75 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_60d_pp | -6.71 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma20 | 70.03 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma50 | 72.15 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma200 | 70.18 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma20_pct | 3.47 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma50_pct | 0.43 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma200_pct | 3.24 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_sma | 1.29 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_pct | 1.78 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.drawdown_from_63d_high_pct | -6.49 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.volume_vs_previous20_ratio | 1.00 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/KRE/history/ |
| prices.SKYY.value | 167.36 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_1d_pct | 1.85 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_5d_pct | 5.58 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_20d_pct | 1.63 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_60d_pct | 19.52 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_1d_pp | 2.37 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_5d_pp | 6.01 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_20d_pp | 3.10 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_60d_pp | 16.80 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma20 | 166.84 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma50 | 164.17 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma200 | 135.52 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma20_pct | 0.31 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma50_pct | 1.94 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma200_pct | 23.49 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_sma | 4.74 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_pct | 2.83 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.drawdown_from_63d_high_pct | -4.31 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.volume_vs_previous20_ratio | 2.80 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SKYY/history/ |
| macro.DGS2.value | 4.65 | percent | 2026-10-22 | lagged | source_series_v1:DGS2 | https://fred.stlouisfed.org/series/DGS2 |
| macro.BAMLH0A0HYM2.value | 3.40 | percentage_points | 2026-10-22 | lagged | source_series_v1:BAMLH0A0HYM2 | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| macro.BAMLC0A0CM.value | 0.89 | percentage_points | 2026-10-22 | lagged | source_series_v1:BAMLC0A0CM | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| macro.DGS10.value | 4.96 | percent | 2026-10-22 | lagged | source_series_v1:DGS10 | https://fred.stlouisfed.org/series/DGS10 |
| macro.DFII10.value | 2.64 | percent | 2026-10-22 | lagged | source_series_v1:DFII10 | https://fred.stlouisfed.org/series/DFII10 |
| macro.T10YIE.value | 2.34 | percent | 2026-10-23 | ok | source_series_v1:T10YIE | https://fred.stlouisfed.org/series/T10YIE |
| macro.STLFSI4.value | -0.63 | index | 2026-10-16 | lagged | source_series_v1:STLFSI4 | https://fred.stlouisfed.org/series/STLFSI4 |
| macro.CBOE_VIX.value | 19.45 | index | 2026-10-23 | ok | source_series_v1:CBOE_VIX | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| macro.GPRD.value | 248.66 | index | 2026-10-19 | lagged | source_series_v1:GPRD | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_ACT.value | 230.19 | index | 2026-10-19 | lagged | source_series_v1:GPRD_ACT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_THREAT.value | 310.16 | index | 2026-10-19 | lagged | source_series_v1:GPRD_THREAT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA7.value | 177.92 | index | 2026-10-19 | lagged | source_series_v1:GPRD_MA7 | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA30.value | 176.01 | index | 2026-10-19 | lagged | source_series_v1:GPRD_MA30 | https://www.matteoiacoviello.com/gpr.htm |
| quotes.SPY.value | 759.97 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.QQQ.value | 704.40 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.RSP.value | 216.54 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.IWM.value | 275.75 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.SMH.value | 527.20 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.IGV.value | 110.59 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.XLE.value | 69.33 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.XLF.value | 55.90 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.GLD.value | 366.61 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.TLT.value | 81.34 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.NVDA.value | 210.96 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.MSFT.value | 524.51 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.AMZN.value | 248 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.GOOGL.value | 320.21 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.META.value | 642.62 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |

## 指标历史比较（不同日期观测，非连续交易日）

```json
[
  {
    "id": "prices.SPY.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -3.99005126953125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.280029296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.6586902894217261,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.5842304477708282,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.5847739347737968,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.537965878147718,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.0556209745421041,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.6801435395481623,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.270506994267585,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.933862926278417,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.569000244140625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.0334991455077898,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.319664306640675,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.5018151855468886,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.37867279052727554,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.1248291015624545,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.44485348839014005,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.29308075144210965,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.4787785832023661,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.3626202095568076,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.6063284820302162,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.7633452957447107,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.12142508370535676,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.2950003487723212,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.010958769476296815,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.04271148081880716,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.5121425165247939,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.421007737721113,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.5236001560840184,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.7047555518179971,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.0699462890625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -5.39996337890625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.8485985379229084,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.490072752638328,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.471374343854482,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 4.759217700300544,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.44350829722363727,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.873873541092398,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -3.412121838636506,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.4725749429228543,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.1899082485011823,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.9058423048675,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.8866004090806854,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 3.221251822152827,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.6121126773184664,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.193730001544236,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.1416148443689211,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.4064378692012713,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.004998779296784,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -7.283999633788994,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.5381591796875682,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.8858776855469159,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.4124868774414381,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.438488464355487,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.2510668104909408,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.21259429039192046,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.06234408046562612,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.6250332186274465,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.07395448439302399,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.1787146944971294,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.021432059151786476,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.9778660365513403,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.0032122479336107457,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.29167323900905195,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.009207578592429044,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.710839529500773,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.0141020110623589,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.0825119048297926,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.920013427734375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 5.30999755859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.40125289645965845,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.3542453891226547,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.3854425625298816,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 5.010716300335449,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.43427277811347587,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.6022584710631347,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.6359753061950921,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.6609241617212218,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.0599431858813846,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.7700149413518265,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.8006686277560848,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 3.4727504221877314,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.6213481964286283,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 4.282402010611297,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.6345316880724923,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.594787087999638,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.3110000610351449,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.1189987182617074,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.5391876220703011,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.576995239257826,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.10995567321776889,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.6260729217528933,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.22004491497431555,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.6558112185868676,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.1396624835758975,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.699944445517022,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.37155064088871814,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.6949123569211855,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.06357029506138412,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.2735682896205356,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.01852796889336661,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.1274261681015929,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.3023423483777812,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.7450148914663473,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.18922052765143704,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.4935507473778522,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.6800079345703125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.4499969482421875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.499190284331009,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.34661138805212044,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.3532978598610903,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.6515104888630718,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.2136769913426049,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.3451353570839597,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.6179604974563713,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.48721877340334174,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.157880573752735,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.9308418358229487,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.9380717946348871,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.8864553892846461,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.15805601680050074,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 3.0252788966321216,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.6525464968112136,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.4466441528750753,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.2714996337890625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.10711791992187614,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.40025177001953693,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.12026092529296761,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.6063722229003758,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.9211511232488645,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.6166677580969449,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.7310319287001654,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.3249555031354832,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.8776284474044438,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.8826303531550783,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.004285539899553825,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.04714311872209853,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.009371624194733141,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.011008913448881885,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.7569794278786346,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.1039217434762327,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.8715329662850654,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.5163700452272099,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.3900146484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -15.4000244140625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.977978900547972,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.4647991101884963,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.44896957481503863,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.3630588962728964,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.019389134286885,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.036205240181099,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.236703732262224,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -5.620767580344877,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.3192886111262458,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.0490295579593245,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.0337435095888354,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -4.901024774420614,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.03623184025521908,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.35606170063293696,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.033803262005360324,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -4.68690465406646,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.3400009155272983,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -5.22650146484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.6470001220703239,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.6790002441406386,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.21310012817383495,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.7693000793457259,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.28760344160750906,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.6919314980644815,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.4526772464354174,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.2504968283504017,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.531198092071417,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.5469622681093664,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.15143040248325867,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.18785531180245574,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.05044840938299355,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.10774596402709213,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.5583233133704013,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.5975480997430758,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.9922838645707295,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.06965105807351835,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -52.5,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -173.2001953125,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.8660624051719523,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.556758729493779,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.5118181448831258,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.307606830861698,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.7221523931928777,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.7405825533741481,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.8458082000023643,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -5.480673170062145,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.20737211575022618,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.1409891772646072,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.0965920796569226,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -4.845572709009415,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.6665314186507736,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.060439013825986265,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.5753012057347799,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -4.546810243783728,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -15.665014648438046,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -58.844995117187864,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -8.25,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -32.548007812500146,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.2730004882814683,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -7.799001464843968,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.896455702469312,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.7631485352381246,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.0318016980013223,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.272568711713242,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.113304261364135,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.66253138897601,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.6285574776785694,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.1000104631696388,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.06330141056088245,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.04799729234287109,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.1175444289391656,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.6868364450030384,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.41424705902755,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.3580507534039641,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.7999954223632812,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.8599929809570312,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.4321833119809835,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.30896125064610036,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.3030507333508625,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -8.574148524187496,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 6.615088512757271,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 10.64528629825583,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 5.77175847658755,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 13.542401683850478,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.7734930225592578,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.27526919712472697,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.2817232014229343,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -10.112114402335214,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 7.670709487299375,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 12.325429837803991,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 8.042265470855135,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 14.476264610128897,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.5429996490478572,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.7895000457763643,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.4403999328613253,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.9462002563476517,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.23639997482300146,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.0958000183105554,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.4060958209507506,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.09777791844400774,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.579462267383061,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.33279120401310536,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 4.131368457884086,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.6332486256213947,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.1385716029575894,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.3707144601004462,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.022771221674052988,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.28774347570235914,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.59065988530316,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.7575290076308319,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.08604144457867635,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.3063424717595432,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.5500030517578125,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 6.8600006103515625,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.8605490754280076,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.5829144117405871,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.6004771758859606,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.3359851349848517,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 5.723277746122757,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 6.119682859567077,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 6.38290072484773,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 21.994720388292997,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.5192393648497338,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.167144859511415,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.1852511106597579,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.20198074316286618,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 6.778898720664861,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 7.799826399115239,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 8.653407719115314,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 22.928583314571416,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.6200000762939339,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.1730003356933594,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.5930000305175724,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.416399841308589,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.2838000106811478,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.265150032043465,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.723588659399301,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 4.305249371411191,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.8567500145888474,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 4.128267366112025,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.506085757155695,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 5.828539491636729,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.06428582327706467,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.025714329310825956,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.05023555513643929,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.18966932334460118,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.0,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.0,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.054118104615966556,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.35954793665680584,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.40000152587890625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.2899932861328125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.3587502500387547,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.5893981779611979,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.6018413987605609,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.0430419276564518,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.37604860619975256,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 4.039763829121856,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.42858292485502547,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.011771470609136,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -3.017440539460481,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.173628625732026,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.1866153335343577,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.5810078058041697,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.6795723683423511,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 5.719907368670018,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.8419240694125594,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.9456343968875536,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.11690864562987713,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.08877754211425781,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.012093963623044601,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.11166397094726221,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.01745460510254304,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.09544944763183594,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.66251437330207,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.5238023647185184,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.48301404646946544,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.7457419388741235,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.4595865210570871,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.6583977305821178,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.01857103620256695,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.008152563529163492,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.017734772697780343,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.026599796181886237,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.4805117007213866,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.5496072367671587,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.5966482568819631,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.1431721493821575,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.05999946594238281,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.03999900817871094,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.27676848743972693,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.4834724174205052,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.4831380581660327,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.48290040359079134,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.4560151156948189,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.6788827178057399,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.2250505727747996,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.6534940378403862,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.3819218019819992,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.10075803035032305,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.10163587660776408,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.0550654745569266,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.511636090236923,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.0012608217424224,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.4955575670423844,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.5873569641188032,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.01699991226196218,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.08799991607665802,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.01559997558593551,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.07899997711181683,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.008799991607663316,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.045549983978268926,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.14861757520147068,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.16652309570888146,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.1550469775538854,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.14195983010389934,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.1824664590009073,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.026267970207571878,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.0071428843906947564,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.019285746983119426,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.025581247207012325,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.0672630529669116,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.2059713960554932,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.13731208146612328,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.37213570177828725,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.4784971629905942,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.04999542236328125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.19000244140625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.2207232026747552,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.2852090961442566,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.286099670867912,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.7262978533668418,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.026185531490141578,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.0910806828760777,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.34964775292768424,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.05468280983832452,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.8794134920964813,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.2990213516265716,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.2986742639058848,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.8116680247808761,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.0294354430519626,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.77122422242424,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.920859241339901,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.879180116440093,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.023255920410150566,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.23385925292969034,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.03907257080076931,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.18574874877928949,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.0016010665893588794,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.008196868896476417,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.03469460622143039,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.5486343203751187,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.014582382816252792,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.47818488128996695,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.06215075686648586,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.25431235021121656,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.0021427699497768016,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.06043520927828483,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.003018461565812647,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.07954234282191125,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.06317951969295743,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.2401072422453021,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.1655587060482112,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.29967434017116146,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.43000030517578125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.4499969482421875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.449072620648828,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.31573477598699773,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.31842187203705574,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.5315002129890667,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.47744463190053654,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.869766510921289,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.5868594260782789,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.2894078515925158,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.107762910070554,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.899965223757826,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.9031958068108525,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.0694660911367846,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.5781763426415676,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 3.5499100504694514,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.683647568189306,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.2232707778709324,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.054171371459958095,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.037701797485354405,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.035974426269532955,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.18473953247070085,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.014353981018075501,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.07642875671386662,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.47262049073009127,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.4754428193736615,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.3792233804338574,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.6099747463896077,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.39265815261375625,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.49528210002590667,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.005713871547154081,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.01889633040961569,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.008023409982781282,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.015589959491278726,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.4058287670606564,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.4247083688591724,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.3977919497547374,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.016722669951687474,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.4200000762939453,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.5399990081787109,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -11.881689211330304,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -19.2388930558977,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -18.314965095347457,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -37.404846860427874,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 9.358025014160631,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -4.176086814230491,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 10.28685992452951,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 14.049726213284039,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -12.54037950075203,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -19.82312350366853,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -18.899739030121253,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -38.94281273857559,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 10.413645988702733,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.4959432746823325,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 11.560440570049433,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 15.61266541791022,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.22900004386901784,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.8055000782012929,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.10400001525878899,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.3348000335693353,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.02480000495910417,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.07970001220703082,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.9238074107187337,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -9.455806245037191,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.8511606748146576,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -6.080903871787967,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.1640485606578164,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.448233607919615,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.051428590502057725,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.40928547722952713,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.0557058736279572,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.31004609253603,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.0329142274730154,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.6137415884170623,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.3599987030029297,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.020000457763671875,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -5.689383011431004,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -9.081484420903974,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -8.91314508146699,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -15.46053153674194,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 5.052135305602757,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.8316175600039397,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 11.444239425886648,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 5.511077414144361,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -6.348073300852731,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -9.665714868674803,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -9.497919016240786,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -16.99849741488966,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 6.10775628014486,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 3.5117610995521016,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 13.714746420154235,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 6.444940340422778,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.12749996185302948,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.3874999046325698,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.03739997863769773,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.08319999694824531,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.009449996948241335,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.033249998092649946,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.188774967148909,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.4516180097764924,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.726768215798625,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.6095531914889207,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.712653223572469,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.2604854798537115,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.06714275905064171,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.25714288439069466,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.23829523348306747,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.25955831535913,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.6744125721066538,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.09302538494730861,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.7599945068359375,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.2100067138671875,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -12.531287683975533,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -17.101244542775838,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -16.794725831991496,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -29.679769938984656,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 5.707619344590853,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.8977820138593913,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 17.28607720002666,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 8.312820349884786,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -13.18997797339726,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -17.685474990546666,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -17.379499766765292,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -31.217735817132375,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 6.763240319132958,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.7823615256887706,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 19.556584194294246,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 9.246683276163203,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.0930000305175867,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 4.016000747680664,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.4055999755859432,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.290400085449221,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.08919998168946108,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.31060001373292323,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.5109914595220459,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -5.574482162097816,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.407041173920696,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.9854962805559992,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.6845304166011275,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.5644732206793854,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.37000002179827085,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.441428593226841,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.20162187273234977,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.237839673507146,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.60130511163169,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.19107151930665145,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -3.529998779296875,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.2099990844726562,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -14.665265768874281,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.9477756521325218,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.058361490422178,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.7887326368568601,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -13.14733432908709,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -33.856732361629064,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.1433301797864033,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 6.783426009246838,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -15.323956058296009,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.53200609990335,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.6431354251959753,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.8385088820210052,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -12.708948890476446,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -32.5831570740129,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.2105064422220906,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 4.715090676286792,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.06350021362305824,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 3.433000183105463,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.624400024414058,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.709400024414066,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.18744998931884993,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.9412999916076643,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -3.357437713979472,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.2303251215240785,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -4.892158764668242,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.1494545622553929,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -4.94423703810687,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.2435415054633978,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.08142852783203125,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.2114285060337613,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.25755027424251775,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.08915563140685734,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -3.107393333373177,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.9454217554202842,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.25,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.1699981689453125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.807948944712336,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.8380155505140707,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.8305014782876485,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 5.1272304766707855,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.7611035030128059,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.6069484934386993,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -3.5251022069300326,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 5.5963537981541736,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.14925865529061,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.2537851027432425,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.24572754351385173,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 3.589264598523067,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.2945174715292982,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.9268049538905374,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.2545952126624478,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 6.530216724432591,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.7055000305175838,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.6354995727539006,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.281763610839846,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.5692224121093545,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.11145751953125682,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.7053701019287075,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.26082612496478674,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.30892088476538504,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.4413246293528461,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.1795855564028734,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.671890001537534,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.9252846068792628,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.1771425519670755,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.21642957414899566,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.06678384013291172,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.1430234232919707,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.5224878662844255,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.3250284635342382,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.4510924705714827,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.3595083741880527,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.42999267578125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -4.53997802734375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.8854716778116907,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.58432101476328,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.545389036216117,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.26695225298325465,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -3.0335008513162176,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -5.527102929139849,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -17.184255885544978,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -22.415772915870072,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.2267813883899645,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.000090566992452,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.96061510144232,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.2710136251644633,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.977879876774113,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.8469593895916865,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -14.913748891277393,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -21.481909989591657,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.41700134277346024,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 6.481504821777321,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.5712725830078398,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.98911926269534,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.2204402160644463,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.3380795288085778,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.5728315954208862,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.1134323861918047,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.5594049387999123,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.5086290004883152,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.7272061977522171,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.4174226513054222,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.3392813546316962,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.6999991280691962,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.07896700524570432,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.11424902727720898,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.6311514580433224,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.8353993790351066,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.35769593542633205,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.43801904239206024,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.3800048828125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.0,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.6193215025686953,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.917865980777155,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.9192611549949992,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 3.9364985034838877,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.0698766554021355,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.793419886381852,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -5.162036994612662,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.6852095460589522,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.960631213146969,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.33363553300632676,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.33448722022120236,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.39853262533617,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.014255680860031372,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.4735634259300143,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.8915300003450772,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.7513466197805352,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.08349990844726562,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.2040000915527287,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.3426000976562591,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.4283996582031193,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.03220001220702784,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.5648001098632847,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.9031407778556377,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.253256931396829,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.7998952836537843,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.23896838695713907,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.9918691692945014,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.0611575504624993,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.029999869210379337,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.1828536987304688,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.01517429325786468,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.49599631173270087,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.8379709086947198,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.7041757895088541,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.6681642062133986,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.40345712993362337,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -4.010009765625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -20.3800048828125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.9117092605837271,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.2344054530403104,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.1750754332036308,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.835806581538192,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.5955394732116819,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -4.333539720420209,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.321837460313279,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -11.246561660411281,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.253018971162001,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.6501750052694821,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.5903014984298336,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -4.3737724596859096,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.5399184986695786,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.6533961808720474,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.9486695339543072,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -10.312698734132862,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.1855010986328125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.329499816894497,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.5185504150390443,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.6149743652343886,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.005724182128915345,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.4285473632812682,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.8433931783532351,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -4.986084037476646,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.0267286285217896,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -5.478152905096512,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.1744110711763955,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -6.10249318253604,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.09571402413504337,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.5728563581194184,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.002876944448934715,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.011452167656915702,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.0625148481194113,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -5.40000126143315,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.4301566127466504,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.35978091182758176,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -6.22998046875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -66.71002197265625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 6.0174264991356035,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.757666925209379,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.5225382741269495,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -8.105034139525902,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.0497324840335835,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -21.136640674892615,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 8.425493830151433,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.1877157791958126,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 5.358736209713877,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.1734364774385506,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.9377643393531532,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -9.64300001767362,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.105353458575687,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -19.456497135344453,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 10.69600082441902,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 3.1215787054742314,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -5.451998901367233,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -18.12599792480478,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.9623840332030795,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 8.621085205078089,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.022021179199214203,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.5924938964843705,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.1864164131977315,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -6.860666244168145,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.0808657942804833,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -11.460142335005784,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.9827073179346613,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -10.666511318891246,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.28571864536830205,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 3.169281005859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.006257710618274626,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.8168206044338961,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.8011908915477761,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -8.579073762356225,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.3287631870885646,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.1855872412826417,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.3649978637695312,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -7.154998779296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 7.606438608149945,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 9.45485840619571,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 8.563122954618475,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 13.55212662459224,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.23050003530235585,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -13.535595471442221,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -18.027579748876356,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.306956305665288,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 6.94774831872822,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 8.870627958424881,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 7.9783490198446785,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 12.01416074644452,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.2861210098444644,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -11.85545193189406,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -15.757072754608771,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.3730933793868694,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.6677497863769446,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -7.095249938964841,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.0411000061035054,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.7659001159667866,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.11472499847411655,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.4400250244140551,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.22285665674812805,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.5106280897535314,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.8147371058616102,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -5.402682032835585,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.4084236394666405,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -7.4595346041562465,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.1185714176722934,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.5667855398995538,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.07853355846420307,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.30850142193491,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.2670545077836763,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -6.641602669955155,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.7633331444940477,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.5733625672117437,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 21.05999755859375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.2900390625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 8.717148958357846,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 8.085774771704058,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 7.8801430790920275,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 14.432580145563511,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.818006233042258,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -5.434441500436304,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -15.570542149525735,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 11.579345820407504,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 8.058458668936119,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 7.50154432393323,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 7.295369144318231,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 12.894614267415793,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.873627207584363,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.75429796088814,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -13.300035155258149,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 12.51320874668592,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -10.227987670898415,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -46.26421203613279,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.4426110839843886,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.3765393066406659,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.691236877441497,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 14.269433135986333,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.0253530931636856,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 3.8592415515381404,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.2710902315906782,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.09702761817724692,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.4455750332446513,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.5639226419157417,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.1480785423115876,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 3.074887069619578,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.006936984054935813,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.35829644477042333,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.9194008190998133,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.1175737094149305,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.4214550348482594,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.32488717623816654,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.3800010681152344,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.6100006103515625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 10.099943126757637,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 8.859252341427005,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 8.712392745166564,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 20.092744957912366,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.7830049631659577,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.9095972475851681,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -11.938501832264826,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 10.238013631562081,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 9.441252837335911,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 8.275021893656177,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 8.127618810392768,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 18.55477907976465,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.8386259377080627,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.22945370803700627,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -9.667994837997242,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 11.171876557840498,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.742499923706049,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.5889999389648395,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.19739997863769787,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.4973998260498078,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.6503271700349718,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 6.365323737335016,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.717454261936023,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.791654376718487,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.1007142748151506,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.33714348929268967,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.04554639375842218,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.6497772286138588,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.1691309199686444,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.9588189572349215,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.7303451436465718,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.741209480360872,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.269989013671875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -12.099990844726562,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 7.156485013459846,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 3.2296179949338533,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.060173323346781,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 9.114691570504318,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -3.013597563739445,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -6.048539871325211,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.277965784730707,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 17.52730113404697,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 6.497794724038119,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.645387547163025,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.475399388572984,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 7.576725692356601,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.9579765891973402,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -4.368396331777046,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.007458790463122256,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 18.461164060325384,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.9479995727539006,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -11.999000549316406,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.8535925292968614,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -7.753938293457026,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.1144935607910611,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.7711656188964753,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.5226045810198592,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.8139533790654578,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.07386020784171521,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.35542279797194,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.503127246204258,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -4.719236011056616,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.10357012067522398,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.2614266531808038,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.09247613102348051,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.967905408567928,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.4323102320139398,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.6589968111045081,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.25686290679654933,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.0672878538235695,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.8899993896484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.2400054931640625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.7765241879900713,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 3.5115150506375814,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.4898873778470008,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 7.571166339862578,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.29087014899340424,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.5237167574338253,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -5.205638110004096,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.4564915262887057,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.117833898568345,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.927284602866753,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.905113443073204,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 6.03320046171486,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.764750825548699,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.8435732178856634,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.935131115736511,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.3903544525671228,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.6520004272460938,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.5965011596679517,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.14635284423829376,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.2680862426757926,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.18613319396973793,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.0102477645874046,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.7779482032853835,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.1347894097542888,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.5438006861532174,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.010096687133054338,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.4090528934620252,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.8018958332113311,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.09857068743024566,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.680713108607701,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.04303987131112974,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.37397462360144607,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.4405937572516958,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.11881460057626647,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.5809299501964825,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.1056939305912108,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.7600021362304688,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.0900039672851562,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.4703255065250183,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.08067039123005326,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.07987834820391004,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.258246654171937,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.8111855931700855,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 5.008733555346034,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.3934791443933854,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.6832088708406374,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.811635217103292,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.503560056540775,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.5048955865698868,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -4.796212532319655,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 4.866806567712189,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 6.688877094894196,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 4.66398613866097,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 3.6170717971190562,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.3645000457763672,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.4790006637573185,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.17261596679688296,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.838136444091802,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.1253849792480466,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.5862059211730966,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.1120634580935604,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.7475739472827314,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.459401737366651,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.29091332022606053,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.800666151453111,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.6740328046408237,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.032142911638532334,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.13928658621651802,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.0077650751290523345,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.17017931934071062,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.9818261868689615,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.0,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.09987699592730492,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.04593377452629688,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.75,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.3800010681152344,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.412428043762027,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.7762437104849038,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.8123956786681106,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.7590113883159111,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.95487512947774,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.189797295895546,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.8835435720532034,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.37943164391926,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -3.0711183331837533,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.360474158255732,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.3971696134419074,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.296977266463629,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.8992541549356354,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 3.869940835443708,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.3869634222143814,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.44556871764084294,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.0530000686645451,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.2380002975463853,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.043090667724612786,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.1799880981445341,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.004809627532956995,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.024436302185058878,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.4719901001001512,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.25109342438354165,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.262026141283723,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.9967830926719712,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.4151451102141666,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.6644871573570743,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.012142726353236655,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.01714324951171875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.03835156516619409,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.02213189524524295,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.285270445591535,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.6512055228556362,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.11461639447373373,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.3142430133758033,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.1100006103515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.1399993896484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.32677441540416297,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.1880849409432792,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.180790436419299,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.9913634536167448,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.165164579985146,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.5023194536873183,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.10371183948983,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.07494309582843961,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.9854647048258891,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.7723153887141074,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.7655643711930957,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.5293293317644627,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.1095436054430419,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.822175914139156,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.16679515477775375,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.0088060221068567,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.29049987792970455,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.8235008239746264,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.41343994140623863,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.83049713134767,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.034542312622050986,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.2274234771728345,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.083471559079463,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.3808085209452758,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.9942941894432904,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.7985045133369288,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.2432235492810584,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.949788838466271,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.07714189801897309,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.11285509381975434,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.06689204973232199,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.09777566968430262,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.1343475120825008,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.6880803152918613,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.4874446296844481,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.29313916468935775,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.0200042724609375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.5699920654296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.433055896949521,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.8432845039301307,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.8651885989885644,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.999780023687836,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.7023165321963685,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.3161777271811106,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.5809825855990436,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.18002565267487647,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -3.091746186371247,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.4275149517009589,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.4499625337623612,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.537745901835554,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.6466955576542635,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.3639658123670522,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.8514895798666284,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.1138885789532935,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.42900009155275143,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.336000823974615,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.23083892822265284,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.184770812988262,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.1078769683837777,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.6074047851562625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.433282483609477,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.08336961392056974,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.326385805068031,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.7820067996581415,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.365817176890392,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.1996837018531945,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.021428789411272575,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.2050018310546875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.03131602449015514,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.09056118339882224,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.114177737704869,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.8432845039301307,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.28736947349474473,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.08975161773160001,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.7299957275390625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.6399993896484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -5.228592567409462,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.006882483265594,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -3.088214331929273,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -4.291751062059412,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.591427287665172,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.0382331752480933,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.25544154912959804,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.0489356055035657,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -5.887282856831188,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.591112931036422,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -3.6729882667030695,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -5.82971694020713,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.535806313123068,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.718376714796256,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.525948543397183,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.1150726792251486,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.3100002288818473,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.4740001678466825,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.056438140869147446,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.3452468872070398,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.06544185638426825,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.304107666015625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.4457557607937996,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.090071288803962,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.128865673200897,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.33153603432749534,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.1604596269155563,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.3828933732910711,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.07071413312639496,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.19928468976701996,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.10846726815932684,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.21608635757942363,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.9224311241322622,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.9224311241322622,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.3071403019069441,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.5533005768573163,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.910003662109375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.6399993896484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.2106316673344053,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.8230556624192809,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.8417182488324126,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.9146816512966782,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.9538753019073374,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.7863713981558496,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.4199112295590686,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.776353875619053,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.8693219567561314,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.407286110190109,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.4264921836062094,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.6232842268510397,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.8982543273652337,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.466514937704012,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.14940423529148372,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.842490949340636,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.12700004577637003,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.8754997253417969,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.10179382324218977,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.40404327392577954,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.03526500701904922,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.11361366271972884,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.8223657725592979,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.21988971370345833,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.59454736537058,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.917476077646795,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.625365846860649,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.6507676153804098,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.05857140677315842,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.16642924717494423,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.07382334787249611,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.14014379215550066,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.5970384858410407,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.5351317782577132,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.2509526163933572,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.6251227813557136,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.9099960327148438,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -4.80999755859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.35565111387232395,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.10738868350076425,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.10456573800696667,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -4.305685845803742,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.8315889897888455,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -6.481176805497502,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.9075427228310784,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -5.710502966096365,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.01434140329405,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.476841764270064,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.48020819676683013,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -5.84365172395146,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.22403198475325858,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -4.80103326594934,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.178049717098663,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -4.776640039817948,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.37249984741211506,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.2804996490478544,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.13340560913086108,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.26319458007813523,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.05261119842528217,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.19654628753661996,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.401730890437725,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.2089369126941163,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.598944331306373,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -4.083685252400959,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.650355848234808,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -4.097717463740935,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.029285430908203125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.042857578822544484,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.055784707074931106,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.10878842437631908,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.6644845601000764,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -4.191719005310457,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.11170416093623481,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.17089438264738466,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.30999755859375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.3500022888183594,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.7945367498212192,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.0676426256725833,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.09997249648628,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.1027058350468133,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.1981058050163371,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 4.263690675555543,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.16094251875593546,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 3.943178736227848,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -3.4532270392429454,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.6518730734434115,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.6847464312600766,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.640671713194531,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.142484830474233,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 5.943834215103705,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.1095644755116494,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 4.877041662506266,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.15250015258789062,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.5430002212524414,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.02317085266113139,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.11973884582519645,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.007730350494384197,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.008411197662354652,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.1419367255816937,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.5224502213782456,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.6861401212484797,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.1287821691587707,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.7254614147927163,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.7810201731345945,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.010714122227260092,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.015714372907365992,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.013305168580497462,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.023827571676347414,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.3537312085033051,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.3283586453081817,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.3119094776451997,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.39602060751127544,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.049999237060546875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.4099998474121094,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.9760835629827325,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.28726399675005343,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.2897169192959792,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.3493103817651111,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.341384354551022,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.465781894849084,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.4705533695107071,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.18192917888509808,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.6347738524044586,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.8714944445208817,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.874490854069776,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.887276259912829,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.3970053290931261,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 4.145925434397246,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.741060363778291,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.1157921051635151,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.050499916076660156,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.05299987792968608,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.043467636108402985,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.20016052246094063,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.01687137603759936,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.06975975036620952,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.004274498784995195,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.8576231312026783,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.2184312788616083,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.4212800623788602,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.07773619102358076,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.7986566954295893,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.028642926897321397,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.05257170540945877,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.06556005044258129,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.1097815658227097,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.10958508746531415,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.89861109450562,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.19808003672951546,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.119651983251289,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.37999725341796875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.3900032043457031,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.4561109806684347,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.447165532271566,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.4690492353819362,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.248445780352326,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.0137574662690607,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.7030065362075621,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.5448881644192771,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.9004713182103061,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.114801270090161,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.031395980042394,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.053823170155733,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.786411658500044,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.0418635082730443,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.383150075755725,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.7256188298483077,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.9666083919318891,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.07550010681152486,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.32500019073486186,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.015207443237308382,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.12919731140137003,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.02610963821411616,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.13607313156128242,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.9180651783279536,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.11281528063438184,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.716280281038939,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.0196001435379132,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.8034336067322956,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.49933125587322547,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.028571810041155055,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.07357188633510037,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.045645160078331415,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.15451844255356106,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.7112837881934619,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.7300130569351193,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.10658620937855579,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.35316825621059933,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.85003662109375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -12.5899658203125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 6.726318082215954,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 4.144507864104918,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 4.018281512787103,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 8.199173789863957,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.233080294531252,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -7.287801382528636,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -5.965065148249849,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 4.7889385809571365,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 6.067627792794228,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 3.56027741633409,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.4335075780133057,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 6.661207911716238,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.8225406800108512,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -5.607657842980474,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -3.694558153982264,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 5.722801507235552,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -3.967999267578193,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -15.49550170898442,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.2383996582030932,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.938399658203025,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.7109001159668651,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 4.09205017089846,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.2591165368555988,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.2265288286302134,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.8650090636363448,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.5507904774374586,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.6067130484084693,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.280639019661713,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.299285888671875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.732862200055804,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.031549160958405764,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.5875657728021708,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.6073570709596581,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.986112215715698,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.049744326669042,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.6865386539341864,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.8699951171875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 6.25,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.8119036765291585,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 6.519282295134565,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 6.792950009216647,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 13.383306929705473,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.8551062351074297,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 4.329926761389569,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.8183646703853213,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.2744242620454678,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.1532133871074324,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 5.935051847363737,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 6.20817607444285,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 11.845341051557757,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.9107272096495334,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 6.0100703009377305,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.088871664652906,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.34056133576704894,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.22899971008300213,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.2954998016357422,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.08619995117187784,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.40139984130860284,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.021849555969239987,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.09024024963379418,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.510563711303936,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 5.493720172895522,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.6761539531924496,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 5.507504347831715,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.9663587721830087,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 6.555216009936494,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.08000019618443055,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.1328582763671875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.028268805791007434,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.030479601310598348,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.659709902882489,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 5.547173250707182,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.3725024881176916,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.3484467739663764,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 4.82000732421875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.30999755859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.5286179435997767,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.36865657611035996,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.3621989049317431,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.9723922948362134,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 4.158474208026153,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 5.5791476983870325,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.9080310282854711,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.2695094553942141,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.8699276541780505,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.9528870238811882,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.9469728397055399,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -5.510358172983931,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 5.214095182568256,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 7.259291237935194,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.178538022553056,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.203372381672633,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.0095001220703352,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 4.1270004272461165,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.46463134765625114,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.442774963378895,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.3965822219848576,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.864852981567367,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.9681568332711619,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.6094599201032844,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.287110902648548,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.6884746519851381,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.595793061582043,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.5624083423079824,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.0014299665178576504,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.251431056431362,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.05878957940451812,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.1095850233320741,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.7516766544035889,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.0,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.6382108012469936,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.11943367390696058,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 20.3599853515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 15.17999267578125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 9.613135779974936,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 3.9161546509936196,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.863075858806342,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 5.636685799604368,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 5.29803785127283,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 5.080637727595461,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.2662964792672167,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 5.932330102526285,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 8.954445490553208,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 3.331924203222791,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.278301924032545,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 4.0987199214566505,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 6.353658825814934,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 6.7607812671436225,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 5.5368034735348015,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 6.866193028804702,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.18399963378908524,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.8640014648437386,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.2642004394531341,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.0155999755859284,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.462599945068348,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.1517001342773483,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 5.23250235372651,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 4.412681435040722,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 5.120818966774099,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 4.245453497513574,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 5.037412865144175,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 3.310215328628563,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.432854788643974,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.9592851911272327,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.04230625568217672,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.397101241922309,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 4.663517792332971,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 3.477024403927542,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.20850787757350853,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.2779685457652654,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.25,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -6.8400115966796875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.4637820392910941,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.1394054771996296,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.092436062140879,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -4.442705657993795,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.5243159959842383,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.1853898593662837,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.6264028198049072,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.838824454212208,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -1.1224723287128202,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.723635924970458,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.6772099969146756,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -5.980671536141513,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.46869502144213415,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.5052463198181214,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.6441041744626794,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.9049615279337893,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.5790000915527287,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.211000823974615,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.9434179687499977,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -4.544535522460933,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.11806312561034815,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.45291976928712074,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.812900650489079,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.2402066849659508,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.6274149379130289,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.1808879558316994,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.9356718367415802,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.8041881610307975,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.3321424211774553,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.7421417236328125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.18466347566467411,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.4210707240822904,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.889585432652428,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.704344300257766,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.007004206706634153,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.0497751951926042,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.21000099182128906,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.034999847412109375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.7202014615841827,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.85417743287516,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.8307707093144785,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 7.103344791745236,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.849717786692727,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.7428091317758696,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.0530204470576185,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.7617516357269825,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.0615111721624566,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.269946985104332,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.2459967745406817,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 5.5653789135975185,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.9053387612348303,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.06266559222770773,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.2174865472099663,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.6956145620053995,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.14274997711181925,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.6972500801086454,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.1001999664306581,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.44999996185302393,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.011100006103511362,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.02385002136230696,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.0962546023729818,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.9564152736724294,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.9410831364016996,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.1769117824674602,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.6758762027579408,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.040337395670686504,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.02035699571881977,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.08357129778180805,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.05068002030476082,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.28271589640902217,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.6024124731625164,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.10040116695154744,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.5522353499028396,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.5047916219244071,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.04999542236328125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.6500015258789062,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -2.465649008746218,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.016973094456607107,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.01760524100760108,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.6367744679147265,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.8003430407365508,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 4.766537642396518,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.41888934342989526,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.5881712197692863,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -3.124339298167944,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.6012035422274353,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.6023791757813974,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.0988085897670086,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.2552779338055533,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 6.44668118194468,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.689396337697479,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 3.5220341460477034,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.04549980163574219,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.03399963378906534,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.09699371337890739,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.5326858520507898,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.03427463531494368,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.15225278854370572,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.0041673365722472155,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 3.8324964983466048,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.2040231425357364,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 4.381918630529002,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.02082531410834143,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 3.5596079545223147,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.006428854806082462,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.03214427403041298,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.01010692746336761,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.11358820089891175,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.06451966082330429,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 3.4198570898866247,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.16039679053097478,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.0362436628945384,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.0399932861328125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 8.850006103515625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_1d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.236347998488587,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 6.717407887734028,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_5d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 6.963627225818991,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 14.949137957086899,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_20d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.1791357213304616,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 3.793808662027054,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_60d_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.9260163881298347,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.6767030467505144,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_1d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.5776577090668606,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 6.1331774399632,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_5d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 6.3788532910451945,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 13.411172078939181,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_20d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 4.234756695872566,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 5.473952201575216,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_60d_pp",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 3.1965233823974195,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.7428401204720956,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma20",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.13400039672850994,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.5999992370605298,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma50",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.031000061035172166,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.26440032958984716,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma200",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.18150001525879134,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.8742000198364224,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma20_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.742898911043822,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 5.644807222487946,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma50_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.8705924183171296,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 5.234900945540688,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma200_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.0805826445889224,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 5.77096411715565,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_sma",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.18214307512555727,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.3935732160295755,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.058457181820678716,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.09018965496545928,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.drawdown_from_63d_high_pct",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 1.7382316294483058,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 5.060327139574249,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.volume_vs_previous20_ratio",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 2.209683161815285,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.77104623334947,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS2.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.15999999999999925,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-15",
        "to": "2026-10-22",
        "change": -0.11999999999999922,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLH0A0HYM2.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.1299999999999999,
        "unit": "percentage_points"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-15",
        "to": "2026-10-22",
        "change": 0.16999999999999993,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLC0A0CM.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": 0.010000000000000009,
        "unit": "percentage_points"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-15",
        "to": "2026-10-22",
        "change": 0.050000000000000044,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS10.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.16999999999999993,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-15",
        "to": "2026-10-22",
        "change": -0.13999999999999968,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DFII10.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-21",
        "to": "2026-10-22",
        "change": -0.11999999999999966,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-15",
        "to": "2026-10-22",
        "change": -0.13999999999999968,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.T10YIE.value",
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.020000000000000018,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.010000000000000231,
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
    "available_prior_observations": 5,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.41999999999999815,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.5399999999999991,
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
| 事实指标引用 | ["macro.BAMLH0A0HYM2.value", "macro.DGS10.value", "prices.^VIX.value", "prices.^MOVE.value"] |
| 推断与解释 | 推断：风险压力尚存；夜盘初步缓和，尚无全面恐慌或过热的充分证据。 |
| 反证与缺口 | VIX低于三个月指数但都是23日观察；MOVE与信用仍有压力，夜盘修复需现货验证。 |
| 确认条件 | 信用与波动持续上行、成分广度同步恶化。 |
| 失效条件 | 油价风险消退、信用改善且股市承接恢复。 |
| 观察期限 | 下周至两周 |
| 条件式指导 | 避免仅凭VIX未到极端就认定安全。 |
| 主观置信等级 | medium |
| 判断变化原因 | 较昨晚：现货及宏观观察未变；夜盘期指小涨、WTI回落，AI融资/需求新证据与现金回报疑问并存。 |

## 判断依据 · 反弹是否可靠？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 反弹是否可靠？ |
| 事实指标引用 | ["prices.QQQ.distance_sma20_pct", "prices.SMH.distance_sma20_pct", "prices.SPY.distance_sma20_pct", "prices.RSP.return_1d_pct", "prices.RSP.return_5d_pct"] |
| 推断与解释 | 推断：周初反弹回吐，尚未确认周线反转；周五与周线的等权表现要分开。 |
| 反证与缺口 | MU/DRAM与软件仍收涨；没有交易所成分广度。 |
| 确认条件 | QQQ709.30/SMH533.34收复回踩，SPY/RSP跟随，之后收复动态均线。 |
| 失效条件 | QQQ701.16/SMH521.47失守且反抽失败。 |
| 观察期限 | 未来1–5交易日 |
| 条件式指导 | 等待确认后分批试探，不把一次拉升当趋势。 |
| 主观置信等级 | medium |
| 判断变化原因 | 较昨晚：现货及宏观观察未变；夜盘期指小涨、WTI回落，AI融资/需求新证据与现金回报疑问并存。 |

## 判断依据 · 优先观察哪些板块？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 优先观察哪些板块？ |
| 事实指标引用 | ["prices.IGV.return_5d_pct", "prices.SMH.relative_spy_5d_pp", "prices.XLE.return_1d_pct", "prices.OIH.volume_vs_previous20_ratio"] |
| 推断与解释 | 推断：软件/云、能源优先观察，区域银行作轮动辅助；半导体仍待修复，不称主力净流入。 |
| 反证与缺口 | 能源依赖事件，软件涨幅未证明利润增长；申赎缺失。 |
| 确认条件 | 相对SPY持续领先，回踩守住，订单/利润或发行人申赎补证。 |
| 失效条件 | 领涨消失、跌破回踩低点或经营逻辑证伪。 |
| 观察期限 | 未来一周 |
| 条件式指导 | 先看强势无杠杆篮子，避免同时集中多个同一风险链。 |
| 主观置信等级 | medium |
| 判断变化原因 | 较昨晚：现货及宏观观察未变；夜盘期指小涨、WTI回落，AI融资/需求新证据与现金回报疑问并存。 |

## 判断依据 · AI需求与估值如何区分？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | AI需求与估值如何区分？ |
| 事实指标引用 | ["prices.NVDA.return_1d_pct", "prices.CRWV.distance_sma20_pct", "prices.MU.return_1d_pct"] |
| 推断与解释 | 需求和融资支撑增强，不能跨越到投资回报已改善的结论。 |
| 反证与缺口 | 25日H1002.89、七日+6.2%，SpaceX融资及AWS预订为需求反证；未独立核验新增融资条款和回报。 |
| 确认条件 | 企业自由现金流、融资与价格承接同步改善。 |
| 失效条件 | 订单/指引下修、资本投入长期超过现金生成且融资收紧。 |
| 观察期限 | 下一季度并每日跟踪风险 |
| 条件式指导 | 用公司整体FCFF情景，保留META输入缺口。 |
| 主观置信等级 | medium |
| 判断变化原因 | 较昨晚：现货及宏观观察未变；夜盘期指小涨、WTI回落，AI融资/需求新证据与现金回报疑问并存。 |

## AI资本开支的融资与回报率重估 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | Reuters25日报道Musk称SpaceX已完成400亿美元GPU债务融资，设备预期2027年一、二季度到货；另补核验Jassy23日称AWS2027大部分容量已预订、2028部分已订。均为管理层表述，不是本次独立财务审计。 |
| 事实：市场反应 | 23:08UTC供应商延迟报价：12月ES7682.00、NQ29253.75，较接口previousClose分别+0.29%/+0.47%；12月WTI102.26、−0.98%。取数23:18UTC，约10分钟延迟；非美股现货确认，不与23日不同交割Brent直接拼接。 |
| 推断：解释 | 推断：需求和融资渠道仍有支撑，但借款增加不证明投入回报达标；采购承诺不等于供应商已确认收入，更不等于所有AI公司受益。 |
| 受益篮子 | ["现金流可兑现企业观察"] |
| 受损篮子 | ["依赖持续融资的高投入公司"] |
| 反证 | 25日H100租金2.89美元/GPU小时、七日+6.2%；水平较24日2.88更高，七日涨幅下降不等于租金下降。资本开支、折旧、融资成本和现金回收仍须财报验证。 |
| 下一催化剂 | 微软28日及Amazon29日披露，核验云增长、资本开支与现金回收。 |
| 证据 | ["https://www.marketscreener.com/news/musk-says-spacex-raised-40-billion-in-debt-for-gpus-ce785cdfd18ff22c", "https://ca.finance.yahoo.com/news/amazon-cloud-capacity-sold-2027-230625532.html", "https://www.silicondata.com/products/silicon-index/h100", "https://www.apollo.com/wealth/insights-news/insights/daily-spark/no-signs-of-ai-payoff-outside-the-tech-sector", "https://www.gartner.com/en/newsroom/press-releases/2026-10-14-gartner-says-over-us-dollars-three-and-a-half-trillion-of-artificial-intelligence-infrastructure-spending-could-be-exposed-to-impairment-by-the-end-of-2030", "https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/default.aspx", "https://investor.lamresearch.com/2026-10-21-Lam-Research-Corporation-Reports-Financial-Results-for-the-Quarter-Ended-September-27,-2026", "https://nebius.com/newsroom/nebius-secures-3-5-billion-financing-facility-with-citi"] |

## 能源供给风险与通胀尾部 · 待核验

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 25日AP报道Trump称当日不会打击伊朗、外交沟通仍在；此话不保证之后停火，沙特供应设施损失仍未独立核实。 |
| 事实：市场反应 | WTI105触价合约76%→62.5%，沙特管线命中合约25.5%→30.5%，美伊专门停火合约82.5%→79.5%；延迟WTI期货小幅回落。 |
| 推断：解释 | 推断：油价初步缓和与设施尾部风险并存，各合约定义不同，不能合成统一战争概率。 |
| 受益篮子 | ["XLE", "OIH", "XOP观察"] |
| 受损篮子 | ["运输及能源成本敏感行业"] |
| 反证 | 袭击主张不证明管线受损；停火、通航与油价各有独立结算条件，不能合成战争概率。 |
| 下一催化剂 | 实际供应公告、周一油价跳空后的承接与回落。 |
| 证据 | ["https://apnews.com/article/4779a3deeb1a23f59414164532d5c885", "https://www.internazionale.it/ultime-notizie-reuters/2026/10/24/houthis-say-they-attacked-saudi-oil-sites-strikes-reported-on-yemen-s-aden", "https://www.energy.gov/articles/energy-department-use-defense-production-act-funding-restart-american-refinery-and-expand"] |

## 软件与云的相对强势 · 待核验

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 软件/云周线相对半导体领先；Jassy需求表述提供背景，本周微软与Amazon财报仍须验证实际增速与现金回报。 |
| 事实：市场反应 | 周五IGV涨1.72%、SKYY涨1.85%，但IGV量仅约前20日均量0.84倍；本周累计强势尚需开市续验。 |
| 推断：解释 | 推断：市场在AI链条内部重新选择；相对强势是观察证据，不能冒充机构净申购或盈利上修。 |
| 受益篮子 | ["IGV", "SKYY"] |
| 受损篮子 | ["不分软硬件的整条AI追涨/追空"] |
| 反证 | IGV周五量仅前20日均量约0.84倍，缺完整成分广度及订单验证。 |
| 下一催化剂 | 微软财报、回踩20日线后能否持续领先。 |
| 证据 | ["https://www.microsoft.com/en-us/investor/faq", "https://finance.yahoo.com/quote/IGV/history/"] |

## 等权小盘改善但持续性不足 · 待核验

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 周线改善与周五转弱并存，不能只取一个方向。 |
| 事实：市场反应 | RSP周+1.14%、IWM+1.96%、KRE+3.80%；XLF+0.68%、XLI−1.87%，周五RSP又跌0.77%。 |
| 推断：解释 | 推断：轮动不只是防御，也有区域银行修复；尚缺连续广度确认。 |
| 受益篮子 | ["RSP", "IWM", "KRE观察"] |
| 受损篮子 | ["机械追防御或等权赢家"] |
| 反证 | RSP/SPY本周没有连续三个交易日上升；信用仍较上周偏弱，工业未跟随。 |
| 下一催化剂 | 等权与金融同步跟随大盘、信用回落。 |
| 证据 | ["https://finance.yahoo.com/quote/RSP/history/", "https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/10/us-flash-pmi-signals-sustained-strong-growth-but-also-further-inflation-uplift-in-october"] |

## 跨境科技投资限制 · 待核验

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 财政部22日发布COINS拟议规则，仍是征求意见程序。 |
| 事实：市场反应 | SMH周−2.33%；本次不建立该公告对整个周跌幅的单一因果解释。 |
| 推断：解释 | 推断：投资与融资约束值得跟踪；不能写成已经生效的全面芯片销售禁令。 |
| 受益篮子 | ["合规与替代供应链观察"] |
| 受损篮子 | ["跨境科技投资敏感企业"] |
| 反证 | 例外条款及最终规则尚未确定，未量化单家公司营收影响。 |
| 下一催化剂 | 公司官方回应与最终规则。 |
| 证据 | ["https://home.treasury.gov/news/press-releases/sb0667/"] |

## 航天与工业需要独立催化剂 · 待核验

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | SpaceX融资消息强化算力与航天的交叉主题；Tesla/SpaceX控制权合约12.5%，没有核验正式控制权交易。Rocket Lab11月9日电话会沿用昨日官方日程核验。 |
| 事实：市场反应 | ARKX周−0.12%、ITA−3.27%、XLI−1.87%，不能与软件强势等同。 |
| 推断：解释 | 推断：SpaceX融资不能直接归为整个上市航天行业收入；工业订单与盈利仍需逐公司检查。 |
| 受益篮子 | ["正式合同与订单披露观察"] |
| 受损篮子 | ["仅凭并购传闻追价"] |
| 反证 | 控制权合约不代表行业景气，也不等于普通商业合作。 |
| 下一催化剂 | Rocket Lab11月9日财报；工业与航天需独立订单和利润验证。 |
| 证据 | ["https://www.marketscreener.com/news/musk-says-spacex-raised-40-billion-in-debt-for-gpus-ce785cdfd18ff22c", "https://investors.rocketlabcorp.com/node/13431/pdf", "https://polymarket.com/event/tesla-and-spacex-merger-officially-announced-by-june-30"] |

## 财政刺激承诺尚未成为已落实支出 · 待核验

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 周末社交线索再提现金分红；可核验的白宫9月10日声明将每名成年公民5000美元承诺与共和党赢得两院挂钩。 |
| 事实：市场反应 | 未核验新的拨款法案或发放时间，不将周五市场表现归因于这一再传播线索。 |
| 推断：解释 | 推断：若财政扩张真正落地可能影响消费、利率与通胀；当前只是政策观察，不能把承诺计入确定需求。 |
| 受益篮子 | ["消费相关观察"] |
| 受损篮子 | ["久期与通胀敏感资产观察"] |
| 反证 | 选举、立法与财政执行存在不确定性。 |
| 下一催化剂 | 正式立法、预算及实施公告 |
| 证据 | ["https://www.whitehouse.gov/releases/2026/09/trump-dividend-america-is-winning-and-americans-should-win-with-it/"] |

## tc 报价（供应商时戳不等于成交时戳）

| 标的 | 价格 USD | 变化% | 观测时间 | 供应商时间 | 抓取时间 | 质量 |
| --- | --- | --- | --- | --- | --- | --- |
| SPY | 759.97 | -0.52 | 缺失 | 缺失 | 2026-10-25T23:14:26.921Z | unverified_trade_timestamp |
| QQQ | 704.40 | -0.01 | 缺失 | 缺失 | 2026-10-25T23:14:26.921Z | unverified_trade_timestamp |
| RSP | 216.54 | -0.77 | 缺失 | 缺失 | 2026-10-25T23:14:26.921Z | unverified_trade_timestamp |
| IWM | 275.75 | -0.33 | 缺失 | 缺失 | 2026-10-25T23:14:26.921Z | unverified_trade_timestamp |
| SMH | 527.20 | 0.74 | 缺失 | 缺失 | 2026-10-25T23:14:26.921Z | unverified_trade_timestamp |
| IGV | 110.59 | 1.72 | 缺失 | 缺失 | 2026-10-25T23:14:26.921Z | unverified_trade_timestamp |
| XLE | 69.33 | 2.60 | 缺失 | 缺失 | 2026-10-25T23:14:26.921Z | unverified_trade_timestamp |
| XLF | 55.90 | -1.32 | 缺失 | 缺失 | 2026-10-25T23:14:26.921Z | unverified_trade_timestamp |
| GLD | 366.61 | -0.65 | 缺失 | 缺失 | 2026-10-25T23:14:26.921Z | unverified_trade_timestamp |
| TLT | 81.34 | -0.49 | 缺失 | 缺失 | 2026-10-25T23:14:26.921Z | unverified_trade_timestamp |
| NVDA | 210.96 | -0.59 | 缺失 | 缺失 | 2026-10-25T23:14:26.921Z | unverified_trade_timestamp |
| MSFT | 524.51 | 0.66 | 缺失 | 缺失 | 2026-10-25T23:14:26.921Z | unverified_trade_timestamp |
| AMZN | 248 | -0.95 | 缺失 | 缺失 | 2026-10-25T23:14:26.921Z | unverified_trade_timestamp |
| GOOGL | 320.21 | -1.24 | 缺失 | 缺失 | 2026-10-25T23:14:26.921Z | unverified_trade_timestamp |
| META | 642.62 | -0.96 | 缺失 | 缺失 | 2026-10-25T23:14:26.921Z | unverified_trade_timestamp |

## 核心行情与风险代理

| 标的 | 价格/指数 | 单位 | 观测日 | 1日% | 5日% | 20日% | 质量 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 759.97 | USD_per_share | 2026-10-23 | -0.52 | -0.43 | -1.48 | ok |
| QQQ | 704.40 | USD_per_share | 2026-10-23 | -0.01 | -0.76 | -5.39 | ok |
| IWM | 275.75 | USD_per_share | 2026-10-23 | -0.33 | 1.96 | -2.21 | ok |
| RSP | 216.54 | USD_per_share | 2026-10-23 | -0.77 | 1.14 | 2.57 | ok |
| GLD | 366.61 | USD_per_share | 2026-10-23 | -0.65 | -4.03 | -6.81 | ok |
| GC=F | 4,007.90 | USD_per_troy_ounce | 2026-10-23 | -1.29 | -4.14 | -7.25 | ok |
| CL=F | 103.27 | USD_per_barrel | 2026-10-23 | 3.82 | 1.83 | 11.75 | ok |
| BZ=F | 116.72 | USD_per_barrel | 2026-10-23 | 3.14 | 6.24 | 11.89 | ok |
| TLT | 81.34 | USD_per_share | 2026-10-23 | -0.49 | 1.61 | 2.96 | ok |
| UUP | 28.96 | USD_per_share | 2026-10-23 | 0.21 | 0.14 | 1.19 | ok |
| HYG | 77.05 | USD_per_share | 2026-10-23 | -0.06 | 0.25 | -0.60 | ok |
| LQD | 103.85 | USD_per_share | 2026-10-23 | -0.41 | 0.44 | 1.05 | ok |
| ^VIX | 19.45 | index | 2026-10-23 | 2.21 | -2.70 | 30.80 | ok |
| ^VIX3M | 20.48 | index | 2026-10-23 | 1.79 | -0.10 | 14.22 | ok |
| ^VVIX | 109.70 | index | 2026-10-23 | 1.63 | -0.19 | 24.89 | ok |
| ^MOVE | 103.31 | index | 2026-10-23 | -3.30 | 2.19 | -1.21 | ok |
| NVDA | 210.96 | USD_per_share | 2026-10-23 | -0.59 | -1.48 | -6.27 | ok |
| MSFT | 524.51 | USD_per_share | 2026-10-23 | 0.66 | -0.86 | 1.62 | ok |
| AMZN | 248.00 | USD_per_share | 2026-10-23 | -0.95 | -0.80 | -0.67 | ok |
| GOOGL | 320.21 | USD_per_share | 2026-10-23 | -1.24 | -5.98 | -6.89 | ok |
| META | 642.62 | USD_per_share | 2026-10-23 | -0.96 | -9.40 | -14.51 | ok |
| CRWV | 54.24 | USD_per_share | 2026-10-23 | -2.46 | -11.65 | -38.08 | ok |
| MU | 877.55 | USD_per_share | 2026-10-23 | 2.46 | -0.15 | -18.90 | ok |
| DRAM | 47.06 | USD_per_share | 2026-10-23 | 3.02 | 1.31 | -23.99 | ok |
| VRT | 194.32 | USD_per_share | 2026-10-23 | -0.65 | -5.86 | -23.28 | ok |

## 跨资产风险解释

判断不变：分化与风险压力，尚无全面恐慌或过热的充分证据。23日VIX19.45、VIX3M20.48，后者是期限指数而非期货曲线；MOVE103.31。22日2年/10年收益率4.65%/4.96%、实际10年2.64%，HY340bp/IG89bp。周五黄金GLD跌0.65%、TLT跌0.49%、UUP涨0.21%，避险并不同步；WTI103.27、Brent116.72为23日连续期货价格，非周日现价或同交割合约收益。GPR至19日、金融压力至16日，均无法检验周末变化。沙特管线合约回升、油价触价合约下降并存，不能制造统一战争指数。CNN不可用；政策维持合约93.5%不等于Fed已经决定，也不能替代实际利率路径。 夜盘增量：23:08UTC供应商延迟报价：12月ES7682.00、NQ29253.75，较接口previousClose分别+0.29%/+0.47%；12月WTI102.26、−0.98%。取数23:18UTC，约10分钟延迟；非美股现货确认，不与23日不同交割Brent直接拼接。 这些早段修复不能证明现货广度改善。

## 宏观与地缘风险指标

| 指标 | 数值 | 单位 | 观测日 | 20次观测变化 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- | --- |
| DGS2 | 4.65 | percent | 2026-10-22 | -0.20 | lagged | https://fred.stlouisfed.org/series/DGS2 |
| BAMLH0A0HYM2 | 3.40 | percentage_points | 2026-10-22 | 0.60 | lagged | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| BAMLC0A0CM | 0.89 | percentage_points | 2026-10-22 | 0.10 | lagged | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| DGS10 | 4.96 | percent | 2026-10-22 | -0.15 | lagged | https://fred.stlouisfed.org/series/DGS10 |
| DFII10 | 2.64 | percent | 2026-10-22 | -0.12 | lagged | https://fred.stlouisfed.org/series/DFII10 |
| T10YIE | 2.34 | percent | 2026-10-23 | 0.01 | ok | https://fred.stlouisfed.org/series/T10YIE |
| STLFSI4 | -0.63 | index | 2026-10-16 | 0.04 | lagged | https://fred.stlouisfed.org/series/STLFSI4 |
| CBOE_VIX | 19.45 | index | 2026-10-23 | 4.58 | ok | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
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
| XLK | 科技 | 0.49 | -0.13 | -6.64 | 1.01 | 0.30 | -5.17 | 0.85 | 2026-10-23 |
| XLE | 能源 | 2.60 | 1.60 | 11.75 | 3.13 | 2.03 | 13.23 | 1.21 | 2026-10-23 |
| XLF | 金融 | -1.32 | 0.68 | 1.93 | -0.80 | 1.11 | 3.41 | 0.78 | 2026-10-23 |
| XLI | 工业 | -1.27 | -1.87 | -3.41 | -0.74 | -1.44 | -1.93 | 0.96 | 2026-10-23 |
| XLV | 医疗 | -1.11 | 1.45 | 5.03 | -0.59 | 1.88 | 6.50 | 0.90 | 2026-10-23 |
| XLP | 必需消费 | -1.92 | 0.73 | 7.56 | -1.40 | 1.16 | 9.03 | 1.48 | 2026-10-23 |
| XLY | 可选消费 | -1.66 | 0.57 | 2.30 | -1.14 | 1.00 | 3.77 | 0.90 | 2026-10-23 |
| XLC | 通信 | -1.78 | -4.36 | -6.60 | -1.26 | -3.93 | -5.12 | 0.83 | 2026-10-23 |
| XLU | 公用事业 | -0.72 | 0.83 | 7.72 | -0.20 | 1.26 | 9.19 | 0.51 | 2026-10-23 |
| XLRE | 房地产 | 0.12 | 0.97 | 2.43 | 0.64 | 1.40 | 3.91 | 1.22 | 2026-10-23 |
| XLB | 材料 | -0.74 | 0.77 | 3.03 | -0.21 | 1.20 | 4.51 | 0.72 | 2026-10-23 |
| SMH | 半导体 | 0.74 | -2.33 | -13.08 | 1.26 | -1.90 | -11.61 | 0.91 | 2026-10-23 |
| IGV | 软件 | 1.72 | 5.99 | 4.32 | 2.24 | 6.42 | 5.80 | 0.84 | 2026-10-23 |
| XOP | 油气开采 | 2.45 | 0.65 | 11.12 | 2.97 | 1.08 | 12.60 | 0.94 | 2026-10-23 |
| OIH | 油服 | 5.40 | 3.97 | 0.93 | 5.92 | 4.40 | 2.41 | 2.14 | 2026-10-23 |
| ITA | 航空与国防 | -1.10 | -3.27 | -5.42 | -0.58 | -2.84 | -3.94 | 1.00 | 2026-10-23 |
| ARKX | 航天主题 | 0.71 | -0.12 | -8.73 | 1.23 | 0.31 | -7.26 | 0.55 | 2026-10-23 |
| KRE | 区域银行 | 0.07 | 3.80 | 1.27 | 0.59 | 4.23 | 2.75 | 1.00 | 2026-10-23 |
| SKYY | 云计算 | 1.85 | 5.58 | 1.63 | 2.37 | 6.01 | 3.10 | 2.80 | 2026-10-23 |

## 资金证据分层

周五同源收盘：软件IGV+1.72%、云SKYY+1.85%、能源XLE+2.60%、油服OIH+5.40%，半导体SMH+0.74%；SPY−0.52%、RSP−0.77%、IWM−0.33%、XLF−1.32%，表明广度尚未共振。周线窗口16→23日，IGV+5.99%、SKYY+5.58%、OIH+3.97%、KRE+3.80%领先，SMH−2.33%、XLI−1.87%、ITA−3.27%、XLC−4.36%落后。固定19只ETF完整比较见数据章节，不把周线与单日混为一谈。优先观察软件/云与能源回踩承接，金融作为广度验证，半导体等待本周披露。资金证据仅价格量能：重查SMH发行人仍缺连续份额与拆分桥，无法计算净申赎；ICI最新可核验仍截至14日，ETF净发行532.62亿美元、国内股票296.70亿美元，不能代表当前行业主力净流入。 夜盘指数期货的上涨不能当作19个ETF当期净流入；仍等待今晚常规时段板块相对强弱。

## 最近可核验 ETF 申赎窗口

| 标的 | 金额 USD million | 起始日 | 结束日 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- |

## Polymarket 搜索覆盖与限制

2026-10-25T23:20:30.049887+00:00：基础25主题及跟踪清单重新采集；主动搜索Saudi oil attack、Microsoft earnings、Seagate earnings、Sandisk earnings、AI bankruptcy、bank failure、recession、CPI November，复核11个重点合约同规则hash。CPI28条仍截断。SNDK84%但成交151美元/价差18个百分点；STX所查档价差32–41个百分点，排除强定量信号。银行失败合约82.5%、成交1724美元、价差3个百分点，仅为薄市场线索；FDIC403且未找到可核验新关闭公告，不得解读为系统危机82.5%。

## Polymarket · 值得警惕的信号

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["AI bubble burst in 2026?", "期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。", "https://polymarket.com/event/ai-bubble-burst-by"] | [9.049999999999999, {"status": "comparable", "change_pp": 0.050000000000000044}] | {"spread": 0.009000000000000008, "volume24h_usd": 224.567263, "liquidity_usd": 32734.69153, "quality_flags": ["volume24h_under_1000_or_unknown"], "retrieved_at": "2026-10-25T23:15:37.549648+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["本次同定义变化与质量见比较及事件表，需独立经营或供应证据。", "AI估值与融资风险"] | ["同规则价格持续上行并有经营/信用证据", "现金流和信用改善"] | [null, null] |
| ["Will WTI Crude Oil (WTI) hit (HIGH) $105 in October?", "10月交易时段内，Pyth的ICE WTI活跃月合约1分钟最终高价达到105美元即Yes；按规则提前3个交易时段换月，数据不可用时可依ICE日高低。不是月末价格，也不能以Yahoo CL=F直接结算。", "https://polymarket.com/event/what-price-will-wti-hit-in-october-2026"] | [62.5, {"status": "comparable", "change_pp": -13.5}] | {"spread": 0.030000000000000027, "volume24h_usd": 17037.279570000002, "liquidity_usd": 27342.7657, "quality_flags": [], "retrieved_at": "2026-10-25T23:15:37.549648+00:00", "contract_end_at": "2026-11-01T03:59:59.999000+00:00"} | ["本次同定义变化与质量见比较及事件表，需独立经营或供应证据。", "能源成本→利率→成长估值"] | ["供应中断与可核验油价共同走强", "通行恢复及供应增加"] | [null, null] |
| ["Military action against Saudi Oil Pipeline (East-West) by October 31?", "截至10月31日利雅得23:59，空袭或地对地武器直接命中东西输油管线或泵站才算Yes；拦截弹碎片、未执行威胁、网络攻击等排除。按沙特官方及可信报道共识裁决，争议可等待三天。价格不证明已命中或发生供应损失。", "https://polymarket.com/event/military-action-against-saudi-oil-pipeline-east-west-byptptpt"] | [30.5, {"status": "comparable", "change_pp": 4.999999999999999}] | {"spread": 0.030000000000000027, "volume24h_usd": 7646.409641, "liquidity_usd": 30006.1787, "quality_flags": [], "retrieved_at": "2026-10-25T23:14:34.458538+00:00", "contract_end_at": "2026-10-31T20:59:00+00:00"} | ["本次30.5%，较昨晚+5个百分点；24小时成交7646美元、价差3个百分点。并未独立证实管线命中或供应损失。", "若管线或泵站实际受损，可能影响绕行出口能力，抬高能源成本。"] | ["沙特官方/独立来源证实直接命中与供应影响，且市场恢复交易后油价持续走强。", "只有已拦截导弹或警报解除，未发生合格命中；供应正常且价格回落。"] | [null, null] |

## Polymarket · 有参考价值的事件

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["US x Iran ceasefire continues through October 31?", "截至10月31日伊朗标准时间23:59，美国未对伊朗领土及内水实施规则列明的直接命中空袭或地对地打击才为Yes。海域/空域、拦截碎片、小型打击、网络战等不计；争议信息允许三日核验。不是所有交战方全面停火，也不等于海峡畅通。", "https://polymarket.com/event/us-iran-ceasefire-continues-throughptptpt"] | [79.5, {"status": "comparable", "change_pp": -2.9999999999999916}] | {"spread": 0.010000000000000009, "volume24h_usd": 677367.4358180001, "liquidity_usd": 52769.2745, "quality_flags": [], "retrieved_at": "2026-10-25T23:15:37.549648+00:00", "contract_end_at": "2026-10-31T23:59:00+00:00"} | ["本次79.5%，较昨晚−3个百分点；专门美伊停火定义不覆盖地区所有攻击。", "仅美国对伊朗领土合格打击的定义，与沙特/胡塞管线风险不同。"] | ["规则所列打击事实及资产反应共同核验。", "其他地区攻击不能自动算作该合约触发。"] | [null, null] |
| ["Strait of Hormuz traffic returns to normal by December 31?", "期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。", "https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31"] | [11.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.009999999999999995, "volume24h_usd": 115809.69935899998, "liquidity_usd": 502255.2742, "quality_flags": [], "retrieved_at": "2026-10-25T23:15:37.549648+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["通航指标与军事停火不同。", "IMF七日平均船舶到达不少于60，不能由单日放行新闻替代。"] | ["官方Portwatch连续数据达到定义。", "只出现局部绕行或有限通航。"] | [null, null] |

## Polymarket · 将要发生的事件及概率

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Will there be no change in Fed interest rates after the October 2026 meeting?", "以10月27–28日FOMC前后联邦基金目标区间上限不变结算；非25bp标准变动向上取整至25bp档；若下一会议期限仍无声明按不变档结算。", "https://polymarket.com/event/fed-decision-in-october-20260617190323537"] | [93.5, {"status": "comparable", "change_pp": -1.9999999999999907}] | {"spread": 0.009999999999999898, "volume24h_usd": 1322178.7326839997, "liquidity_usd": 1452061.9182, "quality_flags": [], "retrieved_at": "2026-10-25T23:15:37.549648+00:00", "contract_end_at": "2026-10-29T03:59:00+00:00"} | ["Will there be no change in Fed interest rates after the October 2026 meeting?；专门规则解释，变化须结合价差和经营证据。", "政策上限变化影响折现率"] | ["官方声明发布后核验", "会前预期不是实际决定"] | ["2026-10-28T14:00:00-04:00", "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm"] |
| ["Will Microsoft (MSFT) beat quarterly earnings?", "下一季度首次披露GAAP EPS严格大于固定4.82美元，四舍五入到美分；优先稀释、未披露才用基本EPS。官方财报优先，缺失用SeekingAlpha；公告日收盘后96小时仍无数据或预期日后45天无财报则No。除明显即时错误外不采用后续重述。4.82为建约时阈值，不是当前一致预期；合约价格不能解释成股价上涨概率。", "https://polymarket.com/event/msft-quarterly-earnings-gaap-eps-10-28-2026-4pt82"] | [78.0, {"status": "comparable", "change_pp": 2.0000000000000018}] | {"spread": 0.040000000000000036, "volume24h_usd": 1129.186533, "liquidity_usd": 948.3106, "quality_flags": ["liquidity_under_10000_or_unknown"], "retrieved_at": "2026-10-25T23:15:37.549648+00:00", "contract_end_at": "2026-10-28T21:00:00+00:00"} | ["基础快照78%、价差4个百分点、24小时成交1129美元；补查79%属不同时点，不混用。固定GAAP EPS>4.82不等于股价上涨。", "财报影响云/AI估值；EPS之外更须检查资本开支、自由现金流与指引。"] | ["官方首次披露GAAP EPS与专门规则核验，同时看指引与股价承接。", "EPS过线但现金回报/指引转差、股价失守；不可由合约直接推导交易方向。"] | [null, null] |

## Will there be no change in Fed interest rates after the October 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 606422 / 2589812 |
| Yes 概率 % | 93.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-1.0, 6.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -1.9999999999999907} |
| 24h成交量 / 流动性 USD | [1322178.7326839997, 1452061.9182] |
| 价差 pp | 1.00 |
| 到期 | 2026-10-29T03:59:00+00:00 |
| 结算规则摘要 | 以10月27–28日FOMC前后联邦基金目标区间上限不变结算；非25bp标准变动向上取整至25bp档；若下一会议期限仍无声明按不变档结算。 |
| 规则指纹 | fbc973610971c579003bb7db1464373da28fb0d8484ae204350268d22f83fb7e |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-25T23:10:37.023213Z |
| 抓取时间 | 2026-10-25T23:15:37.549648+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-october-20260617190323537 |

## US x Iran ceasefire continues through October 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1038648 / 4641065 |
| Yes 概率 % | 79.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-3.0, -3.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -2.9999999999999916} |
| 24h成交量 / 流动性 USD | [677367.4358180001, 52769.2745] |
| 价差 pp | 1.00 |
| 到期 | 2026-10-31T23:59:00+00:00 |
| 结算规则摘要 | 截至10月31日伊朗标准时间23:59，美国未对伊朗领土及内水实施规则列明的直接命中空袭或地对地打击才为Yes。海域/空域、拦截碎片、小型打击、网络战等不计；争议信息允许三日核验。不是所有交战方全面停火，也不等于海峡畅通。 |
| 规则指纹 | 4ad99c00bba55951472643794eca27dab0743ff8891a0f80509306b4b3c87506 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-25T23:14:37.271275Z |
| 抓取时间 | 2026-10-25T23:15:37.549648+00:00 |
| 来源 | https://polymarket.com/event/us-iran-ceasefire-continues-throughptptpt |

## Strait of Hormuz traffic returns to normal by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 455875 / 2176270 |
| Yes 概率 % | 11.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, -1.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [115809.69935899998, 502255.2742] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。 |
| 规则指纹 | b0c8ba27f4437b0d8ab819ae170bec118166232e39cdcaefb95bd352d29073d4 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-25T23:10:37.023213Z |
| 抓取时间 | 2026-10-25T23:15:37.549648+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31 |

## Strait of Hormuz traffic returns to normal by October 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 830253 / 3501950 |
| Yes 概率 % | 0.45 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, -0.65] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.04999999999999996} |
| 24h成交量 / 流动性 USD | [61417.81804399999, 186595.50134] |
| 价差 pp | 0.10 |
| 到期 | 2026-11-01T03:59:00+00:00 |
| 结算规则摘要 | 10月31日前IMF Portwatch海峡船舶通行7日均值任一天达到60才为Yes；非宣布开放。末日数据等待14日，有窗口内修订和明显数据错误处理。 |
| 规则指纹 | be893052d9d9b648fb6ffa8b901ed6d9775d1cd3d1be9f830e1dcf5d0f046390 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-25T23:14:37.271275Z |
| 抓取时间 | 2026-10-25T23:15:37.549648+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-october-31-20260810151043583 |

## Will WTI Crude Oil (WTI) hit (HIGH) $105 in October?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1078055 / 4951227 |
| Yes 概率 % | 62.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-11.0, 26.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -13.5} |
| 24h成交量 / 流动性 USD | [17037.279570000002, 27342.7657] |
| 价差 pp | 3.00 |
| 到期 | 2026-11-01T03:59:59.999000+00:00 |
| 结算规则摘要 | 10月交易时段内，Pyth的ICE WTI活跃月合约1分钟最终高价达到105美元即Yes；按规则提前3个交易时段换月，数据不可用时可依ICE日高低。不是月末价格，也不能以Yahoo CL=F直接结算。 |
| 规则指纹 | 0c455b139d74a669b793323a95aea1e08486656281c457348bd488137e37ae8a |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-25T23:10:37.023213Z |
| 抓取时间 | 2026-10-25T23:15:37.549648+00:00 |
| 来源 | https://polymarket.com/event/what-price-will-wti-hit-in-october-2026 |

## Will the Fed increase interest rates by 25 bps after the December 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 770450 / 3215008 |
| Yes 概率 % | 76.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, 1.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [12912.86111, 166460.6605] |
| 价差 pp | 1.00 |
| 到期 | 2026-12-09T23:59:00+00:00 |
| 结算规则摘要 | 以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。 |
| 规则指纹 | 933a10a15eeec0ff1de30468fa20540301ed243f75cc3572d42946192f81a123 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-25T23:10:37.023213Z |
| 抓取时间 | 2026-10-25T23:15:37.549648+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-december-20260729232808632 |

## Tesla and SpaceX merger officially announced by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 192962 / 2252540 |
| Yes 概率 % | 12.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-4.0, -15.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -3.0} |
| 24h成交量 / 流动性 USD | [6224.617206, 30066.8133] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59纽约时间前，Tesla或SpaceX正式宣布双方合并或一方收购另一方的控制权即Yes；无需在期限内完成交易。控制权通常为过半权益或等效治理权；少数股权投资及仅讨论不算。以公司公告或可信报道共识核验；旧URL中的june-30不是本合约期限。 |
| 规则指纹 | 909906ae3b6db7e473468713ea6a1e1e4cf4c931fe247c7d3d576e7986513008 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-25T23:14:37.271275Z |
| 抓取时间 | 2026-10-25T23:15:37.549648+00:00 |
| 来源 | https://polymarket.com/event/tesla-and-spacex-merger-officially-announced-by-june-30 |

## Will Microsoft (MSFT) beat quarterly earnings?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1200526 / 5778671 |
| Yes 概率 % | 78.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-1.0, -3.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 2.0000000000000018} |
| 24h成交量 / 流动性 USD | [1129.186533, 948.3106] |
| 价差 pp | 4.00 |
| 到期 | 2026-10-28T21:00:00+00:00 |
| 结算规则摘要 | 下一季度首次披露GAAP EPS严格大于固定4.82美元，四舍五入到美分；优先稀释、未披露才用基本EPS。官方财报优先，缺失用SeekingAlpha；公告日收盘后96小时仍无数据或预期日后45天无财报则No。除明显即时错误外不采用后续重述。4.82为建约时阈值，不是当前一致预期；合约价格不能解释成股价上涨概率。 |
| 规则指纹 | c38981deb507343e93936539de51b155f638166eb35f7eaca3a8513338e39cb0 |
| 质量 | ["liquidity_under_10000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-10-25T23:14:37.271275Z |
| 抓取时间 | 2026-10-25T23:15:37.549648+00:00 |
| 来源 | https://polymarket.com/event/msft-quarterly-earnings-gaap-eps-10-28-2026-4pt82 |

## AI bubble burst in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 691340 |
| Yes 概率 % | 9.05 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.4, 1.3] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.050000000000000044} |
| 24h成交量 / 流动性 USD | [224.567263, 32734.69153] |
| 价差 pp | 0.90 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | fc153b2136a8dfbadcd169dce1add40690acb1748566b99716fe7ae8fcb07330 |
| 质量 | ["volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-10-25T23:10:37.023213Z |
| 抓取时间 | 2026-10-25T23:15:37.549648+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## AI bubble burst by June 30, 2027?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 4838928 |
| Yes 概率 % | 22.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.5, 6.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [126.799131, 12178.6683] |
| 价差 pp | 1.00 |
| 到期 | 2027-07-01T03:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | bd0420587e08487fffa5050e7fd9b79ffff909a9f843d3f620207ee859462505 |
| 质量 | ["volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-10-25T23:10:37.023213Z |
| 抓取时间 | 2026-10-25T23:15:37.549648+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## Military action against Saudi Oil Pipeline (East-West) by October 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1147445 / 5401795 |
| Yes 概率 % | 30.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-4.0, 6.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 4.999999999999999} |
| 24h成交量 / 流动性 USD | [7646.409641, 30006.1787] |
| 价差 pp | 3.00 |
| 到期 | 2026-10-31T20:59:00+00:00 |
| 结算规则摘要 | 截至10月31日利雅得23:59，空袭或地对地武器直接命中东西输油管线或泵站才算Yes；拦截弹碎片、未执行威胁、网络攻击等排除。按沙特官方及可信报道共识裁决，争议可等待三天。价格不证明已命中或发生供应损失。 |
| 规则指纹 | 069363ea2366e79b0328bfc26ff2cd674087f85aac50b63930c45e30f0b86adf |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-25T23:12:37.854162Z |
| 抓取时间 | 2026-10-25T23:14:34.458538+00:00 |
| 来源 | https://polymarket.com/event/military-action-against-saudi-oil-pipeline-east-west-byptptpt |

## AI 压力：合约、经营与估值分开

三层分开。合约：2026年底专门严重下行9.05%、2027年6月底22.5%，前者较昨晚增加0.05个百分点，后者不变；24小时成交仅约225/127美元，变化不具强定量意义。规则要求同一90天内至少三项极端事件，不是一般回撤概率。经营：SpaceX大额GPU债务融资与AWS容量需求表述是反驳需求全面崩塌的线索；融资与预订仍不证明利润、现金流或最终资本回报。25日H1002.89美元/GPU小时、七日+6.2%；较24日2.88上升0.01美元，滚动七日涨幅降低并非当日租金下降。Apollo24日观点和Gartner14日长期情景保留为背景，不能当新减值事实。估值：本次SEC检查五家公司均成功，较昨晚无更新10-Q/K；前四家复用核验底稿、以23日股价重算公司整体五年FCFF和隐含增长，META22日最新财报仍缺租赁新增及净债务桥，不出伪精确估值。情景假设不等于观测，融资额也不等于NVDA当期收入。

## NVDA · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | scenario_analysis |
| 财务底稿 | TTM 至 2026-07-26；最新 10-Q / filed 2026-08-26 |
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001045810.json", "checked_at": "2026-10-25T23:17:56.853658+00:00", "latest_filing_date": "2026-08-26"} |
| 观测财务数据 | {"ttm_revenue_million": 302970, "revenue_quarters": [{"end": "2025-10-26", "value": 57006000000, "filed": "2025-11-19", "duration_days": 91}, {"end": "2026-01-25", "value": 68127000000, "filed": "2026-02-25", "duration_days": 91}, {"end": "2026-04-26", "value": 81615000000, "filed": "2026-05-20", "duration_days": 91}, {"end": "2026-07-26", "value": 96221000000, "filed": "2026-08-26", "duration_days": 91}], "cash_million": 22443.0, "liquid_investments_million": 34143.0, "debt_million": 33366.0, "finance_lease_million": 0, "diluted_shares_million": 24285.0, "latest_operating_income_million": 63734.0, "observed_end": "2026-07-26", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "Revenues", "latest_reported_revenue_million": 96221.0, "income_statement_window": "最近单季度", "ttm_bridge_note": "采用同版 FY2026全年 + FY2027半年 - FY2026半年；与四季逐项求和差1百万为披露舍入差。"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json", "https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。10-Q Note14 表明融资租赁费用不重大；模型按不重大近似零，不将其称为精确零负债。未确认担保仅作为压力情景，非已到期净债务。市场化股权42783和非市场化股权51157不作为类现金；非经营资产加回为0的保守假设。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | 无 |
| 价格 USD | 210.96 |
| 基期输入 USD million / million shares | {"revenue": 302970, "net_debt": -23220.0, "diluted_shares": 24285.0, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.2868908474195032, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## NVDA · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 98.77 | -53.18 | 14.00 | 60.00 | 12.00 | 68.42 |
| 基准 | 154.12 | -26.95 | 20.00 | 65.00 | 11.00 | 74.20 |
| 乐观 | 242.58 | 14.99 | 26.00 | 70.00 | 10.00 | 79.05 |

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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0000789019.json", "checked_at": "2026-10-25T23:17:59.301786+00:00", "latest_filing_date": "2026-07-29"} |
| 观测财务数据 | {"ttm_revenue_million": 331839.0, "revenue_quarters": [{"end": "2025-09-30", "value": 77673000000, "filed": "2025-10-29", "duration_days": 92}, {"end": "2025-12-31", "value": 81273000000, "filed": "2026-01-28", "duration_days": 92}, {"end": "2026-03-31", "value": 82886000000, "filed": "2026-04-29", "duration_days": 90}, {"end": "2026-06-30", "value": 90007000000, "filed": "2026-07-29", "duration_days": 91}], "cash_million": 20935.0, "liquid_investments_million": 55908.0, "debt_million": 40294.0, "finance_lease_million": 66594.0, "diluted_shares_million": 7453.0, "latest_operating_income_million": 155237.0, "observed_end": "2026-06-30", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "RevenueFromContractWithCustomerExcludingAssessedTax", "latest_reported_revenue_million": 331839.0, "income_statement_window": "FY2026 全年"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0000789019.json", "https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。融资租赁66594计入债务；资本开支假设涵盖新增租赁，现金支出115948加融资租赁资产新增24608为本年经济资本开支140556。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | 无 |
| 价格 USD | 524.51 |
| 基期输入 USD million / million shares | {"revenue": 331839.0, "net_debt": 30045.0, "diluted_shares": 7453.0, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.3136388704960468, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## MSFT · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 143.02 | -72.73 | 8.00 | 42.00 | 10.50 | 76.13 |
| 基准 | 266.55 | -49.18 | 14.00 | 47.00 | 9.50 | 81.05 |
| 乐观 | 484.83 | -7.56 | 20.00 | 52.00 | 8.50 | 84.97 |

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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001018724.json", "checked_at": "2026-10-25T23:18:01.797644+00:00", "latest_filing_date": "2026-07-31"} |
| 观测财务数据 | {"ttm_revenue_million": 775680.0, "revenue_quarters": [{"end": "2025-09-30", "value": 180169000000, "filed": "2025-10-31", "duration_days": 92}, {"end": "2025-12-31", "value": 213386000000, "filed": "2026-02-06", "duration_days": 92}, {"end": "2026-03-31", "value": 181519000000, "filed": "2026-04-30", "duration_days": 90}, {"end": "2026-06-30", "value": 200606000000, "filed": "2026-07-31", "duration_days": 91}], "cash_million": 78213.0, "liquid_investments_million": 44775.0, "debt_million": 133320.0, "finance_lease_million": 13451.0, "diluted_shares_million": 10903.0, "latest_operating_income_million": 27461.0, "observed_end": "2026-06-30", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "RevenueFromContractWithCustomerExcludingAssessedTax", "latest_reported_revenue_million": 200606.0, "income_statement_window": "最近单季度"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001018724.json", "https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。总长期债务132995（含当前部分）加短期借款325，融资租赁13451另加；未将其他长期负债全部误作有息债务。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | 无 |
| 价格 USD | 248.00 |
| 基期输入 USD million / million shares | {"revenue": 775680.0, "net_debt": 23783.0, "diluted_shares": 10903.0, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.387477689183534, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## AMZN · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 11.53 | -95.35 | 6.00 | 12.00 | 11.00 | 84.01 |
| 基准 | 87.42 | -64.75 | 12.00 | 17.00 | 10.00 | 83.61 |
| 乐观 | 238.05 | -4.01 | 18.00 | 22.00 | 9.00 | 86.04 |

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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001652044.json", "checked_at": "2026-10-25T23:18:04.226539+00:00", "latest_filing_date": "2026-07-23"} |
| 观测财务数据 | {"ttm_revenue_million": 445867.0, "revenue_quarters": [{"end": "2025-09-30", "value": 102346000000, "filed": "2025-10-30", "duration_days": 92}, {"end": "2025-12-31", "value": 113829000000, "filed": "2026-02-05", "duration_days": 92}, {"end": "2026-03-31", "value": 109896000000, "filed": "2026-04-30", "duration_days": 90}, {"end": "2026-06-30", "value": 119796000000, "filed": "2026-07-23", "duration_days": 91}], "cash_million": 55911.0, "liquid_investments_million": 186563.0, "debt_million": 100164, "finance_lease_million": 2590.0, "diluted_shares_million": 12309.0, "latest_operating_income_million": 40770.0, "observed_end": "2026-06-30", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "Revenues", "latest_reported_revenue_million": 119796.0, "income_statement_window": "最近单季度"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001652044.json", "https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/goog-20260630.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。优先股按完全转换处理：季度稀释股数12309减已计入的16，再加合同最大转换股数54.45825；不再扣19000优先股本金。未来3年优先股息按年1203.125、10%折现约2991.99计入权益桥调整，此为保守假设；capped call 未赋值。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | {"preferred_coupon_pv_million": 2991.9938016528904, "discount_rate": 0.1, "years": 3} |
| 价格 USD | 320.21 |
| 基期输入 USD million / million shares | {"revenue": 445867.0, "net_debt": -136728.0061983471, "diluted_shares": 12347.45825, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.3746363553506026, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## GOOGL · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 66.88 | -79.11 | 7.00 | 31.00 | 11.00 | 79.41 |
| 基准 | 131.94 | -58.79 | 13.00 | 36.00 | 10.00 | 82.80 |
| 乐观 | 250.29 | -21.83 | 19.00 | 41.00 | 9.00 | 85.75 |

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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001326801.json", "checked_at": "2026-10-25T23:18:06.648089+00:00", "latest_filing_date": "2026-10-22"} |
| 观测财务数据 | {"revenue_million": 64601, "operating_cashflow_million": 32790, "reported_capex_including_finance_lease_principal_million": 34910, "company_defined_fcf_million": -2120, "diluted_shares_million": 2573, "reported_operating_income_million": 12988, "legal_charge_million": 9900, "observed_end": "2026-09-30", "published_at": "2026-10-21T16:01:00-04:00", "unit": "USD million; shares million", "noncancelable_commitments_million": 454520, "leases_not_commenced_million": 355730, "contingent_cloud_capacity_max_million": 14720, "restricted_cash_reclassified_million": 10800, "commitments_due_2026_million": 45850, "commitments_due_2027_million": 121410} |
| 来源 | ["https://www.prnewswire.com/news-releases/meta-reports-third-quarter-2026-results-302915964.html", "https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm"] |
| 口径 | 公司FCF扣除融资租赁本金，不能直接代替模型FCFF；融资租赁负债/新增资产未齐，不假设零。法律费用不全归AI经营。 |
| 主观假设说明 | 缺失 |
| 权益桥额外假设 | 无 |
| 缺失原因 | 10月22日新10-Q已核验；多年承诺与受限资金已记录，但完整融资租赁负债及资产新增口径未齐，不将不同承诺简单当现有债务，暂停精确FCFF反推。 |

## 大盘反弹逐级确认

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 下一交易日开盘承接与随后收盘 |
| 关联标的 | ["SPY", "QQQ", "SMH", "RSP"] |
| 确认条件 | 第一层QQQ709.30、SMH533.34、SPY763.47收复且回踩守住，RSP同时跟随；第二层收复21日收盘QQQ725.20、SMH556.70、SPY773.09并有连续收盘承接；动态20日线当前QQQ735.24、SMH585.55另作趋势确认。不能把周五小反弹直接当周线反转。 |
| 失效条件 | QQQ701.16、SMH521.47、SPY758.68失守且反抽不能收回；或科技上涨但等权继续走弱、油价信用压力再上行。 |
| 观察期限 | 10月26日至未来5个交易日 |
| 反证 | 软件和小盘周线领先是积极证据，但指数周中升幅已回吐、完整成分广度与日内VWAP未取得。 |
| 状态 | 观察中：夜盘初步修复，等待26日常规时段确认 |

## 优先观察软件与网络安全的持续性

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 软件/安全相对强势与微软28日财报；周末消息后开盘承接 |
| 关联标的 | ["IGV", "SKYY"] |
| 确认条件 | IGV回踩20日线当前108.58附近守住、形成更高低点，再突破23日高点；SKYY独立检查自身结构，QQQ/RSP不创新低。财报后先看指引与承接，不只看EPS过线。 |
| 失效条件 | IGV收盘跌回108.58之下并反抽失败；安全新闻没有转化为持续相对强势，或大盘跌破前低。 |
| 观察期限 | 未来1–5个交易日 |
| 反证 | 单日事件涨幅可能过度；没有新增订单/一致预期上修证据，不把主题热度等同盈利。 |
| 状态 | 观察中：夜盘初步修复，等待26日常规时段确认 |

## 能源强势中的回踩机会

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 沙特管线受袭线索与能源供给核验；需防跳空后回落 |
| 关联标的 | ["XLE", "OIH", "XOP"] |
| 确认条件 | 等待回踩后更高低点、相对SPY继续领先；XLE当前20日线65.40仅为结构参考，不能追高后把远处均线当近距离止损。 |
| 失效条件 | 油价同交割合约回落、通航实际改善，同时ETF跌破回踩低点；周末缓和造成跳空则重新估计入场风险。 |
| 观察期限 | 下周1–5个交易日 |
| 反证 | 独立消息未证实管线受损，专门停火预期有所回落；周一高开低走可证伪标题追涨逻辑。 |
| 状态 | 观察中：夜盘初步修复，等待26日常规时段确认 |

## 存储和半导体的财报验证

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | STX27日、SNDK29日财报与微软/Amazon资本开支披露 |
| 关联标的 | ["SMH", "MU", "SNDK", "DRAM"] |
| 确认条件 | SMH收复533.34并回踩守住，随后跨过556.70；公司库存、毛利、订单与资本开支现金回收共同改善。各存储产品线分开判断。 |
| 失效条件 | SMH失守521.47且反抽失败，或公司指引和现金流下修；EPS超固定阈值但股价持续下跌也视为警告。 |
| 观察期限 | 10月26日至财报后两个交易日 |
| 反证 | H100价格、Lam增长不代表NAND/HBM每家公司都改善，单日反弹不足验证。 |
| 状态 | 观察中：夜盘初步修复，等待26日常规时段确认 |

## 跨期比较与上期剧本复核

对照昨晚日报（25日12:08:41UTC）：现货仍同为23日收盘；QQQ/SMH收复回踩剧本未获新的常规交易确认。夜盘期指和WTI初步缓和，证据强度低于现货持续承接。AI新增加融资/需求支撑，现金回报疑问未消除。软件/云、能源的观察优先级保留，能源尤其防回吐。同规则合约变化：2589812：95.5%→93.5%（-2.00个百分点）；4641065：82.5%→79.5%（-3.00个百分点）；3215008：76.5%→76.5%（+0.00个百分点）；3501950：0.4%→0.45%（+0.05个百分点）；2176270：11.5%→11.5%（+0.00个百分点）；4951227：76%→62.5%（-13.50个百分点）；2252540：15.5%→12.5%（-3.00个百分点）；5778671：76%→78%（+2.00个百分点）；691340：9%→9.05%（+0.05个百分点）；4838928：22.5%→22.5%（+0.00个百分点）；5401795：25.5%→30.5%（+5.00个百分点）。不同定义不能相互替代；微软补搜79%与基础快照78%时点不同，正式表统一采用基础快照。

## 可计算的跨期变化

```json
[
  {
    "mode": "daily",
    "baseline": "reports/daily/2026-10-23/20261025T120902.061174Z/evidence.json",
    "baseline_cutoff": "2026-10-25T12:08:41.258578+00:00",
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
    "quote_change_pct": {},
    "macro_change": {
      "DGS2": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-10-22"
      },
      "BAMLH0A0HYM2": {
        "change": 0.0,
        "unit": "percentage_points",
        "observation_date": "2026-10-22"
      },
      "BAMLC0A0CM": {
        "change": 0.0,
        "unit": "percentage_points",
        "observation_date": "2026-10-22"
      },
      "DGS10": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-10-22"
      },
      "DFII10": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-10-22"
      },
      "T10YIE": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-10-23"
      },
      "STLFSI4": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-16"
      },
      "CBOE_VIX": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-23"
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
        "change_pp": -1.9999999999999907
      },
      "4641065": {
        "status": "comparable",
        "change_pp": -2.9999999999999916
      },
      "2176270": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "3501950": {
        "status": "comparable",
        "change_pp": 0.04999999999999996
      },
      "4951227": {
        "status": "comparable",
        "change_pp": -13.5
      },
      "3215008": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "2252540": {
        "status": "comparable",
        "change_pp": -3.0
      },
      "5778671": {
        "status": "comparable",
        "change_pp": 2.0000000000000018
      },
      "691340": {
        "status": "comparable",
        "change_pp": 0.050000000000000044
      },
      "4838928": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "5401795": {
        "status": "comparable",
        "change_pp": 4.999999999999999
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
    "event": "下一次常规开盘；重查周末风险",
    "date": "2026-10-26T09:30:00-04:00",
    "source": "tc:get_trading_calendar"
  },
  {
    "event": "Seagate电话会（财报盘后）",
    "date": "2026-10-27T17:00:00-04:00",
    "source": "https://investors.seagate.com/news/news-details/2026/Seagate-Technology-to-Report-Fiscal-First-Quarter-2027-Financial-Results-on-October-27-2026/default.aspx"
  },
  {
    "event": "FOMC政策决定；27–28日会议",
    "date": "2026-10-28T14:00:00-04:00",
    "source": "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm"
  },
  {
    "event": "微软财报盘后，分钟未核验",
    "date": "2026-10-28 after close America/New_York",
    "source": "https://www.microsoft.com/en-us/investor/faq"
  },
  {
    "event": "Q3 GDP初值与9月个人收支/PCE",
    "date": "2026-10-29T08:30:00-04:00",
    "source": "https://www.bea.gov/news/schedule/full"
  },
  {
    "event": "Sandisk财报电话会",
    "date": "2026-10-29T16:30:00-04:00",
    "source": "https://investor.sandisk.com/news-releases/news-release-details/sandisk-report-first-quarter-fiscal-year-2027-results-october-29"
  },
  {
    "event": "Amazon财报电话会",
    "date": "2026-10-29T17:00:00-04:00",
    "source": "https://www.aboutamazon.com/news/company-news/amazon-earnings-q3-2026-report"
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
    "event": "10月FOMC会议纪要",
    "date": "2026-11-18 America/New_York",
    "source": "https://www.federalreserve.gov/monetarypolicy.htm"
  },
  {
    "event": "Rocket Lab财报电话会，财报盘后；已按冬令时",
    "date": "2026-11-09T17:00:00-05:00",
    "source": "https://investors.rocketlabcorp.com/node/13431/pdf"
  }
]
```

## 新闻事件去重与时间

| 事件 | 摘要 | 发生时间（未知留空） | 各来源发布时间 / 抓取时间 |
| --- | --- | --- | --- |
| spacex-gpu-20261025 | Reuters引述Musk称完成400亿美元GPU债务融资；不等于已审计现金到位或当季营收。 | 缺失 | [{"source": "https://www.marketscreener.com/news/musk-says-spacex-raised-40-billion-in-debt-for-gpus-ce785cdfd18ff22c", "published_at": "2026-10-25T16:02:00-04:00", "retrieved_at": "2026-10-25T23:20:30.049887+00:00"}] |
| aws-demand-20261023 | 23日管理层表述：AWS2027大部分容量已预订，2028有部分预订；并非全部2028售罄。 | 缺失 | [{"source": "https://ca.finance.yahoo.com/news/amazon-cloud-capacity-sold-2027-230625532.html", "published_at": "2026-10-23T19:06:00-04:00", "retrieved_at": "2026-10-25T23:20:30.049887+00:00"}] |
| iran-20261025 | 周日“不打击”表述不保证后续停火；供应损失未独立确认。 | 缺失 | [{"source": "https://apnews.com/article/4779a3deeb1a23f59414164532d5c885", "published_at": null, "retrieved_at": "2026-10-25T23:20:30.049887+00:00"}] |
| h100-20261025 | H10025日2.89美元/GPU小时、七日+6.2%，水平上升但滚动七日增幅缩小。 | 缺失 | [{"source": "https://www.silicondata.com/products/silicon-index/h100", "published_at": null, "retrieved_at": "2026-10-25T23:20:30.049887+00:00"}] |
| fiscal-conditional | 9月官方财政分红承诺仍有政治及立法条件，周末转述不是已实施政策。 | 缺失 | [{"source": "https://www.whitehouse.gov/releases/2026/09/trump-dividend-america-is-winning-and-americans-should-win-with-it/", "published_at": null, "retrieved_at": "2026-10-25T23:20:30.049887+00:00"}] |

## 覆盖范围与数据缺口

```json
[
  "CNN API418、网页不可用，不以其他温度替代。",
  "tc周末报价时戳非交易时点；核心状态以新采23日完整SPY/QQQ日线核验。",
  "Polymarket基础及CPI查询截断；缺完整深度/最后成交时戳，微软、远期AI等低流动性合约降低权重。",
  "完整成分广度、盈利一致预期、期货CME概率缺失；无周末实时VWAP。",
  "当周发行人净申赎和机构交易身份缺失，ICI仅到14日；flows留空而非复制旧行业数据为本周。",
  "连续期货有换月/供应商修订，非同交割结算；能源剧本只部分确认。",
  "信用与美债至22日、GPR至19日、金融压力至16日，无法捕捉周末新消息。",
  "META最新租赁新增及完整净债务桥不足，估值不可用；其余四家复用核验底稿并更新披露检查。",
  "沙特管线实际直接命中、供应损失及通航连续实测未确认；不能据预测报价断言。",
  "Alphabet官方动态日程未取得精确时点，媒体28日线索未列为正式日程；NVDA11/17来自8月实录，临近需再核验。",
  "DRAM长历史不足，不能补造SMA200；不从周末页面刷新推断市场成交。",
  "Gartner为14日长期情景、Apollo为24日观点；没有逐企业AI归因回报数据，不能把转发日期当新发生的减值。",
  "本次tc广泛新闻50条且has_more；25–26日高影响补查17条未截断。实际返回含社交、财联社与FinancialJuice，不等于完整财经覆盖。",
  "Reuters/AP关键线索可从搜索返回文本核验，但落地全文受限；新增融资没有独立合同/审计证明。",
  "夜盘仅供应商延迟报价，非逐笔或交易所实时；Brent报价与历史连续序列可能换月，未拼接收益。",
  "银行失败预测合约大幅变动但FDIC正文403、官方搜索未核验新增事件，留待复查。",
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
  "tc 报价质量 unverified_trade_timestamp: SPY, QQQ, RSP, IWM, SMH, IGV, XLE, XLF, GLD, TLT, NVDA, MSFT, AMZN, GOOGL, META；不作为新成交证据",
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
  "指标缺失/历史不足: prices.^VIX.volume_vs_previous20_ratio, prices.^VIX3M.volume_vs_previous20_ratio, prices.^VVIX.volume_vs_previous20_ratio, prices.^MOVE.volume_vs_previous20_ratio, prices.DRAM.sma200, prices.DRAM.distance_sma200_pct, quotes.SPY.value, quotes.QQQ.value, quotes.RSP.value, quotes.IWM.value, quotes.SMH.value, quotes.IGV.value, quotes.XLE.value, quotes.XLF.value, quotes.GLD.value, quotes.TLT.value, quotes.NVDA.value, quotes.MSFT.value, quotes.AMZN.value, quotes.GOOGL.value, quotes.META.value",
  "外部广度、盈利修正及政策定价未补录；不得用 ETF 涨跌代替成分股广度"
]
```

## 来源、时间与核验记录

```json
[
  {
    "url": "https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/default.aspx",
    "checked_at": "2026-10-25T02:10:53.260578+00:00",
    "note": "沿用前期已核验背景，保留原检查时间；复用今日周报已核验背景；官方21日财报；最新财务披露"
  },
  {
    "url": "https://investor.lamresearch.com/2026-10-21-Lam-Research-Corporation-Reports-Financial-Results-for-the-Quarter-Ended-September-27,-2026",
    "checked_at": "2026-10-25T02:10:53.260578+00:00",
    "note": "沿用前期已核验背景，保留原检查时间；复用今日周报已核验背景；官方21日经营数据"
  },
  {
    "url": "https://nebius.com/newsroom/nebius-secures-3-5-billion-financing-facility-with-citi",
    "checked_at": "2026-10-25T02:10:53.260578+00:00",
    "note": "沿用前期已核验背景，保留原检查时间；复用今日周报已核验背景；官方22日融资"
  },
  {
    "url": "https://www.silicondata.com/products/silicon-index/h100",
    "checked_at": "2026-10-25T23:20:30.049887+00:00",
    "note": "24日租金及七日变化"
  },
  {
    "url": "https://www.internazionale.it/ultime-notizie-reuters/2026/10/24/houthis-say-they-attacked-saudi-oil-sites-strikes-reported-on-yemen-s-aden",
    "checked_at": "2026-10-25T02:10:53.260578+00:00",
    "note": "沿用前期已核验背景，保留原检查时间；复用今日周报已核验背景；24日独立报道，命中与损失未确认"
  },
  {
    "url": "https://www.energy.gov/articles/energy-department-use-defense-production-act-funding-restart-american-refinery-and-expand",
    "checked_at": "2026-10-25T02:10:53.260578+00:00",
    "note": "沿用前期已核验背景，保留原检查时间；复用今日周报已核验背景；22日投资计划"
  },
  {
    "url": "https://home.treasury.gov/news/press-releases/sb0667/",
    "checked_at": "2026-10-25T02:10:53.260578+00:00",
    "note": "沿用前期已核验背景，保留原检查时间；复用今日周报已核验背景；22日拟议投资规则"
  },
  {
    "url": "https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/10/us-flash-pmi-signals-sustained-strong-growth-but-also-further-inflation-uplift-in-october",
    "checked_at": "2026-10-25T02:10:53.260578+00:00",
    "note": "沿用前期已核验背景，保留原检查时间；复用今日周报已核验背景；23日PMI"
  },
  {
    "url": "https://www.ici.org/research/stats/etf_flows",
    "checked_at": "2026-10-25T23:20:30.049887+00:00",
    "note": "最新可见截至14日ETF净发行窗口"
  },
  {
    "url": "https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/",
    "checked_at": "2026-10-25T23:20:30.049887+00:00",
    "note": "发行人页面；缺连续份额/拆分桥"
  },
  {
    "url": "https://www.microsoft.com/en-us/investor/faq",
    "checked_at": "2026-10-25T23:20:30.049887+00:00",
    "note": "28日盘后"
  },
  {
    "url": "https://investors.seagate.com/news/news-details/2026/Seagate-Technology-to-Report-Fiscal-First-Quarter-2027-Financial-Results-on-October-27-2026/default.aspx",
    "checked_at": "2026-10-25T23:20:30.049887+00:00",
    "note": "27日17ET电话会"
  },
  {
    "url": "https://investor.sandisk.com/news-releases/news-release-details/sandisk-report-first-quarter-fiscal-year-2027-results-october-29",
    "checked_at": "2026-10-25T23:20:30.049887+00:00",
    "note": "29日16:30ET电话会"
  },
  {
    "url": "https://www.aboutamazon.com/news/company-news/amazon-earnings-q3-2026-report",
    "checked_at": "2026-10-25T23:20:30.049887+00:00",
    "note": "29日17ET电话会"
  },
  {
    "url": "https://investor.nvidia.com/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf",
    "checked_at": "2026-10-25T02:10:53.260578+00:00",
    "note": "沿用前期已核验背景，保留原检查时间；复用今日周报已核验背景；8月实录中预告11/17，临近需复核"
  },
  {
    "url": "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm",
    "checked_at": "2026-10-25T23:20:30.049887+00:00",
    "note": "27–28日会议"
  },
  {
    "url": "https://www.bea.gov/news/schedule/full",
    "checked_at": "2026-10-25T23:20:30.049887+00:00",
    "note": "GDP/PCE日程"
  },
  {
    "url": "https://www.bls.gov/schedule/2026/11_sched.htm",
    "checked_at": "2026-10-25T02:10:53.260578+00:00",
    "note": "沿用前期已核验背景，保留原检查时间；复用今日周报已核验背景；11/6非农、11/10 CPI，已按冬令时处理"
  },
  {
    "url": "https://www.federalreserve.gov/monetarypolicy.htm",
    "checked_at": "2026-10-25T02:10:53.260578+00:00",
    "note": "沿用前期已核验背景，保留原检查时间；复用今日周报已核验背景；11/18会议纪要"
  },
  {
    "url": "https://abc.xyz/investor/",
    "checked_at": "2026-10-25T02:10:53.260578+00:00",
    "note": "沿用前期已核验背景，保留原检查时间；复用今日周报已核验背景；动态页面未返回精确财报日程；不把媒体日期当官方确认"
  },
  {
    "url": "https://www.cnn.com/markets/fear-and-greed",
    "checked_at": "2026-10-25T23:20:30.049887+00:00",
    "note": "网页不可用，API418"
  },
  {
    "url": "https://www.apollo.com/wealth/insights-news/insights/daily-spark/no-signs-of-ai-payoff-outside-the-tech-sector",
    "checked_at": "2026-10-25T12:08:39.986882+00:00",
    "note": "沿用前期已核验背景，保留原检查时间；24日原始观点，发布时间分钟未知"
  },
  {
    "url": "https://www.gartner.com/en/newsroom/press-releases/2026-10-14-gartner-says-over-us-dollars-three-and-a-half-trillion-of-artificial-intelligence-infrastructure-spending-could-be-exposed-to-impairment-by-the-end-of-2030",
    "checked_at": "2026-10-25T12:08:39.986882+00:00",
    "note": "沿用前期已核验背景，保留原检查时间；14日原始情景预测，勿误作新实际损失"
  },
  {
    "url": "https://apnews.com/article/mideast-news-october-25-2026-4779a3deeb1a23f59414164532d5c885",
    "checked_at": "2026-10-25T12:08:39.986882+00:00",
    "note": "沿用前期已核验背景，保留原检查时间；25日报道；供应影响未确认"
  },
  {
    "url": "https://investors.rocketlabcorp.com/node/13431/pdf",
    "checked_at": "2026-10-25T12:08:39.986882+00:00",
    "note": "沿用前期已核验背景，保留原检查时间；20日官方日程，11/9 17ET电话会"
  },
  {
    "url": "https://www.marketscreener.com/news/musk-says-spacex-raised-40-billion-in-debt-for-gpus-ce785cdfd18ff22c",
    "checked_at": "2026-10-25T23:20:30.049887+00:00",
    "note": "Reuters搜索可见文本；落地页受限，管理层表述未独立审计"
  },
  {
    "url": "https://ca.finance.yahoo.com/news/amazon-cloud-capacity-sold-2027-230625532.html",
    "checked_at": "2026-10-25T23:20:30.049887+00:00",
    "note": "Reuters搜索可见文本，落地页429；原播客发布记录可核验"
  },
  {
    "url": "https://apnews.com/article/4779a3deeb1a23f59414164532d5c885",
    "checked_at": "2026-10-25T23:20:30.049887+00:00",
    "note": "AP搜索可见文本；正文打开失败，限窄事实引用"
  },
  {
    "url": "https://www.whitehouse.gov/releases/2026/09/trump-dividend-america-is-winning-and-americans-should-win-with-it/",
    "checked_at": "2026-10-25T23:20:30.049887+00:00",
    "note": "9月10日官方条件性政策承诺"
  },
  {
    "url": "https://www.fdic.gov/bank-failures/failed-bank-list",
    "checked_at": "2026-10-25T23:20:30.049887+00:00",
    "note": "403；未核验新银行关闭，不据合约涨价断言"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/ES=F",
    "checked_at": "2026-10-25T23:20:30.049887+00:00",
    "note": "23:18UTC取得，报价23:08UTC，供应商previousClose基准"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NQ=F",
    "checked_at": "2026-10-25T23:20:30.049887+00:00",
    "note": "12月合约延迟价，不是QQQ现货"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CL=F",
    "checked_at": "2026-10-25T23:20:30.049887+00:00",
    "note": "12月WTI延迟价；Brent换月不直接拼接"
  }
]
```

## 付费信源建议（未订阅）

```json
[]
```
