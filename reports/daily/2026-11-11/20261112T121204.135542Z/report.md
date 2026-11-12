# 每日交易总结 · 2026-11-11

## 一分钟读懂 · Agent 摘要

### 当前判断

目前仍是脆弱修复，尚不能升级为可靠反弹。宽基离关键支撑不远，芯片承受更集中的事件风险。

### 与上次相比

相对早报盘后，SPY、QQQ、SMH和NVDA略有回升，但都未回到11日收盘。正式人事结果仍待核验；新增参议员要求保全出口相关记录的公开信。

### 最重要的信号

- 约20:03北京时间：SPY756.46、QQQ684.39、SMH493.00；NVDA160.28，较收盘-7.74%。
- 最新完整日线量能修订后，SPY/QQQ仅为前20日均量0.79/0.86倍；中期均线压力仍在。
- VIX盘前约18.30高于昨收17.49；新任正式CEO合约41.5%，与离任宣布77.5%并非同一问题。

### 接下来观察

- 开盘后先看SPY755、QQQ680–682、SMH490–493能否回踩守住，再看常规VWAP、更高低点和收盘保持。
- 优先观察非芯片相对强势的工业、医疗、必需消费；芯片需额外核验治理公告与板块承接，避免仅看涨幅追逐杠杆。
- 北京时间今晚21:00 NBIS电话会、明晚21:30 PPI、18日凌晨NVDA业绩。

### 不要忽略

盘前流动性较低；CNN最新值、完整广度、当期单ETF申赎缺失。收盘量能被数据源修订，不是今晚新增成交。预测合约报价不是客观概率。

## 研究结论

11月12日晚报：宽基尚守观察区，芯片治理冲击未解除；盘前小幅回升不足以确认反弹可靠。

## 时点与口径

| 项目 | 内容 |
| --- | --- |
| 模式 | 每日交易总结 |
| 常规交易窗口 | 2026-11-11 → 2026-11-11（纽约交易日） |
| 截止·纽约 | 2026-11-12T07:10:23.040086-05:00 |
| 截止·北京 | 2026-11-12T20:10:23.040086+08:00 |
| 实际生成时间 | 2026-11-12T12:10:24.810458+00:00 |
| 市场阶段 | 盘前 |
| 下一交易日 | 2026-11-12 |
| 运行重点 | 全市场 |
| 上一版本 | reports/daily/2026-11-11/20261111T232944.645060Z/evidence.json |
| 质量 | partial |
| Daily 北京时间计划时段 | 2026-11-12T20:00:00+08:00 |

## 采集、补查与剩余缺口

| 目标 | 补查结果 | 来源 | 观测 / 抓取时间 | 说明 |
| --- | --- | --- | --- | --- |
| 1219851 | 已校验接入 | https://gamma-api.polymarket.com/events/1219851 | 2026-11-12T12:03:09.022076+00:00 / 2026-11-12T12:03:09.022076+00:00 | Gamma observation; metadata timestamp is not trade time |
| 478472 | 未接入 | 缺失 |  /  | 没有可核验的活跃Yes合约 |
| 1250301 | 未接入 | 缺失 |  /  | 没有可核验的活跃Yes合约 |

## 仍需核验的数据与影响

