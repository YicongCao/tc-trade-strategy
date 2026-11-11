# 每日交易总结 · 2026-11-11

## 一分钟读懂 · Agent 摘要

### 当前判断

这是反弹增强后再遇新冲击，尚不是可靠的趋势反转。常规时段的涨幅真实存在，但不能直接延伸为下一交易日的乐观判断。

### 与上次相比

相对昨晚盘前，QQQ守住200日线并收涨，SMH、CoreWeave领涨；盘后媒体报道英伟达董事会准备更换CEO，芯片重新下挫。报道尚不是正式人事决定。

### 最重要的信号

- 收盘SPY+1.32%、QQQ+2.31%、SMH+4.82%，但SPY与QQQ量能只有前20日均量约0.76和0.83倍。
- 23:20UTC附近NVDA158.50，较收盘约−8.77%；SMH492，回到此前490–493观察区。
- CNN37仍属恐惧，收盘VIX17.49；这些读数不能证明盘后事件风险已解除。

### 接下来观察

- 下一交易日看SPY755、QQQ680–682、SMH490–493能否回踩守住；随后还需收复当日VWAP和更高低点。
- 先观察宽基/工业的承接，再看芯片是否摆脱NVDA拖累；不因单日大涨追逐杠杆品种。
- 12日Nebius、13日PPI、17日NVDA财报，以及随时可能公布的治理安排。

### 不要忽略

盘后流动性较低；没有完整市场广度、VWAP和当期ETF申赎。债市假日与滞后信用数据限制交叉确认；合约价格不是客观概率。

## 研究结论

11月12日早报：常规时段AI反弹得到收盘支持，但盘后NVDA治理报道冲击使修复重新脆弱；等待下一交易日承接。

## 时点与口径

| 项目 | 内容 |
| --- | --- |
| 模式 | 每日交易总结 |
| 常规交易窗口 | 2026-11-11 → 2026-11-11（纽约交易日） |
| 截止·纽约 | 2026-11-11T18:29:24.798314-05:00 |
| 截止·北京 | 2026-11-12T07:29:24.798314+08:00 |
| 实际生成时间 | 2026-11-11T23:29:25.225702+00:00 |
| 市场阶段 | 盘后 |
| 下一交易日 | 2026-11-12 |
| 运行重点 | 全市场 |
| 上一版本 | reports/daily/2026-11-10/20261111T121452.588050Z/evidence.json |
| 质量 | partial |
| Daily 北京时间计划时段 | 2026-11-12T07:15:00+08:00 |

## 采集、补查与剩余缺口

