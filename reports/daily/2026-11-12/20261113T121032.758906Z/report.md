# 每日交易总结 · 2026-11-12

## 一分钟读懂 · Agent 摘要

### 当前判断

仍是脆弱的分化修复，盘前上涨尚不足以确认可靠反弹。

### 与上次相比

相对早报，NVDA有所回升但未越过170.24，微软服务恢复有进展却仍有间歇故障；CNN已补核为39，处于恐惧区。

### 最重要的信号

- 12:02UTC附近SPY759.40、QQQ690.21、SMH505；均未越过各自关键确认区，MSFT约515.02低于昨收。
- 最新完整交易日19个ETF仅能源、油气上涨；盘前VIX约18.32有所缓和，昨天高利率和弱广度的反证仍在。
- IEA预计供应趋松，但陆上库存仍低；Google法国数据中心能源合作只是有条件意向，不能直接当作订单兑现。

### 接下来观察

- 今晚21:30北京时间PPI后，看SPY/QQQ回踩形成更高低点，再收复763.04/694.56并获均权、小盘跟随。
- 芯片先看SMH506.96、NVDA170.24能否在常规时段站稳；非芯片继续观察工业、医疗、必需消费。
- 若SPY755、QQQ680被再度跌破且反抽失败，撤销升级判断；油价回落时不要机械追昨天的能源强势。

### 不要忽略

当前仍盘前，尚无今天常规VWAP和完整广度；信用、GPR和ETF申赎有滞后，预测市场不是客观概率。

## 研究结论

11月13日晚报：盘前修复延续但芯片尚未突破；微软服务逐步恢复，PPI将检验利率压力。

## 时点与口径

| 项目 | 内容 |
| --- | --- |
| 模式 | 每日交易总结 |
| 常规交易窗口 | 2026-11-12 → 2026-11-12（纽约交易日） |
| 截止·纽约 | 2026-11-13T07:10:10.455887-05:00 |
| 截止·北京 | 2026-11-13T20:10:10.455887+08:00 |
| 实际生成时间 | 2026-11-13T12:10:10.921640+00:00 |
| 市场阶段 | 盘前 |
| 下一交易日 | 2026-11-13 |
| 运行重点 | 全市场 |
| 上一版本 | reports/daily/2026-11-12/20261112T232709.661331Z/evidence.json |
| 质量 | partial |
| Daily 北京时间计划时段 | 2026-11-13T20:00:00+08:00 |

## 采集、补查与剩余缺口

| 目标 | 补查结果 | 来源 | 观测 / 抓取时间 | 说明 |
| --- | --- | --- | --- | --- |
| 1219851 | 已校验接入 | https://gamma-api.polymarket.com/events/1219851 | 2026-11-13T12:02:30.847067+00:00 / 2026-11-13T12:02:30.847067+00:00 | Gamma snapshot; metadata update is not last trade time |

## 仍需核验的数据与影响