| 数据 | 状态 | 需要核验 | 影响 |
| --- | --- | --- | --- |
| prices.^MOVE | missing_or_stale | 2026-11-11 已完成常规交易日价格；指标需同源复权历史 | 降低相关判断可信度；保留缺口 |
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
| prices.SPY.value | 759.81 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_1d_pct | 1.32 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_5d_pct | -0.91 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_20d_pct | -1.27 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_60d_pct | -0.75 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_1d_pp | 0.00 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_5d_pp | 0.00 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_20d_pp | 0.00 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_60d_pp | 0.00 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma20 | 760.20 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma50 | 764.55 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma200 | 728.65 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma20_pct | -0.05 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma50_pct | -0.62 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma200_pct | 4.28 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_sma | 12.15 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_pct | 1.60 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.drawdown_from_63d_high_pct | -2.47 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.volume_vs_previous20_ratio | 0.79 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SPY/history/ |
| prices.QQQ.value | 690.38 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_1d_pct | 2.31 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_5d_pct | -0.23 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_20d_pct | -5.29 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_60d_pct | -3.68 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_1d_pp | 1.00 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_5d_pp | 0.69 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_20d_pp | -4.02 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_60d_pp | -2.93 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma20 | 698.94 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma50 | 718.87 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma200 | 680.65 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma20_pct | -1.22 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma50_pct | -3.96 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma200_pct | 1.43 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_sma | 17.69 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_pct | 2.56 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.drawdown_from_63d_high_pct | -9.12 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.volume_vs_previous20_ratio | 0.86 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.IWM.value | 283.09 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_1d_pct | 0.89 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_5d_pct | -0.33 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_20d_pct | 4.32 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_60d_pct | -5.46 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_1d_pp | -0.42 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_5d_pp | 0.59 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_20d_pp | 5.59 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_60d_pp | -4.71 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma20 | 277.85 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma50 | 281.31 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma200 | 278.31 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma20_pct | 1.88 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma50_pct | 0.63 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma200_pct | 1.72 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_sma | 5.23 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_pct | 1.85 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.drawdown_from_63d_high_pct | -6.97 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.volume_vs_previous20_ratio | 0.68 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IWM/history/ |
| prices.RSP.value | 222.65 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_1d_pct | 0.80 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_5d_pct | -0.30 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_20d_pct | 4.98 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_60d_pct | 1.68 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_1d_pp | -0.52 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_5d_pp | 0.61 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_20d_pp | 6.25 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_60d_pp | 2.43 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma20 | 218.02 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma50 | 214.72 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma200 | 207.46 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma20_pct | 2.13 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma50_pct | 3.69 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma200_pct | 7.32 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_sma | 2.98 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_pct | 1.34 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.drawdown_from_63d_high_pct | -0.30 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.volume_vs_previous20_ratio | 0.57 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/RSP/history/ |
| prices.GLD.value | 365.17 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_1d_pct | -1.13 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_5d_pct | -1.97 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_20d_pct | -2.88 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_60d_pct | -8.38 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_1d_pp | -2.45 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_5d_pp | -1.05 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_20d_pp | -1.61 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_60d_pp | -7.63 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma20 | 371.50 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma50 | 382.96 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma200 | 409.82 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma20_pct | -1.70 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma50_pct | -4.65 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma200_pct | -10.89 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_sma | 7.13 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_pct | 1.95 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.drawdown_from_63d_high_pct | -14.69 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.volume_vs_previous20_ratio | 0.63 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GC=F.value | 4,000.50 | USD_per_troy_ounce | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_1d_pct | -0.74 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_5d_pct | -1.78 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_20d_pct | -2.61 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_60d_pct | -9.50 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_1d_pp | -2.06 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_5d_pp | -0.87 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_20d_pp | -1.34 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_60d_pp | -8.75 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma20 | 4,064.18 | USD_per_troy_ounce | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma50 | 4,205.17 | USD_per_troy_ounce | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma200 | 4,486.50 | USD_per_troy_ounce | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma20_pct | -1.57 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma50_pct | -4.87 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma200_pct | -10.83 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_sma | 92.49 | USD_per_troy_ounce | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_pct | 2.31 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.drawdown_from_63d_high_pct | -14.84 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.volume_vs_previous20_ratio | 1.13 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.CL=F.value | 86.53 | USD_per_barrel | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_1d_pct | 0.57 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_5d_pct | -1.80 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_20d_pct | -9.00 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_60d_pct | 1.87 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_1d_pp | -0.75 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_5d_pp | -0.89 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_20d_pp | -7.73 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_60d_pp | 2.62 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma20 | 96.84 | USD_per_barrel | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma50 | 95.47 | USD_per_barrel | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma200 | 87.53 | USD_per_barrel | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma20_pct | -10.64 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma50_pct | -9.36 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma200_pct | -1.15 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_sma | 4.72 | USD_per_barrel | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_pct | 5.46 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.drawdown_from_63d_high_pct | -18.24 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.volume_vs_previous20_ratio | 0.99 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.BZ=F.value | 92.76 | USD_per_barrel | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_1d_pct | 1.39 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_5d_pct | -1.97 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_20d_pct | -12.54 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_60d_pct | 1.91 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_1d_pp | 0.07 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_5d_pp | -1.05 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_20d_pp | -11.27 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_60d_pp | 2.66 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma20 | 106.34 | USD_per_barrel | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma50 | 104.25 | USD_per_barrel | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma200 | 93.73 | USD_per_barrel | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma20_pct | -12.77 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma50_pct | -11.02 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma200_pct | -1.04 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_sma | 5.59 | USD_per_barrel | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_pct | 6.02 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.drawdown_from_63d_high_pct | -21.15 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.volume_vs_previous20_ratio | 1.02 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.TLT.value | 80.92 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_1d_pct | 0.05 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_5d_pct | -1.03 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_20d_pct | 3.00 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_60d_pct | 0.29 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_1d_pp | -1.27 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_5d_pp | -0.11 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_20d_pp | 4.28 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_60d_pp | 1.04 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma20 | 80.94 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma50 | 79.90 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma200 | 82.76 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma20_pct | -0.02 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma50_pct | 1.28 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma200_pct | -2.23 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_sma | 0.71 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_pct | 0.88 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.drawdown_from_63d_high_pct | -1.88 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.volume_vs_previous20_ratio | 0.67 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/TLT/history/ |
| prices.UUP.value | 29.35 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_1d_pct | 0.69 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_5d_pct | 1.56 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_20d_pct | 0.79 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_60d_pct | 4.30 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_1d_pp | -0.63 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_5d_pp | 2.47 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_20d_pp | 2.06 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_60d_pp | 5.05 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma20 | 29.01 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma50 | 28.75 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma200 | 28.00 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma20_pct | 1.17 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma50_pct | 2.10 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma200_pct | 4.81 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_sma | 0.13 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_pct | 0.45 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.drawdown_from_63d_high_pct | 0.00 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.volume_vs_previous20_ratio | 0.76 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/UUP/history/ |
| prices.HYG.value | 77.35 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_1d_pct | 0.22 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_5d_pct | -0.22 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_20d_pct | 1.23 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_60d_pct | -1.26 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_1d_pp | -1.10 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_5d_pp | 0.69 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_20d_pp | 2.50 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_60d_pp | -0.51 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma20 | 76.97 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma50 | 77.20 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma200 | 77.49 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma20_pct | 0.50 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma50_pct | 0.20 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma200_pct | -0.18 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_sma | 0.32 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_pct | 0.42 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.drawdown_from_63d_high_pct | -1.74 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.volume_vs_previous20_ratio | 0.26 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/HYG/history/ |
| prices.LQD.value | 103.96 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_1d_pct | 0.08 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_5d_pct | -0.52 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_20d_pct | 1.66 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_60d_pct | -0.56 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_1d_pp | -1.24 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_5d_pp | 0.40 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_20d_pp | 2.93 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_60d_pp | 0.19 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma20 | 103.70 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma50 | 103.24 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma200 | 105.35 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma20_pct | 0.25 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma50_pct | 0.70 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma200_pct | -1.32 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_sma | 0.55 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_pct | 0.53 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.drawdown_from_63d_high_pct | -1.51 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.volume_vs_previous20_ratio | 0.25 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/LQD/history/ |
| prices.^VIX.value | 17.49 | index | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_1d_pct | -10.12 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_5d_pct | 5.30 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_20d_pct | 3.68 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_60d_pct | 17.46 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_1d_pp | -11.44 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_5d_pp | 6.21 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_20d_pp | 4.95 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_60d_pp | 18.42 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma20 | 19.30 | index | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma50 | 17.13 | index | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma200 | 18.43 | index | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma20_pct | -9.40 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma50_pct | 2.10 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma200_pct | -5.11 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_sma | 3.64 | index | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_pct | 20.80 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.drawdown_from_63d_high_pct | -37.93 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-11 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX3M.value | 19.24 | index | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_1d_pct | -6.78 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_5d_pct | 2.34 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_20d_pct | 2.39 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_60d_pct | -0.16 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_1d_pp | -8.10 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_5d_pp | 3.25 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_20d_pp | 3.67 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_60d_pp | 0.59 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma20 | 20.42 | index | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma50 | 19.14 | index | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma200 | 20.60 | index | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma20_pct | -5.76 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma50_pct | 0.50 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma200_pct | -6.59 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_sma | 2.08 | index | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_pct | 10.83 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.drawdown_from_63d_high_pct | -24.70 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-11 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VVIX.value | 90.47 | index | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_1d_pct | -6.37 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_5d_pct | 0.07 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_20d_pct | -4.21 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_60d_pct | -2.58 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_1d_pp | -7.69 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_5d_pp | 0.98 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_20d_pp | -2.94 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_60d_pp | -1.83 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma20 | 103.57 | index | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma50 | 94.76 | index | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma200 | 98.95 | index | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma20_pct | -12.65 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma50_pct | -4.53 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma200_pct | -8.57 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_sma | 14.40 | index | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_pct | 15.92 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.drawdown_from_63d_high_pct | -32.98 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-11 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^MOVE.value | 92.43 | index | 2026-11-10 | stale | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_1d_pct | 7.50 | percent | 2026-11-10 | stale | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_5d_pct | -7.54 | percent | 2026-11-10 | stale | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_20d_pct | -8.57 | percent | 2026-11-10 | stale | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_60d_pct | 32.84 | percent | 2026-11-10 | stale | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_1d_pp | 7.87 | pp | 2026-11-10 | stale | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_5d_pp | -6.96 | pp | 2026-11-10 | stale | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_20d_pp | -4.96 | pp | 2026-11-10 | stale | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_60d_pp | 36.00 | pp | 2026-11-10 | stale | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma20 | 98.17 | index | 2026-11-10 | stale | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma50 | 93.56 | index | 2026-11-10 | stale | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma200 | 78.80 | index | 2026-11-10 | stale | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma20_pct | -5.85 | percent | 2026-11-10 | stale | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma50_pct | -1.21 | percent | 2026-11-10 | stale | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma200_pct | 17.30 | percent | 2026-11-10 | stale | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_sma | 5.62 | index | 2026-11-10 | stale | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_pct | 6.08 | percent | 2026-11-10 | stale | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.drawdown_from_63d_high_pct | -18.64 | percent | 2026-11-10 | stale | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-10 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.NVDA.value | 173.73 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_1d_pct | 2.87 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_5d_pct | -13.19 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_20d_pct | -21.50 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_60d_pct | -20.85 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_1d_pp | 1.55 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_5d_pp | -12.28 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_20d_pp | -20.22 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_60d_pp | -20.10 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma20 | 203.80 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma50 | 217.10 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma200 | 204.19 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma20_pct | -14.76 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma50_pct | -19.98 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma200_pct | -14.92 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_sma | 9.14 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_pct | 5.26 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.drawdown_from_63d_high_pct | -27.38 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.volume_vs_previous20_ratio | 2.03 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.MSFT.value | 521.13 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_1d_pct | -2.26 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_5d_pct | -6.24 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_20d_pct | -2.35 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_60d_pct | 8.41 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_1d_pp | -3.58 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_5d_pp | -5.32 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_20d_pp | -1.08 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_60d_pp | 9.15 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma20 | 530.47 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma50 | 518.20 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma200 | 439.80 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma20_pct | -1.76 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma50_pct | 0.57 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma200_pct | 18.49 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_sma | 17.51 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_pct | 3.36 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.drawdown_from_63d_high_pct | -6.24 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.volume_vs_previous20_ratio | 1.11 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.AMZN.value | 266.17 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_1d_pct | -1.74 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_5d_pct | 0.05 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_20d_pct | 4.76 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_60d_pct | 2.59 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_1d_pp | -3.05 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_5d_pp | 0.97 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_20d_pp | 6.03 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_60d_pp | 3.34 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma20 | 255.87 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma50 | 254.41 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma200 | 244.35 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma20_pct | 4.03 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma50_pct | 4.62 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma200_pct | 8.93 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_sma | 10.31 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_pct | 3.87 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.drawdown_from_63d_high_pct | -1.74 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.volume_vs_previous20_ratio | 0.75 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.GOOGL.value | 293.45 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_1d_pct | 2.11 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_5d_pct | 1.56 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_20d_pct | -15.59 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_60d_pct | -14.69 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_1d_pp | 0.79 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_5d_pp | 2.48 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_20d_pp | -14.32 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_60d_pp | -13.94 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma20 | 308.18 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma50 | 329.88 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma200 | 338.59 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma20_pct | -4.78 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma50_pct | -11.04 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma200_pct | -13.33 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_sma | 11.10 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_pct | 3.78 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.drawdown_from_63d_high_pct | -17.33 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.volume_vs_previous20_ratio | 0.64 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.META.value | 628.77 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_1d_pct | -1.97 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_5d_pct | -0.20 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_20d_pct | -14.75 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_60d_pct | 15.74 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_1d_pp | -3.29 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_5d_pp | 0.72 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_20d_pp | -13.48 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_60d_pp | 16.49 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma20 | 646.10 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma50 | 678.45 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma200 | 630.71 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma20_pct | -2.68 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma50_pct | -7.32 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma200_pct | -0.31 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_sma | 21.23 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_pct | 3.38 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.drawdown_from_63d_high_pct | -19.14 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.volume_vs_previous20_ratio | 0.64 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/META/history/ |
| prices.CRWV.value | 60.77 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_1d_pct | 24.71 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_5d_pct | 25.51 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_20d_pct | -7.62 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_60d_pct | -34.78 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_1d_pp | 23.39 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_5d_pp | 26.42 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_20d_pp | -6.34 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_60d_pp | -34.03 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma20 | 56.06 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma50 | 73.71 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma200 | 89.47 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma20_pct | 8.41 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma50_pct | -17.56 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma200_pct | -32.08 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_sma | 5.77 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_pct | 9.50 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.drawdown_from_63d_high_pct | -42.67 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.volume_vs_previous20_ratio | 2.22 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.MU.value | 811.30 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_1d_pct | 11.89 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_5d_pct | 2.02 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_20d_pct | -11.25 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_60d_pct | -13.75 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_1d_pp | 10.57 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_5d_pp | 2.93 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_20d_pp | -9.98 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_60d_pp | -13.00 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma20 | 849.67 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma50 | 950.43 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma200 | 761.89 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma20_pct | -4.52 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma50_pct | -14.64 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma200_pct | 6.49 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_sma | 63.34 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_pct | 7.81 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.drawdown_from_63d_high_pct | -26.06 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.volume_vs_previous20_ratio | 1.17 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MU/history/ |
| prices.DRAM.value | 44.85 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_1d_pct | 10.36 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_5d_pct | -0.58 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_20d_pct | -10.55 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_60d_pct | -18.60 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_1d_pp | 9.04 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_5d_pp | 0.34 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_20d_pp | -9.28 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_60d_pp | -17.85 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma20 | 46.46 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma50 | 53.84 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma200 | 缺失 | USD_per_share | 2026-11-11 | unavailable | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma20_pct | -3.45 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma50_pct | -16.69 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma200_pct | 缺失 | percent | 2026-11-11 | unavailable | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_sma | 3.43 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_pct | 7.64 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.drawdown_from_63d_high_pct | -29.50 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.volume_vs_previous20_ratio | 1.37 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.VRT.value | 206.51 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_1d_pct | 6.33 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_5d_pct | 0.47 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_20d_pct | -7.32 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_60d_pct | -24.21 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_1d_pp | 5.01 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_5d_pp | 1.38 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_20d_pp | -6.05 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_60d_pp | -23.46 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma20 | 209.46 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma50 | 233.58 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma200 | 271.37 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma20_pct | -1.41 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma50_pct | -11.59 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma200_pct | -23.90 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_sma | 19.06 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_pct | 9.23 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.drawdown_from_63d_high_pct | -29.70 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.volume_vs_previous20_ratio | 0.78 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/VRT/history/ |
| prices.XLK.value | 174.36 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_1d_pct | 3.23 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_5d_pct | -1.21 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_20d_pct | -8.44 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_60d_pct | -5.96 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_1d_pp | 1.91 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_5d_pp | -0.30 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_20d_pp | -7.17 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_60d_pp | -5.21 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma20 | 180.09 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma50 | 187.56 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma200 | 170.29 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma20_pct | -3.18 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma50_pct | -7.04 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma200_pct | 2.39 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_sma | 5.86 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_pct | 3.36 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.drawdown_from_63d_high_pct | -13.68 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.volume_vs_previous20_ratio | 1.18 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLE.value | 63.37 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_1d_pct | 1.86 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_5d_pct | -0.24 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_20d_pct | -6.30 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_60d_pct | 0.10 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_1d_pp | 0.55 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_5d_pp | 0.68 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_20d_pp | -5.03 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_60d_pp | 0.85 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma20 | 66.44 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma50 | 64.90 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma200 | 58.79 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma20_pct | -4.63 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma50_pct | -2.36 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma200_pct | 7.80 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_sma | 1.79 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_pct | 2.83 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.drawdown_from_63d_high_pct | -9.50 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.volume_vs_previous20_ratio | 0.66 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLF.value | 58.63 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_1d_pct | 0.58 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_5d_pct | -0.96 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_20d_pct | 7.54 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_60d_pct | 1.72 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_1d_pp | -0.74 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_5d_pp | -0.05 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_20d_pp | 8.81 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_60d_pp | 2.47 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma20 | 56.76 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma50 | 55.90 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma200 | 53.61 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma20_pct | 3.30 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma50_pct | 4.87 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma200_pct | 9.37 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_sma | 1.00 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_pct | 1.71 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.drawdown_from_63d_high_pct | -0.96 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.volume_vs_previous20_ratio | 0.71 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLI.value | 170.97 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_1d_pct | 1.33 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_5d_pct | 0.89 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_20d_pct | 2.35 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_60d_pct | -6.61 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_1d_pp | 0.01 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_5d_pp | 1.80 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_20d_pp | 3.62 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_60d_pp | -5.86 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma20 | 167.70 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma50 | 169.03 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma200 | 172.74 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma20_pct | 1.95 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma50_pct | 1.15 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma200_pct | -1.03 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_sma | 3.44 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_pct | 2.01 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.drawdown_from_63d_high_pct | -8.09 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.volume_vs_previous20_ratio | 0.74 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLV.value | 188.95 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_1d_pct | 0.04 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_5d_pct | -0.37 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_20d_pct | 8.62 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_60d_pct | 11.75 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_1d_pp | -1.28 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_5d_pp | 0.54 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_20d_pp | 9.89 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_60d_pp | 12.50 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma20 | 182.51 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma50 | 174.28 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma200 | 158.94 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma20_pct | 3.53 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma50_pct | 8.42 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma200_pct | 18.88 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_sma | 3.73 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_pct | 1.97 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.drawdown_from_63d_high_pct | -0.37 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.volume_vs_previous20_ratio | 0.71 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLP.value | 91.45 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_1d_pct | 0.46 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_5d_pct | -0.53 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_20d_pct | 6.26 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_60d_pct | 7.56 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_1d_pp | -0.86 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_5d_pp | 0.38 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_20d_pp | 7.54 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_60d_pp | 8.31 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma20 | 89.03 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma50 | 85.26 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma200 | 83.97 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma20_pct | 2.72 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma50_pct | 7.26 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma200_pct | 8.91 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_sma | 1.69 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_pct | 1.85 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.drawdown_from_63d_high_pct | -0.53 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.volume_vs_previous20_ratio | 0.83 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLY.value | 120.99 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_1d_pct | -0.05 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_5d_pct | -1.10 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_20d_pct | 8.51 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_60d_pct | 4.21 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_1d_pp | -1.37 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_5d_pp | -0.18 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_20d_pp | 9.78 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_60d_pp | 4.96 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma20 | 116.61 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma50 | 113.59 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma200 | 115.09 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma20_pct | 3.76 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma50_pct | 6.52 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma200_pct | 5.13 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_sma | 2.60 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_pct | 2.15 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.drawdown_from_63d_high_pct | -1.10 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.volume_vs_previous20_ratio | 0.70 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLC.value | 108.60 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_1d_pct | 0.78 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_5d_pct | 3.47 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_20d_pct | -2.00 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_60d_pct | -1.38 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_1d_pp | -0.54 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_5d_pp | 4.38 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_20d_pp | -0.73 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_60d_pp | -0.63 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma20 | 105.81 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma50 | 109.49 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma200 | 111.95 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma20_pct | 2.64 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma50_pct | -0.81 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma200_pct | -2.99 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_sma | 2.21 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_pct | 2.03 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.drawdown_from_63d_high_pct | -5.36 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.volume_vs_previous20_ratio | 0.69 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLU.value | 43.82 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_1d_pct | 0.21 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_5d_pct | 0.48 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_20d_pct | 5.03 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_60d_pct | 0.28 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_1d_pp | -1.11 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_5d_pp | 1.39 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_20d_pp | 6.31 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_60d_pp | 1.03 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma20 | 42.87 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma50 | 41.78 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma200 | 43.86 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma20_pct | 2.21 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma50_pct | 4.89 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma200_pct | -0.09 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_sma | 0.61 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_pct | 1.38 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.drawdown_from_63d_high_pct | -0.38 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.volume_vs_previous20_ratio | 0.58 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLRE.value | 44.59 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_1d_pct | 0.02 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_5d_pct | -1.17 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_20d_pct | 7.47 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_60d_pct | 0.75 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_1d_pp | -1.30 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_5d_pp | -0.26 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_20d_pp | 8.74 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_60d_pp | 1.50 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma20 | 43.17 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma50 | 42.49 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma200 | 42.92 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma20_pct | 3.28 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma50_pct | 4.94 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma200_pct | 3.88 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_sma | 0.73 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_pct | 1.63 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.drawdown_from_63d_high_pct | -1.17 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.volume_vs_previous20_ratio | 0.51 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLB.value | 53.02 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_1d_pct | 0.32 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_5d_pct | -1.63 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_20d_pct | 6.74 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_60d_pct | 2.87 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_1d_pp | -1.00 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_5d_pp | -0.72 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_20d_pp | 8.02 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_60d_pp | 3.62 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma20 | 52.08 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma50 | 50.89 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma200 | 50.89 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma20_pct | 1.81 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma50_pct | 4.19 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma200_pct | 4.18 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_sma | 1.00 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_pct | 1.89 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.drawdown_from_63d_high_pct | -1.63 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.volume_vs_previous20_ratio | 0.49 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLB/history/ |
| prices.SMH.value | 506.96 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_1d_pct | 4.82 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_5d_pct | 0.53 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_20d_pct | -10.23 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_60d_pct | -11.02 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_1d_pp | 3.51 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_5d_pp | 1.45 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_20d_pp | -8.96 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_60d_pp | -10.27 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma20 | 523.65 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma50 | 562.10 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma200 | 523.11 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma20_pct | -3.19 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma50_pct | -9.81 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma200_pct | -3.09 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_sma | 25.55 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_pct | 5.04 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.drawdown_from_63d_high_pct | -20.03 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.volume_vs_previous20_ratio | 1.24 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SMH/history/ |
| prices.IGV.value | 102.23 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_1d_pct | 1.89 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_5d_pct | -1.28 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_20d_pct | -5.03 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_60d_pct | 0.26 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_1d_pp | 0.57 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_5d_pp | -0.37 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_20d_pp | -3.76 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_60d_pp | 1.01 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma20 | 105.62 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma50 | 106.27 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma200 | 94.10 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma20_pct | -3.21 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma50_pct | -3.80 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma200_pct | 8.64 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_sma | 3.14 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_pct | 3.08 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.drawdown_from_63d_high_pct | -9.27 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.volume_vs_previous20_ratio | 0.52 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IGV/history/ |
| prices.XOP.value | 180.14 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_1d_pct | 2.63 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_5d_pct | 0.47 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_20d_pct | -8.95 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_60d_pct | -2.42 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_1d_pp | 1.31 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_5d_pp | 1.39 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_20d_pp | -7.67 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_60d_pp | -1.67 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma20 | 192.15 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma50 | 190.42 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma200 | 171.52 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma20_pct | -6.25 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma50_pct | -5.40 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma200_pct | 5.03 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_sma | 6.18 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_pct | 3.43 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.drawdown_from_63d_high_pct | -12.07 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.volume_vs_previous20_ratio | 0.84 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XOP/history/ |
| prices.OIH.value | 369.54 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_1d_pct | 2.84 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_5d_pct | 0.95 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_20d_pct | -3.35 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_60d_pct | -12.12 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_1d_pp | 1.52 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_5d_pp | 1.86 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_20d_pp | -2.08 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_60d_pp | -11.37 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma20 | 383.50 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma50 | 393.35 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma200 | 398.83 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma20_pct | -3.64 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma50_pct | -6.05 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma200_pct | -7.34 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_sma | 14.19 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_pct | 3.84 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.drawdown_from_63d_high_pct | -15.36 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.volume_vs_previous20_ratio | 0.82 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/OIH/history/ |
| prices.ITA.value | 73.24 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_1d_pct | 1.23 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_5d_pct | 3.23 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_20d_pct | 7.58 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_60d_pct | -12.76 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_1d_pp | -0.09 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_5d_pp | 4.15 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_20d_pp | 8.85 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_60d_pp | -12.01 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma20 | 69.90 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma50 | 70.52 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma200 | 75.88 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma20_pct | 4.77 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma50_pct | 3.86 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma200_pct | -3.47 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_sma | 2.07 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_pct | 2.83 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.drawdown_from_63d_high_pct | -13.13 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.volume_vs_previous20_ratio | 0.46 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ARKX.value | 30.34 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_1d_pct | 1.37 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_5d_pct | 4.91 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_20d_pct | -0.61 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_60d_pct | -10.71 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_1d_pp | 0.05 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_5d_pp | 5.82 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_20d_pp | 0.67 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_60d_pp | -9.96 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma20 | 29.86 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma50 | 31.24 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma200 | 32.29 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma20_pct | 1.59 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma50_pct | -2.89 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma200_pct | -6.05 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_sma | 1.03 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_pct | 3.40 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.drawdown_from_63d_high_pct | -12.97 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.volume_vs_previous20_ratio | 0.36 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.KRE.value | 72.95 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_1d_pct | -0.19 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_5d_pct | -1.59 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_20d_pct | 6.43 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_60d_pct | -4.53 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_1d_pp | -1.51 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_5d_pp | -0.68 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_20d_pp | 7.71 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_60d_pp | -3.78 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma20 | 72.10 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma50 | 71.70 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma200 | 70.58 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma20_pct | 1.18 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma50_pct | 1.75 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma200_pct | 3.36 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_sma | 1.55 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_pct | 2.13 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.drawdown_from_63d_high_pct | -5.86 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.volume_vs_previous20_ratio | 0.69 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/KRE/history/ |
| prices.SKYY.value | 154.30 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_1d_pct | 2.90 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_5d_pct | -1.53 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_20d_pct | -5.93 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_60d_pct | -4.38 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_1d_pp | 1.58 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_5d_pp | -0.61 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_20d_pp | -4.65 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_60d_pp | -3.63 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma20 | 160.22 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma50 | 163.19 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma200 | 137.64 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma20_pct | -3.70 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma50_pct | -5.45 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma200_pct | 12.11 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_sma | 5.39 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_pct | 3.49 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.drawdown_from_63d_high_pct | -11.77 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.volume_vs_previous20_ratio | 3.41 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SKYY/history/ |
| macro.DGS2.value | 4.56 | percent | 2026-11-09 | lagged | source_series_v1:DGS2 | https://fred.stlouisfed.org/series/DGS2 |
| macro.BAMLH0A0HYM2.value | 3.34 | percentage_points | 2026-11-09 | lagged | source_series_v1:BAMLH0A0HYM2 | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| macro.BAMLC0A0CM.value | 0.91 | percentage_points | 2026-11-09 | lagged | source_series_v1:BAMLC0A0CM | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| macro.DGS10.value | 4.88 | percent | 2026-11-09 | lagged | source_series_v1:DGS10 | https://fred.stlouisfed.org/series/DGS10 |
| macro.DFII10.value | 2.66 | percent | 2026-11-09 | lagged | source_series_v1:DFII10 | https://fred.stlouisfed.org/series/DFII10 |
| macro.T10YIE.value | 2.20 | percent | 2026-11-10 | lagged | source_series_v1:T10YIE | https://fred.stlouisfed.org/series/T10YIE |
| macro.STLFSI4.value | -0.52 | index | 2026-10-30 | lagged | source_series_v1:STLFSI4 | https://fred.stlouisfed.org/series/STLFSI4 |
| macro.CBOE_VIX.value | 17.49 | index | 2026-11-11 | ok | source_series_v1:CBOE_VIX | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| macro.GPRD.value | 113.95 | index | 2026-11-02 | lagged | source_series_v1:GPRD | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_ACT.value | 129.82 | index | 2026-11-02 | lagged | source_series_v1:GPRD_ACT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_THREAT.value | 108.29 | index | 2026-11-02 | lagged | source_series_v1:GPRD_THREAT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA7.value | 158.85 | index | 2026-11-02 | lagged | source_series_v1:GPRD_MA7 | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA30.value | 184.74 | index | 2026-11-02 | lagged | source_series_v1:GPRD_MA30 | https://www.matteoiacoviello.com/gpr.htm |
| quotes.SPY.value | 756.46 | USD_per_share | 2026-11-12T12:02:44+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SPY |
| quotes.QQQ.value | 684.39 | USD_per_share | 2026-11-12T12:03:03+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| quotes.SMH.value | 493.00 | USD_per_share | 2026-11-12T12:02:34+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SMH |
| quotes.NVDA.value | 160.28 | USD_per_share | 2026-11-12T12:03:07+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| quotes.MSFT.value | 520.00 | USD_per_share | 2026-11-12T12:01:52+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/MSFT |
| quotes.AMZN.value | 267.19 | USD_per_share | 2026-11-12T12:02:44+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AMZN |
| quotes.GOOGL.value | 292.24 | USD_per_share | 2026-11-12T12:02:36+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GOOGL |
| quotes.META.value | 625.50 | USD_per_share | 2026-11-12T12:01:50+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/META |
| observed.SPY.price | 756.46 | USD | 2026-11-12T12:02:44+00:00 | ok | 独立分钟最后非空close，各自时点，不是VWAP；期货连续合约不是结算价，盘前流动性较低。 | https://query1.finance.yahoo.com/v8/finance/chart/SPY |
| observed.QQQ.price | 684.39 | USD | 2026-11-12T12:03:03+00:00 | ok | 独立分钟最后非空close，各自时点，不是VWAP；期货连续合约不是结算价，盘前流动性较低。 | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| observed.SMH.price | 493.00 | USD | 2026-11-12T12:02:34+00:00 | ok | 独立分钟最后非空close，各自时点，不是VWAP；期货连续合约不是结算价，盘前流动性较低。 | https://query1.finance.yahoo.com/v8/finance/chart/SMH |
| observed.NVDA.price | 160.28 | USD | 2026-11-12T12:03:07+00:00 | ok | 独立分钟最后非空close，各自时点，不是VWAP；期货连续合约不是结算价，盘前流动性较低。 | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| observed.MSFT.price | 520.00 | USD | 2026-11-12T12:01:52+00:00 | ok | 独立分钟最后非空close，各自时点，不是VWAP；期货连续合约不是结算价，盘前流动性较低。 | https://query1.finance.yahoo.com/v8/finance/chart/MSFT |
| observed.AMZN.price | 267.19 | USD | 2026-11-12T12:02:44+00:00 | ok | 独立分钟最后非空close，各自时点，不是VWAP；期货连续合约不是结算价，盘前流动性较低。 | https://query1.finance.yahoo.com/v8/finance/chart/AMZN |
| observed.GOOGL.price | 292.24 | USD | 2026-11-12T12:02:36+00:00 | ok | 独立分钟最后非空close，各自时点，不是VWAP；期货连续合约不是结算价，盘前流动性较低。 | https://query1.finance.yahoo.com/v8/finance/chart/GOOGL |
| observed.META.price | 625.50 | USD | 2026-11-12T12:01:50+00:00 | ok | 独立分钟最后非空close，各自时点，不是VWAP；期货连续合约不是结算价，盘前流动性较低。 | https://query1.finance.yahoo.com/v8/finance/chart/META |
| observed.CRWV.price | 56.69 | USD | 2026-11-12T12:03:04+00:00 | ok | 独立分钟最后非空close，各自时点，不是VWAP；期货连续合约不是结算价，盘前流动性较低。 | https://query1.finance.yahoo.com/v8/finance/chart/CRWV |
| observed.MU.price | 783.00 | USD | 2026-11-12T12:03:12+00:00 | ok | 独立分钟最后非空close，各自时点，不是VWAP；期货连续合约不是结算价，盘前流动性较低。 | https://query1.finance.yahoo.com/v8/finance/chart/MU |
| observed.DRAM.price | 43.33 | USD | 2026-11-12T12:03:14+00:00 | ok | 独立分钟最后非空close，各自时点，不是VWAP；期货连续合约不是结算价，盘前流动性较低。 | https://query1.finance.yahoo.com/v8/finance/chart/DRAM |
| observed.SNDK.price | 931.97 | USD | 2026-11-12T12:03:11+00:00 | ok | 独立分钟最后非空close，各自时点，不是VWAP；期货连续合约不是结算价，盘前流动性较低。 | https://query1.finance.yahoo.com/v8/finance/chart/SNDK |
| observed.RSP.price | 222.82 | USD | 2026-11-12T11:47:31+00:00 | ok | 独立分钟最后非空close，各自时点，不是VWAP；期货连续合约不是结算价，盘前流动性较低。 | https://query1.finance.yahoo.com/v8/finance/chart/RSP |
| observed.GLD.price | 361.77 | USD | 2026-11-12T12:03:07+00:00 | ok | 独立分钟最后非空close，各自时点，不是VWAP；期货连续合约不是结算价，盘前流动性较低。 | https://query1.finance.yahoo.com/v8/finance/chart/GLD |
| observed.CL_F.price | 85.93 | USD | 2026-11-12T11:53:09+00:00 | ok | 独立分钟最后非空close，各自时点，不是VWAP；期货连续合约不是结算价，盘前流动性较低。 | https://query1.finance.yahoo.com/v8/finance/chart/CL=F |
| observed.BZ_F.price | 92.24 | USD | 2026-11-12T11:53:09+00:00 | ok | 独立分钟最后非空close，各自时点，不是VWAP；期货连续合约不是结算价，盘前流动性较低。 | https://query1.finance.yahoo.com/v8/finance/chart/BZ=F |
| observed.GC_F.price | 3,950.50 | USD | 2026-11-12T11:53:10+00:00 | ok | 独立分钟最后非空close，各自时点，不是VWAP；期货连续合约不是结算价，盘前流动性较低。 | https://query1.finance.yahoo.com/v8/finance/chart/GC=F |
| observed.DX-Y.NYB.price | 102.91 | index points | 2026-11-12T11:53:17+00:00 | ok | 独立分钟最后非空close，各自时点，不是VWAP；期货连续合约不是结算价，盘前流动性较低。 | https://query1.finance.yahoo.com/v8/finance/chart/DX-Y.NYB |
| observed.VIX.price | 18.30 | index points | 2026-11-12T11:48:01+00:00 | ok | 独立分钟最后非空close，各自时点，不是VWAP；期货连续合约不是结算价，盘前流动性较低。 | https://query1.finance.yahoo.com/v8/finance/chart/^VIX |