| 目标 | 补查结果 | 来源 | 观测 / 抓取时间 | 说明 |
| --- | --- | --- | --- | --- |
| 1219851 | 已校验接入 | https://gamma-api.polymarket.com/events/1219851 | 2026-11-11T23:20:15.848912+00:00 / 2026-11-11T23:20:15.848912+00:00 | Gamma observation; metadata timestamp is not trade time |
| 1360126 | 冲突，保留原值 | 缺失 |  /  | 已有合约不可静默覆盖；重新采集统一时点快照 |
| 478472 | 冲突，保留原值 | 缺失 |  /  | 已有合约不可静默覆盖；重新采集统一时点快照 |
| 1250301 | 冲突，保留原值 | 缺失 |  /  | 已有合约不可静默覆盖；重新采集统一时点快照 |

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
| prices.SPY.volume_vs_previous20_ratio | 0.76 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SPY/history/ |
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
| prices.QQQ.volume_vs_previous20_ratio | 0.83 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/QQQ/history/ |
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
| prices.RSP.volume_vs_previous20_ratio | 0.56 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/RSP/history/ |
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
| prices.GC=F.value | 3,990.60 | USD_per_troy_ounce | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_1d_pct | -0.98 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_5d_pct | -2.02 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_20d_pct | -2.86 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_60d_pct | -9.73 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_1d_pp | -2.30 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_5d_pp | -1.11 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_20d_pp | -1.58 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_60d_pp | -8.98 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma20 | 4,063.69 | USD_per_troy_ounce | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma50 | 4,204.97 | USD_per_troy_ounce | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma200 | 4,486.45 | USD_per_troy_ounce | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma20_pct | -1.80 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma50_pct | -5.10 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma200_pct | -11.05 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_sma | 89.26 | USD_per_troy_ounce | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_pct | 2.24 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.drawdown_from_63d_high_pct | -15.05 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.volume_vs_previous20_ratio | 0.01 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.CL=F.value | 86.34 | USD_per_barrel | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_1d_pct | 0.35 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_5d_pct | -2.02 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_20d_pct | -9.20 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_60d_pct | 1.65 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_1d_pp | -0.97 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_5d_pp | -1.11 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_20d_pp | -7.93 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_60d_pp | 2.40 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma20 | 96.83 | USD_per_barrel | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma50 | 95.46 | USD_per_barrel | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma200 | 87.53 | USD_per_barrel | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma20_pct | -10.83 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma50_pct | -9.56 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma200_pct | -1.36 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_sma | 4.55 | USD_per_barrel | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_pct | 5.27 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.drawdown_from_63d_high_pct | -18.42 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.volume_vs_previous20_ratio | 0.00 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.BZ=F.value | 92.51 | USD_per_barrel | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_1d_pct | 1.11 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_5d_pct | -2.23 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_20d_pct | -12.78 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_60d_pct | 1.64 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_1d_pp | -0.20 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_5d_pp | -1.32 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_20d_pp | -11.50 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_60d_pp | 2.39 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma20 | 106.33 | USD_per_barrel | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma50 | 104.25 | USD_per_barrel | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma200 | 93.73 | USD_per_barrel | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma20_pct | -12.99 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma50_pct | -11.26 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma200_pct | -1.30 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_sma | 5.43 | USD_per_barrel | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_pct | 5.87 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.drawdown_from_63d_high_pct | -21.36 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.volume_vs_previous20_ratio | 0.00 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.TLT.value | 80.92 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_1d_pct | 0.05 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_5d_pct | -1.03 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_20d_pct | 2.57 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_60d_pct | -0.13 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_1d_pp | -1.27 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_5d_pp | -0.11 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_20d_pp | 3.85 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_60d_pp | 0.62 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma20 | 81.14 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma50 | 80.18 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma200 | 83.10 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma20_pct | -0.27 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma50_pct | 0.92 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma200_pct | -2.62 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_sma | 0.71 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_pct | 0.88 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.drawdown_from_63d_high_pct | -2.29 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/TLT/history/ |
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
| prices.HYG.return_20d_pct | 0.70 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_60d_pct | -1.77 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_1d_pp | -1.10 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_5d_pp | 0.69 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_20d_pp | 1.98 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_60d_pp | -1.02 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma20 | 77.21 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma50 | 77.53 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma200 | 77.88 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma20_pct | 0.19 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma50_pct | -0.24 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma200_pct | -0.68 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_sma | 0.34 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_pct | 0.43 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.drawdown_from_63d_high_pct | -2.25 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.volume_vs_previous20_ratio | 0.26 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/HYG/history/ |
| prices.LQD.value | 103.96 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_1d_pct | 0.08 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_5d_pct | -0.52 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_20d_pct | 1.27 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_60d_pct | -0.94 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_1d_pp | -1.24 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_5d_pp | 0.40 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_20d_pp | 2.54 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_60d_pp | -0.19 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma20 | 103.94 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma50 | 103.57 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma200 | 105.74 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma20_pct | 0.02 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma50_pct | 0.37 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma200_pct | -1.68 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_sma | 0.55 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_pct | 0.53 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.drawdown_from_63d_high_pct | -1.88 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.volume_vs_previous20_ratio | 0.24 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/LQD/history/ |
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
| prices.NVDA.volume_vs_previous20_ratio | 1.82 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.MSFT.value | 521.12 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_1d_pct | -2.26 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_5d_pct | -6.24 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_20d_pct | -2.35 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_60d_pct | 8.40 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_1d_pp | -3.58 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_5d_pp | -5.33 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_20d_pp | -1.08 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_60d_pp | 9.15 | pp | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma20 | 530.47 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma50 | 518.20 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma200 | 439.80 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma20_pct | -1.76 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma50_pct | 0.56 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma200_pct | 18.49 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_sma | 17.51 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_pct | 3.36 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.drawdown_from_63d_high_pct | -6.24 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.volume_vs_previous20_ratio | 1.09 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MSFT/history/ |
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
| prices.AMZN.volume_vs_previous20_ratio | 0.74 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/AMZN/history/ |
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
| prices.GOOGL.volume_vs_previous20_ratio | 0.62 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GOOGL/history/ |
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
| prices.META.atr14_sma | 21.22 | USD_per_share | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_pct | 3.38 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.drawdown_from_63d_high_pct | -19.14 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.volume_vs_previous20_ratio | 0.63 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/META/history/ |
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
| prices.CRWV.volume_vs_previous20_ratio | 2.18 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CRWV/history/ |
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
| prices.MU.volume_vs_previous20_ratio | 1.15 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MU/history/ |
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
| prices.DRAM.volume_vs_previous20_ratio | 1.35 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/DRAM/history/ |
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
| prices.VRT.volume_vs_previous20_ratio | 0.77 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/VRT/history/ |
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
| prices.XLK.volume_vs_previous20_ratio | 1.16 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLK/history/ |
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
| prices.XLE.volume_vs_previous20_ratio | 0.65 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLE/history/ |
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
| prices.XLP.volume_vs_previous20_ratio | 0.82 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLP/history/ |
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
| prices.XLY.volume_vs_previous20_ratio | 0.69 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLY/history/ |
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
| prices.XLU.volume_vs_previous20_ratio | 0.57 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLU/history/ |
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
| prices.SMH.volume_vs_previous20_ratio | 1.22 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SMH/history/ |
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
| prices.IGV.atr14_pct | 3.07 | percent | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IGV/history/ |
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
| prices.XOP.volume_vs_previous20_ratio | 0.78 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XOP/history/ |
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
| prices.OIH.volume_vs_previous20_ratio | 0.81 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/OIH/history/ |
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
| prices.KRE.volume_vs_previous20_ratio | 0.66 | ratio | 2026-11-11 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/KRE/history/ |
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
| macro.CBOE_VIX.value | 19.46 | index | 2026-11-10 | lagged | source_series_v1:CBOE_VIX | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| macro.GPRD.value | 113.95 | index | 2026-11-02 | lagged | source_series_v1:GPRD | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_ACT.value | 129.82 | index | 2026-11-02 | lagged | source_series_v1:GPRD_ACT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_THREAT.value | 108.29 | index | 2026-11-02 | lagged | source_series_v1:GPRD_THREAT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA7.value | 158.85 | index | 2026-11-02 | lagged | source_series_v1:GPRD_MA7 | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA30.value | 184.74 | index | 2026-11-02 | lagged | source_series_v1:GPRD_MA30 | https://www.matteoiacoviello.com/gpr.htm |
| quotes.SPY.value | 756.17 | USD_per_share | 2026-11-11T23:19:55+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SPY |
| quotes.QQQ.value | 683.21 | USD_per_share | 2026-11-11T23:20:14+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| quotes.SMH.value | 492.00 | USD_per_share | 2026-11-11T23:19:42+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SMH |
| quotes.NVDA.value | 158.50 | USD_per_share | 2026-11-11T23:20:14+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| quotes.MSFT.value | 522.03 | USD_per_share | 2026-11-11T23:20:07+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/MSFT |
| quotes.AMZN.value | 268.34 | USD_per_share | 2026-11-11T23:20:14+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AMZN |
| quotes.GOOGL.value | 296.52 | USD_per_share | 2026-11-11T23:20:13+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GOOGL |
| quotes.META.value | 628.36 | USD_per_share | 2026-11-11T23:19:42+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/META |
| observed.SPY.price | 756.17 | USD | 2026-11-11T23:19:55+00:00 | ok | 独立分钟最后非空close；各自时点。不是VWAP，期货连续合约非结算；盘后低流动性不与完整日线混算收益。 | https://query1.finance.yahoo.com/v8/finance/chart/SPY |
| observed.QQQ.price | 683.21 | USD | 2026-11-11T23:20:14+00:00 | ok | 独立分钟最后非空close；各自时点。不是VWAP，期货连续合约非结算；盘后低流动性不与完整日线混算收益。 | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| observed.SMH.price | 492.00 | USD | 2026-11-11T23:19:42+00:00 | ok | 独立分钟最后非空close；各自时点。不是VWAP，期货连续合约非结算；盘后低流动性不与完整日线混算收益。 | https://query1.finance.yahoo.com/v8/finance/chart/SMH |
| observed.NVDA.price | 158.50 | USD | 2026-11-11T23:20:14+00:00 | ok | 独立分钟最后非空close；各自时点。不是VWAP，期货连续合约非结算；盘后低流动性不与完整日线混算收益。 | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| observed.MSFT.price | 522.03 | USD | 2026-11-11T23:20:07+00:00 | ok | 独立分钟最后非空close；各自时点。不是VWAP，期货连续合约非结算；盘后低流动性不与完整日线混算收益。 | https://query1.finance.yahoo.com/v8/finance/chart/MSFT |
| observed.AMZN.price | 268.34 | USD | 2026-11-11T23:20:14+00:00 | ok | 独立分钟最后非空close；各自时点。不是VWAP，期货连续合约非结算；盘后低流动性不与完整日线混算收益。 | https://query1.finance.yahoo.com/v8/finance/chart/AMZN |
| observed.GOOGL.price | 296.52 | USD | 2026-11-11T23:20:13+00:00 | ok | 独立分钟最后非空close；各自时点。不是VWAP，期货连续合约非结算；盘后低流动性不与完整日线混算收益。 | https://query1.finance.yahoo.com/v8/finance/chart/GOOGL |
| observed.META.price | 628.36 | USD | 2026-11-11T23:19:42+00:00 | ok | 独立分钟最后非空close；各自时点。不是VWAP，期货连续合约非结算；盘后低流动性不与完整日线混算收益。 | https://query1.finance.yahoo.com/v8/finance/chart/META |
| observed.CRWV.price | 56.76 | USD | 2026-11-11T23:20:12+00:00 | ok | 独立分钟最后非空close；各自时点。不是VWAP，期货连续合约非结算；盘后低流动性不与完整日线混算收益。 | https://query1.finance.yahoo.com/v8/finance/chart/CRWV |
| observed.MU.price | 787.21 | USD | 2026-11-11T23:20:17+00:00 | ok | 独立分钟最后非空close；各自时点。不是VWAP，期货连续合约非结算；盘后低流动性不与完整日线混算收益。 | https://query1.finance.yahoo.com/v8/finance/chart/MU |
| observed.DRAM.price | 43.93 | USD | 2026-11-11T23:20:09+00:00 | ok | 独立分钟最后非空close；各自时点。不是VWAP，期货连续合约非结算；盘后低流动性不与完整日线混算收益。 | https://query1.finance.yahoo.com/v8/finance/chart/DRAM |
| observed.SNDK.price | 954.90 | USD | 2026-11-11T23:20:18+00:00 | ok | 独立分钟最后非空close；各自时点。不是VWAP，期货连续合约非结算；盘后低流动性不与完整日线混算收益。 | https://query1.finance.yahoo.com/v8/finance/chart/SNDK |
| observed.RSP.price | 222.64 | USD | 2026-11-11T22:58:39+00:00 | ok | 独立分钟最后非空close；各自时点。不是VWAP，期货连续合约非结算；盘后低流动性不与完整日线混算收益。 | https://query1.finance.yahoo.com/v8/finance/chart/RSP |
| observed.GLD.price | 364.80 | USD | 2026-11-11T23:19:40+00:00 | ok | 独立分钟最后非空close；各自时点。不是VWAP，期货连续合约非结算；盘后低流动性不与完整日线混算收益。 | https://query1.finance.yahoo.com/v8/finance/chart/GLD |
| observed.CL_F.price | 86.33 | USD | 2026-11-11T23:09:00+00:00 | ok | 独立分钟最后非空close；各自时点。不是VWAP，期货连续合约非结算；盘后低流动性不与完整日线混算收益。 | https://query1.finance.yahoo.com/v8/finance/chart/CL=F |
| observed.BZ_F.price | 92.51 | USD | 2026-11-11T23:09:14+00:00 | ok | 独立分钟最后非空close；各自时点。不是VWAP，期货连续合约非结算；盘后低流动性不与完整日线混算收益。 | https://query1.finance.yahoo.com/v8/finance/chart/BZ=F |
| observed.GC_F.price | 3,990.70 | USD | 2026-11-11T23:09:00+00:00 | ok | 独立分钟最后非空close；各自时点。不是VWAP，期货连续合约非结算；盘后低流动性不与完整日线混算收益。 | https://query1.finance.yahoo.com/v8/finance/chart/GC=F |
| observed.DX-Y.NYB.price | 102.84 | index points | 2026-11-11T23:04:59+00:00 | ok | 独立分钟最后非空close；各自时点。不是VWAP，期货连续合约非结算；盘后低流动性不与完整日线混算收益。 | https://query1.finance.yahoo.com/v8/finance/chart/DX-Y.NYB |

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
        "change": 0.34855010986325397,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.5281619262694903,
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
        "change": 1.3080496146461895,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.181850868044254,
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
        "change": -0.07159527133239318,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.8117345737402086,
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
        "change": 0.3069580078124545,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.2093319702147483,
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
        "change": 2.2501296766696655,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.4116053148963461,
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
        "change": 0.07631005871709429,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.6768361937731894,
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
        "change": -0.15040771067770164,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.7681011525916053,
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
        "change": -0.04678562709263412,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.6732123238699774,
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
        "change": -0.03191829008154046,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.3055225532750141,
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
        "change": -0.2458977493091542,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.253785214078676,
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
        "change": -0.24797133505139668,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.7197818733184296,
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
        "change": -39.599853515625,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -82.39990234375,
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
        "change": 1.0662749222048906,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -4.347721043435692,
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
        "change": -4.302034160806145,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.5512603864915384,
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
        "change": 0.6659410981191494,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.22047502017405,
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
        "change": 0.18631330749122554,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.438697036712833,
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
        "change": -0.6205503862657724,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -4.014774235044982,
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
        "change": -3.9764209506845893,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.350536841587192,
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
        "change": -1.6724691643957512,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.287774137726494,
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
        "change": -1.7673542663134807,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.928587744421904,
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
        "change": -5.864990234375,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -26.26998291015616,
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
        "change": -8.115996093749345,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -48.027993164062536,
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
        "change": -5.460000000000036,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -22.860001220703452,
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
        "change": -0.8315491890331428,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.3839356370773936,
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
        "change": -0.7571077483994326,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.865751329766562,
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
        "change": -0.7734641859203037,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.3764066985265568,
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
        "change": -6.249982561383931,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 8.671456473214292,
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
        "change": -0.13309979418684215,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.25815442966803803,
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
        "change": -0.8429446796798796,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.754010510655025,
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
        "change": -1.1176879901064678,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.0368749158535249,
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
        "change": 0.29999542236328125,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.7800064086914062,
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
        "change": 1.28130940317015,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 8.642970777564084,
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
        "change": 8.438960399866025,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 12.243491719604748,
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
        "change": -0.5976042312046186,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -9.020572154253149,
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
        "change": -0.17427124907118952,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -4.265253683031034,
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
        "change": -0.40551590530051307,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 8.975917585954797,
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
        "change": 8.76457360998758,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 12.444215264509094,
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
        "change": -2.9360144937195187,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -9.087871271805593,
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
        "change": -2.127938822875897,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -3.755144390740106,
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
        "change": -0.4375,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.2864997863769503,
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
        "change": -0.07760009765625853,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.30879974365234375,
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
        "change": 0.1197499847412189,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.6825499725341899,
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
        "change": 0.7095259227788198,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.645008435244554,
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
        "change": 0.3874549998782335,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.1641511169864014,
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
        "change": 0.20806632009807702,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.8246874689266233,
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
        "change": -0.18071419852120574,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.7078574044363837,
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
        "change": -0.2284066301951535,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.6968545149680292,
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
        "change": 0.2834691648613834,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.6819487649003193,
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
        "change": -1.160920758034087,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.3685418914649594,
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
        "change": 1.0200042724609375,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.1100006103515625,
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
        "change": 2.2815672915519447,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 9.782830310247327,
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
        "change": 9.459216848505957,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 15.720076328308895,
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
        "change": 0.6597397231917537,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -7.206926609926456,
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
        "change": 0.9547209598783413,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -4.7852144753726344,
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
        "change": 0.5947419830812817,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 10.115777118638038,
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
        "change": 9.784830058627513,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 15.920799873213241,
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
        "change": -1.6786705393231465,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -7.2742257274789,
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
        "change": -0.9989466139263659,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -4.275105183081706,
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
        "change": -0.6774997711181641,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.7110000610351648,
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
        "change": -0.042799987792975,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.4238002014160145,
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
        "change": 0.12470001220702898,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.7242000579833956,
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
        "change": 1.504118519240249,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.2281060068259002,
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
        "change": 1.014470916583532,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.394548509072191,
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
        "change": 0.958195293166797,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -3.0371738345154164,
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
        "change": -0.2607138497488837,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.05000032697405121,
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
        "change": -0.3503865336805898,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.0780135638107442,
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
        "change": 0.8670556594296386,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.7936081445927208,
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
        "change": -1.2569191491547982,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.6585009519775809,
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
        "change": -0.6295473682979891,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -3.4021716567412597,
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
        "change": -0.3310326611743908,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.016130462838370718,
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
        "change": -2.96795763081289,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -3.469470774293704,
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
        "change": -2.284700234979098,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.5262397551292985,
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
        "change": 0.10149993896483522,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.8224990844726534,
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
        "change": -0.01243194580078466,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.226011505126948,
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
        "change": -0.019603385925293537,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.37822261810303814,
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
        "change": -0.07555276122134247,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.067194722734611,
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
        "change": 0.06552844389533519,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.7610300605170872,
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
        "change": 0.07109455277172216,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.5650670652612488,
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
        "change": -0.08514295305524555,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.0587158203125,
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
        "change": -0.10570457182324033,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.06280212383993411,
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
        "change": 0.048299886375968715,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.6182675680001748,
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
        "change": -0.3684477475789216,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.44324424391994643,
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
        "change": 0.09056186143106393,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.11702378932543023,
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
        "change": 0.5862828618708793,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.2625107857435305,
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
        "change": 0.314377998081794,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.1955190159135256,
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
        "change": -1.7521274006440213,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.19521166819108648,
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
        "change": -1.6392895757229131,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.7056283082044534,
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
        "change": 0.027000045776361503,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.04950027465820028,
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
        "change": -0.02799255371093068,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.34156051635741846,
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
        "change": -0.0014871978759742888,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.3117811584472605,
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
        "change": 0.18521588089421837,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.28460436628261476,
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
        "change": 0.2551849484563218,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.21926883083420723,
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
        "change": 0.2201791374472406,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.17862541543438581,
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
        "change": -0.009999956403459798,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.011428288051060276,
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
        "change": -0.013914680647583832,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.015696185166125365,
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
        "change": 0.2148277213182559,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.21909409075753228,
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
        "change": -0.6455044365909333,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.0388455216005585,
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
        "change": -0.03061114454514513,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.0843266700324872,
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
        "change": -0.05486799181413371,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.05357982261975369,
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
        "change": -2.369021407060046,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.1516257875849312,
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
        "change": -2.008535565618841,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.5636891149106815,
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
        "change": 0.0649997711181669,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.45149917602539347,
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
        "change": -0.01615875244141307,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.33543716430664006,
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
        "change": -0.015059738159180824,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.4660053634643617,
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
        "change": 0.014431534012437908,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.9581278579806174,
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
        "change": 0.09288673855991636,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.19566345219292902,
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
        "change": 0.08964797367269073,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.07706050403180065,
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
        "change": -0.06284986223493305,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.06285040719168533,
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
        "change": -0.06090928881189406,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.05741359503989818,
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
        "change": 0.07551176040805352,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.08591260239980691,
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
        "change": -0.5663341030661955,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.0639876714769925,
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
        "change": -1.2856906628906282,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.3407402887780011,
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
        "change": -12.03497314453125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -34.67498779296875,
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
        "change": -0.05251118162667989,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -8.938801056265488,
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
        "change": -8.57468700211279,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -10.907210652323784,
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
        "change": -0.4608978612356318,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -7.269792631949912,
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
        "change": -2.799040668311136,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -2.12307913344436,
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
        "change": -1.739336490097343,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -8.605854247874777,
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
        "change": -8.249073791991234,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -10.706487107419438,
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
        "change": -2.7993081237505324,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -7.337091749502356,
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
        "change": -4.752708242115842,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.612969841153431,
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
        "change": -0.6282501220703125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.49825439453127274,
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
        "change": 0.40210021972654886,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.8546984863280613,
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
        "change": 0.21787307739259631,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.842602691650427,
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
        "change": -2.149859628638706,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -6.438379079107682,
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
        "change": -2.4023630102535165,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -7.285587533789273,
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
        "change": -2.796523245683666,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -8.415874711092595,
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
        "change": 0.11616544698711007,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.6563261648904417,
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
        "change": -2.165342462910269,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -6.238752888545385,
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
        "change": 0.05757728748592328,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.1753596821397323,
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
        "change": -0.04306164911971744,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.4337342832200102,
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
        "change": -0.20225219726563637,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.0755882263183594,
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
        "change": 1.8433869891552046,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.605158144690467,
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
        "change": -0.0874789836661205,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.8480330385503264,
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
        "change": -2.6714390345982153,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.1421552385602673,
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
        "change": -0.35009092824014987,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.17470428106389102,
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
        "change": 0.1098817238168549,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.751091574829573,
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
        "change": 0.948544712014946,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.2084601802329553,
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
        "change": 2.0067991638183003,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 8.158659973144495,
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
        "change": 11.061381738879462,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.9794252720589869,
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
        "change": 0.23832679150786362,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.1782192506369633,
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
        "change": 0.4516101142031783,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.10185481736113577,
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
        "change": 0.08715446472166377,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.22951263427734148,
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
        "change": 4.505838394432914,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.28963927548828394,
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
        "change": -0.1064278738839306,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 2.5332151140485486,
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
        "change": -0.638809326855716,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.1893045885064488,
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
        "change": 0.00787431267394012,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.9872791227452649,
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
        "change": 0.13421062469481626,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.5798808288574264,
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
        "change": 3.122100016574958,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.6107739440841984,
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
        "change": 0.33249669676352245,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.1280903375473681,
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
        "change": -0.24397330358367442,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.4769858181010345,
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
        "change": 0.031351966857904756,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.13021633148193246,
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
        "change": 0.5706222201542257,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.3322232846383795,
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
        "change": -0.11496832076221053,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.8382491233475736,
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
        "change": 0.15426923185690367,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.8045183958574296,
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
        "change": 0.17701835632323082,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.789678802490215,
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
        "change": -0.08846677080374121,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.042557376475628,
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
        "change": -0.06321498325892838,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.5274974278041293,
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
        "change": -0.034199777015865074,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.2855172815235423,
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
        "change": -0.058521970004611124,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.9858093416769235,
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
        "change": 0.04930885314941236,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.2447850036621162,
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
        "change": 0.4364776369065293,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.9036581027556565,
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
        "change": -0.12000002179827018,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.10000010899135026,
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
        "change": -0.14037272218264052,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.11864084241548434,
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
        "change": 0.21482887925584504,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.636360236912666,
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
        "change": -0.004709854125977131,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.05053901672363281,
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
        "change": -0.04783375024783876,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.1176599997378078,
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
        "change": -0.031071799142019962,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.3967851911272322,
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
        "change": -0.02460347077159808,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.34789265154520965,
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
        "change": -0.1100450756734691,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.7195096988014946,
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
        "change": -0.03621978759765909,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.2219894027710012,
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
        "change": 0.7814619309353898,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 3.4369848904001965,
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
        "change": -0.07335008893694184,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.23307909284319206,
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
        "change": -0.08392992510883923,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.15149579179692196,
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
        "change": -0.043000445176960334,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.8990730310889476,
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
        "change": 0.006389846801752697,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.03783794403076257,
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
        "change": 0.190678129667321,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.39295429051341424,
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
        "change": -0.04035731724330349,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.0010716574532644296,
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
        "change": -0.09513401139683819,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.00911749443351173,
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
        "change": -0.003439568172176166,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.9866775234755807,
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
        "change": 0.021551990509031782,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.10277839660644617,
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
        "change": -0.028881627485177752,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.4870725754012382,
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
        "change": -0.2377331084226597,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.6063881775464226,
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
        "change": 0.018368682861328978,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.08751981735229464,
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
        "change": 0.2965418001472875,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.911545933793879,
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
        "change": -0.14392501564758092,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.4872291084108444,
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
        "change": 0.3694512953795064,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.1455324559112514,
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
        "change": 0.06642804827008897,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.012857709612165369,
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
        "change": 0.007976707193513732,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.027075697531111498,
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
        "change": -0.19860485288924246,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.946562893436037,
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
        "change": -0.8028765795472668,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.6470352553583865,
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
        "change": -0.972856794084823,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.8907121930803559,
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
        "change": -0.37986025435686344,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.20681568468835554,
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
        "change": 0.05251372079838268,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.5144308789047658,
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
        "change": -0.027843132019029326,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -152.32850585937499,
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
        "change": 1.2079533174693453,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 3.2592281234707587,
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
        "change": -0.0969080968286376,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.8607310473773528,
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
        "change": -0.03035722460065582,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.1907142911638532,
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
        "change": -0.14800647345938067,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.49249797443270626,
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
        "change": -2.9829540875855964,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.0272645486724028,
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
        "change": 0.029304103851316654,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.1304360771179205,
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
        "change": -0.24136135505881118,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -1.86626757465298,
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
        "change": -0.11535699026925217,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.0903581891741072,
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
        "change": -0.15375231716782078,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 0.15576773922840914,
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
        "change": -0.041740038574978766,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": -0.5050098165828205,
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
        "change": 2.5927378571794994,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-04",
        "to": "2026-11-11",
        "change": 1.3760418499913425,
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
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.46000000000000085,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.3699999999999974,
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