| 数据 | 状态 | 需要核验 | 影响 |
| --- | --- | --- | --- |
| history.DRAM | insufficient_history | 连续完整交易日 OHLC；SMA200 至少200条，ATR14至少15条 | 降低相关判断可信度；保留缺口 |
| macro.GPRD | missing_or_stale | 原始序列与单位，允许发布滞后；检查最近公告（提示阈值7天） | 降低相关判断可信度；保留缺口 |
| macro.GPRD_ACT | missing_or_stale | 原始序列与单位，允许发布滞后；检查最近公告（提示阈值7天） | 降低相关判断可信度；保留缺口 |
| macro.GPRD_THREAT | missing_or_stale | 原始序列与单位，允许发布滞后；检查最近公告（提示阈值7天） | 降低相关判断可信度；保留缺口 |
| macro.GPRD_MA7 | missing_or_stale | 原始序列与单位，允许发布滞后；检查最近公告（提示阈值7天） | 降低相关判断可信度；保留缺口 |
| macro.GPRD_MA30 | missing_or_stale | 原始序列与单位，允许发布滞后；检查最近公告（提示阈值7天） | 降低相关判断可信度；保留缺口 |
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
| prices.SPY.value | 757.12 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_1d_pct | -0.35 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_5d_pct | 3.29 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_20d_pct | -1.90 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_60d_pct | -1.31 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_1d_pp | 0.00 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_5d_pp | 0.00 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_20d_pp | 0.00 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_60d_pp | 0.00 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma20 | 759.47 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma50 | 764.43 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma200 | 728.99 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma20_pct | -0.31 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma50_pct | -0.96 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma200_pct | 3.86 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_sma | 12.45 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_pct | 1.64 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.drawdown_from_63d_high_pct | -2.82 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.volume_vs_previous20_ratio | 0.77 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SPY/history/ |
| prices.QQQ.value | 688.17 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_1d_pct | -0.32 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_5d_pct | 6.35 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_20d_pct | -5.47 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_60d_pct | -3.80 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_1d_pp | 0.03 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_5d_pp | 3.06 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_20d_pp | -3.57 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_60d_pp | -2.49 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma20 | 696.94 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma50 | 718.46 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma200 | 680.94 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma20_pct | -1.26 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma50_pct | -4.22 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma200_pct | 1.06 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_sma | 18.16 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_pct | 2.64 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.drawdown_from_63d_high_pct | -9.41 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.volume_vs_previous20_ratio | 0.72 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.IWM.value | 278.44 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_1d_pct | -1.64 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_5d_pct | 2.75 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_20d_pct | 1.22 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_60d_pct | -7.47 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_1d_pp | -1.29 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_5d_pp | -0.54 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_20d_pp | 3.12 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_60d_pp | -6.17 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma20 | 278.02 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma50 | 281.01 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma200 | 278.40 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma20_pct | 0.15 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma50_pct | -0.91 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma200_pct | 0.02 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_sma | 5.36 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_pct | 1.92 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.drawdown_from_63d_high_pct | -8.19 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.volume_vs_previous20_ratio | 0.92 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IWM/history/ |
| prices.RSP.value | 220.72 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_1d_pct | -0.87 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_5d_pct | 1.78 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_20d_pct | 2.66 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_60d_pct | -0.23 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_1d_pp | -0.51 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_5d_pp | -1.52 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_20d_pp | 4.56 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_60d_pp | 1.07 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma20 | 218.30 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma50 | 214.78 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma200 | 207.59 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma20_pct | 1.11 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma50_pct | 2.76 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma200_pct | 6.33 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_sma | 2.97 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_pct | 1.34 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.drawdown_from_63d_high_pct | -1.17 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.volume_vs_previous20_ratio | 0.72 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/RSP/history/ |
| prices.GLD.value | 354.89 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_1d_pct | -2.82 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_5d_pct | -5.49 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_20d_pct | -7.27 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_60d_pct | -14.24 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_1d_pp | -2.46 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_5d_pp | -8.78 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_20d_pp | -5.37 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_60d_pp | -12.94 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma20 | 370.11 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma50 | 382.00 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma200 | 409.12 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma20_pct | -4.11 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma50_pct | -7.10 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma200_pct | -13.26 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_sma | 7.66 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_pct | 2.16 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.drawdown_from_63d_high_pct | -17.10 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.volume_vs_previous20_ratio | 1.53 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GC=F.value | 3,885.30 | USD_per_troy_ounce | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_1d_pct | -2.88 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_5d_pct | -5.55 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_20d_pct | -6.83 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_60d_pct | -14.52 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_1d_pp | -2.53 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_5d_pp | -8.84 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_20d_pp | -4.93 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_60d_pp | -13.21 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma20 | 4,049.94 | USD_per_troy_ounce | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma50 | 4,194.58 | USD_per_troy_ounce | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma200 | 4,479.41 | USD_per_troy_ounce | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma20_pct | -4.07 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma50_pct | -7.37 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma200_pct | -13.26 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_sma | 98.05 | USD_per_troy_ounce | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_pct | 2.52 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.drawdown_from_63d_high_pct | -17.30 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.volume_vs_previous20_ratio | 0.78 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.CL=F.value | 88.74 | USD_per_barrel | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_1d_pct | 2.55 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_5d_pct | -1.97 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_20d_pct | -9.42 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_60d_pct | 3.39 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_1d_pp | 2.91 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_5d_pp | -5.26 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_20d_pp | -7.52 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_60d_pp | 4.70 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma20 | 96.37 | USD_per_barrel | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma50 | 95.42 | USD_per_barrel | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma200 | 87.66 | USD_per_barrel | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma20_pct | -7.92 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma50_pct | -7.00 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma200_pct | 1.23 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_sma | 4.65 | USD_per_barrel | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_pct | 5.24 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.drawdown_from_63d_high_pct | -16.15 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.volume_vs_previous20_ratio | 0.82 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.BZ=F.value | 95.82 | USD_per_barrel | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_1d_pct | 3.30 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_5d_pct | -2.51 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_20d_pct | -9.54 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_60d_pct | 4.58 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_1d_pp | 3.65 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_5d_pp | -5.80 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_20d_pp | -7.63 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_60d_pp | 5.89 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma20 | 105.83 | USD_per_barrel | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma50 | 104.26 | USD_per_barrel | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma200 | 93.87 | USD_per_barrel | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma20_pct | -9.46 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma50_pct | -8.09 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma200_pct | 2.08 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_sma | 5.61 | USD_per_barrel | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_pct | 5.86 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.drawdown_from_63d_high_pct | -18.55 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.volume_vs_previous20_ratio | 0.69 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.TLT.value | 79.72 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_1d_pct | -1.48 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_5d_pct | -2.70 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_20d_pct | 0.11 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_60d_pct | -2.81 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_1d_pp | -1.13 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_5d_pp | -5.99 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_20d_pp | 2.01 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_60d_pp | -1.50 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma20 | 80.94 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma50 | 79.87 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma200 | 82.74 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma20_pct | -1.51 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma50_pct | -0.18 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma200_pct | -3.65 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_sma | 0.76 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_pct | 0.95 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.drawdown_from_63d_high_pct | -3.34 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.volume_vs_previous20_ratio | 1.23 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/TLT/history/ |
| prices.UUP.value | 29.42 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_1d_pct | 0.24 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_5d_pct | 1.73 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_20d_pct | 1.45 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_60d_pct | 5.52 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_1d_pp | 0.59 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_5d_pp | -1.56 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_20d_pp | 3.35 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_60d_pp | 6.83 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma20 | 29.03 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma50 | 28.77 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma200 | 28.02 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma20_pct | 1.34 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma50_pct | 2.26 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma200_pct | 5.00 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_sma | 0.13 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_pct | 0.46 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.drawdown_from_63d_high_pct | 0.00 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.volume_vs_previous20_ratio | 0.62 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/UUP/history/ |
| prices.HYG.value | 76.98 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_1d_pct | -0.48 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_5d_pct | -0.39 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_20d_pct | 0.33 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_60d_pct | -1.96 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_1d_pp | -0.12 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_5d_pp | -3.68 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_20d_pp | 2.23 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_60d_pp | -0.65 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma20 | 76.98 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma50 | 77.17 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma200 | 77.49 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma20_pct | 0.00 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma50_pct | -0.24 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma200_pct | -0.66 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_sma | 0.33 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_pct | 0.43 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.drawdown_from_63d_high_pct | -2.21 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.volume_vs_previous20_ratio | 0.86 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/HYG/history/ |
| prices.LQD.value | 103.05 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_1d_pct | -0.88 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_5d_pct | -1.54 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_20d_pct | -0.05 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_60d_pct | -2.10 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_1d_pp | -0.52 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_5d_pp | -4.83 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_20d_pp | 1.85 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_60d_pp | -0.79 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma20 | 103.70 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma50 | 103.21 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma200 | 105.33 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma20_pct | -0.63 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma50_pct | -0.16 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma200_pct | -2.17 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_sma | 0.58 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_pct | 0.56 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.drawdown_from_63d_high_pct | -2.37 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.volume_vs_previous20_ratio | 0.63 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/LQD/history/ |
| prices.^VIX.value | 18.70 | index | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_1d_pct | 6.92 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_5d_pct | -33.64 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_20d_pct | 13.61 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_60d_pct | 16.80 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_1d_pp | 7.27 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_5d_pp | -36.93 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_20d_pp | 15.51 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_60d_pp | 17.27 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma20 | 19.42 | index | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma50 | 17.22 | index | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma200 | 18.44 | index | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma20_pct | -3.69 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma50_pct | 8.61 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma200_pct | 1.42 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_sma | 3.65 | index | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_pct | 19.52 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.drawdown_from_63d_high_pct | -33.64 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-12 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX3M.value | 20.06 | index | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_1d_pct | 4.26 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_5d_pct | -21.49 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_20d_pct | 8.49 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_60d_pct | 8.02 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_1d_pp | 4.62 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_5d_pp | -24.78 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_20d_pp | 10.39 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_60d_pp | 9.33 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma20 | 20.49 | index | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma50 | 19.19 | index | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma200 | 20.60 | index | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma20_pct | -2.12 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma50_pct | 4.53 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma200_pct | -2.63 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_sma | 2.07 | index | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_pct | 10.32 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.drawdown_from_63d_high_pct | -21.49 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-12 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VVIX.value | 96.71 | index | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_1d_pct | 6.90 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_5d_pct | -28.36 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_20d_pct | 4.47 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_60d_pct | 11.76 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_1d_pp | 7.25 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_5d_pp | -31.65 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_20d_pp | 6.37 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_60d_pp | 13.07 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma20 | 103.78 | index | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma50 | 94.97 | index | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma200 | 98.93 | index | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma20_pct | -6.81 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma50_pct | 1.83 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma200_pct | -2.25 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_sma | 14.26 | index | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_pct | 14.74 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.drawdown_from_63d_high_pct | -28.36 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-12 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^MOVE.value | 98.43 | index | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_1d_pct | 6.49 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_5d_pct | 4.85 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_20d_pct | -0.64 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_60d_pct | 30.15 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_1d_pp | 5.53 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_5d_pp | 6.11 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_20d_pp | 0.99 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_60d_pp | 31.92 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma20 | 98.14 | index | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma50 | 94.03 | index | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma200 | 79.01 | index | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma20_pct | 0.30 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma50_pct | 4.68 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma200_pct | 24.57 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_sma | 5.27 | index | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_pct | 5.36 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.drawdown_from_63d_high_pct | -13.35 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-12 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.NVDA.value | 166.19 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_1d_pct | -4.34 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_5d_pct | -8.49 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_20d_pct | -23.50 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_60d_pct | -23.53 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_1d_pp | -3.99 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_5d_pp | -11.78 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_20d_pp | -21.60 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_60d_pp | -22.22 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma20 | 201.25 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma50 | 215.94 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma200 | 204.07 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma20_pct | -17.42 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma50_pct | -23.04 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma200_pct | -18.56 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_sma | 10.66 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_pct | 6.41 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.drawdown_from_63d_high_pct | -30.53 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.volume_vs_previous20_ratio | 4.49 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.MSFT.value | 523.00 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_1d_pct | 0.36 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_5d_pct | -2.41 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_20d_pct | -3.05 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_60d_pct | 8.19 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_1d_pp | 0.71 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_5d_pp | -5.70 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_20d_pp | -1.15 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_60d_pp | 9.50 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma20 | 529.64 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma50 | 518.72 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma200 | 440.03 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma20_pct | -1.25 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma50_pct | 0.82 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma200_pct | 18.86 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_sma | 17.48 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_pct | 3.34 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.drawdown_from_63d_high_pct | -5.90 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.volume_vs_previous20_ratio | 0.70 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.AMZN.value | 267.44 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_1d_pct | 0.48 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_5d_pct | 2.78 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_20d_pct | 4.98 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_60d_pct | 0.60 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_1d_pp | 0.83 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_5d_pp | -0.51 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_20d_pp | 6.88 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_60d_pp | 1.91 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma20 | 256.50 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma50 | 254.66 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma200 | 244.47 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma20_pct | 4.26 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma50_pct | 5.02 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma200_pct | 9.40 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_sma | 10.56 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_pct | 3.95 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.drawdown_from_63d_high_pct | -1.27 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.volume_vs_previous20_ratio | 0.68 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.GOOGL.value | 298.70 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_1d_pct | 1.79 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_5d_pct | 5.71 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_20d_pct | -14.47 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_60d_pct | -13.29 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_1d_pp | 2.14 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_5d_pp | 2.42 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_20d_pp | -12.57 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_60d_pp | -11.99 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma20 | 305.66 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma50 | 329.12 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma200 | 338.41 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma20_pct | -2.28 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma50_pct | -9.24 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma200_pct | -11.73 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_sma | 11.44 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_pct | 3.83 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.drawdown_from_63d_high_pct | -15.85 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.volume_vs_previous20_ratio | 0.88 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.META.value | 623.61 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_1d_pct | -0.82 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_5d_pct | 3.06 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_20d_pct | -15.35 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_60d_pct | 14.30 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_1d_pp | -0.47 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_5d_pp | -0.23 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_20d_pp | -13.45 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_60d_pp | 15.61 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma20 | 640.44 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma50 | 679.07 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma200 | 630.50 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma20_pct | -2.63 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma50_pct | -8.17 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma200_pct | -1.09 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_sma | 20.93 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_pct | 3.36 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.drawdown_from_63d_high_pct | -19.80 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.volume_vs_previous20_ratio | 0.42 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/META/history/ |
| prices.CRWV.value | 56.60 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_1d_pct | -6.86 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_5d_pct | 29.64 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_20d_pct | -18.78 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_60d_pct | -37.71 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_1d_pp | -6.51 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_5d_pp | 26.35 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_20d_pp | -16.88 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_60d_pp | -36.41 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma20 | 55.40 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma50 | 73.22 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma200 | 89.22 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma20_pct | 2.16 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma50_pct | -22.70 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma200_pct | -36.56 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_sma | 6.38 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_pct | 11.27 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.drawdown_from_63d_high_pct | -46.60 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.volume_vs_previous20_ratio | 1.43 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.MU.value | 798.44 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_1d_pct | -1.59 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_5d_pct | 21.64 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_20d_pct | -14.26 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_60d_pct | -14.78 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_1d_pp | -1.23 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_5d_pp | 18.35 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_20d_pp | -12.36 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_60d_pp | -13.48 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma20 | 843.03 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma50 | 947.28 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma200 | 763.70 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma20_pct | -5.29 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma50_pct | -15.71 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma200_pct | 4.55 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_sma | 64.15 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_pct | 8.03 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.drawdown_from_63d_high_pct | -27.23 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.volume_vs_previous20_ratio | 0.86 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MU/history/ |
| prices.DRAM.value | 43.66 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_1d_pct | -2.65 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_5d_pct | 17.97 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_20d_pct | -11.49 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_60d_pct | -20.82 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_1d_pp | -2.30 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_5d_pp | 14.68 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_20d_pp | -9.59 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_60d_pp | -19.51 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma20 | 46.17 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma50 | 53.58 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma200 | 缺失 | USD_per_share | 2026-11-12 | unavailable | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma20_pct | -5.44 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma50_pct | -18.52 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma200_pct | 缺失 | percent | 2026-11-12 | unavailable | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_sma | 3.46 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_pct | 7.93 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.drawdown_from_63d_high_pct | -31.37 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.volume_vs_previous20_ratio | 1.01 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.VRT.value | 209.64 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_1d_pct | 1.52 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_5d_pct | 18.62 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_20d_pct | -2.38 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_60d_pct | -19.66 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_1d_pp | 1.87 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_5d_pp | 15.33 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_20d_pp | -0.48 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_60d_pp | -18.35 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma20 | 209.20 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma50 | 232.64 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma200 | 271.45 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma20_pct | 0.21 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma50_pct | -9.89 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma200_pct | -22.77 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_sma | 19.85 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_pct | 9.47 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.drawdown_from_63d_high_pct | -28.29 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.volume_vs_previous20_ratio | 0.65 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/VRT/history/ |
| prices.XLK.value | 173.77 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_1d_pct | -0.34 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_5d_pct | 7.01 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_20d_pct | -8.15 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_60d_pct | -5.26 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_1d_pp | 0.02 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_5d_pp | 3.72 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_20d_pp | -6.25 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_60d_pp | -3.96 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma20 | 179.32 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma50 | 187.37 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma200 | 170.42 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma20_pct | -3.09 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma50_pct | -7.26 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma200_pct | 1.97 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_sma | 6.09 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_pct | 3.50 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.drawdown_from_63d_high_pct | -13.98 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.volume_vs_previous20_ratio | 0.77 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLE.value | 64.33 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_1d_pct | 1.51 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_5d_pct | 4.38 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_20d_pct | -3.35 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_60d_pct | 1.78 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_1d_pp | 1.87 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_5d_pp | 1.09 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_20d_pp | -1.45 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_60d_pp | 3.09 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma20 | 66.33 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma50 | 64.89 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma200 | 58.86 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma20_pct | -3.02 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma50_pct | -0.87 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma200_pct | 9.29 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_sma | 1.74 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_pct | 2.71 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.drawdown_from_63d_high_pct | -8.13 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.volume_vs_previous20_ratio | 0.69 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLF.value | 58.21 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_1d_pct | -0.72 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_5d_pct | 1.23 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_20d_pct | 5.32 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_60d_pct | 1.63 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_1d_pp | -0.36 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_5d_pp | -2.06 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_20d_pp | 7.22 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_60d_pp | 2.94 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma20 | 56.91 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma50 | 55.92 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma200 | 53.64 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma20_pct | 2.29 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma50_pct | 4.10 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma200_pct | 8.53 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_sma | 1.01 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_pct | 1.73 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.drawdown_from_63d_high_pct | -1.67 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.volume_vs_previous20_ratio | 0.63 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLI.value | 169.44 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_1d_pct | -0.89 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_5d_pct | 4.29 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_20d_pct | 0.92 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_60d_pct | -6.63 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_1d_pp | -0.54 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_5d_pp | 1.00 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_20d_pp | 2.82 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_60d_pp | -5.32 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma20 | 167.77 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma50 | 168.97 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma200 | 172.77 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma20_pct | 0.99 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma50_pct | 0.28 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma200_pct | -1.93 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_sma | 3.34 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_pct | 1.97 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.drawdown_from_63d_high_pct | -8.82 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.volume_vs_previous20_ratio | 0.72 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLV.value | 187.83 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_1d_pct | -0.59 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_5d_pct | 1.58 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_20d_pct | 6.00 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_60d_pct | 7.33 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_1d_pp | -0.24 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_5d_pp | -1.71 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_20d_pp | 7.91 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_60d_pp | 8.63 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma20 | 183.04 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma50 | 174.59 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma200 | 159.12 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma20_pct | 2.62 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma50_pct | 7.58 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma200_pct | 18.05 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_sma | 3.75 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_pct | 2.00 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.drawdown_from_63d_high_pct | -0.96 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.volume_vs_previous20_ratio | 0.68 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLP.value | 91.06 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_1d_pct | -0.43 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_5d_pct | -0.21 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_20d_pct | 5.05 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_60d_pct | 5.92 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_1d_pp | -0.07 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_5d_pp | -3.50 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_20d_pp | 6.95 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_60d_pp | 7.22 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma20 | 89.25 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma50 | 85.39 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma200 | 84.02 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma20_pct | 2.03 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma50_pct | 6.65 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma200_pct | 8.38 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_sma | 1.63 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_pct | 1.80 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.drawdown_from_63d_high_pct | -0.96 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.volume_vs_previous20_ratio | 0.71 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLY.value | 120.46 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_1d_pct | -0.44 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_5d_pct | 2.40 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_20d_pct | 6.22 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_60d_pct | 1.80 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_1d_pp | -0.08 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_5d_pp | -0.89 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_20d_pp | 8.12 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_60d_pp | 3.11 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma20 | 116.96 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma50 | 113.70 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma200 | 115.09 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma20_pct | 2.99 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma50_pct | 5.94 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma200_pct | 4.67 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_sma | 2.60 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_pct | 2.16 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.drawdown_from_63d_high_pct | -1.53 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.volume_vs_previous20_ratio | 0.93 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLC.value | 107.56 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_1d_pct | -0.96 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_5d_pct | 3.09 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_20d_pct | -4.34 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_60d_pct | -3.06 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_1d_pp | -0.60 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_5d_pp | -0.20 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_20d_pp | -2.44 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_60d_pp | -1.75 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma20 | 105.56 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma50 | 109.40 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma200 | 111.91 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma20_pct | 1.89 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma50_pct | -1.68 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma200_pct | -3.89 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_sma | 2.18 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_pct | 2.02 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.drawdown_from_63d_high_pct | -6.27 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.volume_vs_previous20_ratio | 0.54 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLU.value | 43.81 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_1d_pct | -0.02 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_5d_pct | 1.18 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_20d_pct | 5.19 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_60d_pct | 0.25 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_1d_pp | 0.33 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_5d_pp | -2.11 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_20d_pp | 7.09 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_60d_pp | 1.56 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma20 | 42.98 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma50 | 41.80 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma200 | 43.87 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma20_pct | 1.93 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma50_pct | 4.80 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma200_pct | -0.13 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_sma | 0.60 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_pct | 1.37 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.drawdown_from_63d_high_pct | -0.11 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.volume_vs_previous20_ratio | 0.63 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLRE.value | 44.36 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_1d_pct | -0.52 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_5d_pct | 0.14 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_20d_pct | 5.64 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_60d_pct | -0.57 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_1d_pp | -0.16 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_5d_pp | -3.16 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_20d_pp | 7.54 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_60d_pp | 0.74 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma20 | 43.29 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma50 | 42.51 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma200 | 42.95 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma20_pct | 2.46 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma50_pct | 4.35 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma200_pct | 3.29 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_sma | 0.70 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_pct | 1.57 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.drawdown_from_63d_high_pct | -1.68 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.volume_vs_previous20_ratio | 0.68 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLB.value | 52.34 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_1d_pct | -1.28 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_5d_pct | 0.02 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_20d_pct | 3.52 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_60d_pct | 0.12 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_1d_pp | -0.93 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_5d_pp | -3.27 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_20d_pp | 5.42 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_60d_pp | 1.42 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma20 | 52.16 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma50 | 50.88 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma200 | 50.91 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma20_pct | 0.34 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma50_pct | 2.87 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma200_pct | 2.81 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_sma | 1.00 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_pct | 1.92 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.drawdown_from_63d_high_pct | -2.89 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.volume_vs_previous20_ratio | 0.77 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLB/history/ |
| prices.SMH.value | 501.73 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_1d_pct | -1.03 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_5d_pct | 12.06 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_20d_pct | -10.22 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_60d_pct | -10.55 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_1d_pp | -0.68 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_5d_pp | 8.77 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_20d_pp | -8.32 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_60d_pp | -9.24 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma20 | 520.79 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma50 | 561.12 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma200 | 523.54 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma20_pct | -3.66 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma50_pct | -10.58 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma200_pct | -4.17 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_sma | 26.50 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_pct | 5.28 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.drawdown_from_63d_high_pct | -20.85 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.volume_vs_previous20_ratio | 0.83 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SMH/history/ |
| prices.IGV.value | 101.45 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_1d_pct | -0.76 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_5d_pct | 2.46 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_20d_pct | -7.44 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_60d_pct | -1.32 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_1d_pp | -0.41 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_5d_pp | -0.83 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_20d_pp | -5.54 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_60d_pp | -0.01 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma20 | 105.21 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma50 | 106.23 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma200 | 94.12 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma20_pct | -3.57 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma50_pct | -4.50 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma200_pct | 7.79 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_sma | 3.09 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_pct | 3.05 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.drawdown_from_63d_high_pct | -9.96 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.volume_vs_previous20_ratio | 0.55 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IGV/history/ |
| prices.XOP.value | 183.11 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_1d_pct | 1.65 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_5d_pct | 5.18 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_20d_pct | -6.04 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_60d_pct | -1.34 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_1d_pp | 2.00 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_5d_pp | 1.88 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_20d_pp | -4.14 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_60d_pp | -0.03 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma20 | 191.56 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma50 | 190.24 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma200 | 171.76 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma20_pct | -4.41 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma50_pct | -3.75 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma200_pct | 6.61 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_sma | 6.09 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_pct | 3.33 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.drawdown_from_63d_high_pct | -10.62 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.volume_vs_previous20_ratio | 0.98 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XOP/history/ |
| prices.OIH.value | 369.14 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_1d_pct | -0.11 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_5d_pct | 6.18 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_20d_pct | -1.98 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_60d_pct | -11.83 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_1d_pp | 0.25 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_5d_pp | 2.89 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_20d_pp | -0.08 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_60d_pp | -10.53 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma20 | 383.13 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma50 | 392.00 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma200 | 398.96 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma20_pct | -3.65 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma50_pct | -5.83 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma200_pct | -7.47 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_sma | 13.09 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_pct | 3.54 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.drawdown_from_63d_high_pct | -15.45 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.volume_vs_previous20_ratio | 0.42 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/OIH/history/ |
| prices.ITA.value | 71.73 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_1d_pct | -2.06 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_5d_pct | 5.31 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_20d_pct | 4.00 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_60d_pct | -12.48 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_1d_pp | -1.71 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_5d_pp | 2.02 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_20d_pp | 5.90 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_60d_pp | -11.17 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma20 | 70.04 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma50 | 70.47 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma200 | 75.85 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma20_pct | 2.41 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma50_pct | 1.79 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma200_pct | -5.43 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_sma | 2.04 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_pct | 2.85 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.drawdown_from_63d_high_pct | -14.56 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.volume_vs_previous20_ratio | 1.49 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ARKX.value | 29.83 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_1d_pct | -1.68 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_5d_pct | 10.30 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_20d_pct | -2.29 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_60d_pct | -11.33 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_1d_pp | -1.33 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_5d_pp | 7.01 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_20d_pp | -0.39 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_60d_pp | -10.02 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma20 | 29.83 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma50 | 31.20 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma200 | 32.27 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma20_pct | 0.00 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma50_pct | -4.40 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma200_pct | -7.57 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_sma | 1.03 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_pct | 3.44 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.drawdown_from_63d_high_pct | -14.03 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.volume_vs_previous20_ratio | 0.69 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.KRE.value | 72.52 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_1d_pct | -0.59 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_5d_pct | 0.29 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_20d_pct | 3.97 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_60d_pct | -2.76 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_1d_pp | -0.24 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_5d_pp | -3.00 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_20d_pp | 5.87 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_60d_pp | -1.45 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma20 | 72.24 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma50 | 71.67 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma200 | 70.61 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma20_pct | 0.39 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma50_pct | 1.18 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma200_pct | 2.70 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_sma | 1.54 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_pct | 2.12 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.drawdown_from_63d_high_pct | -5.76 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.volume_vs_previous20_ratio | 0.67 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/KRE/history/ |
| prices.SKYY.value | 154.19 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_1d_pct | -0.07 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_5d_pct | 4.77 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_20d_pct | -7.46 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_60d_pct | -4.33 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_1d_pp | 0.28 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_5d_pp | 1.48 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_20d_pp | -5.56 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_60d_pp | -3.02 | pp | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma20 | 159.60 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma50 | 163.08 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma200 | 137.77 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma20_pct | -3.39 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma50_pct | -5.45 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma200_pct | 11.92 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_sma | 5.40 | USD_per_share | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_pct | 3.50 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.drawdown_from_63d_high_pct | -11.84 | percent | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.volume_vs_previous20_ratio | 0.31 | ratio | 2026-11-12 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SKYY/history/ |
| macro.DGS2.value | 4.73 | percent | 2026-11-10 | lagged | source_series_v1:DGS2 | https://fred.stlouisfed.org/series/DGS2 |
| macro.BAMLH0A0HYM2.value | 3.30 | percentage_points | 2026-11-11 | lagged | source_series_v1:BAMLH0A0HYM2 | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| macro.BAMLC0A0CM.value | 0.90 | percentage_points | 2026-11-11 | lagged | source_series_v1:BAMLC0A0CM | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| macro.DGS10.value | 4.98 | percent | 2026-11-10 | lagged | source_series_v1:DGS10 | https://fred.stlouisfed.org/series/DGS10 |
| macro.DFII10.value | 2.78 | percent | 2026-11-10 | lagged | source_series_v1:DFII10 | https://fred.stlouisfed.org/series/DFII10 |
| macro.T10YIE.value | 2.24 | percent | 2026-11-12 | ok | source_series_v1:T10YIE | https://fred.stlouisfed.org/series/T10YIE |
| macro.STLFSI4.value | -0.49 | index | 2026-11-06 | lagged | source_series_v1:STLFSI4 | https://fred.stlouisfed.org/series/STLFSI4 |
| macro.CBOE_VIX.value | 18.70 | index | 2026-11-12 | ok | source_series_v1:CBOE_VIX | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| macro.GPRD.value | 113.95 | index | 2026-11-02 | lagged | source_series_v1:GPRD | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_ACT.value | 129.82 | index | 2026-11-02 | lagged | source_series_v1:GPRD_ACT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_THREAT.value | 108.29 | index | 2026-11-02 | lagged | source_series_v1:GPRD_THREAT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA7.value | 158.85 | index | 2026-11-02 | lagged | source_series_v1:GPRD_MA7 | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA30.value | 184.74 | index | 2026-11-02 | lagged | source_series_v1:GPRD_MA30 | https://www.matteoiacoviello.com/gpr.htm |
| quotes.SPY.value | 759.40 | USD_per_share | 2026-11-13T12:01:49+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SPY |
| quotes.QQQ.value | 690.21 | USD_per_share | 2026-11-13T12:02:25+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| quotes.SMH.value | 505.00 | USD_per_share | 2026-11-13T12:01:52+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SMH |
| quotes.NVDA.value | 169.60 | USD_per_share | 2026-11-13T12:02:30+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| quotes.MSFT.value | 515.02 | USD_per_share | 2026-11-13T12:02:25+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/MSFT |
| quotes.AMZN.value | 270.28 | USD_per_share | 2026-11-13T12:01:49+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AMZN |
| quotes.GOOGL.value | 302.34 | USD_per_share | 2026-11-13T12:02:26+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GOOGL |
| quotes.META.value | 623.99 | USD_per_share | 2026-11-13T12:02:01+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/META |
| observed.SPY.price | 759.40 | USD | 2026-11-13T12:01:49+00:00 | ok | 各自最后非空分钟close；不是VWAP/官方结算，不假定端点一致。 | https://query1.finance.yahoo.com/v8/finance/chart/SPY |
| observed.QQQ.price | 690.21 | USD | 2026-11-13T12:02:25+00:00 | ok | 各自最后非空分钟close；不是VWAP/官方结算，不假定端点一致。 | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| observed.SMH.price | 505.00 | USD | 2026-11-13T12:01:52+00:00 | ok | 各自最后非空分钟close；不是VWAP/官方结算，不假定端点一致。 | https://query1.finance.yahoo.com/v8/finance/chart/SMH |
| observed.NVDA.price | 169.60 | USD | 2026-11-13T12:02:30+00:00 | ok | 各自最后非空分钟close；不是VWAP/官方结算，不假定端点一致。 | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| observed.MSFT.price | 515.02 | USD | 2026-11-13T12:02:25+00:00 | ok | 各自最后非空分钟close；不是VWAP/官方结算，不假定端点一致。 | https://query1.finance.yahoo.com/v8/finance/chart/MSFT |
| observed.AMZN.price | 270.28 | USD | 2026-11-13T12:01:49+00:00 | ok | 各自最后非空分钟close；不是VWAP/官方结算，不假定端点一致。 | https://query1.finance.yahoo.com/v8/finance/chart/AMZN |
| observed.GOOGL.price | 302.34 | USD | 2026-11-13T12:02:26+00:00 | ok | 各自最后非空分钟close；不是VWAP/官方结算，不假定端点一致。 | https://query1.finance.yahoo.com/v8/finance/chart/GOOGL |
| observed.META.price | 623.99 | USD | 2026-11-13T12:02:01+00:00 | ok | 各自最后非空分钟close；不是VWAP/官方结算，不假定端点一致。 | https://query1.finance.yahoo.com/v8/finance/chart/META |
| observed.CRWV.price | 56.75 | USD | 2026-11-13T12:02:26+00:00 | ok | 各自最后非空分钟close；不是VWAP/官方结算，不假定端点一致。 | https://query1.finance.yahoo.com/v8/finance/chart/CRWV |
| observed.MU.price | 805.05 | USD | 2026-11-13T12:02:31+00:00 | ok | 各自最后非空分钟close；不是VWAP/官方结算，不假定端点一致。 | https://query1.finance.yahoo.com/v8/finance/chart/MU |
| observed.DRAM.price | 43.72 | USD | 2026-11-13T12:00:45+00:00 | ok | 各自最后非空分钟close；不是VWAP/官方结算，不假定端点一致。 | https://query1.finance.yahoo.com/v8/finance/chart/DRAM |
| observed.SNDK.price | 943.10 | USD | 2026-11-13T12:02:36+00:00 | ok | 各自最后非空分钟close；不是VWAP/官方结算，不假定端点一致。 | https://query1.finance.yahoo.com/v8/finance/chart/SNDK |
| observed.NBIS.price | 127.50 | USD | 2026-11-13T12:02:03+00:00 | ok | 各自最后非空分钟close；不是VWAP/官方结算，不假定端点一致。 | https://query1.finance.yahoo.com/v8/finance/chart/NBIS |
| observed.CSCO.price | 99.06 | USD | 2026-11-13T12:02:24+00:00 | ok | 各自最后非空分钟close；不是VWAP/官方结算，不假定端点一致。 | https://query1.finance.yahoo.com/v8/finance/chart/CSCO |
| observed.AMAT.price | 384.00 | USD | 2026-11-13T12:02:10+00:00 | ok | 各自最后非空分钟close；不是VWAP/官方结算，不假定端点一致。 | https://query1.finance.yahoo.com/v8/finance/chart/AMAT |
| observed.CBRS.price | 113.00 | USD | 2026-11-13T12:02:25+00:00 | ok | 各自最后非空分钟close；不是VWAP/官方结算，不假定端点一致。 | https://query1.finance.yahoo.com/v8/finance/chart/CBRS |
| observed.GLD.price | 356.85 | USD | 2026-11-13T12:02:17+00:00 | ok | 各自最后非空分钟close；不是VWAP/官方结算，不假定端点一致。 | https://query1.finance.yahoo.com/v8/finance/chart/GLD |
| observed.TLT.price | 79.55 | USD | 2026-11-13T12:00:50+00:00 | ok | 各自最后非空分钟close；不是VWAP/官方结算，不假定端点一致。 | https://query1.finance.yahoo.com/v8/finance/chart/TLT |
| observed.CL_F.price | 88.42 | USD | 2026-11-13T11:52:30+00:00 | ok | 各自最后非空分钟close；不是VWAP/官方结算，不假定端点一致。 | https://query1.finance.yahoo.com/v8/finance/chart/CL=F |
| observed.BZ_F.price | 95.95 | USD | 2026-11-13T11:51:58+00:00 | ok | 各自最后非空分钟close；不是VWAP/官方结算，不假定端点一致。 | https://query1.finance.yahoo.com/v8/finance/chart/BZ=F |
| observed.GC_F.price | 3,896.40 | USD | 2026-11-13T11:52:27+00:00 | ok | 各自最后非空分钟close；不是VWAP/官方结算，不假定端点一致。 | https://query1.finance.yahoo.com/v8/finance/chart/GC=F |
| observed.DX-Y.NYB.price | 103.22 | index points | 2026-11-13T11:52:40+00:00 | ok | 各自最后非空分钟close；不是VWAP/官方结算，不假定端点一致。 | https://query1.finance.yahoo.com/v8/finance/chart/DX-Y.NYB |
| observed.VIX.price | 18.32 | index points | 2026-11-13T11:47:31+00:00 | ok | 各自最后非空分钟close；不是VWAP/官方结算，不假定端点一致。 | https://query1.finance.yahoo.com/v8/finance/chart/^VIX |
| observed.Treasury2Y.value | 4.86 | percent | 2026-11-12T15:30:00-05:00 | ok | 财政部平价曲线指示报价插值，非今天实时成交 | https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value_month=202611&type=daily_treasury_yield_curve |
| observed.Treasury10Y.value | 5.10 | percent | 2026-11-12T15:30:00-05:00 | ok | 财政部平价曲线指示报价插值，非今天实时成交 | https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value_month=202611&type=daily_treasury_yield_curve |
| observed.CNN.value | 39 | index points | 2026-11-13T11:47:46+00:00 | ok | CNN Fear & Greed，官方页面39 Fear；不是tc温度 | https://edition.cnn.com/markets/fear-and-greed |