## 指标历史比较（不同日期观测，非连续交易日）

```json
[
  {
    "id": "prices.SPY.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 9.8900146484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -7.0,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.686825308470663,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.33294680839071056,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.32561321012155586,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.20072354490434652,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.3384102625149006,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.067299117552444,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.9536675738047071,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.5101092922909278,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.489498901367142,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -7.375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.0016613769531659273,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.9029931640625364,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.34855041503897155,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.528162231445208,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.3644564401100179,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.048363575640086864,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.2937885519670678,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.6665523068154822,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.3080495709729467,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.181850911717497,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.04785592215401735,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.717145647321429,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.014714856366083051,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.36894682147756175,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.269431555728573,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.8984840979486153,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.04834988723050615,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.7884891896383216,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 15.6199951171875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.57000732421875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.99053722245618,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.34157415457965,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.3082456444478363,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 4.411955914785937,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 3.9628307607795676,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 3.390015394179269,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 3.773451530566208,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.09273286518981516,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.303711913985517,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.6745209629703606,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.6338588545693922,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 4.612679459690283,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.6244204982646675,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 3.3227162766268243,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.8197839567615013,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.41737642710111267,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.928500366210983,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -18.488504028320335,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.330467529296925,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -4.439010009765639,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.3069583129882858,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.2093322753905795,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.500469299582686,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.3266831594649373,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.2159964314634517,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.37233274985026776,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.2501296311930874,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.41160536037292417,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.1778564453125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.997148786272321,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.08568636351257286,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.4389603367036603,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.0561824591771245,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.20667237707943187,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.10485470495213967,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.648291547538144,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.510009765625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.92999267578125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.577748889585362,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.6172620995306577,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.6097859245728698,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.2979608263411158,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.9165958541516046,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.0429984392829503,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.0184598098132005,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.0710859008957394,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.10907641888530106,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.28431529113994713,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.284172714451314,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.0972372814367692,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.5781855916367045,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.9756993217305063,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.06479223600849338,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.439023391395188,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.586000061035179,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.4175003051757926,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.13446166992184772,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.6861450195312386,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.10071830749507171,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.3434951782226108,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.6899359536824967,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.4885323088585247,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.9399240686586152,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.27097846909691636,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.8653691747070091,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.46026058713861673,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.025000435965401913,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.2357134137834822,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.007625831138965422,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.4411323770556208,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.8248599684670177,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.30562181061015714,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.14304664862339456,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.7607400905372982,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.769989013671875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.6800079345703125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.8330128877630183,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.0549120132731904,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.043339312820979,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -3.018007002856804,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.4253362059854613,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.0656148979522495,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.2652085219683418,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.10538843104963558,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.8538124207076447,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.7219652048824798,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.717726102699423,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.8172834579524575,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.9130740565294397,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.132914015504693,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.6884590518363654,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.6154977233405634,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.5279998779296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.6955001831054801,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.11749694824217727,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.005880126953115905,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.13035552978513465,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.5658580017089605,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.5659015410594437,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.1148069940679628,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.7679870737588246,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.3195365880861445,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.7862177188489028,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.6221846481918147,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.046428135463169706,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.6735698154994418,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.03175772792602105,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.3056831154305335,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.7925442167017183,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.30448570679936227,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.2354954584138259,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.2433829231833478,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -4.189971923828125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -7.319976806640625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.5452465431456286,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -4.816951262268876,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -4.776474789433505,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.6920569719519607,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.34757656889481403,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.9758425508809019,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.5348543151614926,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.2748951525845875,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.14157876532503444,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -4.484004453878166,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -4.450861579311949,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.4913334270476142,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.9908336936200866,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.043141668433346,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.4188132586432136,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.7647858602936592,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.5409988403320085,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.047000122070301,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.6315997314453625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -3.9182012939453443,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.5546499633789495,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.1606002807617415,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.9832707076030123,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.4209278965946148,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.9352964709571032,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.926335691115332,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.9005849332030422,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.3094784344076178,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.43642970493861544,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.8671439034598221,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.09599598010687016,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.27118940583638595,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.9788053010344804,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.7099952534391232,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.24321757135852018,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.7150281096255531,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -29.699951171875,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -72.5,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.3119178794698594,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -4.1020780861707244,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -4.058972477924982,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.3081987036103757,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.9069377771789733,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.979478341114226,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.4102625932227877,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.214747750981271,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.37490742900080365,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -3.7691312777800134,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -3.7333592678034266,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.107475158706029,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.4314724853359273,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.04677745866667,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.5434049805819186,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.7046384586903418,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -5.3699951171875,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -25.77498779296866,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -7.917998046874345,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -47.829995117187536,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -5.410500488281286,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -22.810501708984702,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.5999207011507135,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.1523071491949644,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.5261539846995396,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.6347975660666689,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.5537856150239389,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.156728127630192,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -3.028564453125,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 11.892874581473222,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.05810989809214995,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.33314432576273023,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.6322098089884598,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.5432756399636052,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.00872145044355932,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.08953452469650225,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.48999786376953125,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.5900039672851562,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.502139760427812,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 8.863801134821747,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 8.65457823405138,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 12.459109553790103,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.3977909503931407,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -8.82075887344167,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.04941892745937704,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -4.041563506500467,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.1846855480428511,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 9.196747943212458,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 8.980191444172936,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 12.659833098694449,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -2.736201212908041,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -8.888057990994113,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.9042486463453305,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -3.5314542142095395,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.4279998779296932,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.2769996643066435,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.07380004882813296,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.3125997924804693,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.12069999694824673,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.6834999847412178,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.896988437505474,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.4575459205178998,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.5828783256703325,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.9687277911943024,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.4240572321975278,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.6086965568271725,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.006428309849330738,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.5335715157645087,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.03855964871796491,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.5070075334908406,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.46300468231281755,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.5024132474488852,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.17277412922633018,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.3803952626572026,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.2700042724609375,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.8600006103515625,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.5548212054631203,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 10.056084224158502,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 9.723431594588305,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 15.984291074391244,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.8954553612784846,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -6.971210971839725,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.2293858788196,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -4.510549556431376,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.8679958969924573,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 10.389031032549212,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 10.049044804709862,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 16.18501461929559,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.4429549012364156,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -7.038510089392169,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.7242816949851072,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -4.0004402641404475,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.6649997711181612,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.698500061035162,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.03779998779296534,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.42880020141602415,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.12595001220702784,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.7254500579833945,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.7289883241002766,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.4529758116859277,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.2500192688951746,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.1590001567605484,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.22359708991987,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.7717720377623434,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.10142844063895051,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.10928508213588195,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.19448401382600355,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.23391608366533045,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.079568411297263,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.5810953927250964,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.2327275181588082,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.6343093209815909,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.04000091552734375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.8400039672851562,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.3671753256184083,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.7519255982381567,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.7438324208815961,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.9781420447559817,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.19784456508098458,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.970468853524255,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.0893184266001601,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.4364815506129216,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.31964998285225477,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.4189787898474462,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.4182192107600402,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.7774184998516351,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -2.5362548275958856,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -3.0377679710766996,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.864349147204547,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.9465908429038494,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.1018856048584098,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.6191135406494084,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.29379837036132983,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.5073779296874932,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.3542007446288977,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.7128199768066423,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.17506508614617555,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.816576875367093,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.4209465116800981,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.4056119927323243,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.46479616649474087,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.17136545153823013,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.0823811010483847,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.055953968305639146,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.10229150698221712,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.05938905899891089,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.45953100131884694,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.20703645305729657,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.3667089203453836,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.4415054166864084,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.20000076293945312,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.4500007629394531,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.06477549176271413,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.0652906669375573,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.0745059842472537,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.107680567686143,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.34186954969577243,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.2719316850380413,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.5632805061985158,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.5991498674480908,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.622049816707949,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.3982374753282678,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.4001191943688096,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.3084041125904897,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.9965407128191286,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.2046325674855973,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.3903870676061914,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.109259159739019,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.011499977111814275,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.012499904632566228,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.02280002593994368,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.09939994812011932,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.014400005340576172,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.05469999313354634,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.6495505319847661,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.5081979910429588,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.6152576032171453,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.2165920556728826,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.6606322491791605,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.4049405081101085,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.007857322692871094,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.029285975864955363,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.023882412834488165,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.09436291262744478,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.0,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.7895624746398933,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.09057622596372694,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.11703815385809324,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.1699981689453125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.1699981689453125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.6460158104082958,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.48121020810529824,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.47909965965848844,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.12907847055547705,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.110525785399119,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.7867537092717702,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.8257283675990768,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.7068693854308084,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.0408094980623672,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.14826339971458768,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.15348644953693258,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.07164507434886946,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.2278844771157815,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.7194545917193262,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.1279392062056304,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.2169786777217362,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.21282844543456747,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.1903282165527287,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.3655227661132727,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.6790907287597605,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.3888085556030205,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.6991025161743067,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.4973995255012076,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.027579278324374457,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.6913912799620947,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.6554751623399802,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.7166147928538646,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.6750610708410099,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.022826979172888506,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.0013987347183684329,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.030497774406428868,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.0008869085927196707,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.7236816145727909,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.7279479840120673,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.6443769478275918,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.037718032837217,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.0800018310546875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.5400009155273438,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.8317676227758475,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.6750097945135369,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.6710049339722302,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.9299310162654395,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.35936770684534824,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.6943478186419938,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.3266148857055007,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.4350627001393881,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.8550576856948156,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.3420629861228264,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.3453917238506743,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.729207471361093,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.9790425556695528,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.7616469361944378,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.6270526880992064,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.9451719924303159,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.1738468170166101,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.21265258789061647,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.34952896118164745,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.6688073730468744,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.4047132110595726,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.8556588363647535,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.24478677516626135,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.727772616826794,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.4170002986518151,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.1284501078989697,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.45328096431631604,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.28657248661182466,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.06369791067993746,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.06369845563668974,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.06172503376425342,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.058229339992257545,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.45334947335867737,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.29192511055081694,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.5623256392011424,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.0599792076119394,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.9699993133544922,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.8799991607666016,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -7.814084937304721,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 10.135911401140152,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 11.875064379200417,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 7.072101668782049,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -23.76425739365735,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -6.470736701861047,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -5.392149156879135,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 3.3033009336138157,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -9.500910245775385,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 10.468858209530861,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 12.200677589321973,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 7.272825213686396,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -26.10266765617225,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -6.5380358194134915,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -6.476264400647715,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 3.771943549257827,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.030999946594238992,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.6544998645782485,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.045799999237061684,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.70579996109009,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.0030500030517579546,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.1443499946594251,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -10.367281608746259,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -3.5073348264419213,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -11.804694824746198,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.9703532538904991,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -10.705199767099614,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 4.062932136039931,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.1071428571428572,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.7957144464765276,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.555035594974953,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 3.688607853743843,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -6.990771085948733,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -16.468990211328705,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.3999996185302734,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.4400005340576172,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -5.775745105695185,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 4.829661306324706,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 5.302351620219348,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 4.525652667931257,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -12.527166765431708,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -3.6999232398270854,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -8.559038893874659,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.4260200676322601,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -7.462570414165848,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 5.162608114715418,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 5.627964830340904,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 4.7263762128356035,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -14.86557702794661,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -3.767222357379529,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -10.512706467679365,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.9361293599231879,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.022499942779539595,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.0174999237060547,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.018199996948240482,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.43979999542236214,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.00010000228881779094,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.07664999961852814,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -6.9687309945698495,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.6747047985529515,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -7.415825463390546,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.010793329534131146,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -6.797426010227925,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.795258156410262,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.034285817827496956,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.5264284951346263,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.5684368373502267,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.546697960128963,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -5.47945072538225,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -11.733703804817964,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -6.159996032714844,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.05999755859375,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -4.546114054635142,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 9.44453673077741,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 10.094298433673277,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 6.483913556299014,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -17.390253721734005,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -12.905862656472499,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -5.4696926246608495,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.045207584682529,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -6.232939363105805,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 9.77748353916812,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 10.419911643794833,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 6.684637101203361,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -19.728663984248904,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -12.973161774024943,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -7.423360198465557,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.5350982923916012,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.1989997863769588,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 5.208000564575201,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.015599975585928405,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.2030001831054733,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.05395000457764354,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.2046500015258772,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -5.768688700809633,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -4.563939398369099,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -6.483776003909846,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.2075300244134617,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -6.171970966143247,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.12871989768213865,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.627142769949776,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.9585718427385608,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.36565893697312113,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.155759347636261,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -4.563297860615897,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -14.821448852400696,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 4.839996337890625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -26.400009155273438,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 8.339546309108991,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 6.039602455418914,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 5.096829211625218,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -6.110921118666123,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 4.598287599964014,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -5.771620356801131,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 4.007205555304239,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -12.966674489464834,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 6.652721000638328,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 6.372549263809623,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 5.422442421746775,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -5.910197573761777,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.2598773374491117,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -5.838919474353576,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.053537981499531,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -12.456565197173909,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -2.3785003662109148,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -12.318500518798828,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.8693395996093614,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -4.053157653808597,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.07174949645994388,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.19558479309080212,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 3.3307848558030706,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -7.356594963442387,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.539677079289593,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -10.470890000376475,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.3993852725331823,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -12.835305988672307,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.1471437726702014,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.630713326590401,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.2379285151802275,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.0086709132555254,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.0230714875271616,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -11.034947562742715,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.0792793640815344,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.5471515875870949,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -12.02996826171875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -34.66998291015625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.05157246096785251,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -8.937862335606662,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -8.573786519399151,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -10.906310169610144,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.4599600728585562,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -7.268854843572836,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -2.7979995569832106,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.1220380221164348,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.7383977694385155,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -8.604915527215951,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -8.248173309277595,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -10.705586624705798,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -2.798370335373457,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -7.33615396112528,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -4.751667130787917,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.6119287298255056,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.6279998779297102,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.4980041503906705,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.40220031738283524,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.8547985839843477,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.2178981018066679,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.8426277160644986,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -2.1489624852061184,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -6.437481935675093,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -2.4014166121511638,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -7.28464113568692,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -2.795392007742791,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -8.41474347315172,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.21500069754464235,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.482862200055804,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.11613318011261464,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.6562938980159463,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -2.1644419801966297,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -6.237852405831745,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.07383758584659206,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.1590993837790635,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -4.699981689453125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.1400146484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -3.2111863374326033,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -7.8542527067232415,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -7.9971484497290755,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -4.4367609949595765,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.005463687277629248,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.4076308163204274,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.0683942369180466,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 4.881933941081162,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -4.898011645903266,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -7.521305898332531,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -7.671535239607519,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -4.23603745005523,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -2.332946575237272,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.3403316987679834,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -3.022061810722754,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 5.392043233372091,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.6045005798339957,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.7400001525878963,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.22500030517576874,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.5163998413085835,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.10745010375975994,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.6778499603271371,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -2.087581243773906,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.6571688090465155,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.9416722145276344,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.15765106146092833,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.9722415920756298,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.24556487430382745,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.3657139369419653,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.9728611537388385,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.06779978314935464,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.36365724419915546,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.7351429741857327,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.6015817255191642,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.03460506222810644,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.4252776963283993,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 6.07000732421875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 4.52001953125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.3794065945772713,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.0660402694851356,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.060321412161902,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 12.632767422377167,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 3.1807600601342934,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.9783712920000163,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.7160675132403398,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.2163035317971378,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.6925812861066083,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.7330934610944251,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.7347082020403461,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 12.833490967281513,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.8423497976193932,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.9110721744475718,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.23760006056436644,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.726412824088067,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -2.709500122070324,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -15.88800048828125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.8270953369140557,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -5.323712768554685,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.2022515869140875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.0755876159668105,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.7822990552213707,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 6.0629997505339155,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.05794517882647,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.7612543178750055,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.843386832926786,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.6051579884620484,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.3142874581473212,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.4328526088169653,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.18922752449309366,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.09066036489745821,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.7100057197353742,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.8019582956940283,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.07006946569835515,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.8306235205825611,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -12.6199951171875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.22998046875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.9707221791174234,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -3.4119706913060988,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -3.473657034407718,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -3.05405881988694,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.135607253012239,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.0887575531617806,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.9269195585041707,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 10.506936564365876,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -3.6575474875880865,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -3.079023882915388,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -3.148043824286162,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.8533352749825935,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.2028030095026612,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.156056670714225,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.9732519846994627,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 11.017045856656804,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -5.4384979248047784,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -27.78999633789067,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.0137255859374363,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 5.057763671875023,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.2123605346680506,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.6476852416992642,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.1246259441895834,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 3.830687526159904,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -2.0015928611042284,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.878745655658264,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.9666769871383494,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.09254466308977749,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -2.6678553989955383,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.1385716029575903,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.3495209844624001,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.17413433728614125,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.6229625742786524,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.15817852933686183,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.11417066962404065,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.7468026290223873,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 12.040000915527344,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 12.35000228881836,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 25.217986866244868,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 34.60709685866763,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 34.828663317930385,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 49.76690854860427,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 29.756792578856036,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 37.64091330679747,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 19.253161878660556,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 11.615472566494567,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 23.531161557774205,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 34.94004366705834,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 35.15427652805194,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 49.96763209350861,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 27.418382316341138,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 37.57361418924503,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 17.29949430485585,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 12.125581858785495,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.250499916076663,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -6.948500061035162,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.42159996032715696,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -3.5448001098632886,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.24045000076294798,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.1872500228881933,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 21.86496917215746,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 31.55726234483034,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 16.71005773429162,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 19.768725095673357,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 13.603569120165744,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 14.512872783813812,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.3553573063441684,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.18307140895298524,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.6184439564037127,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.8016365584112357,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 11.48392029700316,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 12.38449463402717,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.9965511811017553,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.2564666493197647,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 86.19000244140625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 16.07000732421875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 12.983116061443422,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 18.887992893016136,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 17.222530068474384,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 21.141453721385762,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 12.667155818517596,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 15.64856121873105,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 14.572186992741933,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -5.323558084094447,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 11.296290752972759,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 19.220939701406845,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 17.54814327859594,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 21.342177266290108,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 10.328745556002694,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 15.581262101178606,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 12.618519418937227,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -4.813448791803518,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -5.1415008544922784,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -65.23097534179692,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -2.439862060546943,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -21.642611083984434,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.0067994689941315,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 8.158660278320326,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 10.657286749596661,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 8.564401330428574,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 9.263846358182837,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 3.5536707229329334,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 11.061381696226158,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.9794252294056838,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.717860630580361,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 12.300715855189736,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.5531515167320196,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.38904937725549,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 7.8553267076112725,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.4646148526479266,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.2557627688820324,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.1607832732627945,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 4.209999084472656,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.26000213623046875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 13.087826757275499,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 15.669910685144416,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 14.117161429033098,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 16.071812832469345,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 12.538109972932808,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 14.278731344581306,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 14.1015490616699,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -7.244712997440606,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 11.401001448804836,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 16.002857493535124,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 14.442774639154655,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 16.27253637737369,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 10.199699710417907,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 14.211432227028862,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 12.147881487865192,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -6.734603705149681,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.26450004577636577,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -3.4125001907348604,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.20420005798339957,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.5488002014160145,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 9.55780936083288,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 6.085321144367439,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 8.105384034667651,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.860269618046118,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.0985715048653737,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.5957142966134206,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.5492029116545165,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.3646333118097322,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 6.617414578991312,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.4086798814769601,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.47031410692744324,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.1205588100854007,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 12.289993286132812,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.959991455078125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 9.445545556743784,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 19.21934052028399,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 18.15996246115718,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 15.857666511411683,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 10.826810956177724,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 9.285221519375277,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 9.358755053850178,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.8338414254596387,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 7.7587202482731215,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 19.5522873286747,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 18.48557567127873,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 16.05839005631603,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 8.488400693662824,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 9.217922401822833,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 7.40508748004547,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 3.343950717750566,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.8160003662109432,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -11.259999847412104,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.9879452514648221,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -6.875002746582027,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.08715301513672102,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.22951118469239873,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 6.227418093626502,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 5.46476878470169,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 5.6118681835969255,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.9271267193798476,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 4.505838800926529,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.2896396819818996,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.1014284406389514,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.538214547293528,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.6363884109785367,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.1917255043836281,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 4.18357150477723,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.32678560539378765,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.012346181580490612,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.9828072538387144,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 5.4499969482421875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.1399993896484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 4.379424972888368,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 3.232230775696421,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 3.0932357629442797,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 6.37915879322234,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 5.505570225590107,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 3.9203113939815246,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 5.189371563878598,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.9138012661805028,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.6925996644177053,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 3.5651775840871314,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 3.4188489730658356,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 6.579882338126685,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 3.167159963075207,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 3.85301227642908,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 3.235703990073892,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.40369197388957456,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.8034996032714901,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -6.917998504638689,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.18131896972656136,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.6985824584961051,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.13421058654785156,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.5798807907104617,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 3.4429467346021596,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.437383256687231,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.9927094691315492,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.2963983910512553,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 3.122100039510256,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.6107739211489003,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.038572038922991325,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.9800000871930807,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.08553857736851533,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.5959652597073619,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.698018291209003,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.0594056384398254,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.34902321937831815,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.11156381493257239,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.1599998474121094,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.15000152587890625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.4287453034576458,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 6.603703706410924,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 6.467512571935774,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 6.966184170364942,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.1266148797062776,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -6.551502525959263,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.1050579192502954,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -4.765755874347066,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.2580800050130172,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 6.936650514801634,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 6.79312578205733,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 7.166907715269288,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.211795382808623,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -6.618801643511707,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.8486096545544117,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -4.255646582056139,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.21299991607665447,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.0194999694824105,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.020345535278323723,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.06984039306641421,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.07332626342773096,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.34902776718139705,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.0450146719298576,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.21892839251041,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.8173326100656473,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.12591545595405096,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.8410564792338047,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.9005010884767017,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.09285681588309158,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.060713904244559025,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.2019759682728961,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.10225810481162911,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.6566693844978548,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.21422669675857975,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.23292169817186315,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.4659342126892234,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.3400001525878906,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.5699996948242188,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.06596145331871917,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.9313135773996857,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -2.886254542369726,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -6.432282591248439,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.208710129362589,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.601017271883155,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.13324038155835272,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.0600479522963058,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.6208638551519439,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.598366769008975,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -2.5606413322481703,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -6.231559046344093,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.129700133152312,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.6683163894355992,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.820427192246354,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.5499386600053779,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.2055000305175838,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.8110002517700252,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.03263450622559105,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.02879486083984517,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.03135192871093295,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.13021629333496065,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.22584729132357761,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.516217965537515,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.5472746046874422,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.0741583113965003,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.5706222979847464,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.3322232068078588,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.01714270455496658,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.16857119968959267,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.03937222280461383,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.30119436410948563,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.5743245746725356,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.9628373099296539,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.1132272608667464,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.8365080634521095,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.2400054931640625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.5099945068359375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.422306425147557,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.413255949621629,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.4028599665799177,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.31535993356117675,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.317163757265206,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.3875235694971177,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.583809635626211,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.8864711320300875,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.264518883323106,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.7462027580123394,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.7284731767014736,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.5160834784655233,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.021246505249694625,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.3202244519446737,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.6301420618215037,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.396580424321016,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.19650039672853836,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.4389991760253906,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.02594024658202443,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.9608029174804642,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.036082916259772446,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.07372314453124318,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.2177195923981143,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.1642856131610424,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.340528145838249,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.459975047804618,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.2763321527786808,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.8322506891246917,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.06142752511160676,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.5807168143136163,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.06311159709146663,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.3247617479152718,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.204238826167181,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.8117810505287935,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.1590586250774214,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.7997290026369118,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.0699920654296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.7100067138671875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.2549858189357268,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -3.0278274831308627,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -3.0153751911601745,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -5.905184689865384,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -2.7116224223870056,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -3.7342503404166347,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.7507472703889313,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.5682519231896137,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.9418111274063898,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.694880674740152,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -2.6897619810386186,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -5.704461144961037,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -5.050032684901906,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -3.801549457969079,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -3.7044148441936375,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.0581426308986845,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.749499511718767,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 4.064499664306652,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.35868988037108807,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.6130612182617199,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.17701927185058253,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.7896797180175668,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.38841362232164833,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.7560808644979007,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.18334873248440076,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.4240129360775242,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.08846745559565505,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.0425580612675418,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.06285749162946397,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.5278549194335938,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.034010577949848075,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.2857064805895593,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.03690396714026711,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.37435764007054395,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.0579057089977113,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.9851930806700236,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.4199981689453125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.4900054931640625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.30735267454911064,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.9000609507222386,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -2.8713567304109677,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -6.405839157856219,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.8614040130529697,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -6.270595178858485,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.6439490445762317,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.7127421689556055,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.3794726339215524,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.567114142331528,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -2.545743520289412,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -6.2051156129518725,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -4.19981427556787,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -6.337894296410929,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -2.597616618380938,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.202632876664678,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.2694999694824247,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.6594997406005803,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.13514007568359432,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.6092024230956952,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.04930934906005291,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.24478549957275675,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.16130142661952007,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.5118725223801652,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.3231035554002837,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.350682869458696,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.436476993724888,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.9036587459372978,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.11928558349609375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.10071454729352669,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.13959148836523472,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.11942207623289014,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.45681766129272994,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.5329622364066644,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.21849624642569765,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.6326928697428134,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.06000518798828125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.3400039672851562,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.08262645489208742,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -4.311055214257465,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -4.265946530131459,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -7.164940407169551,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.7771376518757469,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.3397261038014214,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.29659618458486303,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.3906658864839327,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.7694517633627505,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -3.9781084058667537,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -3.9403333200099033,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -6.9642168622652045,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.5612726106391541,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.4070252213538659,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.657071389219844,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.9007751787748601,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.4744998931884794,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.879000473022458,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.13303649902343295,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.36235549926757926,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.004709815978998222,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.050538978576653903,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.4755968543993294,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.867252198305903,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.17779729224296492,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.5244132282302472,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.047833785092676884,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.117660034582646,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.031428745814732206,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.39642824445451996,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.024898492408935713,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.347597629907872,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.04905189821802214,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.0954009214646954,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.10712065602772658,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.716585279155752,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.839996337890625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 3.6399993896484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.40692694783905914,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.6905215445216957,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -2.762296207261694,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.7033957221141316,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.022397596158077,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 3.6591653834794458,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.0630571404876221,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 3.98230142563949,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.279898360631604,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.357574736130985,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -2.436682997140138,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.9041192670184781,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.3160126663568237,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 3.591866265927002,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.890610433317085,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 4.492410717930418,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.11100006103515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.2074996948242216,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.03831527709959914,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.49325149536132074,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.03621974945068018,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.2219893646240223,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.900632109476085,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 4.559571118972161,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.801630520056329,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 3.7544833949850425,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.7814618978802312,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 3.436984857345038,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.07321439470563629,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.2332147870744976,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.0838049764594726,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.1516207404462886,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.7320229524101274,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 3.172112757863565,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.042997843509043454,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.8990704294210308,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.09000015258789062,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.20999908447265625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.34282943776875463,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.23178328632595946,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.2324210700085816,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.1543728899671155,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.5912301999977609,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.9445731082826203,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.568371465088835,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.4115054156217379,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.3439958707019084,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.1011635220647511,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.09319214011297428,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.953649345062769,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.74718006251714,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.0118722258350648,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.3852961087158722,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.0986038766691899,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.10499992370605327,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.5034999847412109,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.03141311645507727,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.10247146606445057,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.006389770507809089,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.037837867736818964,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.040495371889681664,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.7189663645006616,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.13666495142410362,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.2459928610407891,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.19067830347148096,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.3929544643175742,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.040000098092215386,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.0007144383021763234,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.09431881478895154,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.008302297825625082,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.20460824281646195,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.47741634243404496,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.0007117651409601633,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.9839497204443647,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.009998321533203125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.529998779296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.15683095256995294,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -3.2979312932342797,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -3.258461581814931,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -8.27171792714616,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.8974472084510854,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -3.7435058941331265,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.4719707644213589,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.469585711432698,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.52999435590071,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.964984484843569,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -2.932848371693375,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -8.070994382241814,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.4409630540638148,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -3.81080501168557,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.4816968093833482,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.9594764191417702,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.15499992370605042,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.7204999923706055,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.01835205078124602,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.031724319458007244,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.02155195236205998,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.10277835845947436,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.3488728645070438,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -3.001179563969325,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.021802074133758786,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.3266413698709956,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.028881535160829586,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.48707248307689,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.022499901907784614,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.044999531337193144,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.05083682997301353,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.11890143858398905,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.02215940108574177,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.1746427124189163,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.2354942115182287,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.6041492806419916,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.17000198364257812,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.8800010681152344,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.4916729230084016,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.1693016161927536,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -2.127042372172283,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -5.56632428227738,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.44927090721309515,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -3.30040178844333,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.2327112860849976,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.1603913121466247,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.1951523854622614,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.836354807802043,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.8014291620507272,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -5.365600737373033,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.889139355301804,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -3.3677009059957737,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.72095628771971,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.6705006044375525,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.16750011444091228,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.7780000686645465,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.023770599365235512,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.010735702514644174,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.018368759155272585,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.08751989364623824,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.0010296305743562328,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -3.2595895085987703,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.28553178128136736,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.706921954232321,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.29654164397401317,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.9115460899671533,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.03285734994070877,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.20857157026018414,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.06824222087887843,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.41777539629891436,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.31540255812599893,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.632654996665861,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.1432701107819066,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.4865742035451701,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 23.329986572265625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.69000244140625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 5.599460361609687,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 7.57214504383189,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 7.262213941552842,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 11.701904691025788,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 7.53552395402113,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 9.089421324771706,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 7.566651012522007,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.9602618270956089,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 3.912635053139024,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 7.905091852222601,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 7.587827151674398,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 11.902628235930136,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 5.19711369150623,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 9.022122207219262,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 5.6129834387173005,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.470371119386538,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -2.8889999389648438,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -28.238000488281273,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.7651995849610103,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -7.880799560546961,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.4985499572754861,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.8938999938965253,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 4.962049721934914,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 5.441034297192903,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 4.267504620209273,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.7189777202819219,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 4.37163021896726,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.16395908872767206,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.2249973842075903,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 4.384279523577007,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.2896210254567606,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.8425484372416081,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 3.680388968880443,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.42435752292212214,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.3961307314875788,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.11885301980317897,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.9000015258789062,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.3299942016601562,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 3.00748881692513,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.017077781968645,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.9853555246513435,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 6.1770840067191255,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 4.561491405068486,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.6825728754333076,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.8924206162822532,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.6112348387717348,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.3206635084544671,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.3500245903593555,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.3109687347728993,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 6.377807551623471,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.2230811425535855,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.615273757880864,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.061246957522453904,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.1213441310626626,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.2709999084472656,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.5129997253417997,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.07899993896484148,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.7291999816894474,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.022441635131841053,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.0769061279296892,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.0420519085951327,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.0194985139420853,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.8579918269012512,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.5874037699767243,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.9936934264684236,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.5033992465214308,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.06714248657226562,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.012143271309988712,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.008675561031640022,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.027774551369237788,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.6863420225053272,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.1804333214471718,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.19800921788156522,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.9459672584283597,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 4.6199951171875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.850006103515625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.845491686454337,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 9.0179374738544,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 8.828314368965584,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 10.994633851547697,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 3.2143237746336535,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -4.192047175376056,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.4654434696953267,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -3.3399447673557625,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.1586663779836739,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 9.350884282245108,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 9.15392757908714,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 11.195357396452044,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.8759135121187533,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -4.2593462929285,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.48822410410938044,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.8298354750648347,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.8849998474121037,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -4.963999938964832,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.23629241943359602,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.122931518554708,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.23236404418946677,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.0587125396728538,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.8232067983297133,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.792240178674777,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.5404019725737363,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.9983451563312382,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.5547304764946155,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.15364684513292648,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.21928623744419617,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.2264251708984375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.2151945817606502,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.11003279264998156,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.2551962820574474,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.4149204827604951,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.7394129910181777,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.5835716668292974,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 10.21002197265625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 3.480010986328125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 3.188069213320488,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 7.78804113307593,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 7.644858040858404,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 11.471323861483818,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 4.62451198379642,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.7043892527207496,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 3.6520624663604835,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.26032474044690446,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.501243904849825,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 8.120987941466641,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 7.97047125097996,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 11.672047406388165,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.286101721281519,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.6370901351683056,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.6983948925557772,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.2497845518440247,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.6409988403320312,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -7.171501159667969,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.146799926757808,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -6.0190008544921625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.09115005493163153,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.3798997497558503,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.8186714572249087,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.6596350865697556,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.8612443694079452,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.2873102112908494,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.5393887412937577,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.7850420652690939,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.9707140241350452,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.8928549630301337,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.37928040646482764,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.20739553258039134,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.3386371997531334,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.7971073098542263,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.056872892852234846,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.5100717068509137,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.8899993896484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -139.5999984741211,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.2813369590460857,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.7705856206776125,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.8253771715139875,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.77747911826751,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.1822558380562898,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 3.04100693759759,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.7307466887261249,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.6443723453314583,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.4054883494245773,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 3.103532429068323,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 3.1509903816355433,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.9782026631718566,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.1561544244586113,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.9737078200451457,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.2229208850785813,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 3.1544816376223874,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.25799980163574787,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -137.94749946594237,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.03652633666992244,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -142.8991766357422,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.027843246459951843,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -152.3285059738159,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.8897598494693515,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.3712207031879595,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.3151494872835734,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 4.127649040475989,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.207953463058153,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 3.2592282690595664,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.02428545270647353,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -3.17380850655692,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.0683541077620129,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.3636583925316912,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.0556407198200297,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.7201587223083976,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.0959329642591753,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.8597559148078905,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.4099998474121094,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.4200000762939453,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.7028640855968002,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 4.679791530933974,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 4.84322827038397,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 11.01399059997793,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 4.196740764540885,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 10.736672517743385,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 3.034216725954476,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 5.242481761814389,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.016038777126137216,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 5.0127383393246845,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 5.168841480505526,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 11.214714144882276,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.8583305020259844,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 10.66937340019094,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.0805491521497697,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 5.752591054105318,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.009249973297119851,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.6114999771118157,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.029799995422365555,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.32129997253418097,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.017749996185301598,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.11317500114441259,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.4038983982708864,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 6.697848484309232,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.403622367777868,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 5.4874401256221,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.3204805178829826,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 4.709781364653542,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.03000000544956749,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.19107151031494152,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.14682908667858952,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.4936753612134974,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.1761326455351764,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 4.073436751094839,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -2.9825908516395385,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.0269013127263447,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.1399993896484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.1800003051757812,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.2985863455444937,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.9066920989234681,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.8799423133848303,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -4.393069812608042,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.598689337297742,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.172132762983047,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.4841948225865025,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.5947219405465844,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.3882389629261693,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.5737452905327576,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.5543291032632744,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -4.1923462677036945,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.7397209252171582,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.2394318805354914,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.4694727512182046,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.0846126482556566,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.22049980163575356,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.9119995117187614,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.014825134277344887,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.06635940551757358,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.029304122924799003,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.13043609619140284,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.5051718303026975,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.9539194376580147,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.21634620440549313,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.550191138685153,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.2413613829886696,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.8662676025828384,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.11571448189871658,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.0900006975446428,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.15424236740006148,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.15527768899616845,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.18067080361783283,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.5228038060790876,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.015756822197473985,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.47902660020531573,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.value",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 4.350006103515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.3899993896484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_1d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 3.4052573182363433,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.4457802392428007,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_5d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.3405752357919196,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 7.539750130562816,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_20d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 6.649689705131722,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.324271359013375,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_60d_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 3.1939713638719613,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.6498422225884601,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_1d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.7184320097656802,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.7787270476335113,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_5d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.6661884459134755,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 7.740473675467162,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_20d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 4.311279442616822,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.2569722414609306,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_60d_pp",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 1.2403037900672538,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.1397329302975323,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma20",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.48600006103515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -5.224999999999994,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma50",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -0.1283999633789108,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.3817999267578216,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma200",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.13659999847411086,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.6387000274658021,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma20_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.9979697332081834,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.5967552043716244,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma50_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.73792139649912,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.6583563624446231,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma200_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 3.052284891345991,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.2672230150752277,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_sma",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.1857147216796875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.37357330322265625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 0.02248762885442357,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.2917115272332653,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.drawdown_from_63d_high_pct",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.4872812160196656,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.3665729304073064,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.volume_vs_previous20_ratio",
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": 2.595800763421976,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.3791047562338195,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS2.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.04999999999999982,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.03000000000000025,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLH0A0HYM2.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.08000000000000007,
        "unit": "percentage_points"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.0900000000000003,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLC0A0CM.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.020000000000000018,
        "unit": "percentage_points"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.029999999999999916,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS10.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.019999999999999574,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.03000000000000025,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DFII10.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.03000000000000025,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.040000000000000036,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.T10YIE.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.020000000000000018,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.09999999999999964,
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
    "available_prior_observations": 18,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-10",
        "to": "2026-11-11",
        "change": -1.9700000000000024,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.879999999999999,
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
  }
]
```