## 判断依据 · 反弹是否可靠

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 反弹是否可靠 |
| 事实指标引用 | ["prices.SPY.volume_vs_previous20_ratio", "prices.QQQ.sma200", "observed.QQQ.price"] |
| 推断与解释 | 收盘修复成立，盘后新冲击将持续性降为待验证；量能与中期均线仍不充分。 |
| 反证与缺口 | 收盘上涨量不足，盘后仍可能跳空；一次盘中突破不能证明趋势反转 |
| 确认条件 | SPY755附近、QQQ680–682首轮回踩守住，随后站回当日常规VWAP并出现更高低点；收盘再看SPY760.20/764.55、QQQ698.94；均权参与同步 |
| 失效条件 | 跌破755/680并反抽失败则撤销升级；未取得VWAP前不声称满足该条件 |
| 观察期限 | 未来1–3交易日 |
| 条件式指导 | 先等常规时段回踩和收盘保持；条件失效撤销方向升级，不凭反弹幅度追高。 |
| 主观置信等级 | medium |
| 判断变化原因 | 新增完整11日收盘与盘后治理冲击，替代昨晚仅盘前的判断。 |

## 判断依据 · AI事件是否意味着泡沫已经破裂

| 要素 | 记录 |
| --- | --- |
| 评估问题 | AI事件是否意味着泡沫已经破裂 |
| 事实指标引用 | ["observed.NVDA.price", "prices.SMH.sma200", "prices.CRWV.return_1d_pct"] |
| 推断与解释 | 个股治理风险、合同阈值和行业现金流不能混为一谈。 |
| 反证与缺口 | 盘后NVDA已跌破原支撑，SMH仍低于523附近中期均线；CRWV利润与利息不匹配 |
| 确认条件 | SMH490–493守住并逐步收复506.96，NVDA重新建立更高低点且恢复170.24才重评原修复剧本；CRWV守住财报前高51.02，融资兑现进一步确认 |
| 失效条件 | SMH失490反抽失败、NVDA持续创新低或官方事件进一步影响经营；不等待所有条件同时触发 |
| 观察期限 | 未来1–3交易日 |
| 条件式指导 | 先等常规时段回踩和收盘保持；条件失效撤销方向升级，不凭反弹幅度追高。 |
| 主观置信等级 | medium |
| 判断变化原因 | 新增完整11日收盘与盘后治理冲击，替代昨晚仅盘前的判断。 |

## 判断依据 · 轮动是否可以写成主力流入

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 轮动是否可以写成主力流入 |
| 事实指标引用 | ["prices.XLI.sma20", "prices.RSP.return_1d_pct", "prices.SMH.relative_spy_20d_pp"] |
| 推断与解释 | 观察池参与扩散，但均权未领先；只有价格量能而非当前申赎证据。 |
| 反证与缺口 | 上涨不证明净申购；防御篮子在强风险偏好阶段可能落后 |
| 确认条件 | XLI守167.70并突破172.74再回踩；XLF/XLV/XLP保持各自20日线和多日相对SPY强度，且指数不创新低 |
| 失效条件 | 跌破各自20日线且相对强度持续转弱；新信用数据恶化时不把金融视作防御 |
| 观察期限 | 未来1–3交易日 |
| 条件式指导 | 先等常规时段回踩和收盘保持；条件失效撤销方向升级，不凭反弹幅度追高。 |
| 主观置信等级 | medium |
| 判断变化原因 | 新增完整11日收盘与盘后治理冲击，替代昨晚仅盘前的判断。 |