## 指标历史比较（不同日期观测，非连续交易日）

```json
[
  {
    "id": "prices.SPY.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.69000244140625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 24.1199951171875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.6728455226830752,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 4.055139171659306,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 4.203458777787472,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 8.016590181137463,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.6286873752887612,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.3878171375484323,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.5584165435409072,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.5683347176982076,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.7334991455078352,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -6.0619995117187955,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.12289306640627728,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.4022387695313228,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.3354452514648756,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.5990478515624318,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.2576652461310336,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.9401946284944422,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.33592153481828424,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.3308822568355323,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.4169887362970526,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.0876573704015975,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.29214041573660765,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.4742867606026788,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.04426920814037927,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.1470359682048621,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.3452749167209279,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.0959188650558906,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.01976458046790852,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.294996144214653,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.21002197265625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 41.1199951171875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.635013132549835,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 6.16879483085463,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 6.581891176557986,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 15.901509569695127,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.179983043467991,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 7.976237663684693,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.1165994762514111,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 6.700777197578267,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.9621676098667598,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.1136556591953237,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 2.3784323987705136,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 7.884919388557665,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.4487043318207702,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 4.58842052613626,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.4418170672894961,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.1324424798800594,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.9915008544921875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -15.453503417968705,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.4066345214843068,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -3.574053955078057,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.2854962158203307,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.3305215454101926,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.03485195171818445,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 7.913973574175214,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.25325035922827377,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 6.16915669815692,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.36708181944640206,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 5.852696044996875,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.4707118443080347,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.7442888532366077,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.07663105724821362,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.10183514649207348,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.2909225246537801,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 5.412947446339134,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.14162290424512802,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.273962098819067,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -4.649993896484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 7.459991455078125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.537164073766407,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.948633382983301,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 3.080406597343599,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 7.340833470842634,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -3.0973585460058795,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.5956431772822706,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.012034917103544,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.7734401608138555,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.8643185510833318,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.1065057886760048,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.1230521804438731,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.6757567102948281,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.4686711707171183,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.20782603973383829,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.4536183735626365,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.7948945568843522,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.16800079345699714,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.9150009155273438,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.29608215332029886,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.4388012695312113,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.0845710754394986,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.40309432983400484,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.7340996341398185,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.3614109866061828,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.5487131833155088,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.1459316350905038,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.7011706723381037,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.53848117021086,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.12357003348214324,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.7771388462611606,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.075249307241809,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.23382865425717858,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.2181539665082628,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.7615286116344553,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.233090204918454,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.1726389085407036,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.92999267578125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.850006103515625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.6681631864126745,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.025755384965744,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 2.079745627580587,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.2159062876547018,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.318551592075768,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.3005279320154264,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.9163351016846186,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.3012451454814111,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.004682336270400711,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.029383786693562,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.123713150206885,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -4.800683893482761,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.689864216787007,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -3.087289205533006,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.3579185581437114,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.2670895722167965,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.2860000610351392,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.7315002441406193,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.05877258300782273,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.15281707763674035,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.124016189575201,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.5907408142089707,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.0178915164749114,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.9693508145538043,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.9269497191351839,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.7206142907855382,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.9938385860091659,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.556493377694168,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.01714324951171875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.2999986921037947,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.003950334669383659,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.11447202366788001,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.8641887162304518,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.7239090457842332,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.14775453404068606,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.0303218095148057,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -10.279998779296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -20.5999755859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.6807396909980565,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -3.6205175330905615,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -3.5210111336091643,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -7.363680368467684,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -4.391475760506736,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -6.442518088940307,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -5.8692768024771755,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -6.97652348140011,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.007894168314981354,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -7.675656704749867,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -7.7244699113966355,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -15.380270549605147,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -3.7627883852179744,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -9.830335226488739,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -5.310860258936268,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -10.544858199098318,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.3909988403320312,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -3.28149871826173,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.9577996826171784,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -3.959400634765643,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.6983499145507608,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.518400115966813,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.4081149455356337,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -4.674279995518449,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.4520042941063362,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -4.3842746036383495,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.3606166756230724,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -4.473692863311495,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.5242854527064731,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.2135707310267856,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.2043237330927976,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.44158848605499057,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.4014760677944054,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -4.812291268595038,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.892045609499702,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.12087189630511697,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -115.199951171875,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -228.199951171875,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.1427038948694466,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -3.873991881158778,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -3.7675712946579893,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -7.584101867582393,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -4.215101209375794,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -5.783145730997086,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -5.017252095280856,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -6.596594153710723,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.4698583721863714,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -7.929131052818084,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -7.971030072445462,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -15.600692048719857,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -3.586413834087032,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -9.17096286854552,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -4.45883555173995,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -10.164928871408932,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -14.240002441406432,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -37.839990234375364,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -10.5860009765629,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -47.61999999999989,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -7.091500244140661,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -26.282001953125473,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.4983817546418203,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -4.694432178043672,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.5063077109832026,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -4.339517156169892,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.4306042834266286,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -4.558765386042918,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 5.564296177455361,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 14.892892020089292,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.21176100192923863,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.502048842643521,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.4522107361179444,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -4.85759207840605,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.3548676738787272,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.6786353601534757,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 2.2099990844726562,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.779998779296875,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.9845264148395492,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.16952528932365762,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.16205284602560655,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 9.28849026591675,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.4192588263210233,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -8.361028192370712,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.5185130164327099,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -5.316199145482203,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 3.6573719375226243,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -4.2246644609829636,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -4.365511623813079,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.2719000847792863,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.20942854896773788,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -11.748845329919146,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 2.076929559973617,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -8.884533863180412,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.4615001678466797,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.689999771118167,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.045400085449216476,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.10139984130859148,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.12764999389648324,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.6616499900817843,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 2.7210340825054136,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.22829442200638184,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 2.3591508517207265,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.966309489648821,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 2.377110551317718,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.8158502064626,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.075714111328125,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.5821424211774557,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.2212704419505549,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.5401159874175141,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 2.0882538469579437,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.6819415557966622,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.16691278662527975,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.7850096836499968,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 3.05999755859375,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.470001220703125,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.9106984445786734,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.5798375402082501,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.5472146807141476,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 11.928180109729213,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 3.004570416459428,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -3.7913488305797003,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 2.6724745926341553,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -5.878873796876639,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 3.5835439672617486,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -4.634976711867556,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -4.75067345850162,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.9115899285917513,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 3.633257791748189,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -7.179165968128133,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 3.2308911361750625,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -9.447208514574847,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.5049999237060518,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.9040000915527315,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.0038000488281255684,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.22360015869141137,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.13709999084473168,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.6973000335693342,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 3.307548939423466,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.14642787454040018,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 2.9318542756320625,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.5718191009952545,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 3.1153177958381018,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -3.4149769199124824,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.02642822265625,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.08357075282505644,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.16479424237068763,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.23226478064525224,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 2.601154007539897,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.09962702611206,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.3306495039368762,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.0191568692274406,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.1999969482421875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.2099990844726562,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.5323994996645163,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.690865772880168,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.6700214174996453,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -3.2373700647528203,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.8979672304354276,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -5.10687734283648,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -3.105920758361136,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.974564087869558,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.1404460230185589,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -5.746004944539473,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -5.873480195287117,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -11.253960245890283,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.2692798551466664,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -8.494694480384911,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.5475042148202287,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -6.5428988055677655,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.004257965087901994,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.4203716278076257,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.03118362426758381,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.517521057128917,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.022862625122073155,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.7217981719970652,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.4878471329106913,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -3.258905005504198,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.4629698235084088,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.106682376067426,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.4233254756268132,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.8146717559352377,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.048015132183199416,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.010081606072216531,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.07348579053348336,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.013431864793010062,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.4550580627244125,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.8665387228915309,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.5560137396228771,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.10451821394167116,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.06999969482421875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.5,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.44760916384272154,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.16929407178774003,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.17181123991847347,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.142133343396535,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.6584425550698603,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.655313623047061,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.2237437892180347,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.9704873485002503,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.2252363588403536,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -3.885845099871566,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -4.031647537868999,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -5.874456837740928,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.2871299303586214,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.7325035145013707,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.7821603327589415,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.5978473691979573,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.021000003814698687,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.0364998817443869,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.02499999999999858,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.106399955749513,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.013950004577637287,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.06039999961853226,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.16793297439190447,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.5968419690755242,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.154580668303117,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.3647493216118578,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.197655847187983,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.561570480360519,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.002857208251953125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.03428609030587333,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.008646332436181459,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.11066344568992842,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.0,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.7209031600505234,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.14213086145189036,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.6438957658545923,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.3699951171875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.29999542236328125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.698600824905049,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.16874410013121288,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.16889694738405625,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.0014913134135374762,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.9021780442076466,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.1436121393122658,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.6942025895078974,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.43892781150481897,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.9742446977780261,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -4.223883271790519,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -4.372355725171529,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -8.018081494551,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.2734906689188854,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -3.2442049982361665,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.13578604596699018,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -3.1294069061933887,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.012472534179678973,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.1848556518554716,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.027433471679685795,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.6628338623046801,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.0007068252563584565,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.6964857864379894,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.49692983736742136,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.14921109960892576,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.44384411310930405,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.464109267119428,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.47656185358092573,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.5012390718742266,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.009374332311608669,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.0029756193915103646,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.014188413799242072,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.0055295586197349755,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.46999912873387784,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.5598922179330224,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.5984666301167183,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.5259688911013269,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.9099960327148438,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.6100006103515625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.9523465610426385,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.0284464117506165,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.0215677840906823,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.9605012511552777,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.7076448349960138,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.1885677413485904,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.5456828782140608,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.14073533873561,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.7204989616404367,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -5.083585583409922,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -5.225026561878154,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -9.97709143229274,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.0789574597072527,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -5.576384878897023,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.9872663346731536,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -4.709070056433818,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.00264739990234375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.10050506591795738,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.028899230957023292,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.6642343139648403,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.016788711547846447,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.8597919845581004,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.8749597786716912,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.650450266956649,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.8534891090702934,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.9114802378258902,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.8481841571400417,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.7240084792832335,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.031560156014298846,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.029995529672614096,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.035284690518492035,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.02000174452775505,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.8621499094914276,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.7205854077304341,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.3791012328286795,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.0336224719376998,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.210000991821289,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -9.479999542236328,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 17.041571610310534,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -62.73858408104216,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -38.93888606580907,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -97.47808187732144,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 9.933602938364093,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -69.25951171462097,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.6593773870031896,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -75.81590714026552,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 18.71441713299361,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -66.79372325270147,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -43.14234484359655,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -105.4946720584589,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 10.562290313652856,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -72.64732885216941,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.1447484151903566,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -80.87938664299125,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.11200008392333771,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.127999925613402,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.08760002136230582,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.5199999809265137,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.006300001144406764,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.09019999504089427,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 5.709340598580614,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -57.777790834405295,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 6.508154530465582,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -60.15621138227309,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 6.529887349253138,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -52.16504941587994,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.01214299883161285,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.43928595951625304,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.2809243019243013,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 8.125124610509786,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 4.293828881183693,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -33.640878068035896,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.8199996948242188,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -5.489999771118164,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 11.044896815310878,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -31.642304049709022,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -23.82770805687481,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -53.39227767943863,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 6.096190019850511,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -32.8252933458908,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 8.179378997119157,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -29.860809346411912,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 12.717742337993954,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -35.69744322136833,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -28.03116683466228,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -61.408867860576095,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 6.724877395139272,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -36.21311048343923,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 8.737795540660063,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -33.42914406411012,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.07849998474121378,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.7224999427795424,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.04659999847412166,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.33520000457763643,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.0038000011444090376,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.049500007629394105,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 3.6400257142727654,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -31.34234339219614,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 4.028997113205257,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -30.975647688702672,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 3.9631000653190696,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -26.94751381264221,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.012857028416224825,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.27857140132359115,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.5067689673833264,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.3083458010320586,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 3.2093922477884114,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -21.48727958924891,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 6.239997863769531,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -38.280006408691406,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 13.272139480740975,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -42.41139324486849,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -28.424021353412545,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -66.08850611040417,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 8.686155979469302,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -49.52040830330193,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 14.34896553193886,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -40.76637325228971,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 14.94498500342405,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -46.4665324165278,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -32.627480131200016,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -74.10509629154163,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 9.314843354758061,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -52.908225440850366,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 14.907382075479767,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -44.33470796998792,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.20699996948242472,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.0485004425048885,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.20919998168945142,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.417200012207033,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.018749999999997158,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.023799972534177982,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 5.838599576150871,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -40.823078226538044,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 6.3601750154341214,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -42.46060374757651,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 6.3245539135162065,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -38.725260466540426,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.14071437290736633,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.9085715157645087,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.172502499616476,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 4.854225310313302,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 4.622562863800702,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -28.357659716244633,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-12",
        "change": 6.0,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-12",
        "change": 4.5500030517578125,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-12",
        "change": -1.0103418744630277,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-12",
        "change": 12.583230317384253,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-12",
        "change": 12.388879592064306,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-12",
        "change": 5.555241977142689,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-12",
        "change": 7.9306447483395655,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-12",
        "change": 10.12448085776192,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-12",
        "change": -2.693121178978128,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-12",
        "change": 5.736490822223207,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-12",
        "change": -2.3384619206779256,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-12",
        "change": 13.27488238803073,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-12",
        "change": 13.065297101813,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-12",
        "change": 6.106769821674174,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-12",
        "change": 5.941767038675671,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-12",
        "change": 10.169898415041157,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-12",
        "change": -4.087227106572133,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-12",
        "change": 6.947363798074967,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-12",
        "change": -0.03149986267089844,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-12",
        "change": -1.7174995422363395,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-12",
        "change": 0.46220001220703466,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-12",
        "change": 2.2003999328613304,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-12",
        "change": 0.21329999923706566,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-12",
        "change": 0.8638999938964815,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-12",
        "change": 6.144029179344623,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-12",
        "change": 6.281649692261726,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-12",
        "change": 5.8956273464198405,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-12",
        "change": 2.4465296451843477,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-12",
        "change": 7.276908555187767,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-12",
        "change": 4.445041338249457,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-12",
        "change": -0.34714235578264496,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-12",
        "change": 0.8428568158830911,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-12",
        "change": -0.7234091792094253,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-12",
        "change": 0.6381006610041036,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-12",
        "change": 5.281690211788904,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-12",
        "change": 4.00528443034648,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -7.5399932861328125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -15.410003662109375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -7.205832625626252,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 4.918916662382676,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 4.705745275431028,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 6.519462415955346,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.0001210821805415,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.287921470186884,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.6764827732917453,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -4.65595525414302,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -5.532987102943177,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.8637774907233702,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.5022864976435546,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.4971277651821175,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.3714337068917821,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -5.675738607735319,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.1180662297508377,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -8.224289971841229,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.5519996643066634,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -12.426500701904303,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.159383544921866,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -4.6560281372070165,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.12441444396972656,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.31353904724119275,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.6655969934725405,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.4094392346934335,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -3.062075506577866,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -5.361252282996585,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -3.643002446176725,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -7.414950124910758,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.5185699462890625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.198568071637834,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.1525030108990526,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.305663408639001,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -3.151644003096397,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -6.441231946280688,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 2.458034025082387,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.5581250083407738,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.8699951171875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -12.92999267578125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 2.615187144153397,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.933860855033444,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 3.8252252245790874,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -3.504787340335036,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.6941796843721981,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -5.5963525539270425,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.21303113181661004,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.8466486947340535,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 4.288032666836472,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.12127831662586175,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.3782335532083847,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -11.521377521472498,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.06549230908343695,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -8.984169691475474,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.3453854117242958,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -4.414983412432262,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.8220001220703352,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.9860046386719432,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.5235998535156341,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.587198486328134,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.22203216552730964,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.5915611267089957,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.5055329774947714,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.0632568711500543,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.25898903498446924,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -3.0105562067719083,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.3651842163468153,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -3.380587921169333,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.0292881556919653,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.057146344866071,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.017612814056725767,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.46447901852050544,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.33645109000687334,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.3263751277010742,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.4075232331168449,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.0570476954087562,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.269989013671875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 7.230010986328125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 2.2122774933289513,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.6648604714510027,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 2.725898200537036,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -3.9567750591890327,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.2188883378818618,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.5565510491692978,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.9882266910024926,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.247036958446048,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 3.8851230160120265,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.3902787002083032,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.4775605772504363,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -11.973365240326494,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.847575713170623,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.8312660883791345,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.4298101474615854,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.32129775925215975,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.6340003967285384,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.0665008544922046,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.2492001342773449,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.7670001220703,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.1221500396728743,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.6555000305176009,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.23799493138396688,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.9947665393016178,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.3963249382900935,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.530435656731922,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.4650576901078516,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.671252541976844,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.24999891008649655,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.22143009730747742,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.07508336252877301,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.024622284964640695,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.46885555305689053,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 5.163287579148246,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.06672148372271125,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.1881148400058361,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 5.25,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 16.1300048828125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.3231273741762797,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.990281290598119,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 4.143922083322749,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 6.148741615458486,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.1214424035613675,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 4.402810711689131,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.3952688954625074,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 4.400435249453537,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.3497181485067955,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.06485788106118706,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.05953669446472354,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.867848565678976,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.7501297788501287,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.0149935741406981,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.9536854390034133,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.8321005317553283,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.525999450683628,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -15.12799987792971,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.764068603515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -4.903575439453107,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.18328811645505994,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.0330128479004088,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 2.504514924161339,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 9.63686193771014,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.8017043520969676,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 6.161445930683785,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.5983178429803004,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 5.02053453358684,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.3399985177176337,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.27642386300223265,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.04736839945771587,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.12071784835829691,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.4789982201160132,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 5.061017313456718,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.24358965448483105,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.5693555631522967,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -5.1600341796875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 18.52996826171875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.1469455583859478,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.1348975922492417,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 3.2576346344856066,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 6.175190556220289,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.6055162073835056,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.7116778781139139,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.4460169059808514,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 9.684233533172272,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 2.819791081069023,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.9202415794100642,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.9458241433018655,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.8413996249171731,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.02317116790525553,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.6761392594345192,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.8876003624399438,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 6.115898815474063,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -5.6554992675780795,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -27.654995727539017,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.6245507812500364,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 5.094427490234352,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.21701385498045056,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.8331680297851562,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.05367689982741508,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 6.8040813817640595,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.8451006097278562,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.0552020761591017,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.7840936827838485,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.06559509867429,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.29856654575892705,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.537854875837052,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.019941794231861376,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.5222034181657635,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.6635931533940038,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.3829997327322836,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.2147476104720762,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.747628153562643,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -4.170001983642578,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 12.939998626708984,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -31.56951611721146,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.9687037286740825,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 4.132114694938149,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 57.7579670048299,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -11.166893364401165,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 27.69879456507925,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.938079805020976,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 21.75953712347183,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -29.896670594528384,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.0864354429852234,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.07134408284932192,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 49.741376823692434,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -10.538205989112406,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 24.310977427530815,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.3796632614800686,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 18.191202405773623,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.6545001983642535,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -5.707000160217284,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.4866000366210841,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -3.1444001007079976,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.2470999908447169,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.1823999977111725,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -6.246084641519278,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 30.716101337913813,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -5.1469674115068855,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 20.12672394666082,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -4.485757689688832,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 15.143643954779371,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.6071428571428577,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.563357489449638,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.772740253987772,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.0512522101540913,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -3.9339641355118715,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 12.868982344063163,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.7931103931394738,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.11703919554071573,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -12.8599853515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 142.04998779296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -13.471581509186969,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 15.873987478694385,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 19.620295190791804,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 51.38410298632898,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -3.0116057610242386,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 22.361576238241387,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.0365651702001326,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 13.17578849628679,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -11.798735986503893,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 11.81884830703508,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 15.416836413004333,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 43.367512805191524,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.3829183857354774,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 18.973759100692952,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.478148626659225,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 9.607453778588582,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -6.6399993896484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -52.90662536621096,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -3.149791259765607,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -19.155155029296907,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.8173872375488145,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 8.638222045898488,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.7733818253244262,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 21.447856941696998,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.0737325004653417,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 16.368899963027395,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.9373047960356216,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 17.61689018307703,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.8092825753348265,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 6.753570556640632,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.2270998770196906,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.7097621746839273,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.172054571645873,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 12.946386255001439,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.3023166191323454,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.9874708667970746,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.1899986267089844,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 6.650001525878906,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -13.012535639860822,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 15.30282635564133,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 18.544495266862295,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 46.45121669383092,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.9435627907667268,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 23.49631884887391,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.2171896425782087,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 11.643774779688211,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -11.339690117177746,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 11.247687183982023,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 14.341036489074822,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 38.43462651269346,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.3148754154779656,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 20.108501711325474,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.658773099037301,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 8.075440061990005,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.2835000991821346,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.700000190734869,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.2509999847412061,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.4122001647949176,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.9845431533688118,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 18.831292438630108,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.8305548127318474,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 14.183871711688944,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.03285707746233246,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.2635713304792131,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.2835728804033639,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.7120823806135679,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.870478853643288,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 10.452690407930966,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.3663734255188851,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.9278394769193716,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 3.1300048828125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 32.910003662109375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -4.812204602652237,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 15.53659034509841,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 18.15459324611568,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 46.756795841664186,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 4.944460828074981,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 25.109924168855912,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 4.550592020651521,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 19.038527908786914,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -3.1393590799691617,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 11.481451173439105,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 13.951134468328208,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 38.740205660526726,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 5.5731482033637425,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 21.72210703130748,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 5.109008564192429,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 15.470193191088708,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.2555000305175952,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -8.165499877929705,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.9399417114258029,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -6.07463775634767,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.08006980895993365,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.33265411376947895,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.6165885367266708,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 18.90482326420309,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.702666300360832,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 16.079733079851298,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.1306120045974986,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 12.043793481210198,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.7907148088727673,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.4803575788225452,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.23934589771786818,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.9260096056274758,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.4095576215033425,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 11.546809237901066,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.12856291517085128,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.8651424931179463,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.589996337890625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 11.389999389648438,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -3.5649467471933205,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 7.661618972565121,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 8.226874298327703,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 20.98071282228433,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.2882571413546309,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 9.748136895558769,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.6923116101145155,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 8.656410339394293,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.8921012245102453,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.6064798009058148,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 4.0234155205402296,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 12.964122641146869,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.916944516643392,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 6.360319758010336,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.2507281536554222,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 5.088075621696086,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.7709999084472656,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -5.918998718261719,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.19231994628904658,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.4859649658203011,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.12538188934325945,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.6098286056518418,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.08726899946311928,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 9.245549617665617,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.21946755514666894,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 6.760853139309586,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.4215295915249939,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 6.341301427902801,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.23142896379743316,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.6407143729073663,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.1445852773290146,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.14883435448845983,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.29207739499534924,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 5.63861355923191,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.41000137520910884,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.5206963831634,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.9600028991699219,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.700000762939453,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.3497347477261492,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 4.4903568433696694,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 4.617132945586344,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 14.68515867538306,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 2.948623235841863,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.183056071479328,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.6763320156164774,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.19765157319679982,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.323110774956926,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.4352176717103635,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.413674167798872,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 6.668568494245597,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 3.577310611130624,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.2047610660691044,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 2.2347485591573846,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -3.370683144501408,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.11149978637695312,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.9504999160766516,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.007706604003899997,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.06892486572265,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.07626337051392085,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.35615438461304194,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.607574268467515,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 5.3829440501325205,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.490915869491094,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 4.261337914858776,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.4912356195934553,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.94953648769285,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.05071449279785156,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.07428605215890083,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.12102151504897041,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.23908114895460653,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.371041052834709,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.856042405575888,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.03422071895581624,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.2724604549241765,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.4200019836425781,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.7099990844726562,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.2996508811330965,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.155262689171955,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 2.1976183264038385,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.25128718648252946,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.219180145139177,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.7105347730461231,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.0961725814752068,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.0022007931454144,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.3731946415499787,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.8998764824873509,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.0058404513836336,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -7.765302994654933,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.5904927698504157,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -4.098351910594555,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.4622439620657004,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.5661339245527932,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.14699993133544353,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.7945001602172823,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.015066986083979828,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.054952545166010225,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.029301471710205362,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.1360878753662078,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.0049209784434465,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.18306964724859043,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.7793337387387078,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.168523463254556,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.8428177162815196,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.0510479207735948,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.006428582327706378,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.04785673958914616,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.02336783436312362,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.06184992311279802,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.7094628010638537,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.1993227623691816,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.07371157464407974,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.4417989111757037,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.529998779296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 6.970001220703125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.222461158273137,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.229977182801047,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 3.3989610311886187,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 8.79246482697177,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.4295093694322025,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 4.444598810830791,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.011677235709761646,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 5.734008158319804,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.5496156355900617,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.8251619888582589,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.8044977465988534,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.7758746458343069,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.8008219941434414,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.0567816732823587,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.546739307831146,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.165673440621596,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.07750015258787357,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.06499938964844887,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.05753753662108352,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.6706082153320096,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.03299629211426236,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.1195848083496287,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.959041224163748,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 4.19192701266099,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.8710296518819494,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 4.505024184197127,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.9044496177609607,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.96903337018667,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.10071345738002258,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.140716552734375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.041274498058341935,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.002081985897601113,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.7296479291597162,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.8399971246844906,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.02417056861496325,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.6330213704356877,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.1199951171875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.9199981689453125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.6298031957412076,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.9117348257479017,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.9535032304200506,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.1064166141948828,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.612064364550414,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -3.955898328319706,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -4.424755267511181,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.872926738063586,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.0430423269418676,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.1434043459114043,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.2499555473674215,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -6.9101735669425794,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.9833769892616528,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -7.343715465868139,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -3.8663387239702747,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -6.4412614557617935,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.5319999694823991,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.7589996337890454,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.31078765869142444,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.683215942382816,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.177048492431652,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.8237860870361544,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.9128012082761705,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.5228723229773413,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.8344788107571546,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.6414709100117877,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.8361673615568037,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.2303531589135552,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.022857666015625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.15428379603794662,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.023940323660799123,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.05188580501006412,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.590527836951249,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.5395961787217138,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.029781864688261828,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.7012268790677556,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.3899993896484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.19000244140625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.8878462455046865,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.3240301904903764,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.3247403828107731,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -3.689736578249414,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.2100061713989918,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -4.333175140948109,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.646820475817412,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.0423193124188055,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.7849992771783887,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -3.7311089811689295,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -3.878718394976699,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -11.706326759386878,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.5813187961102306,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -7.72099227849654,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.0884039322765053,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -5.610654030117012,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.21899986267089844,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.48699951171875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.12177673339843409,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.6201057434082031,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.05147998809815135,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.2444240951538177,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.6890349215964653,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.9452538188015733,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.6097213949956881,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.00432924226872,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.530890662414496,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.5429860862693712,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.0599997384207589,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.030713762555803603,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.057952132684650826,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.029920254013903635,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.4241890138049431,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.20665916506511506,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.12154084962394718,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.4680673917110088,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.529998779296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.8199996948242188,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.3884811509437647,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.39584213959212,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 3.4925445031165347,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.157898763041687,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.294830048517448,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.9079906914086999,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.407457287609871,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.7928618210551361,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.2843643717393105,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.6592970320671858,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.7109142746709374,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -6.858691418095775,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.6661426732286877,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.4798264461397324,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.8490407440689633,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.7754728966430715,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.3524997711181612,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.935000228881833,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.1170483398437483,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.4646543884277321,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.0027882766723621444,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.03827774047850596,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.7658434249180557,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.7190696267759922,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.57578318779965,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.055616724232312,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.45797439444765775,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.48431314797648,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.0,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.15142822265625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.00945227955003336,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.07699615279566929,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.43325330774444115,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.3052396408191123,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.23771122263539457,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.606436811183635,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.0400009155273438,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.220001220703125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.7371501905056763,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.3669397406269037,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.381921187184342,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.006511032400502437,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.3368471239974764,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.557381064580899,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.6815102972220775,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.006648836354574,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.06430466782260114,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -4.42207891228621,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -4.585379964971814,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -8.023101213537965,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.7081597487087152,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.8304360729675331,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.1230937536811703,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.5616858813436338,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.24400024414062216,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.064999771118167,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.08981414794922671,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.4250639343261753,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.04067691802978857,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.2163938140869135,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.7479536657876817,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 4.037563827313983,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.8692200595527222,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.3125072325667198,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.8940617599999978,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.057259872664464,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.033571515764508675,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.1114289419991632,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.011535506891179104,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.04434890996210061,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.90631888063385,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.806101281658501,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.14822890455227622,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.260394728281332,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.009998321533203125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.5100021362304688,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.22862552026792216,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.6880324756449174,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.6962952287302704,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.8069489129694629,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.15252063114561398,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.24367913073666259,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.022880140971692775,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.7602456678528102,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.444220002415153,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -3.3671066960143885,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -3.5071635490572017,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -7.209641268167999,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.7812080064343752,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -3.631496268285095,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.5355364025692144,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.808089049845397,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.10799999237060831,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.5,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.02902923583984318,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.12934890747069971,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.006829700469971556,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.03886968612670927,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.28008624875586197,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.0008434912694088581,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.09675470850711854,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.8984884039255459,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.0383495809479828,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.0751133042770755,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.007857186453683052,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.03642872401646213,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.017618851071513397,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.10022362101593263,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.27033945515125835,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.4525194500449423,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.058225348946398636,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.179113922206081,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.22999954223632812,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.060001373291015625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.538237509202899,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.3015655616612443,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.3100859953181665,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.744254404566848,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.8274777120201202,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.801336387983854,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.3217157364878718,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.9814384533937348,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.1346080134801761,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.7535736099980617,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.8933727824693056,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -10.76084458570431,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.19879033673136,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -6.189153525532287,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.7632991929469646,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -4.5497731710919425,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.11849994659424112,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.6664999008178754,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.019900360107421022,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.05989730834960483,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.022355022430417648,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.10649623870849467,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.813952781109073,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.4613564520037814,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.5901529896806368,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.005890157938837071,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.5896386070051607,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.11672276097143275,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.030357088361467666,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.03657177516392296,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.059972577812051675,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.08468380392910091,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.5097507705697057,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.1329817701937408,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.16913301549512727,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.8002430950728374,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.6800003051757812,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.009998321533203125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.6042043095151226,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.6302653785750354,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.6517612859518471,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.399835306780294,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -3.223951537439662,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.690111486977753,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.750072526357372,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.13335003036156756,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.06864121316795257,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.4248737930842705,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.551697491835625,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -7.616754874357168,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.595264162150902,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -6.0779286245261845,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.191655982816465,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -3.43498468733664,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.08899993896484659,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.7139999389648466,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.007348785400395741,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.0037982940673799703,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.015116691589355469,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.0840647315978984,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.4772617247153175,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.372950775921633,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.3213920245269017,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.011972144102334603,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.3666642935736606,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.15038071448338908,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.004286084856305772,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.0850001743861607,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.03271033973463222,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.16206418870268124,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.2615960777835777,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.01854976113201401,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.28146426785674966,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.2893123216234659,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -5.22998046875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 54.0,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -5.85556856999151,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 10.180607552246013,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 11.527395061868551,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 32.34676858230008,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.011871466117074903,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 16.052290078720034,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.471448733280889,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 12.890407965442684,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -4.182723047308434,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 6.125468380586707,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 7.32393628408108,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 24.33017840116262,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.6405588414058361,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 12.664472941171601,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.0298652768217949,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 9.322073247744477,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.855500793457054,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -23.116500854492188,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.9749993896483602,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -6.694998779296839,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.425500030517469,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.09039993286126,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.4734092437052362,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 14.022701870075304,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.7753441384092614,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 10.56440412888945,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.0777288487404224,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 9.97156636641895,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.9492841448102673,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.55427987234933,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.2417326004422211,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.06645619993043717,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.8250481570156509,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 8.518693472194482,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.41501396867461327,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.018770419124195,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.7800064086914062,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.4399948120117188,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.656743778105408,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.630592272454958,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 3.7486663184800872,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 10.762992764167922,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.4012995411188625,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.218027675106348,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.587643065722888,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.6255600904072973,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.983898255422333,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.42454689920434774,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.4547924593073849,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.74640258303046,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.7726121658301013,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.1697894624420844,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.0292265221819807,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.9427746272909103,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.40750007629394247,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.3915000915527287,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.039400024414064205,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.7010000610351454,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.022040977478027912,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.08080768585205078,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.3664824826154933,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 4.410713861882942,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.698564863014195,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.907812603128346,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.8541573999730767,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.5019793409528424,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.049285888671875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.061428070068359375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.02493371435885816,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.013140494272953163,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.6922929097077049,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.16561183248891,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.024559232958481725,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.2707635593973896,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 2.970001220703125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 9.009994506835938,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.9834574758468717,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 4.5434628265831005,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 4.701087662920189,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 17.91575953289145,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 2.90218744217231,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.9767544105585797,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.0871012610855324,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.7836709937109387,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.6893880468362035,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.48832365492379415,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.4976288851327171,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 9.89916935175399,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 3.530874817461071,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.5889372730101474,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.6455178046264396,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.784663723987269,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.5889999389648608,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -4.583499908447266,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.18565765380859034,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.1160406494140602,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.23882286071776093,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.0915711212158214,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.8387096145144328,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 6.8273950601361655,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.6535256610875622,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 5.2699297759083095,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.5831306256321565,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 4.597401061329198,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.08428737095424133,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.11143275669642883,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.10164986668915876,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.23620560714115602,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.4497711665793283,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 4.398122854628484,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.13883487276917972,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.4394077845455697,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.399993896484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 21.490020751953125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.94964651787496,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 4.920990188865371,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 5.230843631150073,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 20.95228783661144,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.3745813188087652,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 8.071144515802919,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.28228349191372715,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 4.037603375465071,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.2768009951918846,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.8658510172060647,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.0273848533626007,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 12.935697655473977,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 2.0032686940975264,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 4.6833273782544875,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.840700035454633,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.4692686577668628,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.372499084472679,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -5.602000427246139,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.3487994384765898,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -6.223200073242197,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.12625000000002728,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.46419982910157387,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.010715692318474801,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 6.91675266648637,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.22121883943924114,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 6.868135154300147,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.12958057930701017,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 5.285033448632392,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.1078556605747778,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.3550000871930816,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.29595610081583423,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.6088893975142335,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.09161984259170453,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 4.922355905656239,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.39469430984483955,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.210361613820513,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.5099945068359375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.6200027465820312,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -3.2918379582810076,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.936605489212151,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 2.082469250063501,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 9.967292725963562,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -3.5825967590738417,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 4.26516696599607,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.2874838593470148,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 6.22372514944176,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.6189924355979324,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.118533682447155,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.120989527723971,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.9507025448260995,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.9539093837850796,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.8773498284476382,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.8459004028879225,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.6553904317435535,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.13783340454101278,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.7678333282470646,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.052808837890623295,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.46016693115234375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.02985721588134993,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.16354248046874886,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.3619884149139736,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 4.090471436234089,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.0649796546998944,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 5.76415877135773,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.9528831204987713,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 4.966080474282576,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.026666913713727425,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.13404846191406272,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.022354641689592558,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.04531982535011769,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.433372619456387,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 4.651388849213921,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.0295887764941267,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.4329620128234668,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.5100002288818359,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.7849998474121094,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -3.0508124777758105,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 4.802452484662056,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 5.3875543984620125,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 23.027563452513743,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.6867703111638654,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 13.376019176343966,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.6136192483219176,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 10.712246771509026,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.3779669550927354,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.7473133130027501,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.1840956206745403,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 15.01097327137628,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.0580829358751043,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 9.988202038795533,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.05520270478101175,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 7.143912053810819,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.035000038146971946,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.3952500343322747,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.04040000915527031,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.2535999679565428,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.020150003433229813,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.09980000495910701,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.5905158413402454,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 10.52202748201616,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.5087855784688076,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 9.624613243685587,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.5215525328518327,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 8.887493611270681,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.005357197352818144,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.10000010899135048,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.04019512738051256,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.015345874596715436,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.0684328408534167,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 8.383661303159608,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.3333156104999483,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.1063846202090324,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.43000030517578125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.20999908447265625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.3979014227346367,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.8657007755667587,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.8822136700204273,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.0452915471476754,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.4628717815897927,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.06271183368646849,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.778224842402532,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 3.263899691716887,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.2749440999484385,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -2.189438396092547,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.321245107767045,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -6.971298633989787,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.8341844063010315,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -3.3251053038619647,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 2.336641385943439,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.30443502598132044,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.13849983215331463,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.9144992828369141,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.025991210937505116,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.05539779663085653,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.02951335906982422,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.14278881072998217,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.7892641811402479,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.992806154440018,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.5630596728268378,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.37092255199913104,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.6521664223162027,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.0898992563934442,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.0114288330078125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.0914284842354911,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.00314367879253874,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.13260959424443408,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.0981023998365309,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.9240288866095518,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.01606981892295667,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.910688328599888,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.value",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.1100006103515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 7.0200042724609375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_1d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -2.972261207953819,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 6.004403397033864,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_5d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 6.295301175602042,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 16.865326091746358,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_20d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.5339774854833408,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 6.040562644564085,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_60d_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.050402687068184626,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 5.136445190693218,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_1d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -1.299415685270744,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.9492642253745585,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_5d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 2.0918423978145695,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 8.848735910608896,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_20d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.9052901101945796,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 2.652745507015652,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_60d_pp",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.6088192306090918,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 1.5681104729950102,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma20",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.6214996337890568,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -4.697999572753901,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma50",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.10239990234373408,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -1.2301998901367028,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma200",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.13805000305177373,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.6427000427246128,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma20_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.3060855418146491,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 7.035087250772454,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma50_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.00807966349336553,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 4.980182945691535,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma200_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.19217359863612415,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 4.594670618931906,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_sma",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.005713326590401024,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.3350001743861606,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 0.006198120521516692,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 0.060662872348327124,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.drawdown_from_63d_high_pct",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -0.06289702712301981,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": 4.01395408368699,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.volume_vs_previous20_ratio",
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": -3.100003004304545,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -0.31835284329641916,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS2.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.17000000000000082,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.1200000000000001,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLH0A0HYM2.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-11",
        "change": -0.040000000000000036,
        "unit": "percentage_points"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-11",
        "change": -0.10000000000000009,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLC0A0CM.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-11",
        "change": -0.010000000000000009,
        "unit": "percentage_points"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-11",
        "change": -0.030000000000000027,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS10.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.10000000000000053,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.03000000000000025,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DFII10.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.11999999999999966,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.1299999999999999,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.T10YIE.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-12",
        "change": 0.040000000000000036,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-12",
        "change": -0.019999999999999574,
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
    "available_prior_observations": 19,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-11",
        "to": "2026-11-12",
        "change": 1.2100000000000009,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-05",
        "to": "2026-11-12",
        "change": -9.48,
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
        "change": -51.30699157714844,
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
        "change": -19.9444580078125,
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
        "change": -79.09606170654297,
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
        "change": -22.570114135742188,
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
        "change": 9.304443359375,
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
  }
]
```