## 判断依据 · 反弹是否已可靠

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 反弹是否已可靠 |
| 事实指标引用 | ["prices.SPY.volume_vs_previous20_ratio", "prices.QQQ.sma200", "observed.QQQ.price"] |
| 推断与解释 | 当前价仍在宽基观察区上方，但盘前没有常规VWAP/回踩与收盘确认，保持脆弱修复。 |
| 反证与缺口 | 这些价位是观察区而非保证止损成交点；单次穿越VWAP及盘前上涨不代表趋势反转 |
| 确认条件 | SPY755附近、QQQ680–682首轮回踩守住；随后重新站上当日常规VWAP、形成更高低点，RSP参与同步；收盘再看SPY760.20/764.55、QQQ690.38/698.94分层收复 |
| 失效条件 | 跌破755/680并反抽失败，或反弹只集中权重股且收盘回吐，撤销风险偏好升级 |
| 观察期限 | 未来1–3交易日 |
| 条件式指导 | 等待首轮回踩、重新夺回VWAP和收盘保持；条件失效撤销升级，不将盘前小幅回升当确认。 |
| 主观置信等级 | medium |
| 判断变化原因 | 新增12日盘前与治理/政策证据；无新完整日线，成交量修订不算资金变化。 |

## 判断依据 · AI治理风险是否等于泡沫破裂

