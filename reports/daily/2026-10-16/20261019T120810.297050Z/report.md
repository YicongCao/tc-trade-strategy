# 每日交易总结 · 2026-10-16

## 研究结论

10月19日北京时间晚间：美股盘前出现成长修复、原油回落，尚不能确认上周AI去估值结束。更像高利率约束下的局部风险收缩与反弹尝试；既非全面过热，也未获系统性恐慌确认。重点检验反弹能否保持到常规收盘，以及本周META现金流和资本开支披露。

## 时点与口径

| 项目 | 内容 |
| --- | --- |
| 模式 | 每日交易总结 |
| 常规交易窗口 | 2026-10-16 → 2026-10-16（纽约交易日） |
| 截止·纽约 | 2026-10-19T08:08:06.697629-04:00 |
| 截止·北京 | 2026-10-19T20:08:06.697629+08:00 |
| 实际生成时间 | 2026-10-19T12:08:06.930707+00:00 |
| 市场阶段 | 盘前 |
| 下一交易日 | 2026-10-19 |
| 运行重点 | 全市场 |
| 上一版本 | reports/daily/2026-10-16/20261018T120935.196588Z/evidence.json |
| 质量 | partial |
| Daily 北京时间计划时段 | 2026-10-19T20:00:00+08:00 |

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
| prices.SPY.value | 763.25 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_1d_pct | -1.11 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_5d_pct | -1.97 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_20d_pct | 0.20 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_60d_pct | 3.65 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_1d_pp | 0.00 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_5d_pp | 0.00 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_20d_pp | 0.00 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_60d_pp | 0.00 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma20 | 771.18 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma50 | 767.40 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma200 | 721.88 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma20_pct | -1.03 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma50_pct | -0.54 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma200_pct | 5.73 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_sma | 6.89 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_pct | 0.90 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.drawdown_from_63d_high_pct | -2.03 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.volume_vs_previous20_ratio | 1.52 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SPY/history/ |
| prices.QQQ.value | 709.80 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_1d_pct | -2.50 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_5d_pct | -5.52 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_20d_pct | -1.51 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_60d_pct | 2.69 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_1d_pp | -1.39 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_5d_pp | -3.55 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_20d_pp | -1.72 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_60d_pp | -0.97 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma20 | 742.52 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma50 | 726.33 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma200 | 673.66 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma20_pct | -4.41 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma50_pct | -2.28 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma200_pct | 5.36 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_sma | 10.08 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_pct | 1.42 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.drawdown_from_63d_high_pct | -6.56 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.volume_vs_previous20_ratio | 1.90 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.IWM.value | 270.44 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_1d_pct | -1.69 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_5d_pct | -3.05 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_20d_pct | -4.81 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_60d_pct | -7.17 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_1d_pp | -0.58 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_5d_pp | -1.08 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_20d_pp | -5.01 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_60d_pp | -10.82 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma20 | 279.31 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma50 | 288.67 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma200 | 276.54 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma20_pct | -3.18 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma50_pct | -6.31 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma200_pct | -2.21 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_sma | 3.96 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_pct | 1.47 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.drawdown_from_63d_high_pct | -11.13 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.volume_vs_previous20_ratio | 1.30 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IWM/history/ |
| prices.RSP.value | 214.09 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_1d_pct | -0.42 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_5d_pct | 0.49 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_20d_pct | 1.23 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_60d_pct | 1.40 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_1d_pp | 0.68 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_5d_pp | 2.46 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_20d_pp | 1.02 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_60d_pp | -2.25 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma20 | 211.54 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma50 | 215.34 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma200 | 205.35 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma20_pct | 1.21 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma50_pct | -0.58 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma200_pct | 4.26 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_sma | 2.04 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_pct | 0.95 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.drawdown_from_63d_high_pct | -3.54 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.volume_vs_previous20_ratio | 1.25 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/RSP/history/ |
| prices.GLD.value | 382.01 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_1d_pct | -0.18 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_5d_pct | -0.67 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_20d_pct | -4.78 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_60d_pct | 2.82 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_1d_pp | 0.92 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_5d_pp | 1.30 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_20d_pp | -4.98 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_60d_pp | -0.83 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma20 | 384.32 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma50 | 397.18 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma200 | 414.98 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma20_pct | -0.60 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma50_pct | -3.82 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma200_pct | -7.94 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_sma | 5.14 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_pct | 1.35 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.drawdown_from_63d_high_pct | -10.76 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.volume_vs_previous20_ratio | 1.16 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GC=F.value | 4,181.10 | USD_per_troy_ounce | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_1d_pct | 0.26 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_5d_pct | -0.83 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_20d_pct | -5.51 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_60d_pct | 3.23 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_1d_pp | 1.37 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_5d_pp | 1.13 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_20d_pp | -5.71 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_60d_pp | -0.42 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma20 | 4,214.11 | USD_per_troy_ounce | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma50 | 4,374.41 | USD_per_troy_ounce | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma200 | 4,540.70 | USD_per_troy_ounce | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma20_pct | -0.78 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma50_pct | -4.42 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma200_pct | -7.92 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_sma | 72.99 | USD_per_troy_ounce | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_pct | 1.75 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.drawdown_from_63d_high_pct | -11.00 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.volume_vs_previous20_ratio | 1.06 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.CL=F.value | 101.41 | USD_per_barrel | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_1d_pct | 3.51 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_5d_pct | 10.41 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_20d_pct | 1.11 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_60d_pct | 10.00 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_1d_pp | 4.62 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_5d_pp | 12.38 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_20d_pp | 0.90 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_60d_pp | 6.35 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma20 | 92.94 | USD_per_barrel | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma50 | 90.98 | USD_per_barrel | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma200 | 84.19 | USD_per_barrel | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma20_pct | 9.12 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma50_pct | 11.46 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma200_pct | 20.45 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_sma | 4.01 | USD_per_barrel | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_pct | 3.95 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.drawdown_from_63d_high_pct | -4.18 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.volume_vs_previous20_ratio | 0.77 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.BZ=F.value | 109.86 | USD_per_barrel | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_1d_pct | 3.72 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_5d_pct | 4.91 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_20d_pct | 5.77 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_60d_pct | 9.11 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_1d_pp | 4.83 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_5d_pp | 6.88 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_20d_pp | 5.56 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_60d_pp | 5.45 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma20 | 103.69 | USD_per_barrel | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma50 | 98.41 | USD_per_barrel | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma200 | 89.91 | USD_per_barrel | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma20_pct | 5.95 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma50_pct | 11.63 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma200_pct | 22.19 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_sma | 3.96 | USD_per_barrel | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_pct | 3.60 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.drawdown_from_63d_high_pct | 0.00 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.volume_vs_previous20_ratio | 1.32 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.TLT.value | 80.05 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_1d_pct | 0.10 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_5d_pct | 2.65 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_20d_pct | -1.08 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_60d_pct | -2.60 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_1d_pp | 1.21 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_5d_pp | 4.62 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_20d_pp | -1.28 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_60d_pp | -6.26 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma20 | 78.64 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma50 | 80.38 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma200 | 83.40 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma20_pct | 1.80 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma50_pct | -0.41 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma200_pct | -4.02 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_sma | 0.84 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_pct | 1.05 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.drawdown_from_63d_high_pct | -3.84 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.volume_vs_previous20_ratio | 0.84 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/TLT/history/ |
| prices.UUP.value | 28.92 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_1d_pct | -0.28 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_5d_pct | -0.34 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_20d_pct | 1.87 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_60d_pct | 1.26 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_1d_pp | 0.83 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_5d_pp | 1.62 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_20d_pp | 1.66 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_60d_pp | -2.39 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma20 | 28.86 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma50 | 28.40 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma200 | 27.84 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma20_pct | 0.22 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma50_pct | 1.82 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma200_pct | 3.89 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_sma | 0.14 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_pct | 0.48 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.drawdown_from_63d_high_pct | -0.72 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.volume_vs_previous20_ratio | 1.12 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/UUP/history/ |
| prices.HYG.value | 76.86 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_1d_pct | -0.35 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_5d_pct | -0.48 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_20d_pct | -1.69 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_60d_pct | -1.55 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_1d_pp | 0.76 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_5d_pp | 1.49 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_20d_pp | -1.90 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_60d_pp | -5.20 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma20 | 77.27 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma50 | 78.13 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma200 | 77.90 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma20_pct | -0.53 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma50_pct | -1.63 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma200_pct | -1.34 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_sma | 0.34 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_pct | 0.45 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.drawdown_from_63d_high_pct | -2.87 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.volume_vs_previous20_ratio | 1.18 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/HYG/history/ |
| prices.LQD.value | 103.40 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_1d_pct | -0.10 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_5d_pct | 0.97 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_20d_pct | -0.82 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_60d_pct | -1.44 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_1d_pp | 1.01 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_5d_pp | 2.93 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_20d_pp | -1.02 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_60d_pp | -5.09 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma20 | 102.67 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma50 | 104.05 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma200 | 105.99 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma20_pct | 0.71 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma50_pct | -0.63 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma200_pct | -2.44 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_sma | 0.62 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_pct | 0.60 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.drawdown_from_63d_high_pct | -2.41 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.volume_vs_previous20_ratio | 0.80 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/LQD/history/ |
| prices.^VIX.value | 19.99 | index | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_1d_pct | 21.45 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_5d_pct | 34.70 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_20d_pct | 34.98 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_60d_pct | 7.59 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_1d_pp | 22.55 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_5d_pp | 36.67 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_20d_pp | 34.77 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_60d_pp | 4.04 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma20 | 15.73 | index | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma50 | 15.60 | index | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma200 | 18.13 | index | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma20_pct | 27.08 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma50_pct | 28.14 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma200_pct | 10.27 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_sma | 1.48 | index | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_pct | 7.41 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.drawdown_from_63d_high_pct | -3.24 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-16 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX3M.value | 20.50 | index | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_1d_pct | 10.87 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_5d_pct | 15.36 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_20d_pct | 12.39 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_60d_pct | -0.49 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_1d_pp | 11.98 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_5d_pp | 17.33 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_20d_pp | 12.19 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_60d_pp | -4.14 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma20 | 18.22 | index | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma50 | 18.40 | index | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma200 | 20.44 | index | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma20_pct | 12.54 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma50_pct | 11.40 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma200_pct | 0.27 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_sma | 0.84 | index | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_pct | 4.07 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.drawdown_from_63d_high_pct | -4.65 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-16 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VVIX.value | 109.91 | index | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_1d_pct | 18.73 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_5d_pct | 29.49 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_20d_pct | 25.78 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_60d_pct | 7.58 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_1d_pp | 19.84 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_5d_pp | 31.46 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_20d_pp | 25.58 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_60d_pp | 3.92 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma20 | 88.86 | index | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma50 | 89.29 | index | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma200 | 98.37 | index | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma20_pct | 23.69 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma50_pct | 23.10 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma200_pct | 11.73 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_sma | 7.06 | index | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_pct | 6.42 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.drawdown_from_63d_high_pct | 0.00 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-16 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^MOVE.value | 101.10 | index | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_1d_pct | -1.36 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_5d_pct | 0.40 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_20d_pct | 32.64 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_60d_pct | 32.49 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_1d_pp | -0.25 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_5d_pp | 1.78 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_20d_pp | 32.31 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_60d_pp | 30.11 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma20 | 99.75 | index | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma50 | 85.09 | index | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma200 | 75.75 | index | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma20_pct | 1.35 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma50_pct | 18.82 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma200_pct | 33.47 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_sma | 5.46 | index | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_pct | 5.40 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.drawdown_from_63d_high_pct | -11.00 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-16 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.NVDA.value | 214.13 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_1d_pct | -1.43 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_5d_pct | -6.61 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_20d_pct | -3.66 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_60d_pct | 2.69 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_1d_pp | -0.32 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_5d_pp | -4.64 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_20d_pp | -3.87 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_60d_pp | -0.97 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma20 | 228.18 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma50 | 222.96 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma200 | 202.66 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma20_pct | -6.16 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma50_pct | -3.96 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma200_pct | 5.66 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_sma | 5.76 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_pct | 2.69 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.drawdown_from_63d_high_pct | -10.50 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.volume_vs_previous20_ratio | 1.12 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.MSFT.value | 529.05 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_1d_pct | -1.93 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_5d_pct | -1.13 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_20d_pct | 7.14 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_60d_pct | 38.91 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_1d_pp | -0.82 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_5d_pp | 0.84 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_20d_pp | 6.94 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_60d_pp | 35.26 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma20 | 520.22 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma50 | 505.37 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma200 | 434.03 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma20_pct | 1.70 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma50_pct | 4.69 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma200_pct | 21.89 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_sma | 11.74 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_pct | 2.22 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.drawdown_from_63d_high_pct | -2.65 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.volume_vs_previous20_ratio | 1.08 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.AMZN.value | 250.00 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_1d_pct | -1.87 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_5d_pct | -4.74 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_20d_pct | -1.46 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_60d_pct | 6.99 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_1d_pp | -0.76 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_5d_pp | -2.77 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_20d_pp | -1.67 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_60d_pp | 3.34 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma20 | 253.23 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma50 | 257.08 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma200 | 242.73 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma20_pct | -1.27 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma50_pct | -2.75 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma200_pct | 3.00 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_sma | 5.90 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_pct | 2.36 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.drawdown_from_63d_high_pct | -11.98 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.volume_vs_previous20_ratio | 1.11 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.GOOGL.value | 340.59 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_1d_pct | -2.47 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_5d_pct | -3.15 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_20d_pct | -2.56 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_60d_pct | 7.28 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_1d_pp | -1.36 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_5d_pp | -1.18 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_20d_pp | -2.77 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_60d_pp | 3.62 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma20 | 346.41 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma50 | 344.49 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma200 | 340.56 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma20_pct | -1.68 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma50_pct | -1.13 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma200_pct | 0.01 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_sma | 8.96 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_pct | 2.63 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.drawdown_from_63d_high_pct | -9.76 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.volume_vs_previous20_ratio | 1.09 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.META.value | 709.33 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_1d_pct | -3.72 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_5d_pct | -1.30 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_20d_pct | 6.63 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_60d_pct | 17.12 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_1d_pp | -2.61 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_5d_pp | 0.67 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_20d_pp | 6.43 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_60d_pp | 13.47 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma20 | 735.77 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma50 | 654.96 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma200 | 631.07 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma20_pct | -3.59 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma50_pct | 8.30 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma200_pct | 12.40 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_sma | 22.11 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_pct | 3.12 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.drawdown_from_63d_high_pct | -8.78 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.volume_vs_previous20_ratio | 0.93 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/META/history/ |
| prices.CRWV.value | 61.39 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_1d_pct | -11.91 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_5d_pct | -25.21 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_20d_pct | -24.55 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_60d_pct | -24.30 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_1d_pp | -10.80 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_5d_pp | -23.24 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_20d_pp | -24.75 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_60d_pp | -27.96 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma20 | 82.96 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma50 | 87.03 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma200 | 92.44 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma20_pct | -26.00 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma50_pct | -29.46 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma200_pct | -33.59 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_sma | 5.88 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_pct | 9.58 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.drawdown_from_63d_high_pct | -43.01 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.volume_vs_previous20_ratio | 2.49 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.MU.value | 878.84 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_1d_pct | -5.63 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_5d_pct | -14.58 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_20d_pct | -13.47 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_60d_pct | -11.23 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_1d_pp | -4.52 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_5d_pp | -12.61 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_20d_pp | -13.67 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_60d_pp | -14.89 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma20 | 1,032.86 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma50 | 982.97 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma200 | 717.62 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma20_pct | -14.91 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma50_pct | -10.59 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma200_pct | 22.47 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_sma | 47.24 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_pct | 5.38 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.drawdown_from_63d_high_pct | -19.90 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.volume_vs_previous20_ratio | 1.11 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MU/history/ |
| prices.DRAM.value | 46.45 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_1d_pct | -5.84 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_5d_pct | -18.78 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_20d_pct | -22.08 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_60d_pct | -20.33 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_1d_pp | -4.73 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_5d_pp | -16.81 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_20d_pp | -22.28 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_60d_pp | -23.98 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma20 | 58.18 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma50 | 57.12 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma200 | 缺失 | USD_per_share | 2026-10-16 | unavailable | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma20_pct | -20.17 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma50_pct | -18.68 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma200_pct | 缺失 | percent | 2026-10-16 | unavailable | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_sma | 2.39 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_pct | 5.14 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.drawdown_from_63d_high_pct | -26.99 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.volume_vs_previous20_ratio | 1.56 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.VRT.value | 206.42 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_1d_pct | -3.88 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_5d_pct | -14.98 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_20d_pct | -17.23 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_60d_pct | -32.09 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_1d_pp | -2.77 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_5d_pp | -13.01 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_20d_pp | -17.43 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_60d_pp | -35.74 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma20 | 242.20 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma50 | 255.43 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma200 | 268.20 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma20_pct | -14.77 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma50_pct | -19.19 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma200_pct | -23.04 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_sma | 10.57 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_pct | 5.12 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.drawdown_from_63d_high_pct | -32.19 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.volume_vs_previous20_ratio | 1.30 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/VRT/history/ |
| prices.XLK.value | 183.47 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_1d_pct | -3.02 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_5d_pct | -7.70 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_20d_pct | -3.12 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_60d_pct | 2.93 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_1d_pp | -1.92 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_5d_pp | -5.73 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_20d_pp | -3.33 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_60d_pp | -0.72 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma20 | 195.82 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma50 | 189.80 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma200 | 167.18 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma20_pct | -6.31 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma50_pct | -3.34 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma200_pct | 9.74 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_sma | 3.46 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_pct | 1.88 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.drawdown_from_63d_high_pct | -9.17 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.volume_vs_previous20_ratio | 1.96 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLE.value | 68.24 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_1d_pct | 2.52 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_5d_pct | 4.86 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_20d_pct | 6.74 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_60d_pct | 15.60 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_1d_pp | 3.63 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_5d_pp | 6.82 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_20d_pp | 6.54 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_60d_pp | 11.95 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma20 | 63.92 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma50 | 63.31 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma200 | 56.99 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma20_pct | 6.76 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma50_pct | 7.78 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma200_pct | 19.74 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_sma | 1.33 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_pct | 1.95 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.drawdown_from_63d_high_pct | 0.00 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.volume_vs_previous20_ratio | 1.16 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLF.value | 55.52 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_1d_pct | 0.45 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_5d_pct | 1.44 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_20d_pct | -0.26 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_60d_pct | -0.20 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_1d_pp | 1.56 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_5d_pp | 3.41 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_20d_pp | -0.46 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_60d_pp | -3.86 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma20 | 54.45 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma50 | 56.16 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma200 | 53.33 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma20_pct | 1.97 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma50_pct | -1.13 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma200_pct | 4.10 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_sma | 0.70 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_pct | 1.26 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.drawdown_from_63d_high_pct | -4.86 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.volume_vs_previous20_ratio | 1.10 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLI.value | 167.76 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_1d_pct | -0.08 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_5d_pct | -0.88 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_20d_pct | -0.91 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_60d_pct | -7.55 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_1d_pp | 1.03 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_5d_pp | 1.09 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_20d_pp | -1.11 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_60d_pp | -11.20 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma20 | 169.04 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma50 | 173.83 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma200 | 172.18 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma20_pct | -0.76 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma50_pct | -3.49 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma200_pct | -2.57 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_sma | 2.57 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_pct | 1.53 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.drawdown_from_63d_high_pct | -9.81 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.volume_vs_previous20_ratio | 1.25 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLV.value | 176.71 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_1d_pct | -0.27 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_5d_pct | 3.45 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_20d_pct | 5.34 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_60d_pct | 9.88 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_1d_pp | 0.84 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_5d_pp | 5.42 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_20d_pp | 5.14 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_60d_pp | 6.22 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma20 | 170.14 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma50 | 169.61 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma200 | 156.42 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma20_pct | 3.86 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma50_pct | 4.19 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma200_pct | 12.97 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_sma | 2.93 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_pct | 1.66 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.drawdown_from_63d_high_pct | -0.27 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.volume_vs_previous20_ratio | 0.99 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLP.value | 87.62 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_1d_pct | 1.08 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_5d_pct | 5.02 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_20d_pct | 6.52 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_60d_pct | 5.99 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_1d_pp | 2.19 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_5d_pp | 6.99 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_20d_pp | 6.31 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_60d_pp | 2.34 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma20 | 82.84 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma50 | 83.76 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma200 | 83.04 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma20_pct | 5.77 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma50_pct | 4.61 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma200_pct | 5.51 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_sma | 1.17 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_pct | 1.34 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.drawdown_from_63d_high_pct | 0.00 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.volume_vs_previous20_ratio | 2.03 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLY.value | 112.46 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_1d_pct | -0.84 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_5d_pct | -0.35 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_20d_pct | 1.51 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_60d_pct | 3.63 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_1d_pp | 0.27 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_5d_pp | 1.62 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_20d_pp | 1.31 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_60d_pp | -0.02 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma20 | 111.10 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma50 | 113.71 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma200 | 115.46 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma20_pct | 1.22 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma50_pct | -1.10 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma200_pct | -2.60 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_sma | 1.39 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_pct | 1.24 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.drawdown_from_63d_high_pct | -5.97 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.volume_vs_previous20_ratio | 2.52 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLC.value | 110.32 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_1d_pct | -1.89 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_5d_pct | -0.05 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_20d_pct | -0.11 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_60d_pct | 5.03 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_1d_pp | -0.78 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_5d_pp | 1.91 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_20d_pp | -0.32 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_60d_pp | 1.38 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma20 | 111.80 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma50 | 111.68 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma200 | 112.89 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma20_pct | -1.32 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma50_pct | -1.22 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma200_pct | -2.28 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_sma | 1.65 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_pct | 1.50 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.drawdown_from_63d_high_pct | -3.86 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.volume_vs_previous20_ratio | 1.00 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLU.value | 42.21 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_1d_pct | 1.34 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_5d_pct | 1.93 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_20d_pct | 3.46 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_60d_pct | -7.94 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_1d_pp | 2.45 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_5d_pp | 3.90 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_20d_pp | 3.25 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_60d_pp | -11.60 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma20 | 40.58 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma50 | 41.83 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma200 | 43.77 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma20_pct | 4.02 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma50_pct | 0.91 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma200_pct | -3.56 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_sma | 0.67 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_pct | 1.59 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.drawdown_from_63d_high_pct | -8.14 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.volume_vs_previous20_ratio | 0.91 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLRE.value | 42.16 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_1d_pct | 0.40 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_5d_pct | 1.32 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_20d_pct | -0.04 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_60d_pct | -5.42 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_1d_pp | 1.51 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_5d_pp | 3.29 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_20d_pp | -0.24 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_60d_pp | -9.07 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma20 | 41.47 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma50 | 42.89 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma200 | 42.63 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma20_pct | 1.66 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma50_pct | -1.70 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma200_pct | -1.10 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_sma | 0.60 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_pct | 1.42 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.drawdown_from_63d_high_pct | -7.60 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.volume_vs_previous20_ratio | 1.10 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLB.value | 50.92 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_1d_pct | 0.71 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_5d_pct | 3.01 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_20d_pct | 2.33 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_60d_pct | 1.72 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_1d_pp | 1.82 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_5d_pp | 4.98 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_20d_pp | 2.12 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_60d_pp | -1.93 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma20 | 49.59 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma50 | 51.03 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma200 | 50.48 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma20_pct | 2.67 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma50_pct | -0.21 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma200_pct | 0.87 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_sma | 0.75 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_pct | 1.46 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.drawdown_from_63d_high_pct | -4.69 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.volume_vs_previous20_ratio | 1.08 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLB/history/ |
| prices.SMH.value | 539.79 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_1d_pct | -3.41 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_5d_pct | -10.53 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_20d_pct | -5.80 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_60d_pct | -6.96 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_1d_pp | -2.30 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_5d_pp | -8.56 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_20d_pp | -6.00 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_60d_pp | -10.61 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma20 | 601.04 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma50 | 579.03 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma200 | 511.35 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma20_pct | -10.19 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma50_pct | -6.78 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma200_pct | 5.56 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_sma | 15.64 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_pct | 2.90 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.drawdown_from_63d_high_pct | -14.85 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.volume_vs_previous20_ratio | 2.60 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SMH/history/ |
| prices.IGV.value | 104.34 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_1d_pct | -4.80 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_5d_pct | -7.39 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_20d_pct | -0.01 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_60d_pct | 19.79 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_1d_pp | -3.69 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_5d_pp | -5.43 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_20d_pp | -0.21 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_60d_pp | 16.14 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma20 | 108.29 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma50 | 105.90 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma200 | 93.72 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma20_pct | -3.65 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma50_pct | -1.47 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma200_pct | 11.33 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_sma | 2.78 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_pct | 2.67 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.drawdown_from_63d_high_pct | -7.39 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.volume_vs_previous20_ratio | 2.19 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IGV/history/ |
| prices.XOP.value | 200.38 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_1d_pct | 2.82 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_5d_pct | 4.63 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_20d_pct | 5.54 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_60d_pct | 14.53 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_1d_pp | 3.92 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_5d_pp | 6.59 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_20d_pp | 5.34 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_60d_pp | 10.87 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma20 | 187.91 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma50 | 187.16 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma200 | 165.84 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma20_pct | 6.63 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma50_pct | 7.06 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma200_pct | 20.82 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_sma | 4.65 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_pct | 2.32 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.drawdown_from_63d_high_pct | 0.00 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.volume_vs_previous20_ratio | 0.82 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XOP/history/ |
| prices.OIH.value | 382.18 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_1d_pct | 1.48 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_5d_pct | -1.66 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_20d_pct | -4.15 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_60d_pct | -0.20 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_1d_pp | 2.59 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_5d_pp | 0.30 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_20d_pp | -4.35 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_60d_pp | -3.86 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma20 | 387.53 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma50 | 404.44 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma200 | 393.26 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma20_pct | -1.38 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma50_pct | -5.50 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma200_pct | -2.82 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_sma | 9.60 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_pct | 2.51 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.drawdown_from_63d_high_pct | -12.46 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.volume_vs_previous20_ratio | 0.86 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/OIH/history/ |
| prices.ITA.value | 209.07 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_1d_pct | 1.04 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_5d_pct | 1.17 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_20d_pct | -2.23 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_60d_pct | -12.14 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_1d_pp | 2.15 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_5d_pp | 3.14 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_20d_pp | -2.44 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_60d_pp | -15.79 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma20 | 208.64 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma50 | 223.05 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma200 | 229.67 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma20_pct | 0.21 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma50_pct | -6.27 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma200_pct | -8.97 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_sma | 3.34 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_pct | 1.60 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.drawdown_from_63d_high_pct | -17.34 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.volume_vs_previous20_ratio | 2.05 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ARKX.value | 29.88 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_1d_pct | -2.15 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_5d_pct | -7.22 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_20d_pct | -6.99 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_60d_pct | -3.44 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_1d_pp | -1.04 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_5d_pp | -5.25 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_20d_pp | -7.19 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_60d_pp | -7.10 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma20 | 32.09 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma50 | 32.56 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma200 | 32.59 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma20_pct | -6.90 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma50_pct | -8.24 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma200_pct | -8.33 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_sma | 0.68 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_pct | 2.26 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.drawdown_from_63d_high_pct | -14.30 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.volume_vs_previous20_ratio | 1.05 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.KRE.value | 69.81 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_1d_pct | 0.09 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_5d_pct | 1.16 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_20d_pct | -3.49 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_60d_pct | -6.58 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_1d_pp | 1.19 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_5d_pp | 3.13 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_20d_pp | -3.70 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_60d_pp | -10.23 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma20 | 70.06 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma50 | 72.68 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma200 | 70.03 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma20_pct | -0.36 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma50_pct | -3.95 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma200_pct | -0.31 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_sma | 1.32 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_pct | 1.89 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.drawdown_from_63d_high_pct | -9.91 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.volume_vs_previous20_ratio | 0.96 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/KRE/history/ |
| prices.SKYY.value | 158.51 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_1d_pct | -4.87 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_5d_pct | -9.37 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_20d_pct | -2.17 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_60d_pct | 22.19 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_1d_pp | -3.76 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_5d_pp | -7.40 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_20d_pp | -2.37 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_60d_pp | 18.54 | pp | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma20 | 167.44 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma50 | 163.91 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma200 | 134.65 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma20_pct | -5.34 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma50_pct | -3.29 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma200_pct | 17.72 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_sma | 4.35 | USD_per_share | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_pct | 2.74 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.drawdown_from_63d_high_pct | -9.37 | percent | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.volume_vs_previous20_ratio | 1.03 | ratio | 2026-10-16 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SKYY/history/ |
| macro.DGS2.value | 4.77 | percent | 2026-10-15 | lagged | source_series_v1:DGS2 | https://fred.stlouisfed.org/series/DGS2 |
| macro.BAMLH0A0HYM2.value | 3.23 | percentage_points | 2026-10-15 | lagged | source_series_v1:BAMLH0A0HYM2 | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| macro.BAMLC0A0CM.value | 0.84 | percentage_points | 2026-10-15 | lagged | source_series_v1:BAMLC0A0CM | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| macro.DGS10.value | 5.10 | percent | 2026-10-15 | lagged | source_series_v1:DGS10 | https://fred.stlouisfed.org/series/DGS10 |
| macro.DFII10.value | 2.78 | percent | 2026-10-15 | lagged | source_series_v1:DFII10 | https://fred.stlouisfed.org/series/DFII10 |
| macro.T10YIE.value | 2.35 | percent | 2026-10-16 | ok | source_series_v1:T10YIE | https://fred.stlouisfed.org/series/T10YIE |
| macro.STLFSI4.value | -0.72 | index | 2026-10-09 | lagged | source_series_v1:STLFSI4 | https://fred.stlouisfed.org/series/STLFSI4 |
| macro.CBOE_VIX.value | 19.99 | index | 2026-10-16 | ok | source_series_v1:CBOE_VIX | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| macro.GPRD.value | 342.40 | index | 2026-10-13 | lagged | source_series_v1:GPRD | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_ACT.value | 444.55 | index | 2026-10-13 | lagged | source_series_v1:GPRD_ACT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_THREAT.value | 317.83 | index | 2026-10-13 | lagged | source_series_v1:GPRD_THREAT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA7.value | 186.58 | index | 2026-10-13 | lagged | source_series_v1:GPRD_MA7 | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA30.value | 177.90 | index | 2026-10-13 | lagged | source_series_v1:GPRD_MA30 | https://www.matteoiacoviello.com/gpr.htm |
| quotes.IWM.value | 270.44 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.RSP.value | 214.09 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.XLK.value | 183.47 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.XLE.value | 68.24 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.XLF.value | 55.52 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.XLI.value | 167.76 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.XLV.value | 176.71 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.XLP.value | 87.62 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.XLY.value | 112.46 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.XLC.value | 110.32 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.XLU.value | 42.21 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.XLRE.value | 42.16 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.XLB.value | 50.92 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.SMH.value | 539.79 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.IGV.value | 104.34 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.XOP.value | 200.38 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.OIH.value | 382.18 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.ITA.value | 209.07 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.ARKX.value | 29.88 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.KRE.value | 69.81 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.SKYY.value | 158.51 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.GLD.value | 382.01 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.TLT.value | 80.05 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.UUP.value | 28.92 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.HYG.value | 76.86 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.LQD.value | 103.40 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.NVDA.value | 214.13 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.MSFT.value | 529.05 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.AMZN.value | 250 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.GOOGL.value | 340.59 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.META.value | 709.33 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.CRWV.value | 61.39 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.MU.value | 878.84 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.DRAM.value | 46.45 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.VRT.value | 206.42 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.SPY.value | 766.79 | USD_per_share | 2026-10-19T12:05:43+00:00 | ok | tc_last_v1 | https://finance.yahoo.com/quote/SPY/ |
| quotes.QQQ.value | 718.57 | USD_per_share | 2026-10-19T12:05:49+00:00 | ok | tc_last_v1 | https://finance.yahoo.com/quote/QQQ/ |
| quotes.CL=F.value | 98.15 | USD_per_share | 2026-10-19T11:55:50+00:00 | ok | tc_last_v1 | https://finance.yahoo.com/quote/CL=F/ |
| quotes.BZ=F.value | 108.43 | USD_per_share | 2026-10-19T11:55:29+00:00 | ok | tc_last_v1 | https://finance.yahoo.com/quote/BZ=F/ |
| quotes.GC=F.value | 4,186.80 | USD_per_share | 2026-10-19T11:55:51+00:00 | ok | tc_last_v1 | https://finance.yahoo.com/quote/GC=F/ |
| quotes.^VIX.value | 18.83 | USD_per_share | 2026-10-19T11:50:46+00:00 | ok | tc_last_v1 | https://finance.yahoo.com/quote/^VIX/ |