## 判断依据 · 反弹是否可靠

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 反弹是否可靠 |
| 事实指标引用 | ["prices.SPY.volume_vs_previous20_ratio", "prices.QQQ.sma200", "observed.QQQ.price"] |
| 推断与解释 | 盘前延续分化修复，但宽基与芯片关键线未收复；今天可靠常规VWAP尚不存在。 |
| 反证与缺口 | 12日已经穿过原支撑，不能重写成全天守住；盘后上涨流动性和覆盖率有限 |
| 确认条件 | SPY755、QQQ680–682重新回踩守稳并形成更高低点；可靠分钟数据下站稳常规VWAP；随后收复SPY763.04、QQQ694.56日高并保持到收盘，RSP/IWM同步改善 |
| 失效条件 | 再失755/680且反抽失败，或只有权重上涨而广度继续恶化，撤销升级判断 |
| 观察期限 | 未来1–3交易日 |
| 条件式指导 | 将低位承接、突破回踩和趋势反转分层；先确认数据质量，再用收盘及广度验证，失效则撤销升级。 |
| 主观置信等级 | medium |
| 判断变化原因 | 同一已收盘交易日，加上本轮盘前价格、官方服务状态、IEA与CNN核验；不是新常规交易确认。 |

## 判断依据 · AI泡沫与治理是否是一回事