## 判断依据 · 恐慌是否转成过热

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 恐慌是否转成过热 |
| 事实指标引用 | ["prices.^VIX.value", "prices.^VIX3M.value", "macro.BAMLH0A0HYM2.value"] |
| 推断与解释 | CNN37与VIX回落支持恐惧缓解；盘后事件和假日信用缺口阻止全面风险解除判断。 |
| 反证与缺口 | 收盘上涨量不足，盘后仍可能跳空；一次盘中突破不能证明趋势反转 |
| 确认条件 | SPY755附近、QQQ680–682首轮回踩守住，随后站回当日常规VWAP并出现更高低点；收盘再看SPY760.20/764.55、QQQ698.94；均权参与同步 |
| 失效条件 | 跌破755/680并反抽失败则撤销升级；未取得VWAP前不声称满足该条件 |
| 观察期限 | 未来1–3交易日 |
| 条件式指导 | 先等常规时段回踩和收盘保持；条件失效撤销方向升级，不凭反弹幅度追高。 |
| 主观置信等级 | medium |
| 判断变化原因 | 新增完整11日收盘与盘后治理冲击，替代昨晚仅盘前的判断。 |

## 芯片需求修复遇到新的治理冲击 · 新增

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | CRWV财报后反弹；盘后Reuters转述董事会准备撤换NVDA CEO报道 |
| 事实：市场反应 | 收盘SMH+4.82%，盘后492较收盘−2.95%；NVDA盘后约−8.77% |
| 推断：解释 | 推断：需求改善并不能抵消领导连续性和合规风险溢价；未确认所有跌幅因果 |
| 受益篮子 | ["具备订单与融资支持、回踩守住的算力企业（条件式）"] |
| 受损篮子 | ["NVDA及高杠杆半导体篮子"] |
| 反证 | 最终人事决定尚无官方核验；治理稳定也可能促成修复 |
| 下一催化剂 | 官方治理公告、12日NBIS、17日NVDA业绩 |
| 证据 | ["https://sg.finance.yahoo.com/news/nvidia-preparing-oust-ceo-jensen-223546395.html", "https://investor.nvidia.com/news/press-release-details/2026/Statement-from-NVIDIA-Board-of-Directors/default.aspx", "https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Third-Quarter-2026-Results/default.aspx"] |

## 非芯片参与扩散但量能不足 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 板块观察池17/19上涨 |
| 事实：市场反应 | RSP+0.80%、XLI+1.33%，宽基量仍偏低 |
| 推断：解释 | 推断：参与改善有助修复，但风险偏好未全面确认 |
| 受益篮子 | ["XLI", "XLF", "XLV", "XLP"] |
| 受损篮子 | ["失去支撑的高估值篮子"] |
| 反证 | 均权当日弱于市值指数，工业仍低于200日线 |
| 下一催化剂 | 下一交易日回踩与13日PPI |
| 证据 | ["https://finance.yahoo.com/quote/RSP/", "https://www.bls.gov/schedule/2026/11_sched.htm"] |

## 能源供给风险与美元走强 · 待核验

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 油轮事故报道与俄乌谈判并存，未确认全面停火 |
| 事实：市场反应 | XLE+1.87%、XOP+2.63%；黄金下跌而美元走强 |
| 推断：解释 | 推断：油价的供给和需求影响需要分开，不能仅看外交标题 |
| 受益篮子 | ["有供应约束确认的油气篮子"] |
| 受损篮子 | ["能源密集行业（条件式）"] |
| 反证 | 原油仍低于20日线，冲突报道不等于价格上涨会持续 |
| 下一催化剂 | 航运独立核验、俄乌正式协议及PPI |
| 证据 | ["https://apnews.com/article/50075bc97e07d41fa3b66fc28858c06b", "https://apnews.com/article/7c8d1024302e0c6ad8be064eec852a64", "https://www.bls.gov/schedule/2026/11_sched.htm"] |

## tc 报价（供应商时戳不等于成交时戳）

| 标的 | 价格 USD | 变化% | 观测时间 | 供应商时间 | 抓取时间 | 质量 |
| --- | --- | --- | --- | --- | --- | --- |
| SPY | 756.17 | 缺失 | 2026-11-11T23:19:55+00:00 | 2026-11-11T23:19:55+00:00 | 2026-11-11T23:20:24.506219+00:00 | ok |
| QQQ | 683.21 | 缺失 | 2026-11-11T23:20:14+00:00 | 2026-11-11T23:20:14+00:00 | 2026-11-11T23:20:24.506219+00:00 | ok |
| SMH | 492.00 | 缺失 | 2026-11-11T23:19:42+00:00 | 2026-11-11T23:19:42+00:00 | 2026-11-11T23:20:24.506219+00:00 | ok |
| NVDA | 158.50 | 缺失 | 2026-11-11T23:20:14+00:00 | 2026-11-11T23:20:14+00:00 | 2026-11-11T23:20:24.506219+00:00 | ok |
| MSFT | 522.03 | 缺失 | 2026-11-11T23:20:07+00:00 | 2026-11-11T23:20:07+00:00 | 2026-11-11T23:20:24.506219+00:00 | ok |
| AMZN | 268.34 | 缺失 | 2026-11-11T23:20:14+00:00 | 2026-11-11T23:20:14+00:00 | 2026-11-11T23:20:24.506219+00:00 | ok |
| GOOGL | 296.52 | 缺失 | 2026-11-11T23:20:13+00:00 | 2026-11-11T23:20:13+00:00 | 2026-11-11T23:20:24.506219+00:00 | ok |
| META | 628.36 | 缺失 | 2026-11-11T23:19:42+00:00 | 2026-11-11T23:19:42+00:00 | 2026-11-11T23:20:24.506219+00:00 | ok |

## 核心行情与风险代理

| 标的 | 价格/指数 | 单位 | 观测日 | 1日% | 5日% | 20日% | 质量 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 759.81 | USD_per_share | 2026-11-11 | 1.32 | -0.91 | -1.27 | ok |
| QQQ | 690.38 | USD_per_share | 2026-11-11 | 2.31 | -0.23 | -5.29 | ok |
| IWM | 283.09 | USD_per_share | 2026-11-11 | 0.89 | -0.33 | 4.32 | ok |
| RSP | 222.65 | USD_per_share | 2026-11-11 | 0.80 | -0.30 | 4.98 | ok |
| GLD | 365.17 | USD_per_share | 2026-11-11 | -1.13 | -1.97 | -2.88 | ok |
| GC=F | 3,990.60 | USD_per_troy_ounce | 2026-11-11 | -0.98 | -2.02 | -2.86 | ok |
| CL=F | 86.34 | USD_per_barrel | 2026-11-11 | 0.35 | -2.02 | -9.20 | ok |
| BZ=F | 92.51 | USD_per_barrel | 2026-11-11 | 1.11 | -2.23 | -12.78 | ok |
| TLT | 80.92 | USD_per_share | 2026-11-11 | 0.05 | -1.03 | 2.57 | ok |
| UUP | 29.35 | USD_per_share | 2026-11-11 | 0.69 | 1.56 | 0.79 | ok |
| HYG | 77.35 | USD_per_share | 2026-11-11 | 0.22 | -0.22 | 0.70 | ok |
| LQD | 103.96 | USD_per_share | 2026-11-11 | 0.08 | -0.52 | 1.27 | ok |
| ^VIX | 17.49 | index | 2026-11-11 | -10.12 | 5.30 | 3.68 | ok |
| ^VIX3M | 19.24 | index | 2026-11-11 | -6.78 | 2.34 | 2.39 | ok |
| ^VVIX | 90.47 | index | 2026-11-11 | -6.37 | 0.07 | -4.21 | ok |
| ^MOVE | 92.43 | index | 2026-11-10 | 7.50 | -7.54 | -8.57 | stale |
| NVDA | 173.73 | USD_per_share | 2026-11-11 | 2.87 | -13.19 | -21.50 | ok |
| MSFT | 521.12 | USD_per_share | 2026-11-11 | -2.26 | -6.24 | -2.35 | ok |
| AMZN | 266.17 | USD_per_share | 2026-11-11 | -1.74 | 0.05 | 4.76 | ok |
| GOOGL | 293.45 | USD_per_share | 2026-11-11 | 2.11 | 1.56 | -15.59 | ok |
| META | 628.77 | USD_per_share | 2026-11-11 | -1.97 | -0.20 | -14.75 | ok |
| CRWV | 60.77 | USD_per_share | 2026-11-11 | 24.71 | 25.51 | -7.62 | ok |
| MU | 811.30 | USD_per_share | 2026-11-11 | 11.89 | 2.02 | -11.25 | ok |
| DRAM | 44.85 | USD_per_share | 2026-11-11 | 10.36 | -0.58 | -10.55 | ok |
| VRT | 206.51 | USD_per_share | 2026-11-11 | 6.33 | 0.47 | -7.32 | ok |

## 跨资产风险解释

收盘显示恐惧缓解，而非市场全面过热：CNN官方页面37/Fear，11日18:03:19EST更新，前收33；相对昨晚核验的盘前34上升3点，两者不是相同结算时点。VIX收盘17.49、VIX3M19.24，同日比值约0.909，VVIX90.47；这只说明收盘隐含波动率下降，不是盘后治理冲击后的新报价。MOVE92.43仍为10日，不能当11日新变化。SIFMA11日美元债市假日，Yahoo TNX标11日4.998%也不足证明可交易现金债收益率。FRED2年4.56%、10年4.88%、实际10年2.66%、HY334bp与IG91bp仍至9日；盈亏平衡2.20%至10日、金融压力−0.5224至10月30日。23:09UTC WTI86.33、Brent92.51、黄金期货3990.70，美元指数102.843（23:04:59），均保留独立时点；连续期货不是官方结算。黄金和美元可以受贴现率共同影响，不能把黄金下跌直接解释为战争结束。GPR采集仍至2日，官网标9日更新，补查与缺口另列；不制造统一避险/战争影响指数。俄乌换囚与能源谈判不是全面停火；油轮事件部分责任和伤损仍未独立核验。

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
| CBOE_VIX | 19.46 | index | 2026-11-10 | 4.19 | lagged | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| GPRD | 113.95 | index | 2026-11-02 | -245.09 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_ACT | 129.82 | index | 2026-11-02 | -342.91 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_THREAT | 108.29 | index | 2026-11-02 | -240.96 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_MA7 | 158.85 | index | 2026-11-02 | -44.27 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_MA30 | 184.74 | index | 2026-11-02 | 13.98 | lagged | https://www.matteoiacoviello.com/gpr.htm |

## CNN Fear & Greed