## 指标历史比较（不同日期观测，非连续交易日）

```json
[
  {
    "id": "prices.SPY.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SPY.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SPY.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SPY.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SPY.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SPY.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SPY.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SPY.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SPY.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SPY.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SPY.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SPY.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SPY.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SPY.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SPY.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SPY.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SPY.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SPY.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SPY.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.QQQ.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.QQQ.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.QQQ.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.QQQ.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.QQQ.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.QQQ.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.QQQ.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.QQQ.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.QQQ.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.QQQ.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.QQQ.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.QQQ.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.QQQ.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.QQQ.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.QQQ.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.QQQ.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.QQQ.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.QQQ.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.QQQ.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IWM.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IWM.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IWM.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IWM.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IWM.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IWM.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IWM.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IWM.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IWM.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IWM.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IWM.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IWM.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IWM.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IWM.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IWM.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IWM.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IWM.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IWM.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IWM.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.RSP.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.RSP.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.RSP.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.RSP.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.RSP.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.RSP.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.RSP.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.RSP.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.RSP.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.RSP.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.RSP.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.RSP.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.RSP.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.RSP.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.RSP.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.RSP.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.RSP.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.RSP.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.RSP.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GLD.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GLD.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GLD.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GLD.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GLD.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GLD.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GLD.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GLD.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GLD.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GLD.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GLD.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GLD.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GLD.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GLD.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GLD.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GLD.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GLD.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GLD.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GLD.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GC=F.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GC=F.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GC=F.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GC=F.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GC=F.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GC=F.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GC=F.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GC=F.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GC=F.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GC=F.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GC=F.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GC=F.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GC=F.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GC=F.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GC=F.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GC=F.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GC=F.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GC=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GC=F.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CL=F.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CL=F.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CL=F.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CL=F.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CL=F.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CL=F.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CL=F.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CL=F.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CL=F.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CL=F.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CL=F.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CL=F.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CL=F.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CL=F.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CL=F.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CL=F.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CL=F.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CL=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CL=F.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.BZ=F.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.BZ=F.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.BZ=F.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.BZ=F.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.BZ=F.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.BZ=F.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.BZ=F.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.BZ=F.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.BZ=F.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.BZ=F.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.BZ=F.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.BZ=F.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.BZ=F.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.BZ=F.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.BZ=F.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.BZ=F.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.BZ=F.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.BZ=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.BZ=F.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.TLT.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.TLT.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.TLT.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.TLT.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.TLT.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.TLT.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.TLT.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.TLT.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.TLT.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.TLT.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.TLT.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.TLT.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.TLT.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.TLT.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.TLT.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.TLT.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.TLT.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.TLT.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.TLT.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.UUP.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.UUP.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.UUP.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.UUP.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.UUP.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.UUP.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.UUP.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.UUP.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.UUP.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.UUP.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.UUP.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.UUP.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.UUP.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.UUP.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.UUP.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.UUP.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.UUP.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.UUP.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.UUP.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.HYG.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.HYG.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.HYG.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.HYG.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.HYG.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.HYG.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.HYG.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.HYG.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.HYG.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.HYG.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.HYG.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.HYG.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.HYG.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.HYG.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.HYG.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.HYG.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.HYG.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.HYG.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.HYG.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.LQD.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.LQD.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.LQD.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.LQD.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.LQD.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.LQD.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.LQD.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.LQD.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.LQD.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.LQD.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.LQD.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.LQD.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.LQD.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.LQD.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.LQD.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.LQD.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.LQD.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.LQD.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.LQD.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX3M.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX3M.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX3M.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX3M.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX3M.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX3M.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX3M.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX3M.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX3M.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX3M.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX3M.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX3M.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX3M.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX3M.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX3M.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX3M.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX3M.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VIX3M.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VVIX.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VVIX.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VVIX.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VVIX.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VVIX.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VVIX.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VVIX.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VVIX.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VVIX.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VVIX.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VVIX.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VVIX.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VVIX.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VVIX.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VVIX.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VVIX.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VVIX.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^VVIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^MOVE.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^MOVE.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^MOVE.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^MOVE.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^MOVE.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^MOVE.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^MOVE.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^MOVE.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^MOVE.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^MOVE.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^MOVE.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^MOVE.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^MOVE.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^MOVE.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^MOVE.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^MOVE.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^MOVE.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.^MOVE.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.NVDA.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.NVDA.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.NVDA.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.NVDA.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.NVDA.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.NVDA.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.NVDA.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.NVDA.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.NVDA.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.NVDA.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.NVDA.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.NVDA.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.NVDA.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.NVDA.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.NVDA.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.NVDA.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.NVDA.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.NVDA.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.NVDA.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MSFT.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MSFT.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MSFT.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MSFT.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MSFT.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MSFT.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MSFT.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MSFT.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MSFT.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MSFT.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MSFT.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MSFT.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MSFT.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MSFT.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MSFT.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MSFT.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MSFT.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MSFT.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MSFT.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.AMZN.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.AMZN.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.AMZN.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.AMZN.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.AMZN.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.AMZN.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.AMZN.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.AMZN.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.AMZN.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.AMZN.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.AMZN.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.AMZN.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.AMZN.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.AMZN.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.AMZN.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.AMZN.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.AMZN.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.AMZN.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.AMZN.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GOOGL.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GOOGL.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GOOGL.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GOOGL.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GOOGL.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GOOGL.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GOOGL.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GOOGL.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GOOGL.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GOOGL.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GOOGL.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GOOGL.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GOOGL.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GOOGL.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GOOGL.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GOOGL.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GOOGL.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GOOGL.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.GOOGL.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.META.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.META.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.META.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.META.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.META.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.META.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.META.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.META.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.META.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.META.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.META.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.META.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.META.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.META.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.META.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.META.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.META.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.META.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.META.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CRWV.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CRWV.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CRWV.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CRWV.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CRWV.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CRWV.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CRWV.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CRWV.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CRWV.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CRWV.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CRWV.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CRWV.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CRWV.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CRWV.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CRWV.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CRWV.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CRWV.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CRWV.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.CRWV.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MU.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MU.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MU.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MU.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MU.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MU.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MU.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MU.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MU.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MU.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MU.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MU.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MU.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MU.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MU.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MU.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MU.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MU.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.MU.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.DRAM.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.DRAM.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.DRAM.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.DRAM.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.DRAM.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.DRAM.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.DRAM.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.DRAM.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.DRAM.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.DRAM.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.DRAM.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.DRAM.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.DRAM.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.DRAM.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.DRAM.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.DRAM.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.DRAM.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.VRT.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.VRT.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.VRT.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.VRT.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.VRT.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.VRT.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.VRT.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.VRT.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.VRT.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.VRT.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.VRT.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.VRT.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.VRT.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.VRT.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.VRT.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.VRT.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.VRT.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.VRT.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.VRT.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLK.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLK.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLK.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLK.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLK.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLK.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLK.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLK.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLK.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLK.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLK.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLK.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLK.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLK.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLK.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLK.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLK.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLK.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLK.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLE.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLE.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLE.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLE.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLE.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLE.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLE.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLE.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLE.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLE.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLE.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLE.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLE.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLE.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLE.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLE.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLE.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLE.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLE.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLF.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLF.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLF.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLF.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLF.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLF.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLF.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLF.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLF.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLF.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLF.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLF.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLF.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLF.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLF.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLF.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLF.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLF.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLF.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLI.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLI.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLI.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLI.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLI.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLI.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLI.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLI.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLI.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLI.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLI.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLI.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLI.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLI.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLI.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLI.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLI.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLI.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLI.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLV.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLV.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLV.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLV.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLV.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLV.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLV.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLV.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLV.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLV.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLV.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLV.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLV.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLV.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLV.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLV.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLV.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLV.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLV.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLP.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLP.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLP.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLP.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLP.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLP.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLP.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLP.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLP.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLP.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLP.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLP.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLP.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLP.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLP.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLP.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLP.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLP.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLP.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLY.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLY.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLY.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLY.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLY.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLY.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLY.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLY.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLY.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLY.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLY.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLY.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLY.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLY.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLY.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLY.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLY.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLY.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLY.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLC.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLC.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLC.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLC.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLC.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLC.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLC.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLC.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLC.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLC.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLC.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLC.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLC.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLC.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLC.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLC.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLC.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLC.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLC.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLU.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLU.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLU.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLU.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLU.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLU.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLU.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLU.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLU.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLU.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLU.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLU.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLU.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLU.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLU.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLU.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLU.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLU.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLU.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLRE.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLRE.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLRE.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLRE.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLRE.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLRE.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLRE.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLRE.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLRE.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLRE.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLRE.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLRE.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLRE.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLRE.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLRE.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLRE.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLRE.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLRE.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLB.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLB.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLB.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLB.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLB.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLB.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLB.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLB.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLB.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLB.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLB.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLB.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLB.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLB.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLB.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLB.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLB.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLB.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XLB.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SMH.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SMH.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SMH.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SMH.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SMH.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SMH.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SMH.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SMH.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SMH.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SMH.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SMH.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SMH.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SMH.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SMH.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SMH.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SMH.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SMH.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SMH.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SMH.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IGV.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IGV.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IGV.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IGV.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IGV.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IGV.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IGV.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IGV.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IGV.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IGV.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IGV.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IGV.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IGV.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IGV.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IGV.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IGV.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IGV.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IGV.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.IGV.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XOP.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XOP.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XOP.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XOP.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XOP.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XOP.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XOP.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XOP.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XOP.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XOP.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XOP.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XOP.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XOP.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XOP.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XOP.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XOP.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XOP.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XOP.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.XOP.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.OIH.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.OIH.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.OIH.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.OIH.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.OIH.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.OIH.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.OIH.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.OIH.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.OIH.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.OIH.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.OIH.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.OIH.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.OIH.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.OIH.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.OIH.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.OIH.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.OIH.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.OIH.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.OIH.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ITA.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ITA.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ITA.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ITA.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ITA.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ITA.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ITA.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ITA.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ITA.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ITA.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ITA.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ITA.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ITA.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ITA.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ITA.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ITA.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ITA.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ITA.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ITA.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ARKX.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ARKX.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ARKX.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ARKX.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ARKX.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ARKX.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ARKX.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ARKX.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ARKX.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ARKX.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ARKX.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ARKX.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ARKX.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ARKX.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ARKX.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ARKX.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ARKX.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ARKX.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.ARKX.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.KRE.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.KRE.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.KRE.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.KRE.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.KRE.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.KRE.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.KRE.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.KRE.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.KRE.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.KRE.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.KRE.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.KRE.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.KRE.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.KRE.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.KRE.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.KRE.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.KRE.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.KRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.KRE.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SKYY.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SKYY.return_1d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SKYY.return_5d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SKYY.return_20d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SKYY.return_60d_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SKYY.relative_spy_1d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SKYY.relative_spy_5d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SKYY.relative_spy_20d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SKYY.relative_spy_60d_pp",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SKYY.sma20",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SKYY.sma50",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SKYY.sma200",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SKYY.distance_sma20_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SKYY.distance_sma50_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SKYY.distance_sma200_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SKYY.atr14_sma",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SKYY.atr14_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SKYY.drawdown_from_63d_high_pct",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "prices.SKYY.volume_vs_previous20_ratio",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "macro.DGS2.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "macro.BAMLH0A0HYM2.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "macro.BAMLC0A0CM.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "macro.DGS10.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "macro.DFII10.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "macro.T10YIE.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "macro.STLFSI4.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "macro.CBOE_VIX.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "macro.GPRD.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "macro.GPRD_ACT.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "macro.GPRD_THREAT.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "macro.GPRD_MA7.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "macro.GPRD_MA30.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  }
]
```