| 要素 | 记录 |
| --- | --- |
| 评估问题 | AI泡沫与治理是否是一回事 |
| 事实指标引用 | ["observed.NVDA.price", "prices.SMH.sma200", "prices.CRWV.return_1d_pct"] |
| 推断与解释 | 治理、服务可用性、需求与估值分层；NVDA上涨不能抵消MSFT弱势和现金流压力。 |
| 反证与缺口 | AMD等个股上涨可能来自竞争重估，不能替代SMH/NVDA确认；杠杆ETF每日重置放大波动路径损耗 |
| 确认条件 | SMH收复506.96后回踩守稳，再观察520.79–523.54均线区；NVDA形成更高低点并收复170.24，公告与订单兑现没有新增反证；MU重新站回20日约843后观察承接 |
| 失效条件 | SMH再失490反抽失败或失484.50日低；NVDA再向148.80低点扩展，或出现可核验交付/客户恶化 |
| 观察期限 | 未来1–3交易日 |
| 条件式指导 | 将低位承接、突破回踩和趋势反转分层；先确认数据质量，再用收盘及广度验证，失效则撤销升级。 |
| 主观置信等级 | medium |
| 判断变化原因 | 同一已收盘交易日，加上本轮盘前价格、官方服务状态、IEA与CNN核验；不是新常规交易确认。 |

## 判断依据 · 优先观察哪些板块

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 优先观察哪些板块 |
| 事实指标引用 | ["prices.XLI.sma20", "prices.XLV.relative_spy_20d_pp", "prices.XLP.relative_spy_20d_pp"] |
| 推断与解释 | 非芯片相对强度延续；IEA供需变化使昨天能源领涨的持续性更需验证。 |
| 反证与缺口 | 相对强势可与绝对下跌同时出现；没有当期申赎证据，不声称主力已建仓 |
| 确认条件 | 大盘不再创新低；XLI守20日167.77并重夺200日172.77，XLV/XLP分别守183.04/89.25且持续相对SPY领先；XLF守56.90同时信用利差不恶化 |
| 失效条件 | 各自均线失守并反抽失败，或利率/信用压力导致强弱关系反转 |
| 观察期限 | 未来1–3交易日 |
| 条件式指导 | 将低位承接、突破回踩和趋势反转分层；先确认数据质量，再用收盘及广度验证，失效则撤销升级。 |
| 主观置信等级 | medium |
| 判断变化原因 | 同一已收盘交易日，加上本轮盘前价格、官方服务状态、IEA与CNN核验；不是新常规交易确认。 |

## 判断依据 · 是否进入全面恐慌

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 是否进入全面恐慌 |
| 事实指标引用 | ["observed.CNN.value", "observed.VIX.price", "observed.Treasury10Y.value", "macro.BAMLH0A0HYM2.value"] |
| 推断与解释 | CNN39 Fear、VIX盘前18.32缓和，但官方收益率仍高，信用滞后；不能判全面过热或恐慌结束。 |
| 反证与缺口 | 相对强势可与绝对下跌同时出现；没有当期申赎证据，不声称主力已建仓 |
| 确认条件 | 大盘不再创新低；XLI守20日167.77并重夺200日172.77，XLV/XLP分别守183.04/89.25且持续相对SPY领先；XLF守56.90同时信用利差不恶化 |
| 失效条件 | 各自均线失守并反抽失败，或利率/信用压力导致强弱关系反转 |
| 观察期限 | 未来1–3交易日 |
| 条件式指导 | 将低位承接、突破回踩和趋势反转分层；先确认数据质量，再用收盘及广度验证，失效则撤销升级。 |
| 主观置信等级 | medium |
| 判断变化原因 | 同一已收盘交易日，加上本轮盘前价格、官方服务状态、IEA与CNN核验；不是新常规交易确认。 |

## 芯片治理修复仍待价格确认 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | NVDA领导过渡明确，永久继任尚待公告 |
| 事实：市场反应 | NVDA盘前回升，SMH未突破506.96 |
| 推断：解释 | 推断：部分不确定性缓和，尚非行业趋势转强 |
| 受益篮子 | ["经营连续性得到证实的芯片链"] |
| 受损篮子 | ["杠杆半导体与治理风险暴露"] |
| 反证 | NVDA仍低170.24，SMH弱于中期均线 |
| 下一催化剂 | 17日业绩、正式继任与客户交付披露 |
| 证据 | ["https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-CEO-Transition/default.aspx"] |

## 微软服务恢复与AI需求分化 · 新增

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | Microsoft365恢复改善但未全部解决；Google能源项目只是有条件意向 |
| 事实：市场反应 | MSFT盘前偏弱，AI业绩相关股涨跌分化 |
| 推断：解释 | 推断：可交付性、现金转化与基础设施约束继续受到定价 |
| 受益篮子 | ["能兑现合同与现金流的基础设施企业"] |
| 受损篮子 | ["服务持续受损或融资依赖高的企业"] |
| 反证 | Azure状态未显示问题，不能推断全云服务故障；MoU不等于订单 |
| 下一催化剂 | 微软下一状态更新、公司正式合同与业绩承接 |
| 证据 | ["https://status.cloud.microsoft/", "https://newsroom.engie.com/actualites/engie-et-google-s-associent-pour-developper-les-solutions-energetiques-d-un-projet-de-data-center-envisage-pres-de-chateauroux-en-france-07134-ff316.html", "https://www.silicondata.com/products/silicon-index/h100"] |

## 原油供应趋松预期与低库存并存 · 减弱

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | IEA预期4Q供应过剩，同时陆上库存仍低 |
| 事实：市场反应 | WTI盘前较早报回软，昨日能源领涨还未获趋势确认 |
| 推断：解释 | 推断：供给恢复可能削弱追涨能源的逻辑，地缘尾部风险仍在 |
| 受益篮子 | ["能源成本敏感的需求端（条件式）"] |
| 受损篮子 | ["仅押注油价持续急升的篮子"] |
| 反证 | 海上库存增长不等于陆上立即宽松；航运与核监督风险仍在 |
| 下一催化剂 | PPI、实际供应与航运进展 |
| 证据 | ["https://www.iea.org/reports/oil-market-report-november-2026", "https://apnews.com/article/a689242aa635c103033790bacbff7f07"] |

## 高利率下的防御相对强度 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 官方收益率仍高，PPI将检验压力是否延续 |
| 事实：市场反应 | 医疗、必需消费、工业多日相对SPY领先，昨日仍下跌 |
| 推断：解释 | 推断：相对抗跌优先于盲目抄底，但仍需绝对趋势确认 |
| 受益篮子 | ["XLV", "XLP", "XLI"] |
| 受损篮子 | ["利率敏感且现金流远期化的估值"] |
| 反证 | 相对领先不等于已有资金净流入；强美元也影响外需 |
| 下一催化剂 | 13日08:30EST PPI及常规市场广度 |
| 证据 | ["https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value_month=202611&type=daily_treasury_yield_curve", "https://www.bls.gov/schedule/2026/11_sched.htm", "https://www.ici.org/research/stats/etf_flows"] |

## tc 报价（供应商时戳不等于成交时戳）

| 标的 | 价格 USD | 变化% | 观测时间 | 供应商时间 | 抓取时间 | 质量 |
| --- | --- | --- | --- | --- | --- | --- |
| SPY | 759.40 | 0.30 | 2026-11-13T12:01:49+00:00 | 2026-11-13T12:01:49+00:00 | 2026-11-13T12:02:42.074296+00:00 | ok |
| QQQ | 690.21 | 0.30 | 2026-11-13T12:02:25+00:00 | 2026-11-13T12:02:25+00:00 | 2026-11-13T12:02:42.074296+00:00 | ok |
| SMH | 505.00 | 0.65 | 2026-11-13T12:01:52+00:00 | 2026-11-13T12:01:52+00:00 | 2026-11-13T12:02:42.074296+00:00 | ok |
| NVDA | 169.60 | 2.05 | 2026-11-13T12:02:30+00:00 | 2026-11-13T12:02:30+00:00 | 2026-11-13T12:02:42.074296+00:00 | ok |
| MSFT | 515.02 | -1.53 | 2026-11-13T12:02:25+00:00 | 2026-11-13T12:02:25+00:00 | 2026-11-13T12:02:42.074296+00:00 | ok |
| AMZN | 270.28 | 1.06 | 2026-11-13T12:01:49+00:00 | 2026-11-13T12:01:49+00:00 | 2026-11-13T12:02:42.074296+00:00 | ok |
| GOOGL | 302.34 | 1.22 | 2026-11-13T12:02:26+00:00 | 2026-11-13T12:02:26+00:00 | 2026-11-13T12:02:42.074296+00:00 | ok |
| META | 623.99 | 0.06 | 2026-11-13T12:02:01+00:00 | 2026-11-13T12:02:01+00:00 | 2026-11-13T12:02:42.074296+00:00 | ok |