| 要素 | 记录 |
| --- | --- |
| 评估问题 | AI治理风险是否等于泡沫破裂 |
| 事实指标引用 | ["observed.NVDA.price", "prices.SMH.sma200", "prices.CRWV.return_1d_pct"] |
| 推断与解释 | 治理、需求和融资是不同链条；合约规则不能替代基本面及现金流验证。 |
| 反证与缺口 | CEO更替消息可引发双向跳空；杠杆ETF日重置与波动损耗放大路径风险 |
| 确认条件 | SMH490–493守住后收复506.96，进一步关注523附近中期均线；NVDA先停止新低并形成常规时段更高低点，恢复170.24才重评原剧本；CRWV守51.02旧突破区且预付款/融资兑现 |
| 失效条件 | SMH失490反抽失败、NVDA持续新低，或正式公告显示经营受损；任一重要反证足以降低判断，不等全触发 |
| 观察期限 | 未来1–3交易日 |
| 条件式指导 | 等待首轮回踩、重新夺回VWAP和收盘保持；条件失效撤销升级，不将盘前小幅回升当确认。 |
| 主观置信等级 | medium |
| 判断变化原因 | 新增12日盘前与治理/政策证据；无新完整日线，成交量修订不算资金变化。 |

## 判断依据 · 哪些板块优先观察

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 哪些板块优先观察 |
| 事实指标引用 | ["prices.XLI.sma20", "prices.XLV.relative_spy_20d_pp", "prices.XLP.relative_spy_20d_pp"] |
| 推断与解释 | 非芯片多日相对强度较好，可作为条件式观察；行业价量不代表当前资金净流入。 |
| 反证与缺口 | 相对强势不等于绝对上涨；价量无法证明主力净申购 |
| 确认条件 | XLI守167.70并突破172.74回踩；XLV/XLP/XLF守各自20日182.51/89.03/56.76且相对SPY保持多日强势；大盘不创新低 |
| 失效条件 | 各自20日线失守并反抽失败，或信用利差扩大使金融逻辑恶化 |
| 观察期限 | 未来1–3交易日 |
| 条件式指导 | 等待首轮回踩、重新夺回VWAP和收盘保持；条件失效撤销升级，不将盘前小幅回升当确认。 |
| 主观置信等级 | medium |
| 判断变化原因 | 新增12日盘前与治理/政策证据；无新完整日线，成交量修订不算资金变化。 |

## 判断依据 · VIX上行是否证明全面恐慌

| 要素 | 记录 |
| --- | --- |
| 评估问题 | VIX上行是否证明全面恐慌 |
| 事实指标引用 | ["observed.VIX.price", "macro.CBOE_VIX.value", "macro.BAMLH0A0HYM2.value"] |
| 推断与解释 | 盘前VIX高于昨收是风险回升线索，信用与利率数据滞后、CNN缺失，不能据此定义完整恐慌周期。 |
| 反证与缺口 | 这些价位是观察区而非保证止损成交点；单次穿越VWAP及盘前上涨不代表趋势反转 |
| 确认条件 | SPY755附近、QQQ680–682首轮回踩守住；随后重新站上当日常规VWAP、形成更高低点，RSP参与同步；收盘再看SPY760.20/764.55、QQQ690.38/698.94分层收复 |
| 失效条件 | 跌破755/680并反抽失败，或反弹只集中权重股且收盘回吐，撤销风险偏好升级 |
| 观察期限 | 未来1–3交易日 |
| 条件式指导 | 等待首轮回踩、重新夺回VWAP和收盘保持；条件失效撤销升级，不将盘前小幅回升当确认。 |
| 主观置信等级 | medium |
| 判断变化原因 | 新增12日盘前与治理/政策证据；无新完整日线，成交量修订不算资金变化。 |

## 芯片治理与合规风险主导盘前 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 董事会去留讨论仍无正式人事结果核验；参议员要求保全记录 |
| 事实：市场反应 | NVDA盘前约−7.74%、SMH约−2.75%，宽基跌幅较小 |
| 推断：解释 | 推断：集中在治理连续性与合规风险的重估，不足证明全部AI终端需求崩塌 |
| 受益篮子 | ["治理不确定性降低且承接得到验证的篮子（条件式）"] |
| 受损篮子 | ["NVDA", "高杠杆半导体篮子"] |
| 反证 | NVDA较早报盘后低位略回升；官方调查不等于违法结论 |
| 下一催化剂 | 正式治理公告、NBIS电话会及NVDA业绩 |
| 证据 | ["https://www.investing.com/news/economy-news/morning-bid-jensen-hangs-on-as-nvidia-tumbles-5020411", "https://nvidianews.nvidia.com/news/statement-from-the-independent-members-of-the-nvidia-board", "https://www.banking.senate.gov/imo/media/doc/20261111_warren_coons_letter_to_wh_commerce_state_re_nvidia_record_retentionpdf.pdf"] |

## 需求增长与融资压力并存 · 待核验

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | CRWV财报仍显示收入扩张，同时利息负担高；NBIS即将举行电话会 |
| 事实：市场反应 | CRWV盘前回撤，尚不足抹去前日大涨 |
| 推断：解释 | 推断：市场同时评估订单质量和实现现金流所需资金 |
| 受益篮子 | ["能证明预付款、利用率与现金流改善的云基础设施"] |
| 受损篮子 | ["依靠持续外部融资且交付延后的企业"] |
| 反证 | H100租金未崩塌；单个企业资金状况不代表全行业 |
| 下一催化剂 | 北京时间今晚21:00 NBIS电话会 |
| 证据 | ["https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Third-Quarter-2026-Results/default.aspx", "https://www.silicondata.com/products/silicon-index/h100", "https://nebius.com/investor-hub"] |

## 非芯片相对强度作为备选观察 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 11日参与面改善但宽基成交量仍低于近期均值 |
| 事实：市场反应 | 工业、医疗、必需消费20日相对SPY保持正值 |
| 推断：解释 | 推断：可分散单一芯片驱动，但需等自身回踩与大盘稳定 |
| 受益篮子 | ["XLI", "XLV", "XLP", "XLF（信用稳定前提）"] |
| 受损篮子 | ["持续落后并跌破支撑的高估值篮子"] |
| 反证 | 当前行业ETF盘前报价较稀疏；相对抗跌也可能绝对下跌 |
| 下一催化剂 | 12日完整交易、13日PPI及更新信用指标 |
| 证据 | ["https://www.bls.gov/schedule/2026/11_sched.htm", "https://www.ici.org/research/stats/etf_flows"] |

## tc 报价（供应商时戳不等于成交时戳）

| 标的 | 价格 USD | 变化% | 观测时间 | 供应商时间 | 抓取时间 | 质量 |
| --- | --- | --- | --- | --- | --- | --- |
| SPY | 756.46 | -0.44 | 2026-11-12T12:02:44+00:00 | 2026-11-12T12:02:44+00:00 | 2026-11-12T12:03:21.121662+00:00 | ok |
| QQQ | 684.39 | -0.87 | 2026-11-12T12:03:03+00:00 | 2026-11-12T12:03:03+00:00 | 2026-11-12T12:03:21.121662+00:00 | ok |
| SMH | 493.00 | -2.75 | 2026-11-12T12:02:34+00:00 | 2026-11-12T12:02:34+00:00 | 2026-11-12T12:03:21.121662+00:00 | ok |
| NVDA | 160.28 | -7.74 | 2026-11-12T12:03:07+00:00 | 2026-11-12T12:03:07+00:00 | 2026-11-12T12:03:21.121662+00:00 | ok |
| MSFT | 520.00 | -0.22 | 2026-11-12T12:01:52+00:00 | 2026-11-12T12:01:52+00:00 | 2026-11-12T12:03:21.121662+00:00 | ok |
| AMZN | 267.19 | 0.38 | 2026-11-12T12:02:44+00:00 | 2026-11-12T12:02:44+00:00 | 2026-11-12T12:03:21.121662+00:00 | ok |
| GOOGL | 292.24 | -0.41 | 2026-11-12T12:02:36+00:00 | 2026-11-12T12:02:36+00:00 | 2026-11-12T12:03:21.121662+00:00 | ok |
| META | 625.50 | -0.52 | 2026-11-12T12:01:50+00:00 | 2026-11-12T12:01:50+00:00 | 2026-11-12T12:03:21.121662+00:00 | ok |

## 核心行情与风险代理

| 标的 | 价格/指数 | 单位 | 观测日 | 1日% | 5日% | 20日% | 质量 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 759.81 | USD_per_share | 2026-11-11 | 1.32 | -0.91 | -1.27 | ok |
| QQQ | 690.38 | USD_per_share | 2026-11-11 | 2.31 | -0.23 | -5.29 | ok |
| IWM | 283.09 | USD_per_share | 2026-11-11 | 0.89 | -0.33 | 4.32 | ok |
| RSP | 222.65 | USD_per_share | 2026-11-11 | 0.80 | -0.30 | 4.98 | ok |
| GLD | 365.17 | USD_per_share | 2026-11-11 | -1.13 | -1.97 | -2.88 | ok |
| GC=F | 4,000.50 | USD_per_troy_ounce | 2026-11-11 | -0.74 | -1.78 | -2.61 | ok |
| CL=F | 86.53 | USD_per_barrel | 2026-11-11 | 0.57 | -1.80 | -9.00 | ok |
| BZ=F | 92.76 | USD_per_barrel | 2026-11-11 | 1.39 | -1.97 | -12.54 | ok |
| TLT | 80.92 | USD_per_share | 2026-11-11 | 0.05 | -1.03 | 3.00 | ok |
| UUP | 29.35 | USD_per_share | 2026-11-11 | 0.69 | 1.56 | 0.79 | ok |
| HYG | 77.35 | USD_per_share | 2026-11-11 | 0.22 | -0.22 | 1.23 | ok |
| LQD | 103.96 | USD_per_share | 2026-11-11 | 0.08 | -0.52 | 1.66 | ok |
| ^VIX | 17.49 | index | 2026-11-11 | -10.12 | 5.30 | 3.68 | ok |
| ^VIX3M | 19.24 | index | 2026-11-11 | -6.78 | 2.34 | 2.39 | ok |
| ^VVIX | 90.47 | index | 2026-11-11 | -6.37 | 0.07 | -4.21 | ok |
| ^MOVE | 92.43 | index | 2026-11-10 | 7.50 | -7.54 | -8.57 | stale |
| NVDA | 173.73 | USD_per_share | 2026-11-11 | 2.87 | -13.19 | -21.50 | ok |
| MSFT | 521.13 | USD_per_share | 2026-11-11 | -2.26 | -6.24 | -2.35 | ok |
| AMZN | 266.17 | USD_per_share | 2026-11-11 | -1.74 | 0.05 | 4.76 | ok |
| GOOGL | 293.45 | USD_per_share | 2026-11-11 | 2.11 | 1.56 | -15.59 | ok |
| META | 628.77 | USD_per_share | 2026-11-11 | -1.97 | -0.20 | -14.75 | ok |
| CRWV | 60.77 | USD_per_share | 2026-11-11 | 24.71 | 25.51 | -7.62 | ok |
| MU | 811.30 | USD_per_share | 2026-11-11 | 11.89 | 2.02 | -11.25 | ok |
| DRAM | 44.85 | USD_per_share | 2026-11-11 | 10.36 | -0.58 | -10.55 | ok |
| VRT | 206.51 | USD_per_share | 2026-11-11 | 6.33 | 0.47 | -7.32 | ok |