```json
{
  "value": 37,
  "rating": "Fear",
  "observed_at": "2026-11-11T18:03:19-05:00",
  "retrieved_at": "2026-11-11T23:27:41.488448+00:00",
  "source": "https://edition.cnn.com/markets/fear-and-greed",
  "quality": "verified_browser",
  "previous_close": 33,
  "one_week_ago": 34,
  "note": "本轮Chrome页面直接读取；API418；与各组成项时间不同，不能视为盘后事件重新定价完成。retrieved_at为本次将已观察页面数值整理入输入的时刻。"
}
```

## 19 板块与主题 ETF：价格量能证据

| 标的 | 板块 | 1日% | 5日% | 20日% | 相对SPY 1日pp | 相对SPY 5日pp | 相对SPY 20日pp | 成交量/前20日 | 观测日 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLK | 科技 | 3.23 | -1.21 | -8.44 | 1.91 | -0.30 | -7.17 | 1.16 | 2026-11-11 |
| XLE | 能源 | 1.86 | -0.24 | -6.30 | 0.55 | 0.68 | -5.03 | 0.65 | 2026-11-11 |
| XLF | 金融 | 0.58 | -0.96 | 7.54 | -0.74 | -0.05 | 8.81 | 0.71 | 2026-11-11 |
| XLI | 工业 | 1.33 | 0.89 | 2.35 | 0.01 | 1.80 | 3.62 | 0.74 | 2026-11-11 |
| XLV | 医疗 | 0.04 | -0.37 | 8.62 | -1.28 | 0.54 | 9.89 | 0.71 | 2026-11-11 |
| XLP | 必需消费 | 0.46 | -0.53 | 6.26 | -0.86 | 0.38 | 7.54 | 0.82 | 2026-11-11 |
| XLY | 可选消费 | -0.05 | -1.10 | 8.51 | -1.37 | -0.18 | 9.78 | 0.69 | 2026-11-11 |
| XLC | 通信 | 0.78 | 3.47 | -2.00 | -0.54 | 4.38 | -0.73 | 0.69 | 2026-11-11 |
| XLU | 公用事业 | 0.21 | 0.48 | 5.03 | -1.11 | 1.39 | 6.31 | 0.57 | 2026-11-11 |
| XLRE | 房地产 | 0.02 | -1.17 | 7.47 | -1.30 | -0.26 | 8.74 | 0.51 | 2026-11-11 |
| XLB | 材料 | 0.32 | -1.63 | 6.74 | -1.00 | -0.72 | 8.02 | 0.49 | 2026-11-11 |
| SMH | 半导体 | 4.82 | 0.53 | -10.23 | 3.51 | 1.45 | -8.96 | 1.22 | 2026-11-11 |
| IGV | 软件 | 1.89 | -1.28 | -5.03 | 0.57 | -0.37 | -3.76 | 0.52 | 2026-11-11 |
| XOP | 油气开采 | 2.63 | 0.47 | -8.95 | 1.31 | 1.39 | -7.67 | 0.78 | 2026-11-11 |
| OIH | 油服 | 2.84 | 0.95 | -3.35 | 1.52 | 1.86 | -2.08 | 0.81 | 2026-11-11 |
| ITA | 航空与国防 | 1.23 | 3.23 | 7.58 | -0.09 | 4.15 | 8.85 | 0.46 | 2026-11-11 |
| ARKX | 航天主题 | 1.37 | 4.91 | -0.61 | 0.05 | 5.82 | 0.67 | 0.36 | 2026-11-11 |
| KRE | 区域银行 | -0.19 | -1.59 | 6.43 | -1.51 | -0.68 | 7.71 | 0.66 | 2026-11-11 |
| SKYY | 云计算 | 2.90 | -1.53 | -5.93 | 1.58 | -0.61 | -4.65 | 3.41 | 2026-11-11 |

## 资金证据分层

19个板块/主题ETF中17个上涨，仅为观察池参与度，不能冒充全市场广度。SMH+4.82%、XLK+3.23%、SKYY+2.90%、OIH+2.84%、XOP+2.63%，修复扩散；RSP+0.80%弱于SPY+1.32%，并非均权领先。SMH5日相对SPY+1.45个百分点、20日仍−8.96个百分点，且低于20日523.65与200日523.11；一日强势未修复中期结构。XLI收盘170.97在20日167.70之上、200日172.74之下，可作为非芯片承接观察；XLF/XLV/XLP20日相对强度仍好，但当天落后于高弹性修复。SPY/QQQ相对前20日量0.76/0.83倍、SMH1.22倍、NVDA1.82倍、CRWV2.18倍；只有活跃度证据，不能识别主力净流入。ITA/ARKX量仅0.46/0.36倍，不把航天上涨夸大成强资金信号。VanEck页面仍为10日NAV483.84、资产63.48B，缺连续精确份额；未推算净申赎。ICI最新仍是10日发布、截至4日一周总净发行498.30亿美元，国内股308.68亿、债138.89亿、商品1.29亿，早于5日大跌，只作历史窗口。当前单ETF申赎和滞后机构身份证据缺失。

## 最近可核验 ETF 申赎窗口

| 标的 | 金额 USD million | 起始日 | 结束日 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- |
| US_DOMESTIC_EQUITY_ETFS | 30868 | 2026-10-29 | 2026-11-04 | public_report | https://www.ici.org/research/stats/etf_flows |
| US_BOND_ETFS | 13889 | 2026-10-29 | 2026-11-04 | public_report | https://www.ici.org/research/stats/etf_flows |
| US_COMMODITY_ETFS | 129 | 2026-10-29 | 2026-11-04 | public_report | https://www.ici.org/research/stats/etf_flows |

## Polymarket 搜索覆盖与限制

23:20UTC附近按原清单及15组主动Gamma搜索重新检查：AI泡沫、NVIDIA CEO/CoreWeave/AMD、Fed/衰退/银行、政府关税、油价/Hormuz/Iran/Ukraine、航天和州数据中心禁令。每组limit10首批，AI/航天/Hormuz等截断，AMD空结果不等于没有相关事件。新CEO人选事件作为未纳入精选的发现线索；补取CRWV评级、能源局部协议、全面停火、WTI阈值。未来一周已核验NBIS/PPI/NVDA官方日程，但未找到同时满足规则和准确官方事件时点的精选预测合约，upcoming为空；其余临近截止放参考栏，不假造事件时间。