## 判断依据 · 恐慌还是过热？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 恐慌还是过热？ |
| 事实指标引用 | ["macro.CBOE_VIX.value", "macro.BAMLH0A0HYM2.value", "macro.DFII10.value"] |
| 推断与解释 | 推断：通胀/实际利率压力叠加局部风险收缩，尚未确认系统性恐慌。 |
| 反证与缺口 | VIX不足20、HY323bp及金融压力负值；宏观有发布滞后。 |
| 确认条件 | 研究假设：VIX持续超过25且HY超过400bp，股债广度同步恶化 |
| 失效条件 | 信用回落及波动缓和 |
| 观察期限 | 下一交易日至未来两周；每日复核 |
| 条件式指导 | 等待多类证据，不因单一情绪指标追空或抄底。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相对昨晚：出现盘前成长反弹和油价缓和，尚无今日完整收盘；新增单日申赎揭示分化。 |

## 判断依据 · 趋势支持提高方向风险吗？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 趋势支持提高方向风险吗？ |
| 事实指标引用 | ["prices.SPY.distance_sma20_pct", "prices.SPY.distance_sma200_pct", "prices.QQQ.return_5d_pct"] |
| 推断与解释 | 短期趋势承压但SPY仍高于200日线；短期调整与长期趋势不同。 |
| 反证与缺口 | 缺真实成分股广度；盘前虽有反弹但尚未完成常规交易日。 |
| 确认条件 | SPY/QQQ收复20日线并至少两次收盘保持，广度配合 |
| 失效条件 | 跌破近期低点同时信用恶化 |
| 观察期限 | 下一交易日至未来两周；每日复核 |
| 条件式指导 | 恢复后分步验证；跳空不当作已确认反转。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相对昨晚：出现盘前成长反弹和油价缓和，尚无今日完整收盘；新增单日申赎揭示分化。 |