## 跨资产风险解释

11日收盘恐惧有所缓解，12日盘前事件风险又上升，尚无全面过热证据。Yahoo VIX在11:48:01UTC为18.30，高于Cboe11日收盘17.49；同期VIX3M未取得盘前值，不能拿18.30与昨收19.24拼成实时期限结构。完整11日期限比值17.49/19.24约0.909，VVIX90.47，仅反映昨收。MOVE92.43仍至10日，补查公开历史也未找到11日新值。FRED2年4.56%、10年4.88%、实际10年2.66%、HY334bp、IG91bp仍至9日；金融压力至10月30日，不能用滞后值证明今晚信用风险稳定。TNX分钟仍标11日19:59UTC，且11日债市假日，不把该值当12日实时现金债收益率。11:53UTC附近WTI85.93、Brent92.24、黄金期货3950.50、美元指数102.914，分别来自连续期货/指数分钟数据，不是官方结算；相对早报原油与黄金略低、美元略高，不能仅凭油金下跌判断战争消退。CNN接口418，官方页读取与Chrome均不可用，本轮最新值缺失；早报37/Fear只作既有历史基线，不补进当前CNN字段。GPR官网标9日更新，而本轮数据仍止于2日；战争、避险以油价、航运、GPR和信用分开呈现。[AP最新乌克兰能源报道](https://apnews.com/article/a149409da79c057c45e6a4adeb903a02)仍描述能源设施受袭，不能把局部停火谈判当作实际全面停火。[EIA11月展望](https://www.eia.gov/outlooks/steo/archives/nov26.pdf)说明航运扰动及需求压力并存；月度现货均价与此刻期货不可直接比较。

## 宏观与地缘风险指标

| 指标 | 数值 | 单位 | 观测日 | 20次观测变化 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- | --- |
| DGS2 | 4.56 | percent | 2026-11-09 | -0.24 | lagged | https://fred.stlouisfed.org/series/DGS2 |
| BAMLH0A0HYM2 | 3.34 | percentage_points | 2026-11-09 | 0.23 | lagged | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| BAMLC0A0CM | 0.91 | percentage_points | 2026-11-09 | 0.08 | lagged | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| DGS10 | 4.88 | percent | 2026-11-09 | -0.36 | lagged | https://fred.stlouisfed.org/series/DGS10 |
| DFII10 | 2.66 | percent | 2026-11-09 | -0.25 | lagged | https://fred.stlouisfed.org/series/DFII10 |
| T10YIE | 2.20 | percent | 2026-11-10 | -0.13 | lagged | https://fred.stlouisfed.org/series/T10YIE |
| STLFSI4 | -0.52 | index | 2026-10-30 | 0.24 | lagged | https://fred.stlouisfed.org/series/STLFSI4 |
| CBOE_VIX | 17.49 | index | 2026-11-11 | 0.62 | ok | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| GPRD | 113.95 | index | 2026-11-02 | -245.09 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_ACT | 129.82 | index | 2026-11-02 | -342.91 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_THREAT | 108.29 | index | 2026-11-02 | -240.96 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_MA7 | 158.85 | index | 2026-11-02 | -44.27 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_MA30 | 184.74 | index | 2026-11-02 | 13.98 | lagged | https://www.matteoiacoviello.com/gpr.htm |

## CNN Fear & Greed

缺失：CNN 无可核验数据，不使用替代指数

## 19 板块与主题 ETF：价格量能证据

| 标的 | 板块 | 1日% | 5日% | 20日% | 相对SPY 1日pp | 相对SPY 5日pp | 相对SPY 20日pp | 成交量/前20日 | 观测日 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLK | 科技 | 3.23 | -1.21 | -8.44 | 1.91 | -0.30 | -7.17 | 1.18 | 2026-11-11 |
| XLE | 能源 | 1.86 | -0.24 | -6.30 | 0.55 | 0.68 | -5.03 | 0.66 | 2026-11-11 |
| XLF | 金融 | 0.58 | -0.96 | 7.54 | -0.74 | -0.05 | 8.81 | 0.71 | 2026-11-11 |
| XLI | 工业 | 1.33 | 0.89 | 2.35 | 0.01 | 1.80 | 3.62 | 0.74 | 2026-11-11 |
| XLV | 医疗 | 0.04 | -0.37 | 8.62 | -1.28 | 0.54 | 9.89 | 0.71 | 2026-11-11 |
| XLP | 必需消费 | 0.46 | -0.53 | 6.26 | -0.86 | 0.38 | 7.54 | 0.83 | 2026-11-11 |
| XLY | 可选消费 | -0.05 | -1.10 | 8.51 | -1.37 | -0.18 | 9.78 | 0.70 | 2026-11-11 |
| XLC | 通信 | 0.78 | 3.47 | -2.00 | -0.54 | 4.38 | -0.73 | 0.69 | 2026-11-11 |
| XLU | 公用事业 | 0.21 | 0.48 | 5.03 | -1.11 | 1.39 | 6.31 | 0.58 | 2026-11-11 |
| XLRE | 房地产 | 0.02 | -1.17 | 7.47 | -1.30 | -0.26 | 8.74 | 0.51 | 2026-11-11 |
| XLB | 材料 | 0.32 | -1.63 | 6.74 | -1.00 | -0.72 | 8.02 | 0.49 | 2026-11-11 |
| SMH | 半导体 | 4.82 | 0.53 | -10.23 | 3.51 | 1.45 | -8.96 | 1.24 | 2026-11-11 |
| IGV | 软件 | 1.89 | -1.28 | -5.03 | 0.57 | -0.37 | -3.76 | 0.52 | 2026-11-11 |
| XOP | 油气开采 | 2.63 | 0.47 | -8.95 | 1.31 | 1.39 | -7.67 | 0.84 | 2026-11-11 |
| OIH | 油服 | 2.84 | 0.95 | -3.35 | 1.52 | 1.86 | -2.08 | 0.82 | 2026-11-11 |
| ITA | 航空与国防 | 1.23 | 3.23 | 7.58 | -0.09 | 4.15 | 8.85 | 0.46 | 2026-11-11 |
| ARKX | 航天主题 | 1.37 | 4.91 | -0.61 | 0.05 | 5.82 | 0.67 | 0.36 | 2026-11-11 |
| KRE | 区域银行 | -0.19 | -1.59 | 6.43 | -1.51 | -0.68 | 7.71 | 0.69 | 2026-11-11 |
| SKYY | 云计算 | 2.90 | -1.53 | -5.93 | 1.58 | -0.61 | -4.65 | 3.41 | 2026-11-11 |

## 资金证据分层

最近完整11日19个ETF中17个上涨，仍只是观察池参与度。SMH+4.82%、XLK+3.23%、SKYY+2.90%，RSP+0.80%弱于SPY+1.32%。SMH20日相对SPY−8.96个百分点，低于20/200日约523.65/523.11；IGV20日相对−3.76个百分点，尚低于20日105.62。非芯片XLI、XLF、XLV、XLP20日相对SPY分别+3.63、+8.81、+9.89、+7.54个百分点，作为优先观察而非无条件买入。XLI收170.97在20日167.70与200日172.74之间；ITA/ARKX虽上涨但量能仅0.46/0.36倍，航天尚无强成交确认。当前12:02–12:03UTC SMH493较收盘−2.75%，宽基跌幅更小，说明芯片仍相对弱；不同标的分钟端点有差异，不把盘前稀疏报价当精确资金排名。价格源修订11日成交量：SPY0.79倍、QQQ0.86倍、SMH1.24倍、NVDA2.03倍、CRWV2.22倍；早报0.76/0.83/1.22/1.82/2.18为当时抓取值，两者差异是同一交易日数据修订，不是跨期资金增量。[VanEck发行人页](https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/overview/)更新到11日NAV507.09、资产65.74B；资产上升含价格作用，缺连续精确份额与拆分核验，不推算申赎。[ICI周度估算](https://www.ici.org/research/stats/etf_flows)最新仍是10日发布、截至4日一周总净发行498.30亿美元，国内股票308.68亿、债138.89亿、商品1.29亿，早于5日大跌。当前单ETF净申赎和机构交易身份缺失，不把上涨或放量写成主力净流入。

## 最近可核验 ETF 申赎窗口

| 标的 | 金额 USD million | 起始日 | 结束日 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- |
| US_DOMESTIC_EQUITY_ETFS | 30868 | 2026-10-29 | 2026-11-04 | public_report | https://www.ici.org/research/stats/etf_flows |
| US_BOND_ETFS | 13889 | 2026-10-29 | 2026-11-04 | public_report | https://www.ici.org/research/stats/etf_flows |
| US_COMMODITY_ETFS | 129 | 2026-10-29 | 2026-11-04 | public_report | https://www.ici.org/research/stats/etf_flows |

## Polymarket 搜索覆盖与限制

12:03UTC附近重新采集原跟踪清单，并主动搜索15组：Fed/衰退/银行/政府关税、AI泡沫/NVIDIA CEO/AMD/CoreWeave、数据中心禁令、Hormuz/Iran/Ukraine/油价、SpaceX。首批每组limit10，多组hasMore，AMD空结果不能证明没有事件。新增正式CEO继任者宣布合约并核验排除临时CEO条款；其他人选及联合市值合约未纳入精选。未来一周/30天催化剂已核验NBIS、PPI、NVDA，未发现同时满足相关性与官方精确时点的精选预测合约，upcoming为空；截止日期不是事件发生日期。

## Polymarket · 值得警惕的信号

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["AI bubble burst in 2026?", "期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。", "https://polymarket.com/event/ai-bubble-burst-by"] | [12.5, {"status": "comparable", "change_pp": 1.7500000000000002}] | {"spread": 0.0040000000000000036, "volume24h_usd": 149617.720768, "liquidity_usd": 86374.84307, "quality_flags": [], "retrieved_at": "2026-11-12T12:03:36.506605+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["多条件AI合约与实际融资分开", "AI估值/融资"] | ["多个实际阈值与信用持续恶化共同出现", "需求、回款与融资恢复且阈值未满足"] | [null, null] |
| ["CoreWeave downgraded by Moody's or S&P by December 31, 2026?", "2026年12月31日23:59ET前，Moody’s或S&P正式下调CoreWeave长期主体/企业家族或高级无担保债信用评级则Yes；仅负面展望/观察名单不算，不要求降至某统一评级档。成交很薄，不视为客观违约概率。", "https://polymarket.com/event/coreweave-downgraded-by-moodys-or-sp-by"] | [18.0, {"status": "comparable", "change_pp": -1.0000000000000009}] | {"spread": 0.16, "volume24h_usd": 420.828022, "liquidity_usd": 298.4697, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"], "retrieved_at": "2026-11-12T12:03:09.022076+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["新发现评级下调合约，24h成交很薄", "算力融资成本"] | ["正式评级行动及实际融资成本共同转坏", "仅展望变化或评级不变；薄盘口不足确认"] | [null, null] |
| ["Jensen Huang announced resignation or removal by December 31, 2026?", "年末23:59美东前，黄仁勋/NVIDIA或授权代表正式明确宣布辞任或被撤去CEO，且预定在宣布后18个月内实施则Yes；不要求年内实际离任。临时休假、停职、条件式考虑、未被接受辞呈和媒体单独传闻不算。以官方信息优先；不得把调查直接视为离任。 合格辞任/撤职实际发生亦可能触发，需按专门规则核验；本次与早报hash相同。", "https://polymarket.com/event/jensen-huang-announced-resignation-or-removal-by-december-31"] | [77.5, {"status": "comparable", "change_pp": 1.0000000000000009}] | {"spread": 0.010000000000000009, "volume24h_usd": 4311274.922216, "liquidity_usd": 59447.8953, "quality_flags": [], "retrieved_at": "2026-11-12T12:03:36.506605+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["CEO离任宣布风险仍高，但媒体讨论不是公司正式决议", "NVDA及芯片风险溢价"] | ["官方明确离任或约束升级", "公司维持治理安排且无新不利事实"] | [null, null] |

## Polymarket · 有参考价值的事件

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Strait of Hormuz traffic returns to normal by December 31?", "期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。", "https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31"] | [7.5, {"status": "comparable", "change_pp": -1.0000000000000009}] | {"spread": 0.009999999999999995, "volume24h_usd": 105618.29569600002, "liquidity_usd": 241664.3798, "quality_flags": [], "retrieved_at": "2026-11-12T12:03:36.506605+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["实际通行量与外交表态分开", "油运/能源"] | ["Portwatch量持续改善并满足规则", "航运事件持续且量未恢复"] | [null, null] |
| ["Russia x Ukraine energy ceasefire agreement by November 15, 2026?", "11月15日23:59基辅时间前，俄乌双方同意暂停打击至少一类明确能源设施，双方官宣或可信报道共识确认；美国第三方单方声称不足。可限定地理范围，但仅一个设施不算；必须明确相互暂停，不是谈判/换囚。约定生效日可晚于截止。", "https://polymarket.com/event/russia-x-ukraine-energy-ceasefire-agreement-by"] | [3.1, {"status": "comparable", "change_pp": -0.75}] | {"spread": 0.008000000000000004, "volume24h_usd": 73025.433489, "liquidity_usd": 93491.09982, "quality_flags": [], "retrieved_at": "2026-11-12T12:03:36.506605+00:00", "contract_end_at": "2026-11-15T21:59:00+00:00"} | ["新能源协议合约；15日是截止非会议日", "能源供给/风险溢价"] | ["双方确认合格能源设施互停安排", "仅换囚或第三方声称"] | [null, null] |
| ["Russia x Ukraine ceasefire agreement by December 31, 2026?", "2026年末23:59ET前，双方官宣或可信共识确认相互暂停直接交战，包含明确生效日的全面暂停；仅限定目标/地点的局部能源安排不算。达成协议可先于实际生效，单方暂停不算。", "https://polymarket.com/event/russia-x-ukraine-ceasefire-agreement-by"] | [10.5, {"status": "comparable", "change_pp": 0.9999999999999996}] | {"spread": 0.009999999999999995, "volume24h_usd": 73462.47418399999, "liquidity_usd": 100610.7828, "quality_flags": [], "retrieved_at": "2026-11-12T12:03:36.506605+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["全年全面停火协议与能源局部暂停定义不同", "军工/欧洲风险偏好"] | ["双边明确全面暂停及生效日", "仅局部或单方暂停"] | [null, null] |
| ["Will WTI Crude Oil (WTI) hit (HIGH) $110 in November?", "11月合资格交易时段，Pyth对ICE Europe WTI活跃月CLL的任一最终1分钟High达到110美元即Yes；按原值不取整，最后三个交易日换月。主数据不可用时依ICE官方日高低。与Yahoo NYMEX连续WTI代理不是同一可直接裁决序列。", "https://polymarket.com/event/what-price-will-wti-hit-in-november-2026"] | [5.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.009999999999999995, "volume24h_usd": 2668.597144, "liquidity_usd": 11611.8877, "quality_flags": [], "retrieved_at": "2026-11-12T12:03:36.506605+00:00", "contract_end_at": "2026-12-01T04:59:59.999000+00:00"} | ["月内WTI高点合约；不直接用Yahoo裁决", "通胀与油气"] | ["指定Pyth/ICE价格和实际供应压力同向", "供应改善且指定价格未触发"] | [null, null] |
| ["Will the Fed increase interest rates by 50+ bps after the December 2026 meeting?", "衡量12月8–9日该次FOMC前后联邦基金目标区间上限上调至少50bp；非标准变化向上取整到最近25bp对应档。按正式声明，若下一次会议结束仍无声明则按不变档处理。不是全年累计加息幅度。", "https://polymarket.com/event/fed-decision-in-december-20260729232808632"] | [9.950000000000001, {"status": "comparable", "change_pp": -0.5999999999999992}] | {"spread": 0.0010000000000000009, "volume24h_usd": 642049.336945, "liquidity_usd": 262770.75853, "quality_flags": [], "retrieved_at": "2026-11-12T12:03:36.506605+00:00", "contract_end_at": "2026-12-09T23:59:00+00:00"} | ["12月单次50+bp风险", "利率与长久期估值"] | ["官方政策及融资/利率同步趋紧", "数据转弱与实际政策不符"] | [null, null] |
| ["Will the Fed increase interest rates by 25 bps after the December 2026 meeting?", "以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。", "https://polymarket.com/event/fed-decision-in-december-20260729232808632"] | [86.5, {"status": "comparable", "change_pp": 1.0000000000000009}] | {"spread": 0.010000000000000009, "volume24h_usd": 189071.97348100002, "liquidity_usd": 708267.9874, "quality_flags": [], "retrieved_at": "2026-11-12T12:03:36.506605+00:00", "contract_end_at": "2026-12-09T23:59:00+00:00"} | ["12月单次加息25bp定价；准确公告时点本轮不强填", "利率和估值"] | ["以正式目标区间变动匹配专门档位", "实际政策与对应档不符"] | [null, null] |
| ["New NVIDIA CEO named by December 31, 2026?", "2026年12月31日23:59纽约时间前，英伟达正式宣布黄仁勋的CEO继任者即满足；实际就任可以更晚，临时CEO不计。以公司公开声明为主要来源，可参照可信报道共识。与离任宣布合约不同。", "https://polymarket.com/event/new-nvidia-ceo-named-by-december-31-2026"] | [41.5, {"status": "no_baseline"}] | {"spread": 0.010000000000000009, "volume24h_usd": 3434.380674, "liquidity_usd": 1461.5692, "quality_flags": ["liquidity_under_10000_or_unknown"], "retrieved_at": "2026-11-12T12:03:36.506605+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["新发现：正式继任者宣布与离任宣布是两个问题，临时CEO不满足", "管理连续性、客户信任与估值风险溢价"] | ["公司公开宣布正式继任CEO，按该合同规则", "只有临时任命、讨论或截止日前没有正式继任宣布"] | [null, null] |

## Polymarket · 将要发生的事件及概率

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |

## 将要发生的事件及概率 · 本次无合格合约

本次未纳入合格合约，不代表相关风险或事件不存在。见搜索覆盖与限制。

## Jensen Huang announced resignation or removal by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1343940 / 6882826 |
| Yes 概率 % | 77.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [61.0, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 1.0000000000000009} |
| 24h成交量 / 流动性 USD | [4311274.922216, 59447.8953] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 年末23:59美东前，黄仁勋/NVIDIA或授权代表正式明确宣布辞任或被撤去CEO，且预定在宣布后18个月内实施则Yes；不要求年内实际离任。临时休假、停职、条件式考虑、未被接受辞呈和媒体单独传闻不算。以官方信息优先；不得把调查直接视为离任。 合格辞任/撤职实际发生亦可能触发，需按专门规则核验；本次与早报hash相同。 |
| 规则指纹 | 967939ae08f1461b2a8b5a40c6c07828619958ef439b679055b7698fa1e18988 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-12T12:01:15.439128Z |
| 抓取时间 | 2026-11-12T12:03:36.506605+00:00 |
| 来源 | https://polymarket.com/event/jensen-huang-announced-resignation-or-removal-by-december-31 |

## Will the Fed increase interest rates by 50+ bps after the December 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 770450 / 3215009 |
| Yes 概率 % | 9.95 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, 9.2] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.5999999999999992} |
| 24h成交量 / 流动性 USD | [642049.336945, 262770.75853] |
| 价差 pp | 0.10 |
| 到期 | 2026-12-09T23:59:00+00:00 |
| 结算规则摘要 | 衡量12月8–9日该次FOMC前后联邦基金目标区间上限上调至少50bp；非标准变化向上取整到最近25bp对应档。按正式声明，若下一次会议结束仍无声明则按不变档处理。不是全年累计加息幅度。 |
| 规则指纹 | a05ecc7aefe678e9936425027277135b8c37cdaf659af595020eb1668ec48e58 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-12T11:57:14.746336Z |
| 抓取时间 | 2026-11-12T12:03:36.506605+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-december-20260729232808632 |

## Will the Fed increase interest rates by 25 bps after the December 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 770450 / 3215008 |
| Yes 概率 % | 86.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [1.0, 9.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 1.0000000000000009} |
| 24h成交量 / 流动性 USD | [189071.97348100002, 708267.9874] |
| 价差 pp | 1.00 |
| 到期 | 2026-12-09T23:59:00+00:00 |
| 结算规则摘要 | 以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。 |
| 规则指纹 | 933a10a15eeec0ff1de30468fa20540301ed243f75cc3572d42946192f81a123 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-12T11:57:14.746336Z |
| 抓取时间 | 2026-11-12T12:03:36.506605+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-december-20260729232808632 |

## AI bubble burst in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 691340 |
| Yes 概率 % | 12.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [3.65, 4.25] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 1.7500000000000002} |
| 24h成交量 / 流动性 USD | [149617.720768, 86374.84307] |
| 价差 pp | 0.40 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | fc153b2136a8dfbadcd169dce1add40690acb1748566b99716fe7ae8fcb07330 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-12T12:01:15.439128Z |
| 抓取时间 | 2026-11-12T12:03:36.506605+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## Strait of Hormuz traffic returns to normal by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 455875 / 2176270 |
| Yes 概率 % | 7.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-1.0, -3.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -1.0000000000000009} |
| 24h成交量 / 流动性 USD | [105618.29569600002, 241664.3798] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。 |
| 规则指纹 | b0c8ba27f4437b0d8ab819ae170bec118166232e39cdcaefb95bd352d29073d4 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-12T12:03:15.52768Z |
| 抓取时间 | 2026-11-12T12:03:36.506605+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31 |

## Russia x Ukraine ceasefire agreement by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 478472 / 2243897 |
| Yes 概率 % | 10.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-4.0, -2.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.9999999999999996} |
| 24h成交量 / 流动性 USD | [73462.47418399999, 100610.7828] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年末23:59ET前，双方官宣或可信共识确认相互暂停直接交战，包含明确生效日的全面暂停；仅限定目标/地点的局部能源安排不算。达成协议可先于实际生效，单方暂停不算。 |
| 规则指纹 | 2ea22f9548269db3205e41396a99073a2d5788dc4fde17989e34c8051ae6b75b |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-12T12:01:15.439128Z |
| 抓取时间 | 2026-11-12T12:03:36.506605+00:00 |
| 来源 | https://polymarket.com/event/russia-x-ukraine-ceasefire-agreement-by |

## Russia x Ukraine energy ceasefire agreement by November 15, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1360126 / 6947935 |
| Yes 概率 % | 3.10 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-1.4, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.75} |
| 24h成交量 / 流动性 USD | [73025.433489, 93491.09982] |
| 价差 pp | 0.80 |
| 到期 | 2026-11-15T21:59:00+00:00 |
| 结算规则摘要 | 11月15日23:59基辅时间前，俄乌双方同意暂停打击至少一类明确能源设施，双方官宣或可信报道共识确认；美国第三方单方声称不足。可限定地理范围，但仅一个设施不算；必须明确相互暂停，不是谈判/换囚。约定生效日可晚于截止。 |
| 规则指纹 | a3874db8482536581cb7832c287d198abdb207e6448a0fd10b7da294d17de561 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-12T12:01:15.439128Z |
| 抓取时间 | 2026-11-12T12:03:36.506605+00:00 |
| 来源 | https://polymarket.com/event/russia-x-ukraine-energy-ceasefire-agreement-by |

## US x Iran Effective Ceasefire by November 15?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1337182 / 6831494 |
| Yes 概率 % | 52.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-1.5, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -1.5000000000000013} |
| 24h成交量 / 流动性 USD | [27380.683061, 75783.4229] |
| 价差 pp | 2.00 |
| 到期 | 2026-11-15T20:29:00+00:00 |
| 结算规则摘要 | 须完成连续14个伊朗标准时间日，美国未对伊朗陆地及内水实施命中目标的合资格空袭/地对地导弹攻击，且该14天首日在创建后至11月15日范围内；最后一次合资格行动次日为首日，无行动则创建日为首日。拦截碎片、威胁、海域/领空、地面入侵、网络、小型武器/部分小型袭击等不算。第14日后再留3个日历日报道窗口，按官方信息及可信报道综合裁定。不是双方全面停火，也不要求14天在15日前完成。 |
| 规则指纹 | c70e370d0e95bf9245a1a527f4f02bb307f13aa2766e1cc24004c7559bfb4b53 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-12T12:01:15.439128Z |
| 抓取时间 | 2026-11-12T12:03:36.506605+00:00 |
| 来源 | https://polymarket.com/event/us-x-iran-effective-ceasefire-begins-by-2-week-pause-20261108 |