## 核心行情与风险代理

| 标的 | 价格/指数 | 单位 | 观测日 | 1日% | 5日% | 20日% | 质量 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 757.12 | USD_per_share | 2026-11-12 | -0.35 | 3.29 | -1.90 | ok |
| QQQ | 688.17 | USD_per_share | 2026-11-12 | -0.32 | 6.35 | -5.47 | ok |
| IWM | 278.44 | USD_per_share | 2026-11-12 | -1.64 | 2.75 | 1.22 | ok |
| RSP | 220.72 | USD_per_share | 2026-11-12 | -0.87 | 1.78 | 2.66 | ok |
| GLD | 354.89 | USD_per_share | 2026-11-12 | -2.82 | -5.49 | -7.27 | ok |
| GC=F | 3,885.30 | USD_per_troy_ounce | 2026-11-12 | -2.88 | -5.55 | -6.83 | ok |
| CL=F | 88.74 | USD_per_barrel | 2026-11-12 | 2.55 | -1.97 | -9.42 | ok |
| BZ=F | 95.82 | USD_per_barrel | 2026-11-12 | 3.30 | -2.51 | -9.54 | ok |
| TLT | 79.72 | USD_per_share | 2026-11-12 | -1.48 | -2.70 | 0.11 | ok |
| UUP | 29.42 | USD_per_share | 2026-11-12 | 0.24 | 1.73 | 1.45 | ok |
| HYG | 76.98 | USD_per_share | 2026-11-12 | -0.48 | -0.39 | 0.33 | ok |
| LQD | 103.05 | USD_per_share | 2026-11-12 | -0.88 | -1.54 | -0.05 | ok |
| ^VIX | 18.70 | index | 2026-11-12 | 6.92 | -33.64 | 13.61 | ok |
| ^VIX3M | 20.06 | index | 2026-11-12 | 4.26 | -21.49 | 8.49 | ok |
| ^VVIX | 96.71 | index | 2026-11-12 | 6.90 | -28.36 | 4.47 | ok |
| ^MOVE | 98.43 | index | 2026-11-12 | 6.49 | 4.85 | -0.64 | ok |
| NVDA | 166.19 | USD_per_share | 2026-11-12 | -4.34 | -8.49 | -23.50 | ok |
| MSFT | 523.00 | USD_per_share | 2026-11-12 | 0.36 | -2.41 | -3.05 | ok |
| AMZN | 267.44 | USD_per_share | 2026-11-12 | 0.48 | 2.78 | 4.98 | ok |
| GOOGL | 298.70 | USD_per_share | 2026-11-12 | 1.79 | 5.71 | -14.47 | ok |
| META | 623.61 | USD_per_share | 2026-11-12 | -0.82 | 3.06 | -15.35 | ok |
| CRWV | 56.60 | USD_per_share | 2026-11-12 | -6.86 | 29.64 | -18.78 | ok |
| MU | 798.44 | USD_per_share | 2026-11-12 | -1.59 | 21.64 | -14.26 | ok |
| DRAM | 43.66 | USD_per_share | 2026-11-12 | -2.65 | 17.97 | -11.49 | ok |
| VRT | 209.64 | USD_per_share | 2026-11-12 | 1.52 | 18.62 | -2.38 | ok |

## 跨资产风险解释

CNN官方页面本轮已可读取：39（Fear），更新时间13日06:47:46EST，前收39、一周前24；这是情绪仍偏谨慎、较上周缓和的证据，不等于买点。[CNN](https://edition.cnn.com/markets/fear-and-greed)。12日VIX18.70、VIX3M20.06，匹配收盘期限比约0.932；Cboe官方CSV已更新至12日18.70，早报的官方CSV滞后缺口解除。盘前VIX18.32来自11:47:31UTC，不能与昨收VIX3M拼成实时期限结构。VVIX96.71、MOVE98.43仍为12日。[财政部最新曲线](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value_month=202611&type=daily_treasury_yield_curve)仍为12日：2年4.86%、10年5.10%，较10日上行13/12bp；今天债市收益率尚未核验。FRED实际利率2.78%至10日，HY330bp/IG90bp至11日，金融压力−0.4918至6日，不能以滞后信用判断当前无风险。11:52UTC附近WTI88.42、Brent95.95、黄金期货3896.40、美元103.224，记录各自端点，非同步股票收盘收益。[IEA新月报](https://www.iea.org/reports/oil-market-report-november-2026)预计4Q26供应过剩，但10月库存增加主要在海上，陆上库存仍偏低；因此原油走软与实际供应链脆弱可以并存。伊朗核监督立场和俄乌会谈尚非已生效的全面停火。GPR序列仍止2日，不能充当今天战争指数。结论：恐惧和折现率压力下的修复，暂无全面过热证据；也不能仅据CNN39判定系统性恐慌已结束。

## 宏观与地缘风险指标

| 指标 | 数值 | 单位 | 观测日 | 20次观测变化 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- | --- |
| DGS2 | 4.73 | percent | 2026-11-10 | -0.06 | lagged | https://fred.stlouisfed.org/series/DGS2 |
| BAMLH0A0HYM2 | 3.30 | percentage_points | 2026-11-11 | 0.14 | lagged | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| BAMLC0A0CM | 0.90 | percentage_points | 2026-11-11 | 0.07 | lagged | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| DGS10 | 4.98 | percent | 2026-11-10 | -0.23 | lagged | https://fred.stlouisfed.org/series/DGS10 |
| DFII10 | 2.78 | percent | 2026-11-10 | -0.10 | lagged | https://fred.stlouisfed.org/series/DFII10 |
| T10YIE | 2.24 | percent | 2026-11-12 | -0.11 | ok | https://fred.stlouisfed.org/series/T10YIE |
| STLFSI4 | -0.49 | index | 2026-11-06 | 0.46 | lagged | https://fred.stlouisfed.org/series/STLFSI4 |
| CBOE_VIX | 18.70 | index | 2026-11-12 | 2.24 | ok | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| GPRD | 113.95 | index | 2026-11-02 | -245.09 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_ACT | 129.82 | index | 2026-11-02 | -342.91 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_THREAT | 108.29 | index | 2026-11-02 | -240.96 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_MA7 | 158.85 | index | 2026-11-02 | -44.27 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_MA30 | 184.74 | index | 2026-11-02 | 13.98 | lagged | https://www.matteoiacoviello.com/gpr.htm |

## CNN Fear & Greed

```json
{
  "value": 39,
  "rating": "Fear",
  "observed_at": "2026-11-13T11:47:46+00:00",
  "retrieved_at": "2026-11-13T12:10:10.023178+00:00",
  "source": "https://edition.cnn.com/markets/fear-and-greed",
  "quality": "ok",
  "method": "官方页面浏览器读取；API仍418"
}
```

## 19 板块与主题 ETF：价格量能证据

| 标的 | 板块 | 1日% | 5日% | 20日% | 相对SPY 1日pp | 相对SPY 5日pp | 相对SPY 20日pp | 成交量/前20日 | 观测日 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLK | 科技 | -0.34 | 7.01 | -8.15 | 0.02 | 3.72 | -6.25 | 0.77 | 2026-11-12 |
| XLE | 能源 | 1.51 | 4.38 | -3.35 | 1.87 | 1.09 | -1.45 | 0.69 | 2026-11-12 |
| XLF | 金融 | -0.72 | 1.23 | 5.32 | -0.36 | -2.06 | 7.22 | 0.63 | 2026-11-12 |
| XLI | 工业 | -0.89 | 4.29 | 0.92 | -0.54 | 1.00 | 2.82 | 0.72 | 2026-11-12 |
| XLV | 医疗 | -0.59 | 1.58 | 6.00 | -0.24 | -1.71 | 7.91 | 0.68 | 2026-11-12 |
| XLP | 必需消费 | -0.43 | -0.21 | 5.05 | -0.07 | -3.50 | 6.95 | 0.71 | 2026-11-12 |
| XLY | 可选消费 | -0.44 | 2.40 | 6.22 | -0.08 | -0.89 | 8.12 | 0.93 | 2026-11-12 |
| XLC | 通信 | -0.96 | 3.09 | -4.34 | -0.60 | -0.20 | -2.44 | 0.54 | 2026-11-12 |
| XLU | 公用事业 | -0.02 | 1.18 | 5.19 | 0.33 | -2.11 | 7.09 | 0.63 | 2026-11-12 |
| XLRE | 房地产 | -0.52 | 0.14 | 5.64 | -0.16 | -3.16 | 7.54 | 0.68 | 2026-11-12 |
| XLB | 材料 | -1.28 | 0.02 | 3.52 | -0.93 | -3.27 | 5.42 | 0.77 | 2026-11-12 |
| SMH | 半导体 | -1.03 | 12.06 | -10.22 | -0.68 | 8.77 | -8.32 | 0.83 | 2026-11-12 |
| IGV | 软件 | -0.76 | 2.46 | -7.44 | -0.41 | -0.83 | -5.54 | 0.55 | 2026-11-12 |
| XOP | 油气开采 | 1.65 | 5.18 | -6.04 | 2.00 | 1.88 | -4.14 | 0.98 | 2026-11-12 |
| OIH | 油服 | -0.11 | 6.18 | -1.98 | 0.25 | 2.89 | -0.08 | 0.42 | 2026-11-12 |
| ITA | 航空与国防 | -2.06 | 5.31 | 4.00 | -1.71 | 2.02 | 5.90 | 1.49 | 2026-11-12 |
| ARKX | 航天主题 | -1.68 | 10.30 | -2.29 | -1.33 | 7.01 | -0.39 | 0.69 | 2026-11-12 |
| KRE | 区域银行 | -0.59 | 0.29 | 3.97 | -0.24 | -3.00 | 5.87 | 0.67 | 2026-11-12 |
| SKYY | 云计算 | -0.07 | 4.77 | -7.46 | 0.28 | 1.48 | -5.56 | 0.31 | 2026-11-12 |

## 资金证据分层

12日19个ETF中仅2个上涨：XLE+1.52%、XOP+1.65%。RSP−0.87%、IWM−1.64%，弱于SPY−0.35%；这是观察池与代理指标，不是全市场涨跌家数。SPY/QQQ成交量约前20日均量0.77/0.72倍，SMH0.83倍，而NVDA4.49倍；NVDA放巨量既可能含恐慌抛售也可能含承接，不能仅据此认定机构买入。SMH20日相对SPY−8.32个百分点，IGV−5.54，仍未确认科技整体重新领涨。XLI、XLF、XLV、XLP20日相对分别+2.82、+7.22、+7.91、+6.95个百分点，适合作为非芯片观察名单；但当天均下跌，相对强度不是绝对收益保证。ITA−2.06%、ARKX−1.68%，不能把航天投资新闻直接写成航天ETF已强势。能源当日领先，但XLE/XOP仍低于20日均线66.33/191.56，中期领涨未证实。[ICI最近可核验周度报告](https://www.ici.org/research/stats/etf_flows)仍是10日公布、截至4日一周：总净发行498.30亿美元、国内股票308.68亿、债138.89亿、商品1.29亿；与当前价格轮动分别展示。[VanEck SMH](https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/overview/)本轮已更新12日NAV502.03、资产64.41B；缺连续精确份额及拆分检查，资产减少不能直接推为赎回。与早报相比仍是同一完整交易日，部分历史成交量修订不代表新增交易或资金流；当前盘前RSP报价较旧，不能用它确认全市场宽度。

## 最近可核验 ETF 申赎窗口

| 标的 | 金额 USD million | 起始日 | 结束日 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- |
| US_DOMESTIC_EQUITY_ETFS | 30868 | 2026-10-29 | 2026-11-04 | public_report | https://www.ici.org/research/stats/etf_flows |
| US_BOND_ETFS | 13889 | 2026-10-29 | 2026-11-04 | public_report | https://www.ici.org/research/stats/etf_flows |
| US_COMMODITY_ETFS | 129 | 2026-10-29 | 2026-11-04 | public_report | https://www.ici.org/research/stats/etf_flows |

## Polymarket 搜索覆盖与限制

本轮12:02–12:04UTC重查固定事件并主动搜索15组：Fed、衰退、银行、关税、AI泡沫/Nvidia CEO/AMD/CoreWeave、数据中心政策、Hormuz/Iran/Ukraine/油价及SpaceX。每组limit10，多组hasMore，覆盖不完整。检查临近15日停火期限与未来一周PPI、NVDA、进口价格，及未来30天政策/融资风险；结算截止不等于已知事件日。没有核验到准确事件日与规则同时匹配的新增高质量upcoming条目；近期风险仍列在risk/reference。永久CEO排除临时任命。新发现人选、破产及数据中心政策合约未因标题相关便认定可交易。

## Polymarket · 值得警惕的信号

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["AI bubble burst in 2026?", "期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。", "https://polymarket.com/event/ai-bubble-burst-by"] | [6.75, {"status": "comparable", "change_pp": 0.15000000000000013}] | {"spread": 0.0030000000000000027, "volume24h_usd": 83382.626974, "liquidity_usd": 139577.91391, "quality_flags": [], "retrieved_at": "2026-11-13T12:02:59.317380+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["多条件AI合约与实际融资分开", "AI估值/融资"] | ["多个实际阈值与信用持续恶化共同出现", "需求、回款与融资恢复且阈值未满足"] | [null, null] |
| ["CoreWeave downgraded by Moody's or S&P by December 31, 2026?", "2026年12月31日23:59ET前，Moody’s或S&P正式下调CoreWeave长期主体/企业家族或高级无担保债信用评级则Yes；仅负面展望/观察名单不算，不要求降至某统一评级档。成交很薄，不视为客观违约概率。", "https://polymarket.com/event/coreweave-downgraded-by-moodys-or-sp-by"] | [17.5, {"status": "comparable", "change_pp": -0.5000000000000004}] | {"spread": 0.13, "volume24h_usd": null, "liquidity_usd": 235.716, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"], "retrieved_at": "2026-11-13T12:02:30.847067+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["新发现评级下调合约，24h成交很薄", "算力融资成本"] | ["正式评级行动及实际融资成本共同转坏", "仅展望变化或评级不变；薄盘口不足确认"] | [null, null] |

## Polymarket · 有参考价值的事件

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Strait of Hormuz traffic returns to normal by December 31?", "期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。", "https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31"] | [5.5, {"status": "comparable", "change_pp": -1.0000000000000002}] | {"spread": 0.009999999999999995, "volume24h_usd": 94694.677987, "liquidity_usd": 242705.383, "quality_flags": [], "retrieved_at": "2026-11-13T12:02:59.317380+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["实际通行量与外交表态分开", "油运/能源"] | ["Portwatch量持续改善并满足规则", "航运事件持续且量未恢复"] | [null, null] |
| ["Russia x Ukraine energy ceasefire agreement by November 15, 2026?", "11月15日23:59基辅时间前，俄乌双方同意暂停打击至少一类明确能源设施，双方官宣或可信报道共识确认；美国第三方单方声称不足。可限定地理范围，但仅一个设施不算；必须明确相互暂停，不是谈判/换囚。约定生效日可晚于截止。", "https://polymarket.com/event/russia-x-ukraine-energy-ceasefire-agreement-by"] | [0.95, {"status": "comparable", "change_pp": -1.25}] | {"spread": 0.002999999999999999, "volume24h_usd": 15671.485143999998, "liquidity_usd": 34890.78789, "quality_flags": [], "retrieved_at": "2026-11-13T12:02:59.317380+00:00", "contract_end_at": "2026-11-15T21:59:00+00:00"} | ["新能源协议合约；15日是截止非会议日", "能源供给/风险溢价"] | ["双方确认合格能源设施互停安排", "仅换囚或第三方声称"] | [null, null] |
| ["Russia x Ukraine ceasefire agreement by December 31, 2026?", "2026年末23:59ET前，双方官宣或可信共识确认相互暂停直接交战，包含明确生效日的全面暂停；仅限定目标/地点的局部能源安排不算。达成协议可先于实际生效，单方暂停不算。", "https://polymarket.com/event/russia-x-ukraine-ceasefire-agreement-by"] | [10.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.009999999999999995, "volume24h_usd": 14777.266203000005, "liquidity_usd": 83058.9392, "quality_flags": [], "retrieved_at": "2026-11-13T12:02:59.317380+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["全年全面停火协议与能源局部暂停定义不同", "军工/欧洲风险偏好"] | ["双边明确全面暂停及生效日", "仅局部或单方暂停"] | [null, null] |
| ["Will WTI Crude Oil (WTI) hit (HIGH) $110 in November?", "11月合资格交易时段，Pyth对ICE Europe WTI活跃月CLL的任一最终1分钟High达到110美元即Yes；按原值不取整，最后三个交易日换月。主数据不可用时依ICE官方日高低。与Yahoo NYMEX连续WTI代理不是同一可直接裁决序列。", "https://polymarket.com/event/what-price-will-wti-hit-in-november-2026"] | [4.5, {"status": "comparable", "change_pp": -1.5}] | {"spread": 0.010000000000000002, "volume24h_usd": 4171.940699, "liquidity_usd": 30628.0633, "quality_flags": [], "retrieved_at": "2026-11-13T12:02:59.317380+00:00", "contract_end_at": "2026-12-01T04:59:59.999000+00:00"} | ["月内WTI高点合约；不直接用Yahoo裁决", "通胀与油气"] | ["指定Pyth/ICE价格和实际供应压力同向", "供应改善且指定价格未触发"] | [null, null] |
| ["Will the Fed increase interest rates by 50+ bps after the December 2026 meeting?", "衡量12月8–9日该次FOMC前后联邦基金目标区间上限上调至少50bp；非标准变化向上取整到最近25bp对应档。按正式声明，若下一次会议结束仍无声明则按不变档处理。不是全年累计加息幅度。", "https://polymarket.com/event/fed-decision-in-december-20260729232808632"] | [9.15, {"status": "comparable", "change_pp": -1.0999999999999996}] | {"spread": 0.0010000000000000009, "volume24h_usd": 649568.417569, "liquidity_usd": 359570.46946, "quality_flags": [], "retrieved_at": "2026-11-13T12:02:59.317380+00:00", "contract_end_at": "2026-12-09T23:59:00+00:00"} | ["12月单次50+bp风险", "利率与长久期估值"] | ["官方政策及融资/利率同步趋紧", "数据转弱与实际政策不符"] | [null, null] |
| ["Will the Fed increase interest rates by 25 bps after the December 2026 meeting?", "以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。", "https://polymarket.com/event/fed-decision-in-december-20260729232808632"] | [88.5, {"status": "comparable", "change_pp": 1.0000000000000009}] | {"spread": 0.010000000000000009, "volume24h_usd": 989227.0551619999, "liquidity_usd": 571767.3087, "quality_flags": [], "retrieved_at": "2026-11-13T12:02:59.317380+00:00", "contract_end_at": "2026-12-09T23:59:00+00:00"} | ["12月单次加息25bp定价；准确公告时点本轮不强填", "利率和估值"] | ["以正式目标区间变动匹配专门档位", "实际政策与对应档不符"] | [null, null] |
| ["New NVIDIA CEO named by December 31, 2026?", "2026年12月31日23:59纽约时间前，英伟达正式宣布黄仁勋的CEO继任者即满足；实际就任可以更晚，临时CEO不计。以公司公开声明为主要来源，可参照可信报道共识。与离任宣布合约不同。", "https://polymarket.com/event/new-nvidia-ceo-named-by-december-31-2026"] | [18.5, {"status": "comparable", "change_pp": -6.0}] | {"spread": 0.010000000000000009, "volume24h_usd": 42662.85372600001, "liquidity_usd": 26443.0415, "quality_flags": [], "retrieved_at": "2026-11-13T12:02:59.317380+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["临时CEO已经任命，但本合约只计正式永久继任者宣布", "管理连续性、客户信任与估值风险溢价"] | ["公司正式公告永久CEO且符合截止要求", "只有临时任命或到期无永久继任宣布"] | [null, null] |

## Polymarket · 将要发生的事件及概率

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |

## 将要发生的事件及概率 · 本次无合格合约

本次未纳入合格合约，不代表相关风险或事件不存在。见搜索覆盖与限制。

## Will the Fed increase interest rates by 25 bps after the December 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 770450 / 3215008 |
| Yes 概率 % | 88.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [2.0, 19.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 1.0000000000000009} |
| 24h成交量 / 流动性 USD | [989227.0551619999, 571767.3087] |
| 价差 pp | 1.00 |
| 到期 | 2026-12-09T23:59:00+00:00 |
| 结算规则摘要 | 以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。 |
| 规则指纹 | 933a10a15eeec0ff1de30468fa20540301ed243f75cc3572d42946192f81a123 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-13T12:01:55.979306Z |
| 抓取时间 | 2026-11-13T12:02:59.317380+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-december-20260729232808632 |

## Will the Fed increase interest rates by 50+ bps after the December 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 770450 / 3215009 |
| Yes 概率 % | 9.15 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.8, 8.6] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -1.0999999999999996} |
| 24h成交量 / 流动性 USD | [649568.417569, 359570.46946] |
| 价差 pp | 0.10 |
| 到期 | 2026-12-09T23:59:00+00:00 |
| 结算规则摘要 | 衡量12月8–9日该次FOMC前后联邦基金目标区间上限上调至少50bp；非标准变化向上取整到最近25bp对应档。按正式声明，若下一次会议结束仍无声明则按不变档处理。不是全年累计加息幅度。 |
| 规则指纹 | a05ecc7aefe678e9936425027277135b8c37cdaf659af595020eb1668ec48e58 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-13T12:01:55.979306Z |
| 抓取时间 | 2026-11-13T12:02:59.317380+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-december-20260729232808632 |

## US x Iran Effective Ceasefire by November 15?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1337182 / 6831494 |
| Yes 概率 % | 36.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-16.0, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -6.5} |
| 24h成交量 / 流动性 USD | [99708.46617300001, 64473.454] |
| 价差 pp | 1.00 |
| 到期 | 2026-11-15T20:29:00+00:00 |
| 结算规则摘要 | 须完成连续14个伊朗标准时间日，美国未对伊朗陆地及内水实施命中目标的合资格空袭/地对地导弹攻击，且该14天首日在创建后至11月15日范围内；最后一次合资格行动次日为首日，无行动则创建日为首日。拦截碎片、威胁、海域/领空、地面入侵、网络、小型武器/部分小型袭击等不算。第14日后再留3个日历日报道窗口，按官方信息及可信报道综合裁定。不是双方全面停火，也不要求14天在15日前完成。 |
| 规则指纹 | c70e370d0e95bf9245a1a527f4f02bb307f13aa2766e1cc24004c7559bfb4b53 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-13T12:01:55.979306Z |
| 抓取时间 | 2026-11-13T12:02:59.317380+00:00 |
| 来源 | https://polymarket.com/event/us-x-iran-effective-ceasefire-begins-by-2-week-pause-20261108 |

## Strait of Hormuz traffic returns to normal by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 455875 / 2176270 |
| Yes 概率 % | 5.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-2.0, -4.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -1.0000000000000002} |
| 24h成交量 / 流动性 USD | [94694.677987, 242705.383] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。 |
| 规则指纹 | b0c8ba27f4437b0d8ab819ae170bec118166232e39cdcaefb95bd352d29073d4 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-13T11:59:56.309984Z |
| 抓取时间 | 2026-11-13T12:02:59.317380+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31 |

## AI bubble burst in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 691340 |
| Yes 概率 % | 6.75 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-5.7, -1.05] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.15000000000000013} |
| 24h成交量 / 流动性 USD | [83382.626974, 139577.91391] |
| 价差 pp | 0.30 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | fc153b2136a8dfbadcd169dce1add40690acb1748566b99716fe7ae8fcb07330 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-13T11:59:56.309984Z |
| 抓取时间 | 2026-11-13T12:02:59.317380+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## New NVIDIA CEO named by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1367877 / 6977205 |
| Yes 概率 % | 18.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-25.0, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -6.0} |
| 24h成交量 / 流动性 USD | [42662.85372600001, 26443.0415] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59纽约时间前，英伟达正式宣布黄仁勋的CEO继任者即满足；实际就任可以更晚，临时CEO不计。以公司公开声明为主要来源，可参照可信报道共识。与离任宣布合约不同。 |
| 规则指纹 | 09c6c6ee9faa8f03a8b6caf37ffb4757f33e53eedba525eae02360d329bf2d68 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-13T12:01:55.979306Z |
| 抓取时间 | 2026-11-13T12:02:59.317380+00:00 |
| 来源 | https://polymarket.com/event/new-nvidia-ceo-named-by-december-31-2026 |