## 判断依据 · 哪些板块相对占优？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 哪些板块相对占优？ |
| 事实指标引用 | ["prices.SMH.relative_spy_5d_pp", "prices.XLE.relative_spy_5d_pp", "prices.RSP.relative_spy_5d_pp"] |
| 推断与解释 | 上周价格偏防御/能源，但14–15日杠杆成长ETF申购明显；资金方向异质，不能用单一板块涨跌识别主力。 |
| 反证与缺口 | 旧资金流窗口XLK仍申购；油服和航天分化。 |
| 确认条件 | 相对强弱连续延续且盈利/供应证据支持 |
| 失效条件 | 原油供给缓和、能源相对强势消退 |
| 观察期限 | 下一交易日至未来两周；每日复核 |
| 条件式指导 | 分开观察能源、防御与成长修复，不追逐单日涨幅。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相对昨晚：出现盘前成长反弹和油价缓和，尚无今日完整收盘；新增单日申赎揭示分化。 |

## 判断依据 · AI催化剂如何转成交易确认？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | AI催化剂如何转成交易确认？ |
| 事实指标引用 | ["prices.SMH.atr14_pct", "prices.NVDA.return_5d_pct", "macro.BAMLH0A0HYM2.value"] |
| 推断与解释 | 等待财报现金流、融资及价格共振；ATR仅用于理解波动尺度。 |
| 反证与缺口 | SEC尚无新季报；META本周披露；估值模型终值敏感，合约定义很窄。 |
| 确认条件 | 官方订单/现金流改善且SMH相对SPY止跌 |
| 失效条件 | 融资或指引恶化并跌破近期结构低点 |
| 观察期限 | 下一交易日至未来两周；每日复核 |
| 条件式指导 | 先把假说列为观察；不以估值差额直接给买卖方向。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相对昨晚：出现盘前成长反弹和油价缓和，尚无今日完整收盘；新增单日申赎揭示分化。 |

## AI资本开支的融资与回报率重估 · 减弱

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 盘前AI相关股票反弹线索与油价下降；META官方确认10月21日盘后披露。去估值主题边际缓和、未失效。 |
| 事实：市场反应 | QQQ12:05:49Z报718.57，高于周五709.80；SMH上周跌幅仍为历史背景。 |
| 推断：解释 | 短线修复可能来自油价/折现率缓和和超跌交易，因果关系尚未识别。 |
| 受益篮子 | ["待确认现金流兑现的大型平台，相对观察MSFT/META"] |
| 受损篮子 | ["高融资依赖算力商", "高估值半导体/光通信/云基础设施篮子"] |
| 反证 | H100租金2.83、周升7.6%；但AI尾部合约价格上升，现金流与融资压力尚未由新财报澄清。 |
| 下一催化剂 | META10月21日盘后及纽约16:30电话会；常规收盘后的相对强弱。 |
| 证据 | ["https://investor.tsmc.com/english/quarterly-results/2026/q3", "https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm", "https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm", "https://finance.yahoo.com/quote/QQQ/", "https://www.silicondata.com/products/silicon-index/h100", "https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-to-Announce-Third-Quarter-2026-Results/default.aspx"] |

## 能源供给风险与通胀尾部 · 减弱

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 俄制裁豁免背景下原油回落；未确认霍尔木兹实际通行恢复。 |
| 事实：市场反应 | Yahoo11:55Z附近WTI98.15、Brent108.43；上周能源强势不能直接外推今天。 |
| 推断：解释 | 供给风险溢价边际缓和可支持成长，但油价仍高且海峡短期通航合约低价。 |
| 受益篮子 | ["XLE", "XOP"] |
| 受损篮子 | ["航空运输成本", "能源密集型制造利润率；需公司核验"] |
| 反证 | 航运仍可能受袭；期限合约和现货供需不同，单次油价下跌不代表战争影响结束。 |
| 下一催化剂 | 实际船舶通行、供应恢复、常规交易时段XLE相对SPY表现。 |
| 证据 | ["https://www.whitehouse.gov/presidential-actions/2026/10/implementing-the-lindsey-o-graham-sanctioning-russia-and-iran-act-of-2026/", "https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31", "https://apnews.com/article/d8b9749fee99a11dd77513d326b824b6", "https://www.cls.cn/detail/2507683"] |

## 防御板块与等权相对占优 · 待核验

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 价格广度出现成长与防御分化；没有当前全市场资金身份数据。 |
| 事实：市场反应 | 5日XLP +5.02%、XLV +3.45%、RSP +0.49%，QQQ -5.52%；ITA +1.17%而ARKX -7.22%。 |
| 推断：解释 | 更像资金偏好变化的价格证据；金融、工业并未整体成为一致强势主线。 |
| 受益篮子 | ["必需消费", "医疗", "相对观察公用事业"] |
| 受损篮子 | ["高估值成长", "部分航天主题"] |
| 反证 | 10月14–15日数据同时存在成长/杠杆ETF申购与SMH赎回；并非单向防御资金迁移。 |
| 下一催化剂 | 10月19日常规收盘及后续申赎更新；当前真实成分股广度仍缺失。 |
| 证据 | ["https://www.etf.com/sections/weekly-etf-flows/etf-inflows-top-41b-investors-pile-brazil-long-bonds", "https://www.ssga.com/us/en/individual/etfs/state-street-technology-select-sector-spdr-etf-xlk", "https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/overview/"] |

## tc 报价（供应商时戳不等于成交时戳）