## AI bubble burst by June 30, 2027?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 4838928 |
| Yes 概率 % | 25.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [3.0, 2.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.5000000000000004} |
| 24h成交量 / 流动性 USD | [13642.157198000003, 80542.7158] |
| 价差 pp | 1.00 |
| 到期 | 2027-07-01T03:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | bd0420587e08487fffa5050e7fd9b79ffff909a9f843d3f620207ee859462505 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-12T12:01:15.439128Z |
| 抓取时间 | 2026-11-12T12:03:36.506605+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## New NVIDIA CEO named by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1367877 / 6977205 |
| Yes 概率 % | 41.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, null] |
| 与上一快照可比变化 | {"status": "no_baseline"} |
| 24h成交量 / 流动性 USD | [3434.380674, 1461.5692] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59纽约时间前，英伟达正式宣布黄仁勋的CEO继任者即满足；实际就任可以更晚，临时CEO不计。以公司公开声明为主要来源，可参照可信报道共识。与离任宣布合约不同。 |
| 规则指纹 | 09c6c6ee9faa8f03a8b6caf37ffb4757f33e53eedba525eae02360d329bf2d68 |
| 质量 | ["liquidity_under_10000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-12T12:01:15.439128Z |
| 抓取时间 | 2026-11-12T12:03:36.506605+00:00 |
| 来源 | https://polymarket.com/event/new-nvidia-ceo-named-by-december-31-2026 |

## Will WTI Crude Oil (WTI) hit (HIGH) $110 in November?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1250301 / 6172751 |
| Yes 概率 % | 5.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-1.5, -9.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [2668.597144, 11611.8877] |
| 价差 pp | 1.00 |
| 到期 | 2026-12-01T04:59:59.999000+00:00 |
| 结算规则摘要 | 11月合资格交易时段，Pyth对ICE Europe WTI活跃月CLL的任一最终1分钟High达到110美元即Yes；按原值不取整，最后三个交易日换月。主数据不可用时依ICE官方日高低。与Yahoo NYMEX连续WTI代理不是同一可直接裁决序列。 |
| 规则指纹 | 97cca376098aad5ff8f5ece05abb9ae13f218bc5005dc802696a1f1922949a52 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-12T12:01:15.439128Z |
| 抓取时间 | 2026-11-12T12:03:36.506605+00:00 |
| 来源 | https://polymarket.com/event/what-price-will-wti-hit-in-november-2026 |

## Tesla and SpaceX merger officially announced by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 192962 / 2252540 |
| Yes 概率 % | 9.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [2475.1, 14539.035] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59纽约时间前，Tesla或SpaceX正式宣布双方合并或一方收购另一方的控制权即Yes；无需在期限内完成交易。控制权通常为过半权益或等效治理权；少数股权投资及仅讨论不算。以公司公告或可信报道共识核验；旧URL中的june-30不是本合约期限。 |
| 规则指纹 | 909906ae3b6db7e473468713ea6a1e1e4cf4c931fe247c7d3d576e7986513008 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-12T11:59:15.035951Z |
| 抓取时间 | 2026-11-12T12:03:36.506605+00:00 |
| 来源 | https://polymarket.com/event/tesla-and-spacex-merger-officially-announced-by-june-30 |

## CoreWeave downgraded by Moody's or S&P by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1219851 / 5939467 |
| Yes 概率 % | 18.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-13.0, -3.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -1.0000000000000009} |
| 24h成交量 / 流动性 USD | [420.828022, 298.4697] |
| 价差 pp | 16.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59ET前，Moody’s或S&P正式下调CoreWeave长期主体/企业家族或高级无担保债信用评级则Yes；仅负面展望/观察名单不算，不要求降至某统一评级档。成交很薄，不视为客观违约概率。 |
| 规则指纹 | 040e522db15913bd31de0e1a7f935727361429e7c42b3c1fc5286a0cf1b0fc42 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"] |
| 元数据更新（不是成交时间） | 2026-11-12T12:01:15.439128Z |
| 抓取时间 | 2026-11-12T12:03:09.022076+00:00 |
| 来源 | https://polymarket.com/event/coreweave-downgraded-by-moodys-or-sp-by |

## AI 压力：合约、经营与估值分开