## Tesla and SpaceX merger officially announced by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 192962 / 2252540 |
| Yes 概率 % | 30.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [20.5, 20.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 1.9999999999999962} |
| 24h成交量 / 流动性 USD | [29041.766064, 24809.7707] |
| 价差 pp | 2.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59纽约时间前，Tesla或SpaceX正式宣布双方合并或一方收购另一方的控制权即Yes；无需在期限内完成交易。控制权通常为过半权益或等效治理权；少数股权投资及仅讨论不算。以公司公告或可信报道共识核验；旧URL中的june-30不是本合约期限。 |
| 规则指纹 | 909906ae3b6db7e473468713ea6a1e1e4cf4c931fe247c7d3d576e7986513008 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-13T12:01:55.979306Z |
| 抓取时间 | 2026-11-13T12:02:59.317380+00:00 |
| 来源 | https://polymarket.com/event/tesla-and-spacex-merger-officially-announced-by-june-30 |

## Russia x Ukraine energy ceasefire agreement by November 15, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1360126 / 6947935 |
| Yes 概率 % | 0.95 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-2.1, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -1.25} |
| 24h成交量 / 流动性 USD | [15671.485143999998, 34890.78789] |
| 价差 pp | 0.30 |
| 到期 | 2026-11-15T21:59:00+00:00 |
| 结算规则摘要 | 11月15日23:59基辅时间前，俄乌双方同意暂停打击至少一类明确能源设施，双方官宣或可信报道共识确认；美国第三方单方声称不足。可限定地理范围，但仅一个设施不算；必须明确相互暂停，不是谈判/换囚。约定生效日可晚于截止。 |
| 规则指纹 | a3874db8482536581cb7832c287d198abdb207e6448a0fd10b7da294d17de561 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-13T12:01:55.979306Z |
| 抓取时间 | 2026-11-13T12:02:59.317380+00:00 |
| 来源 | https://polymarket.com/event/russia-x-ukraine-energy-ceasefire-agreement-by |

## Russia x Ukraine ceasefire agreement by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 478472 / 2243897 |
| Yes 概率 % | 10.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-4.0, -5.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [14777.266203000005, 83058.9392] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年末23:59ET前，双方官宣或可信共识确认相互暂停直接交战，包含明确生效日的全面暂停；仅限定目标/地点的局部能源安排不算。达成协议可先于实际生效，单方暂停不算。 |
| 规则指纹 | 2ea22f9548269db3205e41396a99073a2d5788dc4fde17989e34c8051ae6b75b |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-13T12:01:55.979306Z |
| 抓取时间 | 2026-11-13T12:02:59.317380+00:00 |
| 来源 | https://polymarket.com/event/russia-x-ukraine-ceasefire-agreement-by |

## AI bubble burst by June 30, 2027?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 4838928 |
| Yes 概率 % | 23.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-2.0, -3.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -2.500000000000002} |
| 24h成交量 / 流动性 USD | [12655.833032999997, 73810.0271] |
| 价差 pp | 1.00 |
| 到期 | 2027-07-01T03:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | bd0420587e08487fffa5050e7fd9b79ffff909a9f843d3f620207ee859462505 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-13T11:57:55.910962Z |
| 抓取时间 | 2026-11-13T12:02:59.317380+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## Will WTI Crude Oil (WTI) hit (HIGH) $110 in November?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1250301 / 6172751 |
| Yes 概率 % | 4.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-1.0, -12.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -1.5} |
| 24h成交量 / 流动性 USD | [4171.940699, 30628.0633] |
| 价差 pp | 1.00 |
| 到期 | 2026-12-01T04:59:59.999000+00:00 |
| 结算规则摘要 | 11月合资格交易时段，Pyth对ICE Europe WTI活跃月CLL的任一最终1分钟High达到110美元即Yes；按原值不取整，最后三个交易日换月。主数据不可用时依ICE官方日高低。与Yahoo NYMEX连续WTI代理不是同一可直接裁决序列。 |
| 规则指纹 | 97cca376098aad5ff8f5ece05abb9ae13f218bc5005dc802696a1f1922949a52 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-13T12:01:55.979306Z |
| 抓取时间 | 2026-11-13T12:02:59.317380+00:00 |
| 来源 | https://polymarket.com/event/what-price-will-wti-hit-in-november-2026 |

## CoreWeave downgraded by Moody's or S&P by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1219851 / 5939467 |
| Yes 概率 % | 17.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.5, -4.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.5000000000000004} |
| 24h成交量 / 流动性 USD | [null, 235.716] |
| 价差 pp | 13.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59ET前，Moody’s或S&P正式下调CoreWeave长期主体/企业家族或高级无担保债信用评级则Yes；仅负面展望/观察名单不算，不要求降至某统一评级档。成交很薄，不视为客观违约概率。 |
| 规则指纹 | 040e522db15913bd31de0e1a7f935727361429e7c42b3c1fc5286a0cf1b0fc42 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"] |
| 元数据更新（不是成交时间） | 2026-11-13T12:01:55.979306Z |
| 抓取时间 | 2026-11-13T12:02:30.847067+00:00 |
| 来源 | https://polymarket.com/event/coreweave-downgraded-by-moodys-or-sp-by |

## AI 压力：合约、经营与估值分开