| 标的 | 价格 USD | 变化% | 观测时间 | 供应商时间 | 抓取时间 | 质量 |
| --- | --- | --- | --- | --- | --- | --- |
| IWM | 270.44 | -1.69 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| RSP | 214.09 | -0.42 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| XLK | 183.47 | -3.02 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| XLE | 68.24 | 2.52 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| XLF | 55.52 | 0.45 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| XLI | 167.76 | -0.08 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| XLV | 176.71 | -0.27 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| XLP | 87.62 | 1.08 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| XLY | 112.46 | -0.84 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| XLC | 110.32 | -1.89 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| XLU | 42.21 | 1.34 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| XLRE | 42.16 | 0.40 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| XLB | 50.92 | 0.71 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| SMH | 539.79 | -3.41 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| IGV | 104.34 | -4.80 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| XOP | 200.38 | 2.82 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| OIH | 382.18 | 1.48 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| ITA | 209.07 | 1.04 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| ARKX | 29.88 | -2.13 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| KRE | 69.81 | 0.09 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| SKYY | 158.51 | -4.87 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| GLD | 382.01 | -0.18 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| TLT | 80.05 | 0.10 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| UUP | 28.92 | -0.28 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| HYG | 76.86 | -0.35 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| LQD | 103.40 | -0.10 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| NVDA | 214.13 | -1.43 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| MSFT | 529.05 | -1.93 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| AMZN | 250 | -1.87 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| GOOGL | 340.59 | -2.47 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| META | 709.33 | -3.72 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| CRWV | 61.39 | -11.91 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| MU | 878.84 | -5.63 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| DRAM | 46.45 | -5.84 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| VRT | 206.42 | -3.88 | 缺失 | 缺失 | 2026-10-19T12:05:55.495973+00:00 | unverified_trade_timestamp |
| SPY | 766.79 | -0.65 | 2026-10-19T12:05:43+00:00 | 2026-10-19T12:05:43+00:00 | 2026-10-19T12:05:55.495973+00:00 | ok |
| QQQ | 718.57 | -1.30 | 2026-10-19T12:05:49+00:00 | 2026-10-19T12:05:49+00:00 | 2026-10-19T12:05:55.495973+00:00 | ok |
| CL=F | 98.15 | -0.88 | 2026-10-19T11:55:50+00:00 | 2026-10-19T11:55:50+00:00 | 2026-10-19T12:05:55.495973+00:00 | ok |
| BZ=F | 108.43 | -1.30 | 2026-10-19T11:55:29+00:00 | 2026-10-19T11:55:29+00:00 | 2026-10-19T12:05:55.495973+00:00 | ok |
| GC=F | 4,186.80 | 0.14 | 2026-10-19T11:55:51+00:00 | 2026-10-19T11:55:51+00:00 | 2026-10-19T12:05:55.495973+00:00 | ok |
| ^VIX | 18.83 | -5.80 | 2026-10-19T11:50:46+00:00 | 2026-10-19T11:50:46+00:00 | 2026-10-19T12:05:55.495973+00:00 | ok |

## 核心行情与风险代理

| 标的 | 价格/指数 | 单位 | 观测日 | 1日% | 5日% | 20日% | 质量 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 763.25 | USD_per_share | 2026-10-16 | -1.11 | -1.97 | 0.20 | ok |
| QQQ | 709.80 | USD_per_share | 2026-10-16 | -2.50 | -5.52 | -1.51 | ok |
| IWM | 270.44 | USD_per_share | 2026-10-16 | -1.69 | -3.05 | -4.81 | ok |
| RSP | 214.09 | USD_per_share | 2026-10-16 | -0.42 | 0.49 | 1.23 | ok |
| GLD | 382.01 | USD_per_share | 2026-10-16 | -0.18 | -0.67 | -4.78 | ok |
| GC=F | 4,181.10 | USD_per_troy_ounce | 2026-10-16 | 0.26 | -0.83 | -5.51 | ok |
| CL=F | 101.41 | USD_per_barrel | 2026-10-16 | 3.51 | 10.41 | 1.11 | ok |
| BZ=F | 109.86 | USD_per_barrel | 2026-10-16 | 3.72 | 4.91 | 5.77 | ok |
| TLT | 80.05 | USD_per_share | 2026-10-16 | 0.10 | 2.65 | -1.08 | ok |
| UUP | 28.92 | USD_per_share | 2026-10-16 | -0.28 | -0.34 | 1.87 | ok |
| HYG | 76.86 | USD_per_share | 2026-10-16 | -0.35 | -0.48 | -1.69 | ok |
| LQD | 103.40 | USD_per_share | 2026-10-16 | -0.10 | 0.97 | -0.82 | ok |
| ^VIX | 19.99 | index | 2026-10-16 | 21.45 | 34.70 | 34.98 | ok |
| ^VIX3M | 20.50 | index | 2026-10-16 | 10.87 | 15.36 | 12.39 | ok |
| ^VVIX | 109.91 | index | 2026-10-16 | 18.73 | 29.49 | 25.78 | ok |
| ^MOVE | 101.10 | index | 2026-10-16 | -1.36 | 0.40 | 32.64 | ok |
| NVDA | 214.13 | USD_per_share | 2026-10-16 | -1.43 | -6.61 | -3.66 | ok |
| MSFT | 529.05 | USD_per_share | 2026-10-16 | -1.93 | -1.13 | 7.14 | ok |
| AMZN | 250.00 | USD_per_share | 2026-10-16 | -1.87 | -4.74 | -1.46 | ok |
| GOOGL | 340.59 | USD_per_share | 2026-10-16 | -2.47 | -3.15 | -2.56 | ok |
| META | 709.33 | USD_per_share | 2026-10-16 | -3.72 | -1.30 | 6.63 | ok |
| CRWV | 61.39 | USD_per_share | 2026-10-16 | -11.91 | -25.21 | -24.55 | ok |
| MU | 878.84 | USD_per_share | 2026-10-16 | -5.63 | -14.58 | -13.47 | ok |
| DRAM | 46.45 | USD_per_share | 2026-10-16 | -5.84 | -18.78 | -22.08 | ok |
| VRT | 206.42 | USD_per_share | 2026-10-16 | -3.88 | -14.98 | -17.23 | ok |

## 跨资产风险解释

事实：10月16日收盘VIX19.99，VIX3M20.50、MOVE101.1；10月15日HY利差323bp、实际10年利率2.78%、2年4.77%、10年5.10%；金融压力和GPR有更长滞后，不能称为今日水平。Yahoo盘前报价：VIX18.83（11:50:46Z），WTI98.15、Brent108.43、黄金4186.80（约11:55Z），与收盘系列分列，期货合约换月可影响跨时点比较。推断：边际风险缓和，但高实际利率、上周科技跌幅仍约束风险承担。避险与战争影响分别检查黄金、美元、美债、信用、波动率、原油与GPR，不合成自造指数。研究阈值：VIX持续25以上并且HY400bp以上及广度恶化，才升级系统性压力假说；这些不是统计预测概率。CNN官方接口418且网页不可用，留空。

## 宏观与地缘风险指标

| 指标 | 数值 | 单位 | 观测日 | 20次观测变化 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- | --- |
| DGS2 | 4.77 | percent | 2026-10-15 | 0.03 | lagged | https://fred.stlouisfed.org/series/DGS2 |
| BAMLH0A0HYM2 | 3.23 | percentage_points | 2026-10-15 | 0.53 | lagged | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| BAMLC0A0CM | 0.84 | percentage_points | 2026-10-15 | 0.06 | lagged | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| DGS10 | 5.10 | percent | 2026-10-15 | 0.09 | lagged | https://fred.stlouisfed.org/series/DGS10 |
| DFII10 | 2.78 | percent | 2026-10-15 | 0.10 | lagged | https://fred.stlouisfed.org/series/DFII10 |
| T10YIE | 2.35 | percent | 2026-10-16 | 0.02 | ok | https://fred.stlouisfed.org/series/T10YIE |
| STLFSI4 | -0.72 | index | 2026-10-09 | 0.04 | lagged | https://fred.stlouisfed.org/series/STLFSI4 |
| CBOE_VIX | 19.99 | index | 2026-10-16 | 5.18 | ok | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| GPRD | 342.40 | index | 2026-10-13 | 131.41 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_ACT | 444.55 | index | 2026-10-13 | 262.25 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_THREAT | 317.83 | index | 2026-10-13 | 13.72 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_MA7 | 186.58 | index | 2026-10-13 | 33.03 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_MA30 | 177.90 | index | 2026-10-13 | 22.32 | lagged | https://www.matteoiacoviello.com/gpr.htm |

## CNN Fear & Greed

缺失：CNN 无可核验数据，不使用替代指数

## 19 板块与主题 ETF：价格量能证据

| 标的 | 板块 | 1日% | 5日% | 20日% | 相对SPY 1日pp | 相对SPY 5日pp | 相对SPY 20日pp | 成交量/前20日 | 观测日 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLK | 科技 | -3.02 | -7.70 | -3.12 | -1.92 | -5.73 | -3.33 | 1.96 | 2026-10-16 |
| XLE | 能源 | 2.52 | 4.86 | 6.74 | 3.63 | 6.82 | 6.54 | 1.16 | 2026-10-16 |
| XLF | 金融 | 0.45 | 1.44 | -0.26 | 1.56 | 3.41 | -0.46 | 1.10 | 2026-10-16 |
| XLI | 工业 | -0.08 | -0.88 | -0.91 | 1.03 | 1.09 | -1.11 | 1.25 | 2026-10-16 |
| XLV | 医疗 | -0.27 | 3.45 | 5.34 | 0.84 | 5.42 | 5.14 | 0.99 | 2026-10-16 |
| XLP | 必需消费 | 1.08 | 5.02 | 6.52 | 2.19 | 6.99 | 6.31 | 2.03 | 2026-10-16 |
| XLY | 可选消费 | -0.84 | -0.35 | 1.51 | 0.27 | 1.62 | 1.31 | 2.52 | 2026-10-16 |
| XLC | 通信 | -1.89 | -0.05 | -0.11 | -0.78 | 1.91 | -0.32 | 1.00 | 2026-10-16 |
| XLU | 公用事业 | 1.34 | 1.93 | 3.46 | 2.45 | 3.90 | 3.25 | 0.91 | 2026-10-16 |
| XLRE | 房地产 | 0.40 | 1.32 | -0.04 | 1.51 | 3.29 | -0.24 | 1.10 | 2026-10-16 |
| XLB | 材料 | 0.71 | 3.01 | 2.33 | 1.82 | 4.98 | 2.12 | 1.08 | 2026-10-16 |
| SMH | 半导体 | -3.41 | -10.53 | -5.80 | -2.30 | -8.56 | -6.00 | 2.60 | 2026-10-16 |
| IGV | 软件 | -4.80 | -7.39 | -0.01 | -3.69 | -5.43 | -0.21 | 2.19 | 2026-10-16 |
| XOP | 油气开采 | 2.82 | 4.63 | 5.54 | 3.92 | 6.59 | 5.34 | 0.82 | 2026-10-16 |
| OIH | 油服 | 1.48 | -1.66 | -4.15 | 2.59 | 0.30 | -4.35 | 0.86 | 2026-10-16 |
| ITA | 航空与国防 | 1.04 | 1.17 | -2.23 | 2.15 | 3.14 | -2.44 | 2.05 | 2026-10-16 |
| ARKX | 航天主题 | -2.15 | -7.22 | -6.99 | -1.04 | -5.25 | -7.19 | 1.05 | 2026-10-16 |
| KRE | 区域银行 | 0.09 | 1.16 | -3.49 | 1.19 | 3.13 | -3.70 | 0.96 | 2026-10-16 |
| SKYY | 云计算 | -4.87 | -9.37 | -2.17 | -3.76 | -7.40 | -2.37 | 1.03 | 2026-10-16 |

## 资金证据分层

19个板块/主题ETF仍按相同端点比较：上周SMH相对SPY明显落后，XLE、XLP、XLV和RSP相对占优；盘前QQQ反弹还不是完整日轮动反转。新增可核验10月14和15日申赎：SOXL连续净申购，SMH由14日净申购转15日净赎回，IGV15日申购、DRAM14日赎回。说明下跌中仍有人增加风险，不能把科技下跌等同全行业主力撤退，也不能把杠杆ETF申购当机构看多证明。发行人XLK10月16日份额657.96百万、NAV183.45；无本次完整份额和拆分核验，不据单点计算净流入。当前周完整申赎与机构实时身份仍缺失；旧周10月5–9窗口仅作历史对照。

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

2026-10-19T12:07:43.743919+00:00本次采集器主题搜索覆盖科技、半导体、软件、能源油气、金融、工业、航天、政府政策与Fed；另主动搜索AI泡沫、Fed、海峡航运及条件式选举合约。保留八个已核验结算定义的合约；搜索截断、未核验新航运合约，不使用搜索页AI摘要当事实。近端确定事件为官方FOMC；公司财报另列催化剂，不臆造相关合约。