## Polymarket · 值得警惕的信号

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["AI bubble burst in 2026?", "期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。", "https://polymarket.com/event/ai-bubble-burst-by"] | [10.75, {"status": "comparable", "change_pp": 1.9000000000000004}] | {"spread": 0.0010000000000000009, "volume24h_usd": 75671.229263, "liquidity_usd": 64126.30295, "quality_flags": [], "retrieved_at": "2026-11-11T23:20:36.769397+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["多条件AI合约与实际融资分开", "AI估值/融资"] | ["多个实际阈值与信用持续恶化共同出现", "需求、回款与融资恢复且阈值未满足"] | [null, null] |
| ["CoreWeave downgraded by Moody's or S&P by December 31, 2026?", "2026年12月31日23:59ET前，Moody’s或S&P正式下调CoreWeave长期主体/企业家族或高级无担保债信用评级则Yes；仅负面展望/观察名单不算，不要求降至某统一评级档。成交很薄，不视为客观违约概率。", "https://polymarket.com/event/coreweave-downgraded-by-moodys-or-sp-by"] | [19.0, {"status": "comparable", "change_pp": -12.0}] | {"spread": 0.14, "volume24h_usd": 391.366483, "liquidity_usd": 325.6489, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"], "retrieved_at": "2026-11-11T23:20:15.848912+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["新发现评级下调合约，24h成交很薄", "算力融资成本"] | ["正式评级行动及实际融资成本共同转坏", "仅展望变化或评级不变；薄盘口不足确认"] | [null, null] |
| ["Jensen Huang announced resignation or removal by December 31, 2026?", "年末23:59美东前，黄仁勋/NVIDIA或授权代表正式明确宣布辞任或被撤去CEO，且预定在宣布后18个月内实施则Yes；不要求年内实际离任。临时休假、停职、条件式考虑、未被接受辞呈和媒体单独传闻不算。以官方信息优先；不得把调查直接视为离任。 合格辞任/撤职实际发生亦可能触发，需按专门规则核验；本次与早报hash相同。", "https://polymarket.com/event/jensen-huang-announced-resignation-or-removal-by-december-31"] | [76.5, {"status": "comparable", "change_pp": 60.0}] | {"spread": 0.010000000000000009, "volume24h_usd": 1827058.6870299994, "liquidity_usd": 139936.6396, "quality_flags": [], "retrieved_at": "2026-11-11T23:20:36.769397+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["媒体准备撤换报道后合约定价跃升，但官方人事决定未核验", "NVDA及芯片风险溢价"] | ["官方明确离任或约束升级", "公司维持治理安排且无新不利事实"] | [null, null] |

## Polymarket · 有参考价值的事件

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Strait of Hormuz traffic returns to normal by December 31?", "期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。", "https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31"] | [8.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.009999999999999995, "volume24h_usd": 63477.000355, "liquidity_usd": 208107.2002, "quality_flags": [], "retrieved_at": "2026-11-11T23:20:36.769397+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["实际通行量与外交表态分开", "油运/能源"] | ["Portwatch量持续改善并满足规则", "航运事件持续且量未恢复"] | [null, null] |
| ["Russia x Ukraine energy ceasefire agreement by November 15, 2026?", "11月15日23:59基辅时间前，俄乌双方同意暂停打击至少一类明确能源设施，双方官宣或可信报道共识确认；美国第三方单方声称不足。可限定地理范围，但仅一个设施不算；必须明确相互暂停，不是谈判/换囚。约定生效日可晚于截止。", "https://polymarket.com/event/russia-x-ukraine-energy-ceasefire-agreement-by"] | [3.85, {"status": "comparable", "change_pp": -0.6499999999999999}] | {"spread": 0.0010000000000000009, "volume24h_usd": 84129.368655, "liquidity_usd": 108213.84958, "quality_flags": [], "retrieved_at": "2026-11-11T23:20:36.769397+00:00", "contract_end_at": "2026-11-15T21:59:00+00:00"} | ["新能源协议合约；15日是截止非会议日", "能源供给/风险溢价"] | ["双方确认合格能源设施互停安排", "仅换囚或第三方声称"] | [null, null] |
| ["Russia x Ukraine ceasefire agreement by December 31, 2026?", "2026年末23:59ET前，双方官宣或可信共识确认相互暂停直接交战，包含明确生效日的全面暂停；仅限定目标/地点的局部能源安排不算。达成协议可先于实际生效，单方暂停不算。", "https://polymarket.com/event/russia-x-ukraine-ceasefire-agreement-by"] | [9.5, {"status": "comparable", "change_pp": -4.000000000000001}] | {"spread": 0.010000000000000009, "volume24h_usd": 74071.58728700002, "liquidity_usd": 78872.196, "quality_flags": [], "retrieved_at": "2026-11-11T23:20:36.769397+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["全年全面停火协议与能源局部暂停定义不同", "军工/欧洲风险偏好"] | ["双边明确全面暂停及生效日", "仅局部或单方暂停"] | [null, null] |
| ["Will WTI Crude Oil (WTI) hit (HIGH) $110 in November?", "11月合资格交易时段，Pyth对ICE Europe WTI活跃月CLL的任一最终1分钟High达到110美元即Yes；按原值不取整，最后三个交易日换月。主数据不可用时依ICE官方日高低。与Yahoo NYMEX连续WTI代理不是同一可直接裁决序列。", "https://polymarket.com/event/what-price-will-wti-hit-in-november-2026"] | [5.5, {"status": "comparable", "change_pp": -1.0000000000000002}] | {"spread": 0.009999999999999995, "volume24h_usd": 3790.6829000000002, "liquidity_usd": 27746.7623, "quality_flags": [], "retrieved_at": "2026-11-11T23:20:36.769397+00:00", "contract_end_at": "2026-12-01T04:59:59.999000+00:00"} | ["月内WTI高点合约；不直接用Yahoo裁决", "通胀与油气"] | ["指定Pyth/ICE价格和实际供应压力同向", "供应改善且指定价格未触发"] | [null, null] |
| ["Will the Fed increase interest rates by 50+ bps after the December 2026 meeting?", "衡量12月8–9日该次FOMC前后联邦基金目标区间上限上调至少50bp；非标准变化向上取整到最近25bp对应档。按正式声明，若下一次会议结束仍无声明则按不变档处理。不是全年累计加息幅度。", "https://polymarket.com/event/fed-decision-in-december-20260729232808632"] | [10.549999999999999, {"status": "comparable", "change_pp": 0.5999999999999992}] | {"spread": 0.0010000000000000009, "volume24h_usd": 659311.034143, "liquidity_usd": 389446.26248, "quality_flags": [], "retrieved_at": "2026-11-11T23:20:36.769397+00:00", "contract_end_at": "2026-12-09T23:59:00+00:00"} | ["12月单次50+bp风险", "利率与长久期估值"] | ["官方政策及融资/利率同步趋紧", "数据转弱与实际政策不符"] | [null, null] |
| ["Will the Fed increase interest rates by 25 bps after the December 2026 meeting?", "以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。", "https://polymarket.com/event/fed-decision-in-december-20260729232808632"] | [85.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.010000000000000009, "volume24h_usd": 174566.22523700004, "liquidity_usd": 693322.2174, "quality_flags": [], "retrieved_at": "2026-11-11T23:20:36.769397+00:00", "contract_end_at": "2026-12-09T23:59:00+00:00"} | ["12月单次加息25bp定价；准确公告时点本轮不强填", "利率和估值"] | ["以正式目标区间变动匹配专门档位", "实际政策与对应档不符"] | [null, null] |

## Polymarket · 将要发生的事件及概率

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |

## 将要发生的事件及概率 · 本次无合格合约

本次未纳入合格合约，不代表相关风险或事件不存在。见搜索覆盖与限制。

## Jensen Huang announced resignation or removal by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1343940 / 6882826 |
| Yes 概率 % | 76.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [61.0, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 60.0} |
| 24h成交量 / 流动性 USD | [1827058.6870299994, 139936.6396] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 年末23:59美东前，黄仁勋/NVIDIA或授权代表正式明确宣布辞任或被撤去CEO，且预定在宣布后18个月内实施则Yes；不要求年内实际离任。临时休假、停职、条件式考虑、未被接受辞呈和媒体单独传闻不算。以官方信息优先；不得把调查直接视为离任。 合格辞任/撤职实际发生亦可能触发，需按专门规则核验；本次与早报hash相同。 |
| 规则指纹 | 967939ae08f1461b2a8b5a40c6c07828619958ef439b679055b7698fa1e18988 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-11T23:19:35.568056Z |
| 抓取时间 | 2026-11-11T23:20:36.769397+00:00 |
| 来源 | https://polymarket.com/event/jensen-huang-announced-resignation-or-removal-by-december-31 |

## Will the Fed increase interest rates by 50+ bps after the December 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 770450 / 3215009 |
| Yes 概率 % | 10.55 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.1, 9.8] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.5999999999999992} |
| 24h成交量 / 流动性 USD | [659311.034143, 389446.26248] |
| 价差 pp | 0.10 |
| 到期 | 2026-12-09T23:59:00+00:00 |
| 结算规则摘要 | 衡量12月8–9日该次FOMC前后联邦基金目标区间上限上调至少50bp；非标准变化向上取整到最近25bp对应档。按正式声明，若下一次会议结束仍无声明则按不变档处理。不是全年累计加息幅度。 |
| 规则指纹 | a05ecc7aefe678e9936425027277135b8c37cdaf659af595020eb1668ec48e58 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-11T23:17:36.273133Z |
| 抓取时间 | 2026-11-11T23:20:36.769397+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-december-20260729232808632 |

## Will the Fed increase interest rates by 25 bps after the December 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 770450 / 3215008 |
| Yes 概率 % | 85.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, 8.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [174566.22523700004, 693322.2174] |
| 价差 pp | 1.00 |
| 到期 | 2026-12-09T23:59:00+00:00 |
| 结算规则摘要 | 以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。 |
| 规则指纹 | 933a10a15eeec0ff1de30468fa20540301ed243f75cc3572d42946192f81a123 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-11T23:17:36.273133Z |
| 抓取时间 | 2026-11-11T23:20:36.769397+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-december-20260729232808632 |

## Russia x Ukraine energy ceasefire agreement by November 15, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1360126 / 6947935 |
| Yes 概率 % | 3.85 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.6499999999999999} |
| 24h成交量 / 流动性 USD | [84129.368655, 108213.84958] |
| 价差 pp | 0.10 |
| 到期 | 2026-11-15T21:59:00+00:00 |
| 结算规则摘要 | 11月15日23:59基辅时间前，俄乌双方同意暂停打击至少一类明确能源设施，双方官宣或可信报道共识确认；美国第三方单方声称不足。可限定地理范围，但仅一个设施不算；必须明确相互暂停，不是谈判/换囚。约定生效日可晚于截止。 |
| 规则指纹 | a3874db8482536581cb7832c287d198abdb207e6448a0fd10b7da294d17de561 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-11T23:19:35.568056Z |
| 抓取时间 | 2026-11-11T23:20:36.769397+00:00 |
| 来源 | https://polymarket.com/event/russia-x-ukraine-energy-ceasefire-agreement-by |

## AI bubble burst in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 691340 |
| Yes 概率 % | 10.75 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [1.8, 3.95] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 1.9000000000000004} |
| 24h成交量 / 流动性 USD | [75671.229263, 64126.30295] |
| 价差 pp | 0.10 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | fc153b2136a8dfbadcd169dce1add40690acb1748566b99716fe7ae8fcb07330 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-11T23:19:35.568056Z |
| 抓取时间 | 2026-11-11T23:20:36.769397+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## Russia x Ukraine ceasefire agreement by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 478472 / 2243897 |
| Yes 概率 % | 9.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-5.0, -3.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -4.000000000000001} |
| 24h成交量 / 流动性 USD | [74071.58728700002, 78872.196] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年末23:59ET前，双方官宣或可信共识确认相互暂停直接交战，包含明确生效日的全面暂停；仅限定目标/地点的局部能源安排不算。达成协议可先于实际生效，单方暂停不算。 |
| 规则指纹 | 2ea22f9548269db3205e41396a99073a2d5788dc4fde17989e34c8051ae6b75b |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-11T23:19:35.568056Z |
| 抓取时间 | 2026-11-11T23:20:36.769397+00:00 |
| 来源 | https://polymarket.com/event/russia-x-ukraine-ceasefire-agreement-by |

## Strait of Hormuz traffic returns to normal by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 455875 / 2176270 |
| Yes 概率 % | 8.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, -2.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [63477.000355, 208107.2002] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。 |
| 规则指纹 | b0c8ba27f4437b0d8ab819ae170bec118166232e39cdcaefb95bd352d29073d4 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-11T23:19:35.568056Z |
| 抓取时间 | 2026-11-11T23:20:36.769397+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31 |

## US x Iran Effective Ceasefire by November 15?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1337182 / 6831494 |
| Yes 概率 % | 53.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [5.5, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 1.0000000000000009} |
| 24h成交量 / 流动性 USD | [23253.665145000003, 87323.495] |
| 价差 pp | 1.00 |
| 到期 | 2026-11-15T20:29:00+00:00 |
| 结算规则摘要 | 须完成连续14个伊朗标准时间日，美国未对伊朗陆地及内水实施命中目标的合资格空袭/地对地导弹攻击，且该14天首日在创建后至11月15日范围内；最后一次合资格行动次日为首日，无行动则创建日为首日。拦截碎片、威胁、海域/领空、地面入侵、网络、小型武器/部分小型袭击等不算。第14日后再留3个日历日报道窗口，按官方信息及可信报道综合裁定。不是双方全面停火，也不要求14天在15日前完成。 |
| 规则指纹 | c70e370d0e95bf9245a1a527f4f02bb307f13aa2766e1cc24004c7559bfb4b53 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-11T23:19:35.568056Z |
| 抓取时间 | 2026-11-11T23:20:36.769397+00:00 |
| 来源 | https://polymarket.com/event/us-x-iran-effective-ceasefire-begins-by-2-week-pause-20261108 |

## AI bubble burst by June 30, 2027?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 4838928 |
| Yes 概率 % | 25.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [2.5, 2.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 2.4999999999999996} |
| 24h成交量 / 流动性 USD | [12523.218875999999, 50047.4645] |
| 价差 pp | 2.00 |
| 到期 | 2027-07-01T03:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | bd0420587e08487fffa5050e7fd9b79ffff909a9f843d3f620207ee859462505 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-11T23:19:35.568056Z |
| 抓取时间 | 2026-11-11T23:20:36.769397+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## Will WTI Crude Oil (WTI) hit (HIGH) $110 in November?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1250301 / 6172751 |
| Yes 概率 % | 5.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-2.0, -7.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -1.0000000000000002} |
| 24h成交量 / 流动性 USD | [3790.6829000000002, 27746.7623] |
| 价差 pp | 1.00 |
| 到期 | 2026-12-01T04:59:59.999000+00:00 |
| 结算规则摘要 | 11月合资格交易时段，Pyth对ICE Europe WTI活跃月CLL的任一最终1分钟High达到110美元即Yes；按原值不取整，最后三个交易日换月。主数据不可用时依ICE官方日高低。与Yahoo NYMEX连续WTI代理不是同一可直接裁决序列。 |
| 规则指纹 | 97cca376098aad5ff8f5ece05abb9ae13f218bc5005dc802696a1f1922949a52 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-11T23:19:35.568056Z |
| 抓取时间 | 2026-11-11T23:20:36.769397+00:00 |
| 来源 | https://polymarket.com/event/what-price-will-wti-hit-in-november-2026 |