合约、压力和公司估值分开：AI泡沫2026为6.75%，较早报6.6%升0.15个百分点；2027年6月合约23.5%，较26%降2.5个百分点。期限及结算规则不同，不相减推导崩溃概率。永久NVDA CEO宣布合约18.5%，较24.5%降6个百分点，规则排除临时任命。[公司公告](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-CEO-Transition/default.aspx)中的Kress临时CEO安排仍有效，未核验永久继任公告；NVDA盘前169.60较166.19昨收改善，但未恢复170.24观察线。[微软状态页](https://status.cloud.microsoft/)12:00:37UTC更新显示Microsoft365地区恢复改善、部分用户仍间歇受影响；Azure面板未显示当前问题，不能把本次事故泛化为Azure全面中断。MSFT515.02较昨收523下跌约1.53%，因果可能同时受故障、利率和市场影响，不做单因解释。[ENGIE与Google意向](https://newsroom.engie.com/actualites/engie-et-google-s-associent-pour-developper-les-solutions-energetiques-d-un-projet-de-data-center-envisage-pres-de-chateauroux-en-france-07134-ff316.html)讨论法国候选数据中心能源、储能与电网灵活性，仍待后续协议和项目实施；是需求线索而非已落实合同。[H100指数](https://www.silicondata.com/products/silicon-index/h100)仍为12日3.06美元/GPU小时，没有达到≤1连续5天压力阈值。复用早报已核验的12日CSCO、AMAT、NBIS与CBRS财报：本轮没有新季度数字，股价却分化，CSCO99.06较102.01下降、AMAT384略高于380.95、CBRS113高于97.75、NBIS127.50低于128.64。不能把收入增长等同现金转化或全面估值扩张；CBRS当前IR重试失败，财务事实来源为早报核验记录。五家SEC本轮均检查成功，最新定期披露仍NVDA8月26日、MSFT10月28日、AMZN10月30日、GOOGL10月29日、META10月22日。复用财务底稿；Daily估值按12日完整收盘价计算，盘前价格另列用于观察，未混入估值端点。仅NVDA FCFF输入齐全，其余四家明确缺口。五年公司整体估值不是纯AI估值，治理风险也不自动等于现金流预测下调。

## NVDA · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | scenario_analysis |
| 财务底稿 | TTM 至 2026-07-26；最新 10-Q / filed 2026-08-26 |
| 披露检查 | {"checked_at": "2026-11-13T12:04:46.115409+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001045810.json", "latest_filing_date": "2026-08-26"} |
| 观测财务数据 | {"ttm_revenue_million": 302970, "revenue_quarters": [{"end": "2025-10-26", "value": 57006000000, "filed": "2025-11-19", "duration_days": 91}, {"end": "2026-01-25", "value": 68127000000, "filed": "2026-02-25", "duration_days": 91}, {"end": "2026-04-26", "value": 81615000000, "filed": "2026-05-20", "duration_days": 91}, {"end": "2026-07-26", "value": 96221000000, "filed": "2026-08-26", "duration_days": 91}], "cash_million": 22443.0, "liquid_investments_million": 34143.0, "debt_million": 33366.0, "finance_lease_million": 0, "diluted_shares_million": 24285.0, "latest_operating_income_million": 63734.0, "observed_end": "2026-07-26", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "Revenues", "latest_reported_revenue_million": 96221.0, "income_statement_window": "最近单季度", "ttm_bridge_note": "采用同版 FY2026全年 + FY2027半年 - FY2026半年；与四季逐项求和差1百万为披露舍入差。"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json", "https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。10-Q Note14 表明融资租赁费用不重大；模型按不重大近似零，不将其称为精确零负债。未确认担保仅作为压力情景，非已到期净债务。市场化股权42783和非市场化股权51157不作为类现金；非经营资产加回为0的保守假设。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | 无 |
| 价格 USD | 166.19 |
| 基期输入 USD million / million shares | {"revenue": 302970, "net_debt": -23220.0, "diluted_shares": 24285.0, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.2204894492071755, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## NVDA · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 98.77 | -40.57 | 14.00 | 60.00 | 12.00 | 68.42 |
| 基准 | 154.12 | -7.26 | 20.00 | 65.00 | 11.00 | 74.20 |
| 乐观 | 242.58 | 45.97 | 26.00 | 70.00 | 10.00 | 79.05 |

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
| 披露检查 | {"checked_at": "2026-11-13T12:04:49.063410+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0000789019.json", "latest_filing_date": "2026-10-28"} |
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
| 披露检查 | {"checked_at": "2026-11-13T12:04:52.039798+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001018724.json", "latest_filing_date": "2026-10-30"} |
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
| 披露检查 | {"checked_at": "2026-11-13T12:04:54.502371+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001652044.json", "latest_filing_date": "2026-10-29"} |
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
| 披露检查 | {"checked_at": "2026-11-13T12:04:59.185556+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001326801.json", "latest_filing_date": "2026-10-22"} |
| 观测财务数据 | {"revenue_million": 64601, "operating_cashflow_million": 32790, "reported_capex_including_finance_lease_principal_million": 34910, "company_defined_fcf_million": -2120, "diluted_shares_million": 2573, "reported_operating_income_million": 12988, "legal_charge_million": 9900, "observed_end": "2026-09-30", "published_at": "2026-10-21T16:01:00-04:00", "unit": "USD million; shares million", "noncancelable_commitments_million": 454520, "leases_not_commenced_million": 355730, "contingent_cloud_capacity_max_million": 14720, "restricted_cash_reclassified_million": 10800, "commitments_due_2026_million": 45850, "commitments_due_2027_million": 121410} |
| 来源 | ["https://www.prnewswire.com/news-releases/meta-reports-third-quarter-2026-results-302915964.html", "https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm", "https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Announces-Launch-of-Offering-of-Depositary-Shares-Representing-Series-A-Mandatory-Convertible-Preferred-Stock-and-Offering-of-Class-A-Common-Stock-in-Connection-with-Forward-Sale-Agreements/default.aspx", "https://www.prnewswire.com/news-releases/meta-announces-pricing-of-offering-of-depositary-shares-representing-series-a-mandatory-convertible-preferred-stock-and-offering-of-class-a-common-stock-in-connection-with-forward-sale-agreements-302920247.html"] |
| 口径 | 公司FCF扣除融资租赁本金，不能直接代替模型FCFF；融资租赁负债/新增资产未齐，不假设零。法律费用不全归AI经营。 |
| 主观假设说明 | 缺失 |
| 权益桥额外假设 | 无 |
| 缺失原因 | 沿用底稿的历史核验说明（其中“本次”指原核验日）；本轮最新定期财报列表检查见disclosure_check。22日10-Q已核验，本次无新增定期财报。27日普通股625美元定价、优先票息6.5%已核验；完整融资租赁负债/新增资产、优先权益/远期发行与现金到账桥未齐，不用不同承诺简单充当现有债务，暂停精确FCFF反推。 |

## 宽基修复升级需要再测试

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | PPI和下一交易日承接 |
| 关联标的 | ["SPY", "QQQ", "RSP", "IWM"] |
| 确认条件 | SPY755、QQQ680–682重新回踩守稳并形成更高低点；可靠分钟数据下站稳常规VWAP；随后收复SPY763.04、QQQ694.56日高并保持到收盘，RSP/IWM同步改善 |
| 失效条件 | 再失755/680且反抽失败，或只有权重上涨而广度继续恶化，撤销升级判断 |
| 观察期限 | 未来1–3个常规交易日；NVDA延伸至11月17日财报 |
| 反证 | 12日已经穿过原支撑，不能重写成全天守住；盘后上涨流动性和覆盖率有限 |
| 状态 | 盘前尚未确认；PPI后与开盘后复查 |

## 芯片必须增加治理和价格双确认

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 领导过渡、盘后财报与17日NVDA业绩 |
| 关联标的 | ["SMH", "NVDA", "MU"] |
| 确认条件 | SMH收复506.96后回踩守稳，再观察520.79–523.54均线区；NVDA形成更高低点并收复170.24，公告与订单兑现没有新增反证；MU重新站回20日约843后观察承接 |
| 失效条件 | SMH再失490反抽失败或失484.50日低；NVDA再向148.80低点扩展，或出现可核验交付/客户恶化 |
| 观察期限 | 未来1–3个常规交易日；NVDA延伸至11月17日财报 |
| 反证 | AMD等个股上涨可能来自竞争重估，不能替代SMH/NVDA确认；杠杆ETF每日重置放大波动路径损耗 |
| 状态 | 盘前改善但尚未越过关键线 |

## 非芯片相对强势备选

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 利率冲击后的板块再平衡 |
| 关联标的 | ["XLI", "XLV", "XLP", "XLF"] |
| 确认条件 | 大盘不再创新低；XLI守20日167.77并重夺200日172.77，XLV/XLP分别守183.04/89.25且持续相对SPY领先；XLF守56.90同时信用利差不恶化 |
| 失效条件 | 各自均线失守并反抽失败，或利率/信用压力导致强弱关系反转 |
| 观察期限 | 未来1–3个常规交易日；NVDA延伸至11月17日财报 |
| 反证 | 相对强势可与绝对下跌同时出现；没有当期申赎证据，不声称主力已建仓 |
| 状态 | 观察项，未确认 |

## 能源只作条件式观察

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | PPI、油价与地缘变化 |
| 关联标的 | ["XLE", "XOP"] |
| 确认条件 | 油价上行能够延续，XLE/XOP分别重夺20日66.33/191.56并有回踩承接；同时核验盈利受益不是单日冲击 |
| 失效条件 | 油价涨幅快速回吐或正式消息缓解供给风险，ETF突破失败 |
| 观察期限 | 未来1–3个常规交易日；NVDA延伸至11月17日财报 |
| 反证 | IEA新增供需转松预测构成反证；陆上低库存与地缘风险仍在，油价和ETF需共同确认。 |
| 状态 | 观察项，未确认 |

## 跨期比较与上期剧本复核

对照13日早报：同一12日完整交易尚无新收盘，因此宽度、均线和支撑穿越结论不重置。盘前SPY759.40/QQQ690.21/SMH505.00，相对早报盘后758.51/690.23/505.99并非全面增强；NVDA169.60较167.02改善，仍低170.24。早报的脆弱分化修复判断保留，没有达到趋势反转条件。早报CNN缺口已补为39；微软服务本轮取得官方恢复进展，但仍有间歇问题；IEA供需预测为能源多头新增反证。Cboe官方12日数据已到齐，原滞后提示解除。13日常规市场尚未开盘，不能声称今天回踩已守住或已站稳常规VWAP。同ID同定义预测变化：Strait of Hormuz traffic returns to normal by December 31?：-1.00个百分点；Will the Fed increase interest rates by 25 bps after the December 2026 meeting?：+1.00个百分点；AI bubble burst in 2026?：+0.15个百分点；AI bubble burst by June 30, 2027?：-2.50个百分点；Tesla and SpaceX merger officially announced by December 31?：+2.00个百分点；US x Iran Effective Ceasefire by November 15?：-6.50个百分点；Will the Fed increase interest rates by 50+ bps after the December 2026 meeting?：-1.10个百分点；CoreWeave downgraded by Moody's or S&P by December 31, 2026?：-0.50个百分点；Russia x Ukraine energy ceasefire agreement by November 15, 2026?：-1.25个百分点；Russia x Ukraine ceasefire agreement by December 31, 2026?：+0.00个百分点；Will WTI Crude Oil (WTI) hit (HIGH) $110 in November?：-1.50个百分点；New NVIDIA CEO named by December 31, 2026?：-6.00个百分点。临时CEO与永久CEO合约必须分开。

## 可计算的跨期变化

```json
[
  {
    "mode": "daily",
    "baseline": "reports/daily/2026-11-12/20261112T232709.661331Z/evidence.json",
    "baseline_cutoff": "2026-11-12T23:26:47.425382+00:00",
    "close_change_pct": {
      "SPY": 0.0,
      "QQQ": 0.0,
      "IWM": 0.0,
      "RSP": 0.0,
      "GLD": 0.0,
      "GC=F": 0.10305825238137167,
      "CL=F": -0.1125601961314393,
      "BZ=F": 0.052211604375607124,
      "TLT": 0.0,
      "UUP": 0.0,
      "HYG": 0.0,
      "LQD": 0.0,
      "^VIX": 0.0,
      "^VIX3M": 0.0,
      "^VVIX": 0.0,
      "^MOVE": -0.0002015278446010349,
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
        "change_pct": 0.11744089590475237,
        "from_observed_at": "2026-11-12T23:17:01+00:00",
        "to_observed_at": "2026-11-13T12:01:49+00:00"
      },
      "QQQ": {
        "change_pct": -0.002651290533783879,
        "from_observed_at": "2026-11-12T23:17:52+00:00",
        "to_observed_at": "2026-11-13T12:02:25+00:00"
      },
      "SMH": {
        "change_pct": -0.19565604063321862,
        "from_observed_at": "2026-11-12T23:13:09+00:00",
        "to_observed_at": "2026-11-13T12:01:52+00:00"
      },
      "NVDA": {
        "change_pct": 1.5419710214345628,
        "from_observed_at": "2026-11-12T23:17:55+00:00",
        "to_observed_at": "2026-11-13T12:02:30+00:00"
      },
      "MSFT": {
        "change_pct": -1.3069139966273235,
        "from_observed_at": "2026-11-12T23:17:42+00:00",
        "to_observed_at": "2026-11-13T12:02:25+00:00"
      },
      "AMZN": {
        "change_pct": 0.9159650938591613,
        "from_observed_at": "2026-11-12T23:17:41+00:00",
        "to_observed_at": "2026-11-13T12:01:49+00:00"
      },
      "GOOGL": {
        "change_pct": 0.7934391252166995,
        "from_observed_at": "2026-11-12T23:17:38+00:00",
        "to_observed_at": "2026-11-13T12:02:26+00:00"
      },
      "META": {
        "change_pct": -0.16159999999999508,
        "from_observed_at": "2026-11-12T23:17:51+00:00",
        "to_observed_at": "2026-11-13T12:02:01+00:00"
      }
    },
    "macro_change": {
      "DGS2": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-11-10"
      },
      "BAMLH0A0HYM2": {
        "change": 0.0,
        "unit": "percentage_points",
        "observation_date": "2026-11-11"
      },
      "BAMLC0A0CM": {
        "change": 0.0,
        "unit": "percentage_points",
        "observation_date": "2026-11-11"
      },
      "DGS10": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-11-10"
      },
      "DFII10": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-11-10"
      },
      "T10YIE": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-11-12"
      },
      "STLFSI4": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-11-06"
      },
      "CBOE_VIX": {
        "change": 1.2100000000000009,
        "unit": "index",
        "observation_date": "2026-11-12"
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
        "change_pp": 1.0000000000000009
      },
      "3215009": {
        "status": "comparable",
        "change_pp": -1.0999999999999996
      },
      "6831494": {
        "status": "comparable",
        "change_pp": -6.5
      },
      "2176270": {
        "status": "comparable",
        "change_pp": -1.0000000000000002
      },
      "691340": {
        "status": "comparable",
        "change_pp": 0.15000000000000013
      },
      "6977205": {
        "status": "comparable",
        "change_pp": -6.0
      },
      "2252540": {
        "status": "comparable",
        "change_pp": 1.9999999999999962
      },
      "6947935": {
        "status": "comparable",
        "change_pp": -1.25
      },
      "2243897": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "4838928": {
        "status": "comparable",
        "change_pp": -2.500000000000002
      },
      "6172751": {
        "status": "comparable",
        "change_pp": -1.5
      },
      "5939467": {
        "status": "comparable",
        "change_pp": -0.5000000000000004
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
    "event": "10月PPI，北京13日21:30；CPI已10日发布",
    "date": "2026-11-13T08:30:00-05:00",
    "source": "https://www.bls.gov/schedule/2026/11_sched.htm"
  },
  {
    "event": "10月进口/出口价格，北京17日21:30",
    "date": "2026-11-17T08:30:00-05:00",
    "source": "https://www.bls.gov/schedule/2026/11_sched.htm"
  },
  {
    "event": "NVDA财报预计16:20EST，电话会17:00EST；北京时间18日05:20/06:00",
    "date": "2026-11-17T16:20:00-05:00",
    "source": "https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-CEO-Transition/default.aspx"
  },
  {
    "event": "英伟达永久CEO任命与经营连续性披露，时间未定；临时CEO已公布",
    "date": null,
    "source": "https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-CEO-Transition/default.aspx"
  }
]
```

## 新闻事件去重与时间

| 事件 | 摘要 | 发生时间（未知留空） | 各来源发布时间 / 抓取时间 |
| --- | --- | --- | --- |
| 20261113-msstatus | Microsoft365恢复改善，部分间歇故障仍在；Azure面板未显示当前问题。 | 2026-11-13T12:00:37+00:00 | [{"source": "https://status.cloud.microsoft/", "published_at": null, "retrieved_at": "2026-11-13T12:10:10.023178+00:00"}] |
| 20261113-iea | IEA月报预计4Q26供应趋松，海上库存增加但陆上库存仍低。 | 缺失 | [{"source": "https://www.iea.org/reports/oil-market-report-november-2026", "published_at": null, "retrieved_at": "2026-11-13T12:10:10.023178+00:00"}] |
| 20261113-engie | Google法国数据中心能源合作是MoU，须后续协议和项目实施。 | 缺失 | [{"source": "https://newsroom.engie.com/actualites/engie-et-google-s-associent-pour-developper-les-solutions-energetiques-d-un-projet-de-data-center-envisage-pres-de-chateauroux-en-france-07134-ff316.html", "published_at": null, "retrieved_at": "2026-11-13T12:10:10.023178+00:00"}] |
| 20261113-iran | 伊朗核监督立场仍有冲突，未据此确认已生效停火。 | 缺失 | [{"source": "https://apnews.com/article/a689242aa635c103033790bacbff7f07", "published_at": "2026-11-13T10:12:48+00:00", "retrieved_at": "2026-11-13T12:10:10.023178+00:00"}] |
| 20261113-ukraine | 会谈与欧洲斡旋进展不等于正式停火协议。 | 缺失 | [{"source": "https://apnews.com/article/2a96d57210055edd2e76f71693e0a37c", "published_at": "2026-11-13T05:20:30+00:00", "retrieved_at": "2026-11-13T12:10:10.023178+00:00"}] |
| 20261113-nv | 12日领导过渡公告仍为最新核验安排，永久继任未确认。 | 缺失 | [{"source": "https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-CEO-Transition/default.aspx", "published_at": null, "retrieved_at": "2026-11-13T12:10:10.023178+00:00"}] |

## 覆盖范围与数据缺口

```json
[
  "tc统一请求时间不能当成交时间；核心报价另取Yahoo分钟时间，原始响应保留本地。",
  "盘前还没有13日常规VWAP；早报分钟量异常，未据此重复计算或虚构回踩承接。",
  "19ETF仅观察池，完整涨跌家数与指数成分宽度缺失；RSP盘前报价较旧，未作当前广度确认。",
  "CNN API仍418，但官方浏览器页面已核验39，故数值缺口已补；Cboe官方CSV已更新12日18.70。",
  "FRED收益率至10日、信用至11日；另核验财政部12日2Y/10Y，今天实时现金债收益率缺失。",
  "GPR序列仍止2日；不把下载时间当战争事件发生时间。",
  "tc两批各50且has_more，Gamma15组limit10多组截断，新闻和预测覆盖不保证完整。",
  "ICI最近窗口截至4日，发行人SMH更新至12日但连续份额/拆分缺失；无当期可核验净申赎，不称主力流入。",
  "CRWV降级合约价差13个百分点、24h成交量缺失，质量较低；不将中价17.5%当精确信号。",
  "五家财报检查成功；除NVDA外四家完整FCFF桥仍缺失，不编造估值。",
  "DRAM历史不足200日；期货、现金债与股票时点/口径分开。",
  "CBRS当前IR读取失败，财务数值沿用早报明确核验版本；tc部分评级/合同线索仍未证实，不作为事实。",
  "微软仅代表本次官方状态页观察；恢复仍进行，不泛化Azure故障，不凭该页面计算收入损失。",
  "预测合约截止不是事件日期；未来一周及30天无新增满足精选标准的准确日期合约，不强填upcoming。",
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
  "history.DRAM: insufficient_history",
  "macro.GPRD: missing_or_stale",
  "macro.GPRD_ACT: missing_or_stale",
  "macro.GPRD_THREAT: missing_or_stale",
  "macro.GPRD_MA7: missing_or_stale",
  "macro.GPRD_MA30: missing_or_stale",
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
  "Polymarket 临近事件：本次未纳入合格合约，见搜索说明",
  "指标缺失/历史不足: prices.^VIX.volume_vs_previous20_ratio, prices.^VIX3M.volume_vs_previous20_ratio, prices.^VVIX.volume_vs_previous20_ratio, prices.^MOVE.volume_vs_previous20_ratio, prices.DRAM.sma200, prices.DRAM.distance_sma200_pct",
  "本轮浏览器安全策略禁止file协议，未绕过；HTML同源与结构检查通过，但本次本地页面视觉复验未完成。"
]
```

## 来源、时间与核验记录

```json
[
  {
    "url": "https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-CEO-Transition/default.aspx",
    "checked_at": "2026-11-13T12:10:10.023178+00:00",
    "note": "本轮核验；页面只给日期时不猜具体发布时间。"
  },
  {
    "url": "https://edition.cnn.com/markets/fear-and-greed",
    "checked_at": "2026-11-13T12:10:10.023178+00:00",
    "note": "本轮核验；页面只给日期时不猜具体发布时间。"
  },
  {
    "url": "https://status.cloud.microsoft/",
    "checked_at": "2026-11-13T12:10:10.023178+00:00",
    "note": "本轮核验；页面只给日期时不猜具体发布时间。"
  },
  {
    "url": "https://www.iea.org/reports/oil-market-report-november-2026",
    "checked_at": "2026-11-13T12:10:10.023178+00:00",
    "note": "本轮核验；页面只给日期时不猜具体发布时间。"
  },
  {
    "url": "https://newsroom.engie.com/actualites/engie-et-google-s-associent-pour-developper-les-solutions-energetiques-d-un-projet-de-data-center-envisage-pres-de-chateauroux-en-france-07134-ff316.html",
    "checked_at": "2026-11-13T12:10:10.023178+00:00",
    "note": "本轮核验；页面只给日期时不猜具体发布时间。"
  },
  {
    "url": "https://www.bls.gov/schedule/2026/11_sched.htm",
    "checked_at": "2026-11-13T12:10:10.023178+00:00",
    "note": "本轮核验；页面只给日期时不猜具体发布时间。"
  },
  {
    "url": "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value_month=202611&type=daily_treasury_yield_curve",
    "checked_at": "2026-11-13T12:10:10.023178+00:00",
    "note": "本轮核验；页面只给日期时不猜具体发布时间。"
  },
  {
    "url": "https://www.ici.org/research/stats/etf_flows",
    "checked_at": "2026-11-13T12:10:10.023178+00:00",
    "note": "本轮核验；页面只给日期时不猜具体发布时间。"
  },
  {
    "url": "https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/overview/",
    "checked_at": "2026-11-13T12:10:10.023178+00:00",
    "note": "本轮核验；页面只给日期时不猜具体发布时间。"
  },
  {
    "url": "https://www.silicondata.com/products/silicon-index/h100",
    "checked_at": "2026-11-13T12:10:10.023178+00:00",
    "note": "本轮核验；页面只给日期时不猜具体发布时间。"
  },
  {
    "url": "https://apnews.com/article/a689242aa635c103033790bacbff7f07",
    "checked_at": "2026-11-13T12:10:10.023178+00:00",
    "note": "本轮核验；页面只给日期时不猜具体发布时间。"
  },
  {
    "url": "https://apnews.com/article/2a96d57210055edd2e76f71693e0a37c",
    "checked_at": "2026-11-13T12:10:10.023178+00:00",
    "note": "本轮核验；页面只给日期时不猜具体发布时间。"
  },
  {
    "url": "reports/daily/2026-11-12/20261112T232709.661331Z/evidence.json",
    "checked_at": "2026-11-13T12:10:10.023178+00:00",
    "note": "CSCO/AMAT/NBIS/CBRS财报事实复用早报核验底稿，非本轮新增季度披露；CBRS官网本次读取失败。"
  }
]
```

## 付费信源建议（未订阅）

```json
[]
```