## Polymarket · 值得警惕的信号

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["AI bubble burst in 2026?", "期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。", "https://polymarket.com/event/ai-bubble-burst-by"] | [9.3, {"status": "comparable", "change_pp": 1.8500000000000003}] | {"spread": 0.0020000000000000018, "volume24h_usd": 37692.202579000004, "liquidity_usd": 34968.19695, "quality_flags": [], "retrieved_at": "2026-10-19T12:03:44.247663+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["联合尾部合约升至9.3%，与盘前修复并存", "AI估值与融资风险"] | ["同规则价格持续上行并有经营/信用证据", "现金流和信用改善"] | [null, null] |
| ["Will WTI Crude Oil (WTI) hit (HIGH) $105 in October?", "10月交易时段内，Pyth的ICE WTI活跃月合约1分钟最终高价达到105美元即Yes；按规则提前3个交易时段换月，数据不可用时可依ICE日高低。不是月末价格，也不能以Yahoo CL=F直接结算。", "https://polymarket.com/event/what-price-will-wti-hit-in-october-2026"] | [39.0, {"status": "comparable", "change_pp": -7.500000000000001}] | {"spread": 0.020000000000000018, "volume24h_usd": 58217.693214, "liquidity_usd": 47571.2208, "quality_flags": [], "retrieved_at": "2026-10-19T12:03:44.247663+00:00", "contract_end_at": "2026-11-01T03:59:59.999000+00:00"} | ["WTI触105合约39%，油价上行尾部缓和", "能源成本→利率→成长估值"] | ["供应中断与可核验油价共同走强", "通行恢复及供应增加"] | [null, null] |

## Polymarket · 有参考价值的事件

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Strait of Hormuz traffic returns to normal by October 31?", "10月31日前IMF Portwatch海峡船舶通行7日均值任一天达到60才为Yes；非宣布开放。末日数据等待14日，有窗口内修订和明显数据错误处理。", "https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-october-31-20260810151043583"] | [0.75, {"status": "comparable", "change_pp": -0.5000000000000001}] | {"spread": 0.001, "volume24h_usd": 22348.812855, "liquidity_usd": 186483.20431, "quality_flags": [], "retrieved_at": "2026-10-19T12:03:44.247663+00:00", "contract_end_at": "2026-11-01T03:59:00+00:00"} | ["月底实际通行合约0.75%，宣布重开不等于通航", "航运恢复速度影响供给风险溢价"] | ["IMF同口径船舶通行7日均值回升", "只有口头提议、无实际通航"] | [null, null] |
| ["Strait of Hormuz traffic returns to normal by December 31?", "期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。", "https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31"] | [14.000000000000002, {"status": "comparable", "change_pp": 1.5000000000000013}] | {"spread": 0.01999999999999999, "volume24h_usd": 81343.04748599998, "liquidity_usd": 336719.243, "quality_flags": [], "retrieved_at": "2026-10-19T12:03:44.247663+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["年底通航合约14%，关注实际船舶数据", "能源中期风险"] | ["实际船舶数据支持改善", "封锁和袭击持续"] | [null, null] |
| ["US x Iran ceasefire continues through October 31?", "截至10月31日伊朗标准时间23:59，美国未对伊朗领土及内水实施规则列明的直接命中空袭或地对地打击才为Yes。海域/空域、拦截碎片、小型打击、网络战等不计；争议信息允许三日核验。不是所有交战方全面停火，也不等于海峡畅通。", "https://polymarket.com/event/us-iran-ceasefire-continues-throughptptpt"] | [83.0, {"status": "comparable", "change_pp": 1.5000000000000013}] | {"spread": 0.020000000000000018, "volume24h_usd": 218179.218801, "liquidity_usd": 74509.3443, "quality_flags": [], "retrieved_at": "2026-10-19T12:03:44.247663+00:00", "contract_end_at": "2026-10-31T23:59:00+00:00"} | ["特定美国打击定义下83%，不是全方位停火", "定义差异解释与通航低概率并存"] | ["可信报道符合专门规则", "其他交战行动不能自动当本合约失效"] | [null, null] |
| ["Will the Fed increase interest rates by 25 bps after the December 2026 meeting?", "以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。", "https://polymarket.com/event/fed-decision-in-december-20260729232808632"] | [76.5, {"status": "comparable", "change_pp": 2.0000000000000018}] | {"spread": 0.010000000000000009, "volume24h_usd": 2429.118759, "liquidity_usd": 172100.5068, "quality_flags": [], "retrieved_at": "2026-10-19T12:03:44.247663+00:00", "contract_end_at": "2026-12-09T23:59:00+00:00"} | ["12月25bp加息合约76.5%，不是央行承诺", "贴现率影响长久期资产"] | ["后续通胀及官方政策支持", "通胀缓解及政策转向"] | [null, null] |

## Polymarket · 将要发生的事件及概率

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Will there be no change in Fed interest rates after the October 2026 meeting?", "以10月27–28日FOMC前后联邦基金目标区间上限不变结算；非25bp标准变动向上取整至25bp档；若下一会议期限仍无声明按不变档结算。", "https://polymarket.com/event/fed-decision-in-october-20260617190323537"] | [88.5, {"status": "comparable", "change_pp": 2.0000000000000018}] | {"spread": 0.010000000000000009, "volume24h_usd": 419091.8596069999, "liquidity_usd": 959402.4168, "quality_flags": [], "retrieved_at": "2026-10-19T12:03:44.247663+00:00", "contract_end_at": "2026-10-29T03:59:00+00:00"} | ["官方FOMC临近，按目标利率上限变化结算", "政策上限变化影响折现率"] | ["官方声明发布后核验", "会前预期不是实际决定"] | ["2026-10-28T14:00:00-04:00", "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm"] |

## Will there be no change in Fed interest rates after the October 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 606422 / 2589812 |
| Yes 概率 % | 88.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [2.0, 5.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 2.0000000000000018} |
| 24h成交量 / 流动性 USD | [419091.8596069999, 959402.4168] |
| 价差 pp | 1.00 |
| 到期 | 2026-10-29T03:59:00+00:00 |
| 结算规则摘要 | 以10月27–28日FOMC前后联邦基金目标区间上限不变结算；非25bp标准变动向上取整至25bp档；若下一会议期限仍无声明按不变档结算。 |
| 规则指纹 | fbc973610971c579003bb7db1464373da28fb0d8484ae204350268d22f83fb7e |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-19T12:01:13.809809Z |
| 抓取时间 | 2026-10-19T12:03:44.247663+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-october-20260617190323537 |

## US x Iran ceasefire continues through October 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1038648 / 4641065 |
| Yes 概率 % | 83.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [1.5, 4.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 1.5000000000000013} |
| 24h成交量 / 流动性 USD | [218179.218801, 74509.3443] |
| 价差 pp | 2.00 |
| 到期 | 2026-10-31T23:59:00+00:00 |
| 结算规则摘要 | 截至10月31日伊朗标准时间23:59，美国未对伊朗领土及内水实施规则列明的直接命中空袭或地对地打击才为Yes。海域/空域、拦截碎片、小型打击、网络战等不计；争议信息允许三日核验。不是所有交战方全面停火，也不等于海峡畅通。 |
| 规则指纹 | 4ad99c00bba55951472643794eca27dab0743ff8891a0f80509306b4b3c87506 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-19T12:03:14.258208Z |
| 抓取时间 | 2026-10-19T12:03:44.247663+00:00 |
| 来源 | https://polymarket.com/event/us-iran-ceasefire-continues-throughptptpt |

## Strait of Hormuz traffic returns to normal by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 455875 / 2176270 |
| Yes 概率 % | 14.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [1.5, -0.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 1.5000000000000013} |
| 24h成交量 / 流动性 USD | [81343.04748599998, 336719.243] |
| 价差 pp | 2.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。 |
| 规则指纹 | b0c8ba27f4437b0d8ab819ae170bec118166232e39cdcaefb95bd352d29073d4 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-19T11:57:13.305288Z |
| 抓取时间 | 2026-10-19T12:03:44.247663+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31 |

## Will WTI Crude Oil (WTI) hit (HIGH) $105 in October?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1078055 / 4951227 |
| Yes 概率 % | 39.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-7.5, 17.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -7.500000000000001} |
| 24h成交量 / 流动性 USD | [58217.693214, 47571.2208] |
| 价差 pp | 2.00 |
| 到期 | 2026-11-01T03:59:59.999000+00:00 |
| 结算规则摘要 | 10月交易时段内，Pyth的ICE WTI活跃月合约1分钟最终高价达到105美元即Yes；按规则提前3个交易时段换月，数据不可用时可依ICE日高低。不是月末价格，也不能以Yahoo CL=F直接结算。 |
| 规则指纹 | 0c455b139d74a669b793323a95aea1e08486656281c457348bd488137e37ae8a |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-19T12:01:13.809809Z |
| 抓取时间 | 2026-10-19T12:03:44.247663+00:00 |
| 来源 | https://polymarket.com/event/what-price-will-wti-hit-in-october-2026 |

## AI bubble burst in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 691340 |
| Yes 概率 % | 9.30 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [1.85, 3.15] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 1.8500000000000003} |
| 24h成交量 / 流动性 USD | [37692.202579000004, 34968.19695] |
| 价差 pp | 0.20 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | fc153b2136a8dfbadcd169dce1add40690acb1748566b99716fe7ae8fcb07330 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-19T12:01:13.809809Z |
| 抓取时间 | 2026-10-19T12:03:44.247663+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## Strait of Hormuz traffic returns to normal by October 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 830253 / 3501950 |
| Yes 概率 % | 0.75 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.5, -0.1] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.5000000000000001} |
| 24h成交量 / 流动性 USD | [22348.812855, 186483.20431] |
| 价差 pp | 0.10 |
| 到期 | 2026-11-01T03:59:00+00:00 |
| 结算规则摘要 | 10月31日前IMF Portwatch海峡船舶通行7日均值任一天达到60才为Yes；非宣布开放。末日数据等待14日，有窗口内修订和明显数据错误处理。 |
| 规则指纹 | be893052d9d9b648fb6ffa8b901ed6d9775d1cd3d1be9f830e1dcf5d0f046390 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-19T12:03:14.258208Z |
| 抓取时间 | 2026-10-19T12:03:44.247663+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-october-31-20260810151043583 |

## AI bubble burst by June 30, 2027?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 4838928 |
| Yes 概率 % | 19.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [4.0, 1.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 4.000000000000001} |
| 24h成交量 / 流动性 USD | [7657.169113000002, 11202.6493] |
| 价差 pp | 1.00 |
| 到期 | 2027-07-01T03:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | bd0420587e08487fffa5050e7fd9b79ffff909a9f843d3f620207ee859462505 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-19T12:01:13.809809Z |
| 抓取时间 | 2026-10-19T12:03:44.247663+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## Will the Fed increase interest rates by 25 bps after the December 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 770450 / 3215008 |
| Yes 概率 % | 76.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [1.0, 2.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 2.0000000000000018} |
| 24h成交量 / 流动性 USD | [2429.118759, 172100.5068] |
| 价差 pp | 1.00 |
| 到期 | 2026-12-09T23:59:00+00:00 |
| 结算规则摘要 | 以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。 |
| 规则指纹 | 933a10a15eeec0ff1de30468fa20540301ed243f75cc3572d42946192f81a123 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-19T12:01:13.809809Z |
| 抓取时间 | 2026-10-19T12:03:44.247663+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-december-20260729232808632 |

## AI 压力：合约、经营与估值分开

三层分开：一，2026年底AI合约9.3%、2027年6月底19.5%，分别较昨晚+1.85和+4个百分点；均有至少三个专门事件触发要求，不能解释成所有AI股票崩盘的概率。二，Silicon Data10月18日H100 neo-cloud指数2.83美元/GPU小时、7日+7.6%，与租金崩溃假说相反，但不证明全部新建算力回报足够；融资成本、利用率、客户质量和资本开支兑现仍须核验。CRWV券商升级且目标价下调是tc新闻线索，不是新的公司现金流事实。三，本次SEC五家公司10-Q/10-K列表与底稿一致，复用既有企业FCFF五年及终值假设，以10月16日收盘价为统一估值基准；不把本次盘前报价混入部分公司的估值。META关键租赁分项缺口仍暂停估值。META官方确认10月21日盘后财报/16:30纽约电话会，重点看经营现金流、资本开支、租赁承诺和收入变现；新财报前不能把反弹理解为基本面问题已经解决。