## Tesla and SpaceX merger officially announced by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 192962 / 2252540 |
| Yes 概率 % | 9.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [590.1, 18864.1987] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59纽约时间前，Tesla或SpaceX正式宣布双方合并或一方收购另一方的控制权即Yes；无需在期限内完成交易。控制权通常为过半权益或等效治理权；少数股权投资及仅讨论不算。以公司公告或可信报道共识核验；旧URL中的june-30不是本合约期限。 |
| 规则指纹 | 909906ae3b6db7e473468713ea6a1e1e4cf4c931fe247c7d3d576e7986513008 |
| 质量 | ["volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-11T23:19:35.568056Z |
| 抓取时间 | 2026-11-11T23:20:36.769397+00:00 |
| 来源 | https://polymarket.com/event/tesla-and-spacex-merger-officially-announced-by-june-30 |

## CoreWeave downgraded by Moody's or S&P by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1219851 / 5939467 |
| Yes 概率 % | 19.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-8.5, -2.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -12.0} |
| 24h成交量 / 流动性 USD | [391.366483, 325.6489] |
| 价差 pp | 14.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59ET前，Moody’s或S&P正式下调CoreWeave长期主体/企业家族或高级无担保债信用评级则Yes；仅负面展望/观察名单不算，不要求降至某统一评级档。成交很薄，不视为客观违约概率。 |
| 规则指纹 | 040e522db15913bd31de0e1a7f935727361429e7c42b3c1fc5286a0cf1b0fc42 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"] |
| 元数据更新（不是成交时间） | 2026-11-11T23:19:35.568056Z |
| 抓取时间 | 2026-11-11T23:20:15.848912+00:00 |
| 来源 | https://polymarket.com/event/coreweave-downgraded-by-moodys-or-sp-by |

## AI 压力：合约、经营与估值分开

三层分开：第一，AI泡沫2026合约10.75%、2027年6月25%，均是专门多条件合同；2026同规则较晚报8.85%升1.90个百分点，并非客观破裂概率。H100指数官网更新至11日3.06美元/GPU小时，7日+7.4%，不满足≤1美元连续5日条件；不能据单一租金证明全部算力经济性。CEO离任宣布合约76.5%、买卖价差1个百分点、24h成交约183万美元，反映新的事件定价，但媒体传闻不构成其正式宣布条件。CRWV信用降级合约19%、价差14个百分点、24h成交约391美元，质量弱，不解读为精确违约风险。第二，CRWV官方10日财报收入36.61亿美元、营业利润2.07亿、净利息8.46亿；未来三个月约90亿客户预付款仍是预期。收盘60.77涨24.71%，盘后56.76较收盘−6.60%，需求与融资压力并存。AWS官方搜索结果显示11日智利区域向部分客户开放；不将多年投资计划记为本季已支出。NVDA收盘173.73但23:20UTC158.50；Reuters转述WSJ关于董事会准备撤换CEO的知情人士报道，不是公司正式决议。8日董事会声明确认调查，早于新报道，不能当作对新报道的驳斥。MSFT521.13、AMZN266.17、GOOGL293.45、META628.77的收盘分化表明AI不是统一交易；各自盘后报价另列，不能假定全部受同一因果驱动。第三，SEC五家公司定期披露列表本轮全部重查，与原财务底稿版本一致。仅NVDA具备审核过的FCFF底稿，更新盘后价格反推情景；净债务/租赁/稀释与假设见模型。其余四家公司完整企业现金流桥缺失，估值不可用。情景权重不作客观概率，公司整体价值不全归于AI。tc的40亿美元新贷款线索尚未独立证实，不作为已完成融资或主体评级上调。

## NVDA · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | scenario_analysis |
| 财务底稿 | TTM 至 2026-07-26；最新 10-Q / filed 2026-08-26 |
| 披露检查 | {"checked_at": "2026-11-11T23:20:52.999170+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001045810.json", "latest_filing_date": "2026-08-26"} |
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
| 披露检查 | {"checked_at": "2026-11-11T23:20:54.902271+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0000789019.json", "latest_filing_date": "2026-10-28"} |
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
| 披露检查 | {"checked_at": "2026-11-11T23:20:57.691736+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001018724.json", "latest_filing_date": "2026-10-30"} |
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
| 披露检查 | {"checked_at": "2026-11-11T23:21:00.257144+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001652044.json", "latest_filing_date": "2026-10-29"} |
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
| 披露检查 | {"checked_at": "2026-11-11T23:21:02.990273+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001326801.json", "latest_filing_date": "2026-10-22"} |
| 观测财务数据 | {"revenue_million": 64601, "operating_cashflow_million": 32790, "reported_capex_including_finance_lease_principal_million": 34910, "company_defined_fcf_million": -2120, "diluted_shares_million": 2573, "reported_operating_income_million": 12988, "legal_charge_million": 9900, "observed_end": "2026-09-30", "published_at": "2026-10-21T16:01:00-04:00", "unit": "USD million; shares million", "noncancelable_commitments_million": 454520, "leases_not_commenced_million": 355730, "contingent_cloud_capacity_max_million": 14720, "restricted_cash_reclassified_million": 10800, "commitments_due_2026_million": 45850, "commitments_due_2027_million": 121410} |
| 来源 | ["https://www.prnewswire.com/news-releases/meta-reports-third-quarter-2026-results-302915964.html", "https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm", "https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Announces-Launch-of-Offering-of-Depositary-Shares-Representing-Series-A-Mandatory-Convertible-Preferred-Stock-and-Offering-of-Class-A-Common-Stock-in-Connection-with-Forward-Sale-Agreements/default.aspx", "https://www.prnewswire.com/news-releases/meta-announces-pricing-of-offering-of-depositary-shares-representing-series-a-mandatory-convertible-preferred-stock-and-offering-of-class-a-common-stock-in-connection-with-forward-sale-agreements-302920247.html"] |
| 口径 | 公司FCF扣除融资租赁本金，不能直接代替模型FCFF；融资租赁负债/新增资产未齐，不假设零。法律费用不全归AI经营。 |
| 主观假设说明 | 缺失 |
| 权益桥额外假设 | 无 |
| 缺失原因 | 沿用底稿的历史核验说明（其中“本次”指原核验日）；本轮最新定期财报列表检查见disclosure_check。22日10-Q已核验，本次无新增定期财报。27日普通股625美元定价、优先票息6.5%已核验；完整融资租赁负债/新增资产、优先权益/远期发行与现金到账桥未齐，不用不同承诺简单充当现有债务，暂停精确FCFF反推。 |

## 宽基可靠反弹测试

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 盘后冲击后的首次完整交易及PPI |
| 关联标的 | ["SPY", "QQQ", "RSP"] |
| 确认条件 | SPY755附近、QQQ680–682首轮回踩守住，随后站回当日常规VWAP并出现更高低点；收盘再看SPY760.20/764.55、QQQ698.94；均权参与同步 |
| 失效条件 | 跌破755/680并反抽失败则撤销升级；未取得VWAP前不声称满足该条件 |
| 观察期限 | 11月12–13日常规时段；NVDA业绩延伸至17日 |
| 反证 | 收盘上涨量不足，盘后仍可能跳空；一次盘中突破不能证明趋势反转 |
| 状态 | 观察项，待下一常规时段确认 |

## 芯片先隔离治理风险再评估

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | NVDA正式公告、NBIS及NVDA业绩 |
| 关联标的 | ["SMH", "NVDA", "CRWV", "MU"] |
| 确认条件 | SMH490–493守住并逐步收复506.96，NVDA重新建立更高低点且恢复170.24才重评原修复剧本；CRWV守住财报前高51.02，融资兑现进一步确认 |
| 失效条件 | SMH失490反抽失败、NVDA持续创新低或官方事件进一步影响经营；不等待所有条件同时触发 |
| 观察期限 | 11月12–13日常规时段；NVDA业绩延伸至17日 |
| 反证 | 盘后NVDA已跌破原支撑，SMH仍低于523附近中期均线；CRWV利润与利息不匹配 |
| 状态 | NVDA旧修复条件盘后失效；其余等待验证 |

## 观察非芯片相对强度

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 风险偏好重新分配及PPI |
| 关联标的 | ["XLI", "XLF", "XLV", "XLP"] |
| 确认条件 | XLI守167.70并突破172.74再回踩；XLF/XLV/XLP保持各自20日线和多日相对SPY强度，且指数不创新低 |
| 失效条件 | 跌破各自20日线且相对强度持续转弱；新信用数据恶化时不把金融视作防御 |
| 观察期限 | 11月12–13日常规时段；NVDA业绩延伸至17日 |
| 反证 | 上涨不证明净申购；防御篮子在强风险偏好阶段可能落后 |
| 状态 | 观察项，待下一常规时段确认 |

## 跨期比较与上期剧本复核

复核昨晚剧本：SPY收759.81、QQQ690.38、SMH506.96满足收盘高于755、680–682、490–493的价格部分；未取得完整VWAP/回踩与逐时广度，不能宣称全部条件确认。SPY仍未收复20日760.20，SMH仍低于200日523.11；NVDA日内收在170.24上，但盘后158.50已使该个股修复条件失效，不能用旧收盘掩盖。MSFT收521.13未恢复此前538.70观察线。CRWV收盘突破旧高，盘后回落仍在旧高上；价格修复并未证明现金流兑现。同ID且hash一致比较：Strait of Hormuz traffic returns to normal by December 31?：+0.00个百分点；Will the Fed increase interest rates by 25 bps after the December 2026 meeting?：+0.00个百分点；AI bubble burst in 2026?：+1.90个百分点；AI bubble burst by June 30, 2027?：+2.50个百分点；Tesla and SpaceX merger officially announced by December 31?：+0.00个百分点；Jensen Huang announced resignation or removal by December 31, 2026?：+60.00个百分点；US x Iran Effective Ceasefire by November 15?：+1.00个百分点；Will the Fed increase interest rates by 50+ bps after the December 2026 meeting?：+0.60个百分点；CoreWeave downgraded by Moody's or S&P by December 31, 2026?：-12.00个百分点；Russia x Ukraine energy ceasefire agreement by November 15, 2026?：-0.65个百分点；Russia x Ukraine ceasefire agreement by December 31, 2026?：-4.00个百分点；Will WTI Crude Oil (WTI) hit (HIGH) $110 in November?：-1.00个百分点。对新CEO人选事件已搜索，但未纳入精选：人选之间可能互斥、暂代与正式任命定义需逐份核验，不用它代替原离任合约。

## 可计算的跨期变化