三层分开。合约层：AI泡沫2026为12.5%、2027年6月25.5%，相对早报同规则分别+1.75与+0.50个百分点；两份结算定义不同，不能跨期限相减作为泡沫速度。离任宣布77.5%、24h约431万美元，较早报+1个百分点；新增正式继任CEO宣布合约41.5%，不接受临时CEO，不能与离任合约相减得出另一事件概率。CRWV降级18%、价差16个百分点、24h约421美元，质量很弱。压力证据层：[H100指数](https://www.silicondata.com/products/silicon-index/h100)标11日3.06美元/GPU小时、7日+7.4%，不满足≤1连续5天阈值；页面无日期FAQ仍写2.53，优先采用有日期序列并披露差异。[CRWV官方Q3](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Third-Quarter-2026-Results/default.aspx)收入36.61亿美元、营业利润2.07亿、净利息8.46亿，约90亿未来三个月客户预付款是预期并非已到账。盘前56.69较收盘−6.71%；融资和需求仍需分开。[NVDA10日独立董事公告](https://nvidianews.nvidia.com/news/statement-from-the-independent-members-of-the-nvidia-board)确认聘请外部律师调查；[12日Reuters报道](https://www.investing.com/news/economy-news/morning-bid-jensen-hangs-on-as-nvidia-tumbles-5020411)称董事会已讨论CEO去留，但不是已公布免职。[11日参议员公开信](https://www.banking.senate.gov/imo/media/doc/20261111_warren_coons_letter_to_wh_commerce_state_re_nvidia_record_retentionpdf.pdf)要求行政部门保全相关记录并于17日前确认，不是法院判决或新增正式出口禁令。MSFT520、AMZN267.19、GOOGL292.24、META625.50为12:01–12:02UTC附近盘前报价，与NVDA异动不可假定同一因果。估值层：本次SEC五家最新定期披露列表核验成功，日期仍为NVDA8月26日、MSFT10月28日、AMZN10月30日、GOOGL10月29日、META10月22日；复用相同已核验底稿，仅NVDA完整FCFF可计算，其余四家公司完整企业现金流桥仍缺失。模型更新盘前价格，五年经营假设/折现/终值敏感性与反推见底稿；不是对新闻任意套用固定跌幅，也不把公司整体价值都归因于AI。tc多项评级下调、新贷款及Alphabet债券线索尚未逐份取得原始文件，只作线索，不写成已完成融资或确定盈利下修。

## NVDA · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | scenario_analysis |
| 财务底稿 | TTM 至 2026-07-26；最新 10-Q / filed 2026-08-26 |
| 披露检查 | {"checked_at": "2026-11-12T12:03:06.898525+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001045810.json", "latest_filing_date": "2026-08-26"} |
| 观测财务数据 | {"ttm_revenue_million": 302970, "revenue_quarters": [{"end": "2025-10-26", "value": 57006000000, "filed": "2025-11-19", "duration_days": 91}, {"end": "2026-01-25", "value": 68127000000, "filed": "2026-02-25", "duration_days": 91}, {"end": "2026-04-26", "value": 81615000000, "filed": "2026-05-20", "duration_days": 91}, {"end": "2026-07-26", "value": 96221000000, "filed": "2026-08-26", "duration_days": 91}], "cash_million": 22443.0, "liquid_investments_million": 34143.0, "debt_million": 33366.0, "finance_lease_million": 0, "diluted_shares_million": 24285.0, "latest_operating_income_million": 63734.0, "observed_end": "2026-07-26", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "Revenues", "latest_reported_revenue_million": 96221.0, "income_statement_window": "最近单季度", "ttm_bridge_note": "采用同版 FY2026全年 + FY2027半年 - FY2026半年；与四季逐项求和差1百万为披露舍入差。"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json", "https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。10-Q Note14 表明融资租赁费用不重大；模型按不重大近似零，不将其称为精确零负债。未确认担保仅作为压力情景，非已到期净债务。市场化股权42783和非市场化股权51157不作为类现金；非经营资产加回为0的保守假设。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | 无 |
| 价格 USD | 173.73 |
| 基期输入 USD million / million shares | {"revenue": 302970, "net_debt": -23220.0, "diluted_shares": 24285.0, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.2326540495716557, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## NVDA · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 98.77 | -43.15 | 14.00 | 60.00 | 12.00 | 68.42 |
| 基准 | 154.12 | -11.29 | 20.00 | 65.00 | 11.00 | 74.20 |
| 乐观 | 242.58 | 39.63 | 26.00 | 70.00 | 10.00 | 79.05 |

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
| 披露检查 | {"checked_at": "2026-11-12T12:03:10.485089+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0000789019.json", "latest_filing_date": "2026-10-28"} |
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
| 披露检查 | {"checked_at": "2026-11-12T12:03:14.030610+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001018724.json", "latest_filing_date": "2026-10-30"} |
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
| 披露检查 | {"checked_at": "2026-11-12T12:03:17.751305+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001652044.json", "latest_filing_date": "2026-10-29"} |
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
| 披露检查 | {"checked_at": "2026-11-12T12:03:21.296247+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001326801.json", "latest_filing_date": "2026-10-22"} |
| 观测财务数据 | {"revenue_million": 64601, "operating_cashflow_million": 32790, "reported_capex_including_finance_lease_principal_million": 34910, "company_defined_fcf_million": -2120, "diluted_shares_million": 2573, "reported_operating_income_million": 12988, "legal_charge_million": 9900, "observed_end": "2026-09-30", "published_at": "2026-10-21T16:01:00-04:00", "unit": "USD million; shares million", "noncancelable_commitments_million": 454520, "leases_not_commenced_million": 355730, "contingent_cloud_capacity_max_million": 14720, "restricted_cash_reclassified_million": 10800, "commitments_due_2026_million": 45850, "commitments_due_2027_million": 121410} |
| 来源 | ["https://www.prnewswire.com/news-releases/meta-reports-third-quarter-2026-results-302915964.html", "https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm", "https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Announces-Launch-of-Offering-of-Depositary-Shares-Representing-Series-A-Mandatory-Convertible-Preferred-Stock-and-Offering-of-Class-A-Common-Stock-in-Connection-with-Forward-Sale-Agreements/default.aspx", "https://www.prnewswire.com/news-releases/meta-announces-pricing-of-offering-of-depositary-shares-representing-series-a-mandatory-convertible-preferred-stock-and-offering-of-class-a-common-stock-in-connection-with-forward-sale-agreements-302920247.html"] |
| 口径 | 公司FCF扣除融资租赁本金，不能直接代替模型FCFF；融资租赁负债/新增资产未齐，不假设零。法律费用不全归AI经营。 |
| 主观假设说明 | 缺失 |
| 权益桥额外假设 | 无 |
| 缺失原因 | 沿用底稿的历史核验说明（其中“本次”指原核验日）；本轮最新定期财报列表检查见disclosure_check。22日10-Q已核验，本次无新增定期财报。27日普通股625美元定价、优先票息6.5%已核验；完整融资租赁负债/新增资产、优先权益/远期发行与现金到账桥未齐，不用不同承诺简单充当现有债务，暂停精确FCFF反推。 |

## 宽基反弹可靠性

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 盘前事件冲击后的完整常规时段 |
| 关联标的 | ["SPY", "QQQ", "RSP"] |
| 确认条件 | SPY755附近、QQQ680–682首轮回踩守住；随后重新站上当日常规VWAP、形成更高低点，RSP参与同步；收盘再看SPY760.20/764.55、QQQ690.38/698.94分层收复 |
| 失效条件 | 跌破755/680并反抽失败，或反弹只集中权重股且收盘回吐，撤销风险偏好升级 |
| 观察期限 | 11月12–13日常规交易；NVDA事件延伸至17日 |
| 反证 | 这些价位是观察区而非保证止损成交点；单次穿越VWAP及盘前上涨不代表趋势反转 |
| 状态 | 观察项，未确认 |

## 芯片需额外确认

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 治理公告与云计算业绩 |
| 关联标的 | ["SMH", "NVDA", "CRWV", "MU"] |
| 确认条件 | SMH490–493守住后收复506.96，进一步关注523附近中期均线；NVDA先停止新低并形成常规时段更高低点，恢复170.24才重评原剧本；CRWV守51.02旧突破区且预付款/融资兑现 |
| 失效条件 | SMH失490反抽失败、NVDA持续新低，或正式公告显示经营受损；任一重要反证足以降低判断，不等全触发 |
| 观察期限 | 11月12–13日常规交易；NVDA事件延伸至17日 |
| 反证 | CEO更替消息可引发双向跳空；杠杆ETF日重置与波动损耗放大路径风险 |
| 状态 | NVDA原价格修复条件仍失效；其他观察项待确认 |

## 非芯片备选

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 风险重新分配和PPI |
| 关联标的 | ["XLI", "XLV", "XLP", "XLF"] |
| 确认条件 | XLI守167.70并突破172.74回踩；XLV/XLP/XLF守各自20日182.51/89.03/56.76且相对SPY保持多日强势；大盘不创新低 |
| 失效条件 | 各自20日线失守并反抽失败，或信用利差扩大使金融逻辑恶化 |
| 观察期限 | 11月12–13日常规交易；NVDA事件延伸至17日 |
| 反证 | 相对强势不等于绝对上涨；价量无法证明主力净申购 |
| 状态 | 观察项，未确认 |

## 跨期比较与上期剧本复核

对照北京时间12日早报，尚无新的完整日线，价格量能差异只可能是盘前或源数据修订；SPY 756.46（较11日常规收盘-0.44%）；QQQ 684.39（较11日常规收盘-0.87%）；SMH 493.00（较11日常规收盘-2.75%）；NVDA 160.28（较11日常规收盘-7.74%）；CRWV 56.69（较11日常规收盘-6.71%）。相对早报约23:20UTC的NVDA158.50、QQQ683.21、SMH492，当前略回升，但NVDA仍远低于原170.24修复线，个股旧条件仍失效。SPY755、QQQ680–682、SMH490–493在当前报价处未全部跌破，但这不是常规时段回踩验证；未开盘，没有今天常规VWAP或收盘保持证据。早报“等待下一交易日承接”的剧本继续有效，未升级为确认。同比较ID及rule_hash：Strait of Hormuz traffic returns to normal by December 31?：-1.00个百分点；Will the Fed increase interest rates by 25 bps after the December 2026 meeting?：+1.00个百分点；AI bubble burst in 2026?：+1.75个百分点；AI bubble burst by June 30, 2027?：+0.50个百分点；Tesla and SpaceX merger officially announced by December 31?：+0.00个百分点；Jensen Huang announced resignation or removal by December 31, 2026?：+1.00个百分点；US x Iran Effective Ceasefire by November 15?：-1.50个百分点；Will the Fed increase interest rates by 50+ bps after the December 2026 meeting?：-0.60个百分点；CoreWeave downgraded by Moody's or S&P by December 31, 2026?：-1.00个百分点；Russia x Ukraine energy ceasefire agreement by November 15, 2026?：-0.75个百分点；Russia x Ukraine ceasefire agreement by December 31, 2026?：+1.00个百分点；Will WTI Crude Oil (WTI) hit (HIGH) $110 in November?：+0.00个百分点。新继任CEO合约为首次基线，不制造历史变化。

## 可计算的跨期变化

```json
[
  {
    "mode": "daily",
    "baseline": "reports/daily/2026-11-11/20261111T232944.645060Z/evidence.json",
    "baseline_cutoff": "2026-11-11T23:29:24.798314+00:00",
    "close_change_pct": {
      "SPY": 0.0,
      "QQQ": 0.0,
      "IWM": 0.0,
      "RSP": 0.0,
      "GLD": 0.0,
      "GC=F": 0.2480805418103582,
      "CL=F": 0.22006306400881304,
      "BZ=F": 0.2702410487807061,
      "TLT": 0.0,
      "UUP": 0.0,
      "HYG": 0.0,
      "LQD": 0.0,
      "^VIX": 0.0,
      "^VIX3M": 0.0,
      "^VVIX": 0.0,
      "^MOVE": 0.0,
      "NVDA": 0.0,
      "MSFT": 0.0009603996761864408,
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
        "change_pct": 0.03835116442070241,
        "from_observed_at": "2026-11-11T23:19:55+00:00",
        "to_observed_at": "2026-11-12T12:02:44+00:00"
      },
      "QQQ": {
        "change_pct": 0.17271409961796547,
        "from_observed_at": "2026-11-11T23:20:14+00:00",
        "to_observed_at": "2026-11-12T12:03:03+00:00"
      },
      "SMH": {
        "change_pct": 0.20325203252031798,
        "from_observed_at": "2026-11-11T23:19:42+00:00",
        "to_observed_at": "2026-11-12T12:02:34+00:00"
      },
      "NVDA": {
        "change_pct": 1.1230283911672023,
        "from_observed_at": "2026-11-11T23:20:14+00:00",
        "to_observed_at": "2026-11-12T12:03:07+00:00"
      },
      "MSFT": {
        "change_pct": -0.38886654023714273,
        "from_observed_at": "2026-11-11T23:20:07+00:00",
        "to_observed_at": "2026-11-12T12:01:52+00:00"
      },
      "AMZN": {
        "change_pct": -0.42856078109859697,
        "from_observed_at": "2026-11-11T23:20:14+00:00",
        "to_observed_at": "2026-11-12T12:02:44+00:00"
      },
      "GOOGL": {
        "change_pct": -1.4434102252799064,
        "from_observed_at": "2026-11-11T23:20:13+00:00",
        "to_observed_at": "2026-11-12T12:02:36+00:00"
      },
      "META": {
        "change_pct": -0.4552481489132121,
        "from_observed_at": "2026-11-11T23:19:42+00:00",
        "to_observed_at": "2026-11-12T12:01:50+00:00"
      }
    },
    "macro_change": {
      "DGS2": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-11-09"
      },
      "BAMLH0A0HYM2": {
        "change": 0.0,
        "unit": "percentage_points",
        "observation_date": "2026-11-09"
      },
      "BAMLC0A0CM": {
        "change": 0.0,
        "unit": "percentage_points",
        "observation_date": "2026-11-09"
      },
      "DGS10": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-11-09"
      },
      "DFII10": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-11-09"
      },
      "T10YIE": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-11-10"
      },
      "STLFSI4": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-30"
      },
      "CBOE_VIX": {
        "change": -1.9700000000000024,
        "unit": "index",
        "observation_date": "2026-11-11"
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
        "change_pp": 1.0000000000000009
      },
      "3215009": {
        "status": "comparable",
        "change_pp": -0.5999999999999992
      },
      "3215008": {
        "status": "comparable",
        "change_pp": 1.0000000000000009
      },
      "691340": {
        "status": "comparable",
        "change_pp": 1.7500000000000002
      },
      "2176270": {
        "status": "comparable",
        "change_pp": -1.0000000000000009
      },
      "2243897": {
        "status": "comparable",
        "change_pp": 0.9999999999999996
      },
      "6947935": {
        "status": "comparable",
        "change_pp": -0.75
      },
      "6831494": {
        "status": "comparable",
        "change_pp": -1.5000000000000013
      },
      "4838928": {
        "status": "comparable",
        "change_pp": 0.5000000000000004
      },
      "6172751": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "2252540": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "5939467": {
        "status": "comparable",
        "change_pp": -1.0000000000000009
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
    "event": "NBIS Q3电话会，北京今晚21:00；IR仍展示日程，未核验本季结果正文",
    "date": "2026-11-12T08:00:00-05:00",
    "source": "https://nebius.com/investor-hub"
  },
  {
    "event": "10月PPI，北京13日21:30；CPI已10日公布",
    "date": "2026-11-13T08:30:00-05:00",
    "source": "https://www.bls.gov/schedule/2026/11_sched.htm"
  },
  {
    "event": "NVDA财报预计16:20EST，电话会17:00EST；北京时间18日05:20/06:00",
    "date": "2026-11-17T16:20:00-05:00",
    "source": "https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/default.aspx"
  },
  {
    "event": "英伟达正式治理及人事决定，时间未定",
    "date": null,
    "source": "https://nvidianews.nvidia.com/news/statement-from-the-independent-members-of-the-nvidia-board"
  },
  {
    "event": "参议员要求17日前确认记录保全；是要求期限，不保证届时公开答复",
    "date": null,
    "source": "https://www.banking.senate.gov/imo/media/doc/20261111_warren_coons_letter_to_wh_commerce_state_re_nvidia_record_retentionpdf.pdf"
  }
]
```

## 新闻事件去重与时间

| 事件 | 摘要 | 发生时间（未知留空） | 各来源发布时间 / 抓取时间 |
| --- | --- | --- | --- |
| 20261112-nv | Reuters报道董事会讨论去留，尚未核验正式人事结果。 | 缺失 | [{"source": "https://www.investing.com/news/economy-news/morning-bid-jensen-hangs-on-as-nvidia-tumbles-5020411", "published_at": "2026-11-12T05:37:00+00:00", "retrieved_at": "2026-11-12T12:10:14.349003+00:00"}] |
| 20261112-board | 补充官方10日独立董事公告：已聘外部律师开展独立调查；不等于免职决定。 | 缺失 | [{"source": "https://nvidianews.nvidia.com/news/statement-from-the-independent-members-of-the-nvidia-board", "published_at": null, "retrieved_at": "2026-11-12T12:10:14.349003+00:00"}] |
| 20261112-senate | 11日公开信要求政府保全出口相关记录、17日前确认；正文复开失败，但官方索引段落可核验。 | 缺失 | [{"source": "https://www.banking.senate.gov/imo/media/doc/20261111_warren_coons_letter_to_wh_commerce_state_re_nvidia_record_retentionpdf.pdf", "published_at": null, "retrieved_at": "2026-11-12T12:10:14.349003+00:00"}] |
| 20261112-crwv | 10日财报增长与利息压力并存，未来预付款属于公司预计。 | 缺失 | [{"source": "https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Third-Quarter-2026-Results/default.aspx", "published_at": null, "retrieved_at": "2026-11-12T12:10:14.349003+00:00"}] |
| 20261112-geo | AP报道乌克兰能源设施仍受袭，局部谈判不能当全面停火。 | 缺失 | [{"source": "https://apnews.com/article/a149409da79c057c45e6a4adeb903a02", "published_at": "2026-11-12T05:18:24+00:00", "retrieved_at": "2026-11-12T12:10:14.349003+00:00"}] |

## 覆盖范围与数据缺口

```json
[
  "tc统一请求ts不作为成交时点；另存规范化包，核心状态使用独立分钟实际时戳。",
  "今日常规时段尚未开始，常规VWAP、开盘区间、回踩承接和全成分广度均未核验；17/19只代表ETF观察池。",
  "tc新闻主批和技术批各50条且has_more，15组Gamma搜索亦有截断，不承诺全市场覆盖。",
  "CNN API418，官方页面及Chrome连接不可用，当前值缺失；早报37不当本轮新观测。",
  "MOVE仍至10日；FRED收益率/信用至9日，债市11日假日；TNX旧分钟不能冒充12日现金债。",
  "GPR官网标9日更新而序列仍至2日；保留来源与滞后，不制造综合战争或避险指数。",
  "当前单ETF净申赎、完整机构交易身份缺失；ICI窗口早于5日大跌，VanEck资产变化混合价格效应，不据此推算流入。",
  "源数据修订11日成交量，不能把早晚量能差异写成资金新流入；部分盘前ETF报价稀疏。",
  "CRWV评级合约价差16个百分点、成交薄；预测合约无完整盘口/最后成交时戳，专门结算规则不同。",
  "五家公司SEC定期披露检查成功不等于全覆盖8-K；四家完整FCFF桥缺失，禁止填造估值。",
  "DRAM历史不足200日；连续期货换月与交易时段不同。",
  "NVDA媒体去留报道尚无正式决定核验；参议员PDF复开失败，采用官方索引有限段落；NBIS实际Q3结果尚未取得，不预写财报结论。",
  "H100有日期序列3.06与无日期FAQ2.53冲突；采用有日期序列并保持说明。",
  "本轮浏览器连接不可用，无法重新视觉验收HTML；渲染器未修改，执行同源与结构校验。",
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
  "prices.^MOVE: missing_or_stale",
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
  "指标缺失/历史不足: prices.^VIX.volume_vs_previous20_ratio, prices.^VIX3M.volume_vs_previous20_ratio, prices.^VVIX.volume_vs_previous20_ratio, prices.^MOVE.value, prices.^MOVE.return_1d_pct, prices.^MOVE.return_5d_pct, prices.^MOVE.return_20d_pct, prices.^MOVE.return_60d_pct, prices.^MOVE.relative_spy_1d_pp, prices.^MOVE.relative_spy_5d_pp, prices.^MOVE.relative_spy_20d_pp, prices.^MOVE.relative_spy_60d_pp, prices.^MOVE.sma20, prices.^MOVE.sma50, prices.^MOVE.sma200, prices.^MOVE.distance_sma20_pct, prices.^MOVE.distance_sma50_pct, prices.^MOVE.distance_sma200_pct, prices.^MOVE.atr14_sma, prices.^MOVE.atr14_pct, prices.^MOVE.drawdown_from_63d_high_pct, prices.^MOVE.volume_vs_previous20_ratio, prices.DRAM.sma200, prices.DRAM.distance_sma200_pct"
]
```

## 来源、时间与核验记录

```json
[
  {
    "url": "https://www.investing.com/news/economy-news/morning-bid-jensen-hangs-on-as-nvidia-tumbles-5020411",
    "checked_at": "2026-11-12T12:10:14.349003+00:00",
    "note": "本轮核验。"
  },
  {
    "url": "https://nvidianews.nvidia.com/news/statement-from-the-independent-members-of-the-nvidia-board",
    "checked_at": "2026-11-12T12:10:14.349003+00:00",
    "note": "本轮核验。"
  },
  {
    "url": "https://www.banking.senate.gov/imo/media/doc/20261111_warren_coons_letter_to_wh_commerce_state_re_nvidia_record_retentionpdf.pdf",
    "checked_at": "2026-11-12T12:10:14.349003+00:00",
    "note": "本轮核验。官方PDF正文打开失败，使用可读官方搜索索引，未扩展未核验细节。"
  },
  {
    "url": "https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Third-Quarter-2026-Results/default.aspx",
    "checked_at": "2026-11-12T12:10:14.349003+00:00",
    "note": "本轮核验。"
  },
  {
    "url": "https://www.bls.gov/schedule/2026/11_sched.htm",
    "checked_at": "2026-11-12T12:10:14.349003+00:00",
    "note": "本轮核验。"
  },
  {
    "url": "https://nebius.com/investor-hub",
    "checked_at": "2026-11-12T12:10:14.349003+00:00",
    "note": "本轮核验。"
  },
  {
    "url": "https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/default.aspx",
    "checked_at": "2026-11-12T12:10:14.349003+00:00",
    "note": "本轮核验。"
  },
  {
    "url": "https://www.ici.org/research/stats/etf_flows",
    "checked_at": "2026-11-12T12:10:14.349003+00:00",
    "note": "本轮核验。"
  },
  {
    "url": "https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/overview/",
    "checked_at": "2026-11-12T12:10:14.349003+00:00",
    "note": "本轮核验。"
  },
  {
    "url": "https://edition.cnn.com/markets/fear-and-greed",
    "checked_at": "2026-11-12T12:10:14.349003+00:00",
    "note": "本轮核验。接口418、官方页及Chrome均不可用；最新值缺失。"
  },
  {
    "url": "https://www.silicondata.com/products/silicon-index/h100",
    "checked_at": "2026-11-12T12:10:14.349003+00:00",
    "note": "本轮核验。有日期数据优先于无日期FAQ；冲突已披露。"
  },
  {
    "url": "https://www.matteoiacoviello.com/gpr.htm",
    "checked_at": "2026-11-12T12:10:14.349003+00:00",
    "note": "本轮核验。"
  },
  {
    "url": "https://www.eoddata.com/stockquote/INDEX/MOVE.htm",
    "checked_at": "2026-11-12T12:10:14.349003+00:00",
    "note": "本轮核验。"
  },
  {
    "url": "https://www.eia.gov/outlooks/steo/archives/nov26.pdf",
    "checked_at": "2026-11-12T12:10:14.349003+00:00",
    "note": "本轮核验。"
  },
  {
    "url": "https://apnews.com/article/a149409da79c057c45e6a4adeb903a02",
    "checked_at": "2026-11-12T12:10:14.349003+00:00",
    "note": "本轮核验。"
  }
]
```

## 付费信源建议（未订阅）

```json
[]
```