## NVDA · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | scenario_analysis |
| 财务底稿 | TTM 至 2026-07-26；最新 10-Q / filed 2026-08-26 |
| 披露检查 | {"checked_at": "2026-10-19T12:04:37.815033+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001045810.json", "latest_filing_date": "2026-08-26"} |
| 观测财务数据 | {"ttm_revenue_million": 302970, "revenue_quarters": [{"end": "2025-10-26", "value": 57006000000, "filed": "2025-11-19", "duration_days": 91}, {"end": "2026-01-25", "value": 68127000000, "filed": "2026-02-25", "duration_days": 91}, {"end": "2026-04-26", "value": 81615000000, "filed": "2026-05-20", "duration_days": 91}, {"end": "2026-07-26", "value": 96221000000, "filed": "2026-08-26", "duration_days": 91}], "cash_million": 22443.0, "liquid_investments_million": 34143.0, "debt_million": 33366.0, "finance_lease_million": 0, "diluted_shares_million": 24285.0, "latest_operating_income_million": 63734.0, "observed_end": "2026-07-26", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "Revenues", "latest_reported_revenue_million": 96221.0, "income_statement_window": "最近单季度", "ttm_bridge_note": "采用同版 FY2026全年 + FY2027半年 - FY2026半年；与四季逐项求和差1百万为披露舍入差。"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json", "https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。10-Q Note14 表明融资租赁费用不重大；模型按不重大近似零，不将其称为精确零负债。未确认担保仅作为压力情景，非已到期净债务。市场化股权42783和非市场化股权51157不作为类现金；非经营资产加回为0的保守假设。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | 无 |
| 价格 USD | 214.13 |
| 基期输入 USD million / million shares | {"revenue": 302970, "net_debt": -23220.0, "diluted_shares": 24285.0, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.29112673790675314, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## NVDA · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 98.77 | -53.87 | 14.00 | 60.00 | 12.00 | 68.42 |
| 基准 | 154.12 | -28.03 | 20.00 | 65.00 | 11.00 | 74.20 |
| 乐观 | 242.58 | 13.29 | 26.00 | 70.00 | 10.00 | 79.05 |

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
| 披露检查 | {"checked_at": "2026-10-19T12:04:40.961427+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0000789019.json", "latest_filing_date": "2026-07-29"} |
| 观测财务数据 | {"ttm_revenue_million": 331839.0, "revenue_quarters": [{"end": "2025-09-30", "value": 77673000000, "filed": "2025-10-29", "duration_days": 92}, {"end": "2025-12-31", "value": 81273000000, "filed": "2026-01-28", "duration_days": 92}, {"end": "2026-03-31", "value": 82886000000, "filed": "2026-04-29", "duration_days": 90}, {"end": "2026-06-30", "value": 90007000000, "filed": "2026-07-29", "duration_days": 91}], "cash_million": 20935.0, "liquid_investments_million": 55908.0, "debt_million": 40294.0, "finance_lease_million": 66594.0, "diluted_shares_million": 7453.0, "latest_operating_income_million": 155237.0, "observed_end": "2026-06-30", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "RevenueFromContractWithCustomerExcludingAssessedTax", "latest_reported_revenue_million": 331839.0, "income_statement_window": "FY2026 全年"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0000789019.json", "https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。融资租赁66594计入债务；资本开支假设涵盖新增租赁，现金支出115948加融资租赁资产新增24608为本年经济资本开支140556。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | 无 |
| 价格 USD | 529.05 |
| 基期输入 USD million / million shares | {"revenue": 331839.0, "net_debt": 30045.0, "diluted_shares": 7453.0, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.31599619259213785, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## MSFT · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 143.02 | -72.97 | 8.00 | 42.00 | 10.50 | 76.13 |
| 基准 | 266.55 | -49.62 | 14.00 | 47.00 | 9.50 | 81.05 |
| 乐观 | 484.83 | -8.36 | 20.00 | 52.00 | 8.50 | 84.97 |

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
| 披露检查 | {"checked_at": "2026-10-19T12:04:43.602078+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001018724.json", "latest_filing_date": "2026-07-31"} |
| 观测财务数据 | {"ttm_revenue_million": 775680.0, "revenue_quarters": [{"end": "2025-09-30", "value": 180169000000, "filed": "2025-10-31", "duration_days": 92}, {"end": "2025-12-31", "value": 213386000000, "filed": "2026-02-06", "duration_days": 92}, {"end": "2026-03-31", "value": 181519000000, "filed": "2026-04-30", "duration_days": 90}, {"end": "2026-06-30", "value": 200606000000, "filed": "2026-07-31", "duration_days": 91}], "cash_million": 78213.0, "liquid_investments_million": 44775.0, "debt_million": 133320.0, "finance_lease_million": 13451.0, "diluted_shares_million": 10903.0, "latest_operating_income_million": 27461.0, "observed_end": "2026-06-30", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "RevenueFromContractWithCustomerExcludingAssessedTax", "latest_reported_revenue_million": 200606.0, "income_statement_window": "最近单季度"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001018724.json", "https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。总长期债务132995（含当前部分）加短期借款325，融资租赁13451另加；未将其他长期负债全部误作有息债务。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | 无 |
| 价格 USD | 250.00 |
| 基期输入 USD million / million shares | {"revenue": 775680.0, "net_debt": 23783.0, "diluted_shares": 10903.0, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.38975908974642637, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## AMZN · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 11.53 | -95.39 | 6.00 | 12.00 | 11.00 | 84.01 |
| 基准 | 87.42 | -65.03 | 12.00 | 17.00 | 10.00 | 83.61 |
| 乐观 | 238.05 | -4.78 | 18.00 | 22.00 | 9.00 | 86.04 |

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
| 披露检查 | {"checked_at": "2026-10-19T12:04:46.107272+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001652044.json", "latest_filing_date": "2026-07-23"} |
| 观测财务数据 | {"ttm_revenue_million": 445867.0, "revenue_quarters": [{"end": "2025-09-30", "value": 102346000000, "filed": "2025-10-30", "duration_days": 92}, {"end": "2025-12-31", "value": 113829000000, "filed": "2026-02-05", "duration_days": 92}, {"end": "2026-03-31", "value": 109896000000, "filed": "2026-04-30", "duration_days": 90}, {"end": "2026-06-30", "value": 119796000000, "filed": "2026-07-23", "duration_days": 91}], "cash_million": 55911.0, "liquid_investments_million": 186563.0, "debt_million": 100164, "finance_lease_million": 2590.0, "diluted_shares_million": 12309.0, "latest_operating_income_million": 40770.0, "observed_end": "2026-06-30", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "Revenues", "latest_reported_revenue_million": 119796.0, "income_statement_window": "最近单季度"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001652044.json", "https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/goog-20260630.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。优先股按完全转换处理：季度稀释股数12309减已计入的16，再加合同最大转换股数54.45825；不再扣19000优先股本金。未来3年优先股息按年1203.125、10%折现约2991.99计入权益桥调整，此为保守假设；capped call 未赋值。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | {"preferred_coupon_pv_million": 2991.9938016528904, "discount_rate": 0.1, "years": 3} |
| 价格 USD | 340.59 |
| 基期输入 USD million / million shares | {"revenue": 445867.0, "net_debt": -136728.0061983471, "diluted_shares": 12347.45825, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.3928877817238875, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## GOOGL · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 66.88 | -80.36 | 7.00 | 31.00 | 11.00 | 79.41 |
| 基准 | 131.94 | -61.26 | 13.00 | 36.00 | 10.00 | 82.80 |
| 乐观 | 250.29 | -26.51 | 19.00 | 41.00 | 9.00 | 85.75 |

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
| 财务底稿 | TTM 至 2026-06-30；最新 10-Q / filed 2026-07-30 |
| 披露检查 | {"checked_at": "2026-10-19T12:04:48.554237+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001326801.json", "latest_filing_date": "2026-07-30"} |
| 观测财务数据 | {"ttm_revenue_million": 228247.0, "revenue_quarters": [{"end": "2025-09-30", "value": 51242000000, "filed": "2025-10-30", "duration_days": 92}, {"end": "2025-12-31", "value": 59893000000, "filed": "2026-01-29", "duration_days": 92}, {"end": "2026-03-31", "value": 56311000000, "filed": "2026-04-30", "duration_days": 90}, {"end": "2026-06-30", "value": 60801000000, "filed": "2026-07-30", "duration_days": 91}], "cash_million": 15462.0, "liquid_investments_million": 74798.0, "debt_million": 83664.0, "finance_lease_million": null, "diluted_shares_million": 2566.0, "latest_operating_income_million": 18775.0, "observed_end": "2026-06-30", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "RevenueFromContractWithCustomerExcludingAssessedTax", "latest_reported_revenue_million": 60801.0, "income_statement_window": "最近单季度"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001326801.json", "https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | 无 |
| 缺失原因 | 最新META季报未单列融资租赁负债；仅有租赁资产和本金偿还额，不能假定零负债，暂不输出精确估值。 |

## AI风险扩散：等待价格与信用共振

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 融资条件、云资本开支/回报率披露、10月FOMC前预期重估 |
| 关联标的 | ["SMH", "NVDA", "MSFT", "AMZN", "GOOGL", "META", "CRWV", "VRT"] |
| 确认条件 | 研究假设：SMH相对SPY连续5交易日落后≥10个百分点，同时HY OAS升破400bp且融资/订单出现可核验负面披露；单独跌价不确认。 |
| 失效条件 | SMH相对强势恢复且HY OAS回落至300bp以下；最新财报收入与现金流改善，融资完成。 |
| 观察期限 | 未来5–15个美股交易日，每日报告复核；财报触发后重新估值 |
| 反证 | 当前HY OAS约323bp，未达假设400bp；大型云公司与供应链需求披露并非全面转负。 |
| 状态 | 观察中；阈值为研究假设，未触发完整组合，未给交易方向 |

## 能源相对强势能否延续

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 霍尔木兹实际通行量、供给政策、俄制裁豁免后供应变化 |
| 关联标的 | ["XLE", "XOP", "OIH", "CL=F", "BZ=F"] |
| 确认条件 | 研究假设：XLE相对SPY的5日超额保持正值、Brent连续两次收盘高于110美元，并有航运/供应数据支持；开盘跳空不追认。 |
| 失效条件 | Brent回落至100美元以下且XLE连续5日跑输SPY；通行7日均值恢复或供应明显增加。 |
| 观察期限 | 下一交易日至未来2周 |
| 反证 | OIH周表现弱于能源开采；俄制裁豁免可能改善供给。油价高并不能单独证明滞涨。 |
| 状态 | 观察中；10月16日Brent收盘109.86，10月19日11:55Z盘前108.43，价格确认未完成 |

## 防御轮动还是市场广度改善

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 下一交易周利率、信用与行业盈利消息 |
| 关联标的 | ["RSP", "SPY", "XLP", "XLV", "XLU", "XLF", "KRE", "XLI", "ITA", "ARKX"] |
| 确认条件 | 研究假设：RSP/SPY连续3个交易日改善，XLP/XLV相对强势，同时信用不再走阔；检查金融和工业是否跟随。 |
| 失效条件 | RSP相对SPY转弱或信用持续走阔；防御板块与成长板块同时下跌。 |
| 观察期限 | 本交易周（10月19–23日） |
| 反证 | 板块收益不是净流入；航天与国防分化，不能将ITA上涨推演为所有航天受益。 |
| 状态 | 观察中 |

## 成长反弹能否升级为修复

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 油价与利率缓和、META财报现金流 |
| 关联标的 | ["QQQ", "SMH", "NVDA", "META", "MSFT"] |
| 确认条件 | 假设：QQQ与SMH连续两次常规收盘收复20日线，信用不扩大，披露支持资本开支回报；盘前上涨单独不满足。 |
| 失效条件 | 反弹回吐并跌破10月16日低点，或财报现金流/融资条件恶化。 |
| 观察期限 | 本周至未来两周 |
| 反证 | AI尾部合约上升；反弹可能只是空头回补，尚无订单或资金身份确认。 |
| 状态 | 观察中，不因盘前上涨直接追价 |

## 跨期比较与上期剧本复核

相对10月18日晚间日报：收盘研究基准仍为10月16日，不重复计算新日收益。新增Yahoo盘前SPY766.7935（12:05:43Z）、QQQ718.57（12:05:49Z），分别高于周五763.25、709.80；属于未完成交易时段。八个同ID、同规则合约：10月Fed不变86.5→88.5%；12月加25bp74.5→76.5%；海峡年底正常12.5→14%；10月底正常1.25→0.75%；特定美伊停火81.5→83%；WTI月内触105为46.5→39%；AI年底7.45→9.3%，AI2027年6月底15.5→19.5%。变化为两快照差，不能归因于单条新闻。短期油价缓和与AI尾部合约升价并存，期限和结算定义不能混同。此前信用400bp、Brent两次收盘110上方等剧本仍未确认。

## 可计算的跨期变化

```json
[
  {
    "mode": "daily",
    "baseline": "reports/daily/2026-10-16/20261018T120935.196588Z/evidence.json",
    "baseline_cutoff": "2026-10-18T12:09:35.108960+00:00",
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
        "observation_date": "2026-10-15"
      },
      "BAMLH0A0HYM2": {
        "change": 0.0,
        "unit": "percentage_points",
        "observation_date": "2026-10-15"
      },
      "BAMLC0A0CM": {
        "change": 0.0,
        "unit": "percentage_points",
        "observation_date": "2026-10-15"
      },
      "DGS10": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-10-15"
      },
      "DFII10": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-10-15"
      },
      "T10YIE": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-10-16"
      },
      "STLFSI4": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-09"
      },
      "CBOE_VIX": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-16"
      },
      "GPRD": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-13"
      },
      "GPRD_ACT": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-13"
      },
      "GPRD_THREAT": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-13"
      },
      "GPRD_MA7": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-13"
      },
      "GPRD_MA30": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-13"
      }
    },
    "event_probability_change": {
      "2589812": {
        "status": "comparable",
        "change_pp": 2.0000000000000018
      },
      "4641065": {
        "status": "comparable",
        "change_pp": 1.5000000000000013
      },
      "2176270": {
        "status": "comparable",
        "change_pp": 1.5000000000000013
      },
      "4951227": {
        "status": "comparable",
        "change_pp": -7.500000000000001
      },
      "691340": {
        "status": "comparable",
        "change_pp": 1.8500000000000003
      },
      "3501950": {
        "status": "comparable",
        "change_pp": -0.5000000000000001
      },
      "4838928": {
        "status": "comparable",
        "change_pp": 4.000000000000001
      },
      "3215008": {
        "status": "comparable",
        "change_pp": 2.0000000000000018
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
    "event": "今日常规开盘",
    "date": "2026-10-19T09:30:00-04:00",
    "timezone": "America/New_York",
    "source": "tc get_trading_calendar"
  },
  {
    "event": "META第三季财报盘后，电话会16:30纽约/北京时间10月22日04:30",
    "date": "2026-10-21T16:30:00-04:00",
    "source": "https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-to-Announce-Third-Quarter-2026-Results/default.aspx"
  },
  {
    "event": "FOMC会议",
    "date": "2026-10-27/2026-10-28",
    "timezone": "America/New_York",
    "source": "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm"
  }
]
```

## 新闻事件去重与时间

| 事件 | 摘要 | 发生时间（未知留空） | 各来源发布时间 / 抓取时间 |
| --- | --- | --- | --- |
| meta-q3-scheduled | META官方确认10月21日盘后财报、16:30纽约电话会；本周AI投资回报验证催化剂。 | 2026-10-21T16:30:00-04:00 | [{"source": "https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-to-Announce-Third-Quarter-2026-Results/default.aspx", "published_at": null, "retrieved_at": "2026-10-19T12:07:43.743919+00:00"}] |
| gpu-rental-oct18 | H100 neo-cloud指数10月18日2.83美元/GPU小时、7日+7.6%；FAQ旧值未采用。 | 缺失 | [{"source": "https://www.silicondata.com/products/silicon-index/h100", "published_at": null, "retrieved_at": "2026-10-19T12:07:43.743919+00:00"}] |
| crwv-upgrade-line | tc转述高盛将CRWV由中性上调买入同时目标价139下调106；尚未获得原始研报，作为观点线索，不证明融资问题已解决。 | 缺失 | [{"source": "https://x.com/DeItaone/status/2112148100735287748", "published_at": "2026-10-19T11:45:23+00:00", "retrieved_at": "2026-10-19T12:07:43.743919+00:00"}] |

## 覆盖范围与数据缺口

```json
[
  "tc批量报价与周五收盘相同但ts刷新，成交时间未核验，已剔除当前报价资格；SPY/QQQ以独立Yahoo分钟数据核验。",
  "CNN官方418及网页不可用；CME FedWatch、实际VIX期货曲线和真实成分股广度未取得。",
  "tc10月18与19日查询每次最多50条，可能截断；主动官方补查仍不能证明新闻完整。",
  "Polymarket多主题搜索截断；部分新增航运/选举事件未完成结算核验，不纳入概率决策。",
  "仅取得10月14–15日新增部分ETF申赎与发行人单点，未取得10月12–16全周或本日完整净申赎。",
  "META租赁分项关键输入仍缺失；DRAM历史不足200日；宏观信用/利率/金融压力/GPR数据有发布滞后。",
  "CRWV券商原报告和伊拉克出口官方声明未取得；不将tc转述升级为基本面事实。",
  "原始采集存在请求失败，见采集质量记录",
  "META 估值: 最新META季报未单列融资租赁负债；仅有租赁资产和本金偿还额，不能假定零负债，暂不输出精确估值。",
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
  "tc 报价质量 unverified_trade_timestamp: IWM, RSP, XLK, XLE, XLF, XLI, XLV, XLP, XLY, XLC, XLU, XLRE, XLB, SMH, IGV, XOP, OIH, ITA, ARKX, KRE, SKYY, GLD, TLT, UUP, HYG, LQD, NVDA, MSFT, AMZN, GOOGL, META, CRWV, MU, DRAM, VRT；不作为新成交证据",
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
  "指标缺失/历史不足: prices.^VIX.volume_vs_previous20_ratio, prices.^VIX3M.volume_vs_previous20_ratio, prices.^VVIX.volume_vs_previous20_ratio, prices.^MOVE.volume_vs_previous20_ratio, prices.DRAM.sma200, prices.DRAM.distance_sma200_pct, quotes.IWM.value, quotes.RSP.value, quotes.XLK.value, quotes.XLE.value, quotes.XLF.value, quotes.XLI.value, quotes.XLV.value, quotes.XLP.value, quotes.XLY.value, quotes.XLC.value, quotes.XLU.value, quotes.XLRE.value, quotes.XLB.value, quotes.SMH.value, quotes.IGV.value, quotes.XOP.value, quotes.OIH.value, quotes.ITA.value, quotes.ARKX.value, quotes.KRE.value, quotes.SKYY.value, quotes.GLD.value, quotes.TLT.value, quotes.UUP.value, quotes.HYG.value, quotes.LQD.value, quotes.NVDA.value, quotes.MSFT.value, quotes.AMZN.value, quotes.GOOGL.value, quotes.META.value, quotes.CRWV.value, quotes.MU.value, quotes.DRAM.value, quotes.VRT.value",
  "外部广度、盈利修正及政策定价未补录；不得用 ETF 涨跌代替成分股广度"
]
```

## 来源、时间与核验记录

```json
[
  {
    "url": "https://www.whitehouse.gov/presidential-actions/2026/10/implementing-the-lindsey-o-graham-sanctioning-russia-and-iran-act-of-2026/",
    "checked_at": "2026-10-18T04:03:30.162293+00:00",
    "note": "沿用上期公开报告，原核验时间保留；沿用早前公开报告已核验资料；本次未重开原文。核验10月16日行政令：豁免新法若干制裁和关税，非取消所有既有俄制裁；未确认具体发布时分，作为盘后/周末增量。"
  },
  {
    "url": "https://investor.tsmc.com/english/quarterly-results/2026/q3",
    "checked_at": "2026-10-18T12:09:34.836974+00:00",
    "note": "沿用上期公开报告，原核验时间保留；核验Q3业绩资料页面；作为需求尚未全面崩塌的反证，非本周价格支撑保证。"
  },
  {
    "url": "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm",
    "checked_at": "2026-10-18T12:09:34.836974+00:00",
    "note": "沿用上期公开报告，原核验时间保留；核验2026年FOMC日历；10月27–28日、12月8–9日。"
  },
  {
    "url": "https://www.etf.com/sections/weekly-etf-flows/etf-inflows-top-41b-investors-pile-brazil-long-bonds",
    "checked_at": "2026-10-18T12:09:34.836974+00:00",
    "note": "沿用上期公开报告，原核验时间保留；10月12日发表，窗口10月5–9日，仅选取相关ETF净申赎。"
  },
  {
    "url": "https://www.silicondata.com/products/silicon-index/h100",
    "checked_at": "2026-10-18T12:09:34.836974+00:00",
    "note": "沿用上期公开报告，原核验时间保留；页面主数据10月17日H100 2.82 USD/GPU-hour；正文FAQ存在旧数字，不混用；无逐日序列，不判断连续5天条件。"
  },
  {
    "url": "https://www.ssga.com/us/en/individual/etfs/state-street-technology-select-sector-spdr-etf-xlk",
    "checked_at": "2026-10-18T12:09:34.836974+00:00",
    "note": "沿用上期公开报告，原核验时间保留；发行人仅核验10月15日份额659.41百万、NAV189.19；缺可比前期份额，不能估流量。"
  },
  {
    "url": "https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/overview/",
    "checked_at": "2026-10-18T12:09:34.836974+00:00",
    "note": "沿用上期公开报告，原核验时间保留；发行人10月16日NAV539.75、净资产65.68十亿美元；缺完整同窗口份额序列。"
  },
  {
    "url": "https://www.matteoiacoviello.com/gpr.htm",
    "checked_at": "2026-10-18T04:03:30.162293+00:00",
    "note": "沿用上期公开报告，原核验时间保留；沿用早前公开报告已核验资料；本次未重开原文。GPR是新闻文本地缘风险，不是实时战争强度；最新可取观测10月13日。"
  },
  {
    "url": "https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json",
    "checked_at": "2026-10-18T04:03:30.162293+00:00",
    "note": "沿用上期公开报告，原核验时间保留；沿用早前公开报告已核验资料；本次未重开原文。NVDA SEC结构化财务；filed=2026-08-26，底稿保留TTM与最新披露。"
  },
  {
    "url": "https://data.sec.gov/api/xbrl/companyfacts/CIK0000789019.json",
    "checked_at": "2026-10-18T04:03:30.162293+00:00",
    "note": "沿用上期公开报告，原核验时间保留；沿用早前公开报告已核验资料；本次未重开原文。MSFT SEC结构化财务；filed=2026-07-29，底稿保留TTM与最新披露。"
  },
  {
    "url": "https://data.sec.gov/api/xbrl/companyfacts/CIK0001018724.json",
    "checked_at": "2026-10-18T04:03:30.162293+00:00",
    "note": "沿用上期公开报告，原核验时间保留；沿用早前公开报告已核验资料；本次未重开原文。AMZN SEC结构化财务；filed=2026-07-31，底稿保留TTM与最新披露。"
  },
  {
    "url": "https://data.sec.gov/api/xbrl/companyfacts/CIK0001652044.json",
    "checked_at": "2026-10-18T04:03:30.162293+00:00",
    "note": "沿用上期公开报告，原核验时间保留；沿用早前公开报告已核验资料；本次未重开原文。GOOGL SEC结构化财务；filed=2026-07-23，底稿保留TTM与最新披露。"
  },
  {
    "url": "https://data.sec.gov/api/xbrl/companyfacts/CIK0001326801.json",
    "checked_at": "2026-10-18T04:03:30.162293+00:00",
    "note": "沿用上期公开报告，原核验时间保留；沿用早前公开报告已核验资料；本次未重开原文。META SEC结构化财务；filed=2026-07-30，底稿保留TTM与最新披露。"
  },
  {
    "url": "https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm",
    "checked_at": "2026-10-18T12:09:34.836974+00:00",
    "note": "沿用上期公开报告，原核验时间保留；核验9月加息25bp及目标区间。"
  },
  {
    "url": "https://www.bls.gov/news.release/cpi.nr0.htm",
    "checked_at": "2026-10-18T12:09:34.836974+00:00",
    "note": "沿用上期公开报告，原核验时间保留；核验9月CPI及能源贡献，非全经济需求过热证明。"
  },
  {
    "url": "https://apnews.com/article/d8b9749fee99a11dd77513d326b824b6",
    "checked_at": "2026-10-18T12:09:34.836974+00:00",
    "note": "沿用上期公开报告，原核验时间保留；9月25日报道已有类似附条件七日方案，避免将重复提议误判为新协议。"
  },
  {
    "url": "https://www.cls.cn/detail/2507683",
    "checked_at": "2026-10-18T12:09:34.836974+00:00",
    "note": "沿用上期公开报告，原核验时间保留；tc新闻线索；网页不可访问，未升级为独立核验事实。"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0001045810.json",
    "checked_at": "2026-10-18T12:07:24.117801+00:00",
    "note": "沿用上期公开报告，原核验时间保留；本次查询最新10-Q/10-K列表，日期匹配现有财务底稿。"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0000789019.json",
    "checked_at": "2026-10-18T12:07:26.503310+00:00",
    "note": "沿用上期公开报告，原核验时间保留；本次查询最新10-Q/10-K列表，日期匹配现有财务底稿。"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0001018724.json",
    "checked_at": "2026-10-18T12:07:28.921868+00:00",
    "note": "沿用上期公开报告，原核验时间保留；本次查询最新10-Q/10-K列表，日期匹配现有财务底稿。"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0001652044.json",
    "checked_at": "2026-10-18T12:07:31.513258+00:00",
    "note": "沿用上期公开报告，原核验时间保留；本次查询最新10-Q/10-K列表，日期匹配现有财务底稿。"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0001326801.json",
    "checked_at": "2026-10-18T12:07:33.841946+00:00",
    "note": "沿用上期公开报告，原核验时间保留；本次查询最新10-Q/10-K列表，日期匹配现有财务底稿。"
  },
  {
    "url": "https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-to-Announce-Third-Quarter-2026-Results/default.aspx",
    "checked_at": "2026-10-19T12:07:43.743919+00:00",
    "note": "官方财报日期核验"
  },
  {
    "url": "https://www.silicondata.com/products/silicon-index/h100",
    "checked_at": "2026-10-19T12:07:43.743919+00:00",
    "note": "10月18日主指数2.83；FAQ旧值不采用"
  },
  {
    "url": "https://www.etf.com/sections/daily-etf-flows/etf-fund-flows-small-cap-focused-iwm-nets-22-billion",
    "checked_at": "2026-10-19T12:07:43.743919+00:00",
    "note": "10月15日单日申赎，非周度"
  },
  {
    "url": "https://www.etf.com/sections/daily-etf-flows/etf-fund-flows-semiconductors-leveraged-etfs-dominate",
    "checked_at": "2026-10-19T12:07:43.743919+00:00",
    "note": "10月14日单日申赎"
  },
  {
    "url": "https://www.ssga.com/us/en/individual/etfs/state-street-technology-select-sector-spdr-etf-xlk",
    "checked_at": "2026-10-19T12:07:43.743919+00:00",
    "note": "发行人10月16日单点NAV/份额，未推算净流入"
  },
  {
    "url": "https://finance.yahoo.com/quote/SPY/",
    "checked_at": "2026-10-19T12:07:43.743919+00:00",
    "note": "chart公开分钟行情含盘前，实际行情时戳与抓取时间分开"
  },
  {
    "url": "https://finance.yahoo.com/quote/QQQ/",
    "checked_at": "2026-10-19T12:07:43.743919+00:00",
    "note": "盘前分钟数据替代tc未知成交时戳"
  },
  {
    "url": "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm",
    "checked_at": "2026-10-19T12:07:43.743919+00:00",
    "note": "本次重查官方会议日期"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0001045810.json",
    "checked_at": "2026-10-19T12:04:37.815033+00:00",
    "note": "五家公司最新10-Q/10-K与底稿一致；不代表无8-K或其他新公告。"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0000789019.json",
    "checked_at": "2026-10-19T12:04:40.961427+00:00",
    "note": "五家公司最新10-Q/10-K与底稿一致；不代表无8-K或其他新公告。"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0001018724.json",
    "checked_at": "2026-10-19T12:04:43.602078+00:00",
    "note": "五家公司最新10-Q/10-K与底稿一致；不代表无8-K或其他新公告。"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0001652044.json",
    "checked_at": "2026-10-19T12:04:46.107272+00:00",
    "note": "五家公司最新10-Q/10-K与底稿一致；不代表无8-K或其他新公告。"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0001326801.json",
    "checked_at": "2026-10-19T12:04:48.554237+00:00",
    "note": "五家公司最新10-Q/10-K与底稿一致；不代表无8-K或其他新公告。"
  }
]
```

## 付费信源建议（未订阅）

```json
[
  {
    "product": "LSEG Lipper Fund Flows",
    "gap": "补充可下载的每日/每周ETF和基金流量历史；仍需核验估计口径，不能识别最终机构身份。",
    "url": "https://www.lseg.com/en/data-catalogue/funds",
    "checked_at": "2026-10-18T04:03:30.162293+00:00"
  },
  {
    "product": "Silicon Data历史指数",
    "gap": "补齐同口径GPU租金逐日序列，核验连续5日阈值和融资回报率；需先确认具体数据覆盖及授权。",
    "url": "https://www.silicondata.com/products/silicon-index/h100",
    "checked_at": "2026-10-18T04:03:30.162293+00:00"
  }
]
```