```json
[
  {
    "mode": "daily",
    "baseline": "reports/daily/2026-11-10/20261111T121452.588050Z/evidence.json",
    "baseline_cutoff": "2026-11-11T12:13:46.942972+00:00",
    "close_change_pct": {
      "SPY": 1.3188093228371,
      "QQQ": 2.3148963914759957,
      "IWM": 0.8945790454582214,
      "RSP": 0.8013351025643711,
      "GLD": -1.1343870722325344,
      "GC=F": -0.982577886839342,
      "CL=F": 0.3486697107985881,
      "BZ=F": 1.1148806386242827,
      "TLT": 0.04945711781123574,
      "UUP": 0.6861089727504321,
      "HYG": 0.22026194386255415,
      "LQD": 0.07701370154979958,
      "^VIX": -10.123326855273984,
      "^VIX3M": -6.782944088808518,
      "^VVIX": -6.3748279083149395,
      "^MOVE": 0.0,
      "NVDA": 2.8657684619467716,
      "MSFT": -2.257291197902578,
      "AMZN": -1.7351429741857327,
      "GOOGL": 2.112188468607612,
      "META": -1.9676008090186548,
      "CRWV": 24.707574448244696,
      "MU": 11.886472974112738,
      "DRAM": 10.359249871310293,
      "VRT": 6.32787210837622,
      "XLK": 3.226568486224446,
      "XLE": 1.8646517673742258,
      "XLF": 0.5832906969423624,
      "XLI": 1.3275680376245491,
      "XLV": 0.03705636574560245,
      "XLP": 0.46138435084857043,
      "XLY": -0.049570579492363986,
      "XLC": 0.779506608424807,
      "XLU": 0.20580872062658795,
      "XLRE": 0.022427817681780482,
      "XLB": 0.32166885250870525,
      "SMH": 4.823932828137623,
      "IGV": 1.8937521092427634,
      "XOP": 2.632175823113503,
      "OIH": 2.8414054919412957,
      "ITA": 1.2301304884847708,
      "ARKX": 1.3698624899151968,
      "KRE": -0.191543845482256,
      "SKYY": 2.900971118403617
    },
    "quote_change_pct": {
      "SPY": {
        "change_pct": -0.05683320116310897,
        "from_observed_at": "2026-11-11T12:03:26+00:00",
        "to_observed_at": "2026-11-11T23:19:55+00:00"
      },
      "QQQ": {
        "change_pct": -0.6918906347660458,
        "from_observed_at": "2026-11-11T12:03:20+00:00",
        "to_observed_at": "2026-11-11T23:20:14+00:00"
      },
      "SMH": {
        "change_pct": -3.050366516907077,
        "from_observed_at": "2026-11-11T12:03:23+00:00",
        "to_observed_at": "2026-11-11T23:19:42+00:00"
      },
      "NVDA": {
        "change_pct": -9.609352723125175,
        "from_observed_at": "2026-11-11T12:03:28+00:00",
        "to_observed_at": "2026-11-11T23:20:14+00:00"
      },
      "MSFT": {
        "change_pct": -2.4242990654205654,
        "from_observed_at": "2026-11-11T12:03:25+00:00",
        "to_observed_at": "2026-11-11T23:20:07+00:00"
      },
      "AMZN": {
        "change_pct": -1.265729634263002,
        "from_observed_at": "2026-11-11T12:03:25+00:00",
        "to_observed_at": "2026-11-11T23:20:14+00:00"
      },
      "GOOGL": {
        "change_pct": 2.1320566252195805,
        "from_observed_at": "2026-11-11T12:03:07+00:00",
        "to_observed_at": "2026-11-11T23:20:13+00:00"
      },
      "META": {
        "change_pct": -2.9153337417407665,
        "from_observed_at": "2026-11-11T12:02:03+00:00",
        "to_observed_at": "2026-11-11T23:19:42+00:00"
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
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-11-10"
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
        "change_pp": 60.0
      },
      "3215009": {
        "status": "comparable",
        "change_pp": 0.5999999999999992
      },
      "3215008": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "6947935": {
        "status": "comparable",
        "change_pp": -0.6499999999999999
      },
      "691340": {
        "status": "comparable",
        "change_pp": 1.9000000000000004
      },
      "2243897": {
        "status": "comparable",
        "change_pp": -4.000000000000001
      },
      "2176270": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "6831494": {
        "status": "comparable",
        "change_pp": 1.0000000000000009
      },
      "4838928": {
        "status": "comparable",
        "change_pp": 2.4999999999999996
      },
      "6172751": {
        "status": "comparable",
        "change_pp": -1.0000000000000002
      },
      "2252540": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "5939467": {
        "status": "comparable",
        "change_pp": -12.0
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
    "event": "Nebius Q3电话会，北京12日21:00；当前尚未发生",
    "date": "2026-11-12T08:00:00-05:00",
    "source": "https://nebius.com/investor-events"
  },
  {
    "event": "10月PPI，北京13日21:30；CPI已于10日发布",
    "date": "2026-11-13T08:30:00-05:00",
    "source": "https://www.bls.gov/schedule/2026/11_sched.htm"
  },
  {
    "event": "NVDA业绩预计16:20EST、电话会17:00EST，北京18日05:20/06:00",
    "date": "2026-11-17T16:20:00-05:00",
    "source": "https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/default.aspx"
  },
  {
    "event": "英伟达正式治理/人事公告，具体日期未定；报道不是官方决议",
    "date": null,
    "source": "https://investor.nvidia.com/news/press-release-details/2026/Statement-from-NVIDIA-Board-of-Directors/default.aspx"
  }
]
```

## 新闻事件去重与时间

| 事件 | 摘要 | 发生时间（未知留空） | 各来源发布时间 / 抓取时间 |
| --- | --- | --- | --- |
| 20261111-nv | 盘后Reuters转述WSJ知情人士称董事会准备撤换CEO，尚未取得正式人事决议；与收盘反弹分开。 | 缺失 | [{"source": "https://sg.finance.yahoo.com/news/nvidia-preparing-oust-ceo-jensen-223546395.html", "published_at": "2026-11-11T22:37:00+00:00", "retrieved_at": "2026-11-11T23:27:26.061273+00:00"}] |
| 20261111-crwv | 财报营收增长与利息压力并存，股价收盘大涨后盘后回撤。 | 缺失 | [{"source": "https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Third-Quarter-2026-Results/default.aspx", "published_at": null, "retrieved_at": "2026-11-11T23:27:26.061273+00:00"}] |
| 20261111-aws | 官方搜索摘要显示智利区域向部分客户开放；完整正文读取失败，不扩展未核验金额细节。 | 缺失 | [{"source": "https://www.aboutamazon.com/news/aws/aws-south-america-chile-region-launch", "published_at": null, "retrieved_at": "2026-11-11T23:27:26.061273+00:00"}] |
| 20261111-ship | 油轮事件部分伤损及责任仍待独立核实。 | 缺失 | [{"source": "https://apnews.com/article/50075bc97e07d41fa3b66fc28858c06b", "published_at": null, "retrieved_at": "2026-11-11T23:27:26.061273+00:00"}] |
| 20261111-geo | 俄乌会谈与换囚不是全面停火。 | 缺失 | [{"source": "https://apnews.com/article/7c8d1024302e0c6ad8be064eec852a64", "published_at": null, "retrieved_at": "2026-11-11T23:27:26.061273+00:00"}] |

## 覆盖范围与数据缺口

```json
[
  "tc统一ts不作为成交证据，收盘数与盘后数区分；核心状态以独立Yahoo分钟实际时戳核验，原tc包保留。",
  "常规时段完整VWAP、逐笔回踩及全成分广度未核验；17/19只代表ETF观察池。",
  "tc新闻主批及主题批各50条均有截断，不承诺覆盖全部新闻；按事件去重。CME快讯各档合计不为100%，未采用。",
  "tc日历新闻中CPI/CRWV事件日期与官方不符，采用BLS和公司日期。",
  "GPR官网9日更新但采集止于2日，补查结果另记；MOVE为10日；债市假日和信用/真实利率滞后。",
  "当期单ETF净申赎、机构交易身份与完整市场资金流缺失；只展示旧ICI窗口。",
  "Polymarket搜索首批截断，缺全盘口/最后成交时戳；CRWV评级价差14个百分点且成交薄，不能据中点推断精确风险。",
  "四家完整FCFF桥缺失，五家SEC定期披露检查不等于全覆盖实时8-K；无新定期披露时不编造新基本面。",
  "DRAM历史不足200日；期货换月/成交时段不同。NVDA人事新闻仍是媒体引述，8日声明不能替代后来官方决定。",
  "AWS及Reuters文章正文复开失败，但可读官方/原报道索引支持有限事实；CRWV新贷款线索未独立验证。",
  "CNN API418，已通过本轮Chrome官方页面直接核验。GPR补取官方XLS并成功解析，仍止于11月2日，与网页9日更新标注不一致，保留滞后。",
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
    "url": "https://sg.finance.yahoo.com/news/nvidia-preparing-oust-ceo-jensen-223546395.html",
    "checked_at": "2026-11-11T23:27:26.061273+00:00",
    "note": "本轮核验；具体发布时间未知留空。搜索索引可读、正文打开失败；报道状态明确。"
  },
  {
    "url": "https://investor.nvidia.com/news/press-release-details/2026/Statement-from-NVIDIA-Board-of-Directors/default.aspx",
    "checked_at": "2026-11-11T23:27:26.061273+00:00",
    "note": "本轮核验；具体发布时间未知留空。"
  },
  {
    "url": "https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Third-Quarter-2026-Results/default.aspx",
    "checked_at": "2026-11-11T23:27:26.061273+00:00",
    "note": "本轮核验；具体发布时间未知留空。"
  },
  {
    "url": "https://www.aboutamazon.com/news/aws/aws-south-america-chile-region-launch",
    "checked_at": "2026-11-11T23:27:26.061273+00:00",
    "note": "本轮核验；具体发布时间未知留空。搜索索引可读、正文打开失败；报道状态明确。"
  },
  {
    "url": "https://www.bls.gov/schedule/2026/11_sched.htm",
    "checked_at": "2026-11-11T23:27:26.061273+00:00",
    "note": "本轮核验；具体发布时间未知留空。"
  },
  {
    "url": "https://nebius.com/investor-events",
    "checked_at": "2026-11-11T23:27:26.061273+00:00",
    "note": "本轮核验；具体发布时间未知留空。"
  },
  {
    "url": "https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/default.aspx",
    "checked_at": "2026-11-11T23:27:26.061273+00:00",
    "note": "本轮核验；具体发布时间未知留空。"
  },
  {
    "url": "https://www.ici.org/research/stats/etf_flows",
    "checked_at": "2026-11-11T23:27:26.061273+00:00",
    "note": "本轮核验；具体发布时间未知留空。"
  },
  {
    "url": "https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/overview/",
    "checked_at": "2026-11-11T23:27:26.061273+00:00",
    "note": "本轮核验；具体发布时间未知留空。"
  },
  {
    "url": "https://edition.cnn.com/markets/fear-and-greed",
    "checked_at": "2026-11-11T23:27:26.061273+00:00",
    "note": "本轮核验；具体发布时间未知留空。CNN为浏览器观测。"
  },
  {
    "url": "https://www.silicondata.com/products/silicon-index/h100",
    "checked_at": "2026-11-11T23:27:26.061273+00:00",
    "note": "本轮核验；具体发布时间未知留空。"
  },
  {
    "url": "https://www.matteoiacoviello.com/gpr.htm",
    "checked_at": "2026-11-11T23:27:26.061273+00:00",
    "note": "本轮核验；具体发布时间未知留空。"
  },
  {
    "url": "https://www.sifma.org/resources/general/holiday-schedule",
    "checked_at": "2026-11-11T23:27:26.061273+00:00",
    "note": "本轮核验；具体发布时间未知留空。"
  },
  {
    "url": "https://apnews.com/article/50075bc97e07d41fa3b66fc28858c06b",
    "checked_at": "2026-11-11T23:27:26.061273+00:00",
    "note": "本轮核验；具体发布时间未知留空。"
  },
  {
    "url": "https://apnews.com/article/7c8d1024302e0c6ad8be064eec852a64",
    "checked_at": "2026-11-11T23:27:26.061273+00:00",
    "note": "本轮核验；具体发布时间未知留空。"
  }
]
```

## 付费信源建议（未订阅）

```json
[]
```
