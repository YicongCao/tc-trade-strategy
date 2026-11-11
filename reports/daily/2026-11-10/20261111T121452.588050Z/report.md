# 每日交易总结 · 2026-11-10

## 一分钟读懂 · Agent 摘要

### 当前判断

判断由晨报的脆弱修复上调为盘前修复增强，尚未确认趋势反转。应重点看开盘后能否守住刚收复的区域，而不是只看跳空幅度。

### 与上次相比

相对晨报，CoreWeave财报带来的需求信心扩散到芯片，QQQ盘前越过此前680–682观察区；MSFT修复较慢。股票正常开市，但今天美国债市是假日，旧利率不能证明通胀压力消退。

### 最重要的信号

- 约12:03UTC，SPY756.60、QQQ687.97、SMH507.48，较昨收约+0.89%、+1.96%、+4.93%；CRWV约+15.06%。
- TSMC十月营收同比+59.7%、CoreWeave增长支持需求；高利息与资本开支仍约束现金回收。
- CNN34仍属Fear；VIX盘前约18.63回落，但昨日MOVE上升，信用数据滞后。

### 接下来观察

- SPY755附近、QQQ680–682、SMH490–493若开盘回踩不破，再观察更高低点、量能和收盘保持。
- 芯片优先观察强弱扩散，金融/医疗保留相对强度对照；不把板块上涨写成主力净流入。
- 跟踪13日PPI、17日NVIDIA业绩和治理进展；油轮遇袭报道与外交缓和必须分别核验。

### 不要忽略

盘前不是完整交易日，缺当期ETF申赎、完整广度和常规时段VWAP；宏观及GPR滞后。单一合约和单次高开不足以确认风险解除。

## 研究结论

11月11日晚报：AI硬件带动盘前修复加速，尚待常规时段回踩和收盘确认；债市假日削弱利率交叉验证。

## 时点与口径

| 项目 | 内容 |
| --- | --- |
| 模式 | 每日交易总结 |
| 常规交易窗口 | 2026-11-10 → 2026-11-10（纽约交易日） |
| 截止·纽约 | 2026-11-11T07:13:46.942972-05:00 |
| 截止·北京 | 2026-11-11T20:13:46.942972+08:00 |
| 实际生成时间 | 2026-11-11T12:13:47.685306+00:00 |
| 市场阶段 | 盘前 |
| 下一交易日 | 2026-11-11 |
| 运行重点 | 全市场 |
| 上一版本 | reports/daily/2026-11-10/20261111T000325.344361Z/evidence.json |
| 质量 | partial |
| Daily 北京时间计划时段 | 2026-11-11T20:00:00+08:00 |

## 采集、补查与剩余缺口

| 目标 | 补查结果 | 来源 | 观测 / 抓取时间 | 说明 |
| --- | --- | --- | --- | --- |
| 1219851 | 已校验接入 | https://gamma-api.polymarket.com/events/1219851 | 2026-11-11T12:03:29.635154+00:00 / 2026-11-11T12:03:29.635154+00:00 | Gamma observation; metadata timestamp is not trade time |
| 1360126 | 冲突，保留原值 | 缺失 |  /  | 已有合约不可静默覆盖；重新采集统一时点快照 |
| 478472 | 冲突，保留原值 | 缺失 |  /  | 已有合约不可静默覆盖；重新采集统一时点快照 |
| 1250301 | 冲突，保留原值 | 缺失 |  /  | 已有合约不可静默覆盖；重新采集统一时点快照 |

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
| prices.SPY.value | 749.92 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_1d_pct | -0.37 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_5d_pct | -0.59 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_20d_pct | -3.61 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_60d_pct | -2.70 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_1d_pp | 0.00 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_5d_pp | 0.00 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_20d_pp | 0.00 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_60d_pp | 0.00 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma20 | 760.69 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma50 | 764.55 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma200 | 728.30 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma20_pct | -1.42 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma50_pct | -1.91 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma200_pct | 2.97 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_sma | 12.11 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_pct | 1.61 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.drawdown_from_63d_high_pct | -3.74 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.volume_vs_previous20_ratio | 0.84 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SPY/history/ |
| prices.QQQ.value | 674.76 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_1d_pct | -0.68 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_5d_pct | -1.54 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_20d_pct | -9.25 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_60d_pct | -7.45 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_1d_pp | -0.31 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_5d_pp | -0.95 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_20d_pp | -5.64 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_60d_pp | -4.75 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma20 | 700.86 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma50 | 719.20 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma200 | 680.35 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma20_pct | -3.72 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma50_pct | -6.18 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma200_pct | -0.82 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_sma | 17.87 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_pct | 2.65 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.drawdown_from_63d_high_pct | -11.18 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.volume_vs_previous20_ratio | 0.75 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.IWM.value | 280.58 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_1d_pct | -0.68 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_5d_pct | 0.28 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_20d_pct | 1.40 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_60d_pct | -7.48 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_1d_pp | -0.32 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_5d_pp | 0.87 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_20d_pp | 5.01 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_60d_pp | -4.78 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma20 | 277.27 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma50 | 281.44 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma200 | 278.21 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma20_pct | 1.19 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma50_pct | -0.31 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma200_pct | 0.85 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_sma | 5.21 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_pct | 1.86 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.drawdown_from_63d_high_pct | -7.79 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.volume_vs_previous20_ratio | 0.83 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IWM/history/ |
| prices.RSP.value | 220.88 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_1d_pct | -0.03 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_5d_pct | 0.74 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_20d_pct | 3.55 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_60d_pct | 0.42 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_1d_pp | 0.34 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_5d_pp | 1.33 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_20d_pp | 7.16 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_60d_pp | 3.12 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma20 | 217.49 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma50 | 214.61 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma200 | 207.33 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma20_pct | 1.56 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma50_pct | 2.92 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma200_pct | 6.53 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_sma | 3.03 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_pct | 1.37 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.drawdown_from_63d_high_pct | -1.10 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.volume_vs_previous20_ratio | 0.80 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/RSP/history/ |
| prices.GLD.value | 369.36 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_1d_pct | -2.68 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_5d_pct | 2.81 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_20d_pct | -3.23 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_60d_pct | -8.91 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_1d_pp | -2.31 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_5d_pp | 3.40 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_20d_pp | 0.39 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_60d_pp | -6.21 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma20 | 372.04 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma50 | 383.59 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma200 | 410.37 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma20_pct | -0.72 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma50_pct | -3.71 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma200_pct | -9.99 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_sma | 7.57 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_pct | 2.05 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.drawdown_from_63d_high_pct | -13.72 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.volume_vs_previous20_ratio | 0.88 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GC=F.value | 4,030.20 | USD_per_troy_ounce | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_1d_pct | -2.05 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_5d_pct | 2.28 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_20d_pct | -3.52 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_60d_pct | -9.91 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_1d_pp | -1.68 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_5d_pp | 2.87 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_20d_pp | 0.09 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_60d_pp | -7.21 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma20 | 4,069.55 | USD_per_troy_ounce | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma50 | 4,213.09 | USD_per_troy_ounce | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma200 | 4,491.91 | USD_per_troy_ounce | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma20_pct | -0.97 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma50_pct | -4.34 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma200_pct | -10.28 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_sma | 95.51 | USD_per_troy_ounce | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_pct | 2.37 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.drawdown_from_63d_high_pct | -14.21 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.volume_vs_previous20_ratio | 1.12 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.CL=F.value | 86.04 | USD_per_barrel | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_1d_pct | -0.93 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_5d_pct | -10.46 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_20d_pct | -8.60 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_60d_pct | 1.82 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_1d_pp | -0.56 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_5d_pp | -9.87 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_20d_pp | -4.99 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_60d_pp | 4.53 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma20 | 97.26 | USD_per_barrel | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma50 | 95.54 | USD_per_barrel | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma200 | 87.41 | USD_per_barrel | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma20_pct | -11.54 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma50_pct | -9.94 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma200_pct | -1.57 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_sma | 4.73 | USD_per_barrel | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_pct | 5.50 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.drawdown_from_63d_high_pct | -18.70 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.volume_vs_previous20_ratio | 1.16 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.BZ=F.value | 91.49 | USD_per_barrel | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_1d_pct | -1.17 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_5d_pct | -11.69 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_20d_pct | -13.44 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_60d_pct | 0.68 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_1d_pp | -0.80 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_5d_pp | -11.10 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_20d_pp | -9.83 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_60d_pp | 3.39 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma20 | 107.00 | USD_per_barrel | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma50 | 104.29 | USD_per_barrel | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma200 | 93.61 | USD_per_barrel | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma20_pct | -14.50 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma50_pct | -12.27 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma200_pct | -2.26 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_sma | 5.69 | USD_per_barrel | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_pct | 6.22 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.drawdown_from_63d_high_pct | -22.23 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.volume_vs_previous20_ratio | 1.26 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.TLT.value | 80.88 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_1d_pct | -1.32 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_5d_pct | -0.28 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_20d_pct | 3.20 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_60d_pct | 0.21 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_1d_pp | -0.95 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_5d_pp | 0.30 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_20d_pp | 6.81 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_60d_pp | 2.91 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma20 | 81.04 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma50 | 80.19 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma200 | 83.12 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma20_pct | -0.19 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma50_pct | 0.86 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma200_pct | -2.69 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_sma | 0.80 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_pct | 0.98 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.drawdown_from_63d_high_pct | -2.34 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.volume_vs_previous20_ratio | 1.04 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/TLT/history/ |
| prices.UUP.value | 29.15 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_1d_pct | 0.62 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_5d_pct | 0.48 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_20d_pct | 0.45 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_60d_pct | 3.74 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_1d_pp | 0.99 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_5d_pp | 1.07 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_20d_pp | 4.06 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_60d_pp | 6.44 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma20 | 29.00 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma50 | 28.72 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma200 | 27.99 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma20_pct | 0.52 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma50_pct | 1.49 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma200_pct | 4.15 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_sma | 0.12 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_pct | 0.42 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.drawdown_from_63d_high_pct | 0.00 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.volume_vs_previous20_ratio | 0.67 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/UUP/history/ |
| prices.HYG.value | 77.18 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_1d_pct | -0.43 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_5d_pct | 0.26 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_20d_pct | 0.12 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_60d_pct | -2.09 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_1d_pp | -0.06 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_5d_pp | 0.85 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_20d_pp | 3.73 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_60d_pp | 0.62 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma20 | 77.18 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma50 | 77.56 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma200 | 77.88 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma20_pct | 0.00 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma50_pct | -0.49 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma200_pct | -0.90 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_sma | 0.35 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_pct | 0.45 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.drawdown_from_63d_high_pct | -2.47 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.volume_vs_previous20_ratio | 0.90 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/HYG/history/ |
| prices.LQD.value | 103.88 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_1d_pct | -0.75 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_5d_pct | 0.15 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_20d_pct | 1.30 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_60d_pct | -0.88 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_1d_pp | -0.39 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_5d_pp | 0.74 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_20d_pp | 4.91 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_60d_pp | 1.82 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma20 | 103.88 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma50 | 103.59 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma200 | 105.76 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma20_pct | 0.00 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma50_pct | 0.28 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma200_pct | -1.77 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_sma | 0.61 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_pct | 0.59 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.drawdown_from_63d_high_pct | -1.96 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.volume_vs_previous20_ratio | 0.81 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/LQD/history/ |
| prices.^VIX.value | 19.46 | index | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_1d_pct | -2.31 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_5d_pct | -6.58 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_20d_pct | 27.44 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_60d_pct | 22.85 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_1d_pp | -1.94 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_5d_pp | -5.99 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_20d_pp | 31.05 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_60d_pp | 24.90 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma20 | 19.27 | index | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma50 | 17.08 | index | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma200 | 18.43 | index | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma20_pct | 0.97 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma50_pct | 13.91 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma200_pct | 5.59 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_sma | 3.74 | index | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_pct | 19.24 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.drawdown_from_63d_high_pct | -30.94 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-10 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX3M.value | 20.64 | index | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_1d_pct | -1.01 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_5d_pct | -2.96 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_20d_pct | 14.92 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_60d_pct | 8.40 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_1d_pp | -0.64 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_5d_pp | -2.37 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_20d_pp | 18.53 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_60d_pp | 11.11 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma20 | 20.39 | index | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma50 | 19.13 | index | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma200 | 20.60 | index | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma20_pct | 1.21 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma50_pct | 7.92 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma200_pct | 0.21 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_sma | 2.12 | index | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_pct | 10.26 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.drawdown_from_63d_high_pct | -19.22 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-10 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VVIX.value | 96.63 | index | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_1d_pct | -1.83 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_5d_pct | -10.03 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_20d_pct | 13.18 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_60d_pct | 2.89 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_1d_pp | -1.46 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_5d_pp | -9.44 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_20d_pp | 16.79 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_60d_pp | 5.59 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma20 | 103.77 | index | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma50 | 94.78 | index | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma200 | 99.01 | index | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma20_pct | -6.88 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma50_pct | 1.96 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma200_pct | -2.40 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_sma | 15.03 | index | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_pct | 15.55 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.drawdown_from_63d_high_pct | -28.42 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-10 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^MOVE.value | 92.43 | index | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_1d_pct | 7.50 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_5d_pct | -7.54 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_20d_pct | -8.57 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_60d_pct | 32.84 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_1d_pp | 7.87 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_5d_pp | -6.96 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_20d_pp | -4.96 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_60d_pp | 36.00 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma20 | 98.17 | index | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma50 | 93.56 | index | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma200 | 78.80 | index | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma20_pct | -5.85 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma50_pct | -1.21 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma200_pct | 17.30 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_sma | 5.62 | index | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_pct | 6.08 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.drawdown_from_63d_high_pct | -18.64 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-10 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.NVDA.value | 168.89 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_1d_pct | -5.47 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_5d_pct | -18.29 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_20d_pct | -26.09 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_60d_pct | -24.86 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_1d_pp | -5.11 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_5d_pp | -17.70 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_20d_pp | -22.48 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_60d_pp | -22.15 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma20 | 206.18 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma50 | 217.97 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma200 | 204.26 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma20_pct | -18.09 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma50_pct | -22.52 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma200_pct | -17.32 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_sma | 9.29 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_pct | 5.50 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.drawdown_from_63d_high_pct | -29.41 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.volume_vs_previous20_ratio | 3.11 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.MSFT.value | 533.16 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_1d_pct | -2.20 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_5d_pct | 2.34 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_20d_pct | -1.89 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_60d_pct | 11.20 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_1d_pp | -1.84 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_5d_pp | 2.92 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_20d_pp | 1.72 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_60d_pp | 13.91 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma20 | 531.09 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma50 | 517.80 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma200 | 439.59 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma20_pct | 0.39 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma50_pct | 2.97 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma200_pct | 21.29 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_sma | 17.29 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_pct | 3.24 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.drawdown_from_63d_high_pct | -4.07 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.volume_vs_previous20_ratio | 1.04 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.AMZN.value | 270.87 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_1d_pct | 1.48 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_5d_pct | 8.05 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_20d_pct | 4.75 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_60d_pct | 3.66 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_1d_pp | 1.84 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_5d_pp | 8.64 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_20d_pp | 8.36 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_60d_pp | 6.36 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma20 | 255.26 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma50 | 254.18 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma200 | 244.24 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma20_pct | 6.11 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma50_pct | 6.57 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma200_pct | 10.90 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_sma | 10.68 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_pct | 3.94 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.drawdown_from_63d_high_pct | 0.00 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.volume_vs_previous20_ratio | 0.78 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.GOOGL.value | 287.38 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_1d_pct | -0.27 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_5d_pct | 2.62 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_20d_pct | -18.77 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_60d_pct | -16.41 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_1d_pp | 0.10 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_5d_pp | 3.21 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_20d_pp | -15.16 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_60d_pp | -13.70 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma20 | 310.89 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma50 | 330.71 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma200 | 338.79 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma20_pct | -7.56 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma50_pct | -13.10 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma200_pct | -15.18 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_sma | 11.41 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_pct | 3.97 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.drawdown_from_63d_high_pct | -19.04 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.volume_vs_previous20_ratio | 0.71 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.META.value | 641.39 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_1d_pct | 0.00 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_5d_pct | 3.28 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_20d_pct | -15.88 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_60d_pct | 12.82 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_1d_pp | 0.37 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_5d_pp | 3.87 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_20d_pp | -12.27 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_60d_pp | 15.52 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma20 | 651.54 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma50 | 677.44 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma200 | 630.93 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma20_pct | -1.56 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma50_pct | -5.32 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma200_pct | 1.66 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_sma | 23.90 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_pct | 3.73 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.drawdown_from_63d_high_pct | -17.52 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.volume_vs_previous20_ratio | 0.52 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/META/history/ |
| prices.CRWV.value | 48.73 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_1d_pct | -0.51 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_5d_pct | -9.32 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_20d_pct | -37.37 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_60d_pct | -54.03 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_1d_pp | -0.14 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_5d_pp | -8.74 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_20d_pp | -33.76 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_60d_pp | -51.32 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma20 | 56.31 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma50 | 74.13 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma200 | 89.71 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma20_pct | -13.46 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma50_pct | -34.27 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma200_pct | -45.68 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_sma | 5.42 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_pct | 11.12 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.drawdown_from_63d_high_pct | -54.15 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.volume_vs_previous20_ratio | 1.23 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.MU.value | 725.11 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_1d_pct | -1.10 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_5d_pct | -15.20 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_20d_pct | -23.92 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_60d_pct | -28.32 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_1d_pp | -0.73 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_5d_pp | -14.61 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_20d_pp | -20.31 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_60d_pp | -25.62 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma20 | 854.81 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma50 | 952.87 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma200 | 759.88 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma20_pct | -15.17 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma50_pct | -23.90 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma200_pct | -4.58 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_sma | 60.62 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_pct | 8.36 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.drawdown_from_63d_high_pct | -33.91 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.volume_vs_previous20_ratio | 0.91 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MU/history/ |
| prices.DRAM.value | 40.64 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_1d_pct | -2.73 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_5d_pct | -14.69 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_20d_pct | -23.09 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_60d_pct | -32.70 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_1d_pp | -2.36 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_5d_pp | -14.11 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_20d_pp | -19.48 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_60d_pp | -30.00 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma20 | 46.72 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma50 | 54.04 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma200 | 缺失 | USD_per_share | 2026-11-10 | unavailable | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma20_pct | -13.01 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma50_pct | -24.80 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma200_pct | 缺失 | percent | 2026-11-10 | unavailable | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_sma | 3.33 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_pct | 8.19 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.drawdown_from_63d_high_pct | -36.12 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.volume_vs_previous20_ratio | 0.90 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.VRT.value | 194.22 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_1d_pct | -3.12 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_5d_pct | -17.69 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_20d_pct | -18.15 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_60d_pct | -33.57 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_1d_pp | -2.75 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_5d_pp | -17.11 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_20d_pp | -14.54 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_60d_pp | -30.86 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma20 | 210.27 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma50 | 234.56 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma200 | 271.29 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma20_pct | -7.63 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma50_pct | -17.20 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma200_pct | -28.41 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_sma | 19.17 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_pct | 9.87 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.drawdown_from_63d_high_pct | -33.89 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.volume_vs_previous20_ratio | 0.76 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/VRT/history/ |
| prices.XLK.value | 168.91 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_1d_pct | -1.15 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_5d_pct | -4.31 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_20d_pct | -13.94 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_60d_pct | -11.15 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_1d_pp | -0.78 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_5d_pp | -3.72 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_20d_pp | -10.33 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_60d_pp | -8.44 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma20 | 180.89 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma50 | 187.74 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma200 | 170.16 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma20_pct | -6.62 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma50_pct | -10.03 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma200_pct | -0.73 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_sma | 5.82 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_pct | 3.44 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.drawdown_from_63d_high_pct | -16.38 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.volume_vs_previous20_ratio | 0.83 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLE.value | 62.21 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_1d_pct | 0.44 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_5d_pct | -6.70 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_20d_pct | -7.43 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_60d_pct | -0.00 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_1d_pp | 0.80 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_5d_pp | -6.12 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_20d_pp | -3.82 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_60d_pp | 2.70 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma20 | 66.66 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma50 | 64.92 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma200 | 58.71 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma20_pct | -6.67 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma50_pct | -4.18 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma200_pct | 5.95 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_sma | 1.88 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_pct | 3.03 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.drawdown_from_63d_high_pct | -11.15 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.volume_vs_previous20_ratio | 0.89 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLF.value | 58.29 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_1d_pct | 0.52 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_5d_pct | 1.92 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_20d_pct | 6.33 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_60d_pct | 1.59 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_1d_pp | 0.89 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_5d_pp | 2.51 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_20d_pp | 9.94 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_60d_pp | 4.29 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma20 | 56.55 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma50 | 55.87 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma200 | 53.57 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma20_pct | 3.07 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma50_pct | 4.33 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma200_pct | 8.80 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_sma | 1.02 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_pct | 1.75 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.drawdown_from_63d_high_pct | -1.54 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.volume_vs_previous20_ratio | 0.82 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLI.value | 168.73 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_1d_pct | -0.09 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_5d_pct | -1.51 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_20d_pct | 0.04 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_60d_pct | -9.20 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_1d_pp | 0.27 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_5d_pp | -0.92 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_20d_pp | 3.65 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_60d_pp | -6.49 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma20 | 167.50 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma50 | 169.06 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma200 | 172.71 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma20_pct | 0.73 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma50_pct | -0.19 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma200_pct | -2.30 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_sma | 3.50 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_pct | 2.07 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.drawdown_from_63d_high_pct | -9.29 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.volume_vs_previous20_ratio | 0.59 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLV.value | 188.88 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_1d_pct | 0.29 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_5d_pct | 2.64 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_20d_pct | 11.33 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_60d_pct | 13.50 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_1d_pp | 0.66 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_5d_pp | 3.23 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_20d_pp | 14.94 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_60d_pp | 16.20 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma20 | 181.76 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma50 | 173.92 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma200 | 158.76 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma20_pct | 3.92 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma50_pct | 8.60 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma200_pct | 18.97 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_sma | 3.79 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_pct | 2.01 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.drawdown_from_63d_high_pct | -0.41 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.volume_vs_previous20_ratio | 0.77 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLP.value | 91.03 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_1d_pct | 0.15 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_5d_pct | 2.34 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_20d_pct | 8.12 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_60d_pct | 8.21 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_1d_pp | 0.52 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_5d_pp | 2.93 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_20d_pp | 11.73 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_60d_pp | 10.91 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma20 | 88.76 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma50 | 85.13 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma200 | 83.92 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma20_pct | 2.56 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma50_pct | 6.93 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma200_pct | 8.47 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_sma | 1.81 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_pct | 1.99 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.drawdown_from_63d_high_pct | -0.99 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.volume_vs_previous20_ratio | 0.61 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLY.value | 121.05 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_1d_pct | 0.03 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_5d_pct | 3.17 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_20d_pct | 7.73 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_60d_pct | 3.91 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_1d_pp | 0.40 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_5d_pp | 3.76 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_20d_pp | 11.34 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_60d_pp | 6.61 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma20 | 116.13 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma50 | 113.45 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma200 | 115.09 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma20_pct | 4.23 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma50_pct | 6.70 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma200_pct | 5.17 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_sma | 2.63 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_pct | 2.17 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.drawdown_from_63d_high_pct | -1.05 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.volume_vs_previous20_ratio | 0.80 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLC.value | 107.76 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_1d_pct | 0.37 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_5d_pct | 6.23 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_20d_pct | -4.03 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_60d_pct | -2.44 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_1d_pp | 0.74 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_5d_pp | 6.82 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_20d_pp | -0.42 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_60d_pp | 0.26 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma20 | 105.92 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma50 | 109.53 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma200 | 111.99 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma20_pct | 1.74 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma50_pct | -1.61 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma200_pct | -3.77 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_sma | 2.28 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_pct | 2.12 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.drawdown_from_63d_high_pct | -6.09 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.volume_vs_previous20_ratio | 0.73 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLU.value | 43.73 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_1d_pct | -0.14 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_5d_pct | 0.71 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_20d_pct | 4.44 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_60d_pct | -0.29 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_1d_pp | 0.23 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_5d_pp | 1.30 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_20d_pp | 8.05 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_60d_pp | 2.41 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma20 | 42.77 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma50 | 41.74 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma200 | 43.85 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma20_pct | 2.25 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma50_pct | 4.76 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma200_pct | -0.28 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_sma | 0.65 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_pct | 1.48 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.drawdown_from_63d_high_pct | -0.58 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.volume_vs_previous20_ratio | 0.58 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLRE.value | 44.58 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_1d_pct | -0.13 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_5d_pct | 2.08 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_20d_pct | 6.57 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_60d_pct | 0.28 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_1d_pp | 0.23 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_5d_pp | 2.67 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_20d_pp | 10.18 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_60d_pp | 2.98 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma20 | 43.02 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma50 | 42.47 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma200 | 42.90 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma20_pct | 3.63 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma50_pct | 4.96 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma200_pct | 3.91 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_sma | 0.75 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_pct | 1.68 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.drawdown_from_63d_high_pct | -1.20 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.volume_vs_previous20_ratio | 0.75 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLB.value | 52.85 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_1d_pct | -0.17 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_5d_pct | 0.49 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_20d_pct | 6.30 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_60d_pct | 1.63 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_1d_pp | 0.20 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_5d_pp | 1.08 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_20d_pp | 9.91 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_60d_pp | 4.34 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma20 | 51.91 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma50 | 50.87 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma200 | 50.88 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma20_pct | 1.81 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma50_pct | 3.90 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma200_pct | 3.88 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_sma | 1.03 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_pct | 1.96 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.drawdown_from_63d_high_pct | -1.95 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.volume_vs_previous20_ratio | 0.63 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLB/history/ |
| prices.SMH.value | 483.63 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_1d_pct | -0.78 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_5d_pct | -6.73 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_20d_pct | -17.77 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_60d_pct | -18.59 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_1d_pp | -0.41 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_5d_pp | -6.14 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_20d_pp | -14.16 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_60d_pp | -15.89 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma20 | 526.53 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma50 | 562.86 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma200 | 522.62 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma20_pct | -8.15 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma50_pct | -14.08 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma200_pct | -7.46 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_sma | 25.77 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_pct | 5.33 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.drawdown_from_63d_high_pct | -23.71 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.volume_vs_previous20_ratio | 0.85 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SMH/history/ |
| prices.IGV.value | 100.33 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_1d_pct | -1.11 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_5d_pct | -2.27 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_20d_pct | -9.60 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_60d_pct | -1.63 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_1d_pp | -0.75 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_5d_pp | -1.68 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_20d_pp | -5.99 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_60d_pp | 1.08 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma20 | 105.89 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma50 | 106.35 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma200 | 94.08 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma20_pct | -5.25 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma50_pct | -5.66 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma200_pct | 6.65 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_sma | 3.08 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_pct | 3.07 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.drawdown_from_63d_high_pct | -10.95 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.volume_vs_previous20_ratio | 0.72 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IGV/history/ |
| prices.XOP.value | 175.52 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_1d_pct | 0.79 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_5d_pct | -8.35 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_20d_pct | -12.16 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_60d_pct | -3.89 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_1d_pp | 1.15 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_5d_pp | -7.77 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_20d_pp | -8.55 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_60d_pp | -1.19 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma20 | 193.03 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma50 | 190.66 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma200 | 171.29 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma20_pct | -9.07 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma50_pct | -7.94 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma200_pct | 2.47 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_sma | 6.40 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_pct | 3.64 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.drawdown_from_63d_high_pct | -14.32 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.volume_vs_previous20_ratio | 1.58 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XOP/history/ |
| prices.OIH.value | 359.33 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_1d_pct | -0.35 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_5d_pct | -6.69 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_20d_pct | -7.98 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_60d_pct | -15.77 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_1d_pp | 0.02 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_5d_pp | -6.11 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_20d_pp | -4.37 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_60d_pp | -13.07 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma20 | 384.14 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma50 | 394.49 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma200 | 398.74 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma20_pct | -6.46 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma50_pct | -8.91 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma200_pct | -9.88 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_sma | 15.16 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_pct | 4.22 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.drawdown_from_63d_high_pct | -17.69 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.volume_vs_previous20_ratio | 0.76 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/OIH/history/ |
| prices.ITA.value | 72.35 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_1d_pct | 0.95 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_5d_pct | 0.41 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_20d_pct | 6.40 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_60d_pct | -13.49 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_1d_pp | 1.32 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_5d_pp | 0.99 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_20d_pp | 10.01 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_60d_pp | -10.79 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma20 | 69.65 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma50 | 70.56 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma200 | 75.90 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma20_pct | 3.88 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma50_pct | 2.54 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma200_pct | -4.68 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_sma | 2.10 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_pct | 2.90 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.drawdown_from_63d_high_pct | -14.18 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.volume_vs_previous20_ratio | 0.56 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ARKX.value | 29.93 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_1d_pct | -0.33 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_5d_pct | 0.07 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_20d_pct | -4.80 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_60d_pct | -13.75 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_1d_pp | 0.04 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_5d_pp | 0.65 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_20d_pp | -1.19 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_60d_pp | -11.04 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma20 | 29.87 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma50 | 31.27 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma200 | 32.31 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma20_pct | 0.19 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma50_pct | -4.29 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma200_pct | -7.37 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_sma | 1.06 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_pct | 3.55 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.drawdown_from_63d_high_pct | -14.14 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.volume_vs_previous20_ratio | 3.34 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.KRE.value | 73.09 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_1d_pct | -0.49 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_5d_pct | 0.29 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_20d_pct | 5.84 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_60d_pct | -5.02 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_1d_pp | -0.12 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_5d_pp | 0.88 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_20d_pp | 9.45 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_60d_pp | -2.32 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma20 | 71.88 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma50 | 71.68 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma200 | 70.55 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma20_pct | 1.69 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma50_pct | 1.96 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma200_pct | 3.60 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_sma | 1.67 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_pct | 2.28 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.drawdown_from_63d_high_pct | -5.68 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.volume_vs_previous20_ratio | 0.70 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/KRE/history/ |
| prices.SKYY.value | 149.95 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_1d_pct | -0.50 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_5d_pct | -3.87 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_20d_pct | -12.58 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_60d_pct | -7.58 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_1d_pp | -0.14 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_5d_pp | -3.28 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_20d_pp | -8.97 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_60d_pp | -4.87 | pp | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma20 | 160.71 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma50 | 163.31 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma200 | 137.50 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma20_pct | -6.70 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma50_pct | -8.18 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma200_pct | 9.06 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_sma | 5.21 | USD_per_share | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_pct | 3.47 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.drawdown_from_63d_high_pct | -14.26 | percent | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.volume_vs_previous20_ratio | 0.81 | ratio | 2026-11-10 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SKYY/history/ |
| macro.DGS2.value | 4.56 | percent | 2026-11-09 | lagged | source_series_v1:DGS2 | https://fred.stlouisfed.org/series/DGS2 |
| macro.BAMLH0A0HYM2.value | 3.34 | percentage_points | 2026-11-09 | lagged | source_series_v1:BAMLH0A0HYM2 | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| macro.BAMLC0A0CM.value | 0.91 | percentage_points | 2026-11-09 | lagged | source_series_v1:BAMLC0A0CM | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| macro.DGS10.value | 4.88 | percent | 2026-11-09 | lagged | source_series_v1:DGS10 | https://fred.stlouisfed.org/series/DGS10 |
| macro.DFII10.value | 2.66 | percent | 2026-11-09 | lagged | source_series_v1:DFII10 | https://fred.stlouisfed.org/series/DFII10 |
| macro.T10YIE.value | 2.20 | percent | 2026-11-10 | ok | source_series_v1:T10YIE | https://fred.stlouisfed.org/series/T10YIE |
| macro.STLFSI4.value | -0.52 | index | 2026-10-30 | lagged | source_series_v1:STLFSI4 | https://fred.stlouisfed.org/series/STLFSI4 |
| macro.CBOE_VIX.value | 19.46 | index | 2026-11-10 | ok | source_series_v1:CBOE_VIX | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| macro.GPRD.value | 113.95 | index | 2026-11-02 | lagged | source_series_v1:GPRD | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_ACT.value | 129.82 | index | 2026-11-02 | lagged | source_series_v1:GPRD_ACT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_THREAT.value | 108.29 | index | 2026-11-02 | lagged | source_series_v1:GPRD_THREAT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA7.value | 158.85 | index | 2026-11-02 | lagged | source_series_v1:GPRD_MA7 | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA30.value | 184.74 | index | 2026-11-02 | lagged | source_series_v1:GPRD_MA30 | https://www.matteoiacoviello.com/gpr.htm |
| quotes.SPY.value | 756.60 | USD_per_share | 2026-11-11T12:03:26+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SPY |
| quotes.QQQ.value | 687.97 | USD_per_share | 2026-11-11T12:03:20+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| quotes.SMH.value | 507.48 | USD_per_share | 2026-11-11T12:03:23+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SMH |
| quotes.NVDA.value | 175.35 | USD_per_share | 2026-11-11T12:03:28+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| quotes.MSFT.value | 535.00 | USD_per_share | 2026-11-11T12:03:25+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/MSFT |
| quotes.AMZN.value | 271.78 | USD_per_share | 2026-11-11T12:03:25+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AMZN |
| quotes.GOOGL.value | 290.33 | USD_per_share | 2026-11-11T12:03:07+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GOOGL |
| quotes.META.value | 647.23 | USD_per_share | 2026-11-11T12:02:03+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/META |
| observed.SPY.price | 756.60 | USD | 2026-11-11T12:03:26+00:00 | ok | 独立分钟最后非空close；非VWAP/结算。各自观测时点，盘前不得比全天成交量；TNX直接百分数，债市假日旧值。 | https://query1.finance.yahoo.com/v8/finance/chart/SPY |
| observed.QQQ.price | 687.97 | USD | 2026-11-11T12:03:20+00:00 | ok | 独立分钟最后非空close；非VWAP/结算。各自观测时点，盘前不得比全天成交量；TNX直接百分数，债市假日旧值。 | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| observed.SMH.price | 507.48 | USD | 2026-11-11T12:03:23+00:00 | ok | 独立分钟最后非空close；非VWAP/结算。各自观测时点，盘前不得比全天成交量；TNX直接百分数，债市假日旧值。 | https://query1.finance.yahoo.com/v8/finance/chart/SMH |
| observed.AMD.price | 554.50 | USD | 2026-11-11T12:03:34+00:00 | ok | 独立分钟最后非空close；非VWAP/结算。各自观测时点，盘前不得比全天成交量；TNX直接百分数，债市假日旧值。 | https://query1.finance.yahoo.com/v8/finance/chart/AMD |
| observed.NVDA.price | 175.35 | USD | 2026-11-11T12:03:28+00:00 | ok | 独立分钟最后非空close；非VWAP/结算。各自观测时点，盘前不得比全天成交量；TNX直接百分数，债市假日旧值。 | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| observed.MSFT.price | 535.00 | USD | 2026-11-11T12:03:25+00:00 | ok | 独立分钟最后非空close；非VWAP/结算。各自观测时点，盘前不得比全天成交量；TNX直接百分数，债市假日旧值。 | https://query1.finance.yahoo.com/v8/finance/chart/MSFT |
| observed.AMZN.price | 271.78 | USD | 2026-11-11T12:03:25+00:00 | ok | 独立分钟最后非空close；非VWAP/结算。各自观测时点，盘前不得比全天成交量；TNX直接百分数，债市假日旧值。 | https://query1.finance.yahoo.com/v8/finance/chart/AMZN |
| observed.GOOGL.price | 290.33 | USD | 2026-11-11T12:03:07+00:00 | ok | 独立分钟最后非空close；非VWAP/结算。各自观测时点，盘前不得比全天成交量；TNX直接百分数，债市假日旧值。 | https://query1.finance.yahoo.com/v8/finance/chart/GOOGL |
| observed.META.price | 647.23 | USD | 2026-11-11T12:02:03+00:00 | ok | 独立分钟最后非空close；非VWAP/结算。各自观测时点，盘前不得比全天成交量；TNX直接百分数，债市假日旧值。 | https://query1.finance.yahoo.com/v8/finance/chart/META |
| observed.GLD.price | 370.71 | USD | 2026-11-11T12:02:14+00:00 | ok | 独立分钟最后非空close；非VWAP/结算。各自观测时点，盘前不得比全天成交量；TNX直接百分数，债市假日旧值。 | https://query1.finance.yahoo.com/v8/finance/chart/GLD |
| observed.CRWV.price | 56.07 | USD | 2026-11-11T12:03:24+00:00 | ok | 独立分钟最后非空close；非VWAP/结算。各自观测时点，盘前不得比全天成交量；TNX直接百分数，债市假日旧值。 | https://query1.finance.yahoo.com/v8/finance/chart/CRWV |
| observed.CL_F.price | 86.66 | USD | 2026-11-11T11:53:27+00:00 | ok | 独立分钟最后非空close；非VWAP/结算。各自观测时点，盘前不得比全天成交量；TNX直接百分数，债市假日旧值。 | https://query1.finance.yahoo.com/v8/finance/chart/CL=F |
| observed.BZ_F.price | 92.75 | USD | 2026-11-11T11:53:21+00:00 | ok | 独立分钟最后非空close；非VWAP/结算。各自观测时点，盘前不得比全天成交量；TNX直接百分数，债市假日旧值。 | https://query1.finance.yahoo.com/v8/finance/chart/BZ=F |
| observed.GC_F.price | 4,055.60 | USD | 2026-11-11T11:53:36+00:00 | ok | 独立分钟最后非空close；非VWAP/结算。各自观测时点，盘前不得比全天成交量；TNX直接百分数，债市假日旧值。 | https://query1.finance.yahoo.com/v8/finance/chart/GC=F |
| observed.TNX.price | 4.98 | percent | 2026-11-10T19:59:00+00:00 | lagged | 独立分钟最后非空close；非VWAP/结算。各自观测时点，盘前不得比全天成交量；TNX直接百分数，债市假日旧值。 | https://query1.finance.yahoo.com/v8/finance/chart/^TNX |
| observed.VIX.price | 18.63 | index points | 2026-11-11T11:48:16+00:00 | ok | 独立分钟最后非空close；非VWAP/结算。各自观测时点，盘前不得比全天成交量；TNX直接百分数，债市假日旧值。 | https://query1.finance.yahoo.com/v8/finance/chart/^VIX |
| observed.DX-Y.NYB.price | 102.52 | index points | 2026-11-11T11:53:36+00:00 | ok | 独立分钟最后非空close；非VWAP/结算。各自观测时点，盘前不得比全天成交量；TNX直接百分数，债市假日旧值。 | https://query1.finance.yahoo.com/v8/finance/chart/DX-Y.NYB |

## 指标历史比较（不同日期观测，非连续交易日）

```json
[
  {
    "id": "prices.SPY.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.77001953125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -4.42999267578125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.734432628594452,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.6671783407775189,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.6657101918225883,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.401930180644162,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.3448531047723913,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.43499075229712636,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.10226566899722567,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.5291777986665025,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.4045013427735284,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -7.405999755859398,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.30459960937491815,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.8453869628906432,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.3127954101562409,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.652017822265634,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.1817889281249041,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.37380372428359454,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.3231002862372767,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.3418493448315796,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.4247448440864998,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.8437404881295629,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.1278599330357153,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 3.5871494838169653,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.022928183000730407,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.485009057500535,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.3555454999764618,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.5686111390311832,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.2290950696996964,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.01290927876067105,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -4.5899658203125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -10.52001953125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -4.2193080867572235,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.2908315218130961,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.279661343303773,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 3.452029275569845,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.3148043498774058,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.5372114323575659,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.47658401960389885,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -2.6162919463901044,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.484875458162771,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.6236531810355772,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.6139511514811846,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.050099094925683,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.030048754894984597,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.9722021846546918,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.5788496886011245,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -2.0871141477236024,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -3.4404998779295966,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -19.849002075195244,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.8250781250000045,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -4.469145507812527,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.25711425781253183,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.3321481323241642,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.181400074728566,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.1918333073479337,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.5299655714270379,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.8742996435410655,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.7124031660658448,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.7438885501029233,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.2557155064174097,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 3.330718994140625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.05553596197472066,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.5266968185919239,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.6042131983488357,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.3848326755592328,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.3447484963820895,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.1345552149220952,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.930023193359375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.78997802734375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -3.9133360677367723,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.9160257094186108,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.9249309275168871,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.42153733194383314,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.2566444764001252,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.9531618478222823,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.3219126408078097,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.9943070803548171,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.1789034391423203,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.24884736864109192,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.2592207356942988,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.9803928487003288,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.08820862837226606,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.388152600119408,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.42417830980503624,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.4651292816883146,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.193998718261696,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.14749908447265625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.2516864013671807,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.8402941894531182,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.09189414978027344,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.35882308959963893,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.7674294960066552,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.2312058562005337,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.5960789377045472,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.9265188677590963,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.7272749681890067,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.15407446082331688,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.1571415492466519,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.3564278738839284,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.06830370163714305,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.47956146259105514,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.6342600304659056,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.2596090499919379,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.312017364582165,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.10598623988198841,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.0699920654296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.6200103759765625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.2996684481335294,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.2956252581175711,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.29790386534405133,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.06106833228227693,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.08626189996827627,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.28989704714594833,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.8609813433584246,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.47849139002636987,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.4347641804609226,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.96280359889509,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.9636140571666396,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.462998512926439,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.2585912048041159,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.7248877994430751,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.7587156743611989,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.0076691886928724,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.37900009155274006,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.8040000915527514,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.04623199462892558,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.06380676269529317,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.11997413635253906,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.5833397674560672,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.20952843599211235,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.09835228435914889,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.05479813429383196,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.785239895037626,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.09545958464949322,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.4829777864208351,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.07071467808314713,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.8135692051478793,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.03243938435358262,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.36091679540540555,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.031340198296614385,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.10861215526243306,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.32249023798469467,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.3849658840154019,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -10.170013427734375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 10.0999755859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -4.5614144519409265,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -2.0187780447450066,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.132680532290787,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 6.3086921707174115,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.5397131900200542,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.7939938856699538,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -3.442934834313826,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.841517182857288,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.826981823346474,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.3515997039674876,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.4669703404681989,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 4.9067619900732495,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.194860085247663,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 3.22898463796708,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -3.5452005033110523,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.3706949815237905,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.6155014038085938,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.6755020141601449,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.7812005615234057,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -4.3982019042968545,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.47670013427733693,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.9296504211425827,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.56506661155127,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 3.147657026388462,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.450177066518755,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 3.694694646543439,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.370934893089892,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.8709031443583957,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.5985739571707587,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.7878570556640625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.2126385442849672,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.4400265711630802,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.3757827583635436,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.359421452829757,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.042250072503778324,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.16943247578929588,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -84.300048828125,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 89.800048828125,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -3.0206582178954555,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.3132574192279978,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.3712815412972867,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 5.572537290677526,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.7054386494061435,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.370500608636405,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.638809458084623,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.9311341654659753,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.2862255893010035,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.6460790784504788,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.7055713494746985,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 4.170607110033364,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.3605855446337523,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.8054913609335315,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.7410751270818494,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.4603119641324778,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -7.354992675781432,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -23.79000244140616,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -9.0260009765625,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -52.34199707031257,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -5.261500244140734,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -20.864000244140698,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.8890822614833658,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.7693729160296887,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.7921321475045437,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 3.2791513809539596,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.7695432758002116,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.4047195180195597,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 6.935703822544639,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 19.43570382254464,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.217124417227756,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.4392314470314631,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.7944580938508707,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.91153417688259,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.046487722575702106,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.005207332517113805,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.80999755859375,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -10.049995422363281,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 3.4491760917307763,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.5490581558861507,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.4962608160919757,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -6.6451214252619355,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.2540880736394246,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -16.039349966025195,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -3.577995342732887,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -15.174956241179125,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 6.183608720325228,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.11812018489136822,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.16944937573061303,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -8.047051605906098,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.9092349688670343,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -15.604359213728069,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -3.6802610117301118,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -14.645778442512622,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.4049999237060433,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.8569995880126839,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.0055999755859375,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.5015998840332117,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.12704999923705884,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.7017000007629406,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.4625147348534693,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -9.469829343044445,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.8531276649300654,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -11.049828787198223,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.0712479415756704,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -12.386667998806544,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.1771425519670755,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.1499998910086493,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.15269245764183825,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.41887074980013494,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.7653761169604927,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -9.496357600377747,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.15147047546799053,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.2908401144385311,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.0800018310546875,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -12.110000610351562,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 4.681563975476976,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.049956475936918654,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.04463775125816838,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -2.6621447913535476,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.2334586410983377,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -16.43810460613191,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -3.892952863435095,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -17.420763800430496,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 7.415996604071429,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.6172218648406003,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.6210724405644186,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -4.0640749719977105,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.1113944636740527,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -16.003113853834783,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -3.9952185324323204,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -16.891586001763994,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.7100002288818388,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -2.3125,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.01999999999999602,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.5874002075195364,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.12950000762938885,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.7480000686645525,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.4390712107483985,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -9.269212845659125,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.0526072310864993,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -12.174605593186438,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.2907783652574611,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -13.82874049307632,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.0035716465541293374,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.814999171665737,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.07640847114645766,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.513568439978756,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.9180566445580212,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -10.294118219297745,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.22536699875403476,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.25877697785897014,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.0800018310546875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.23000335693359375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.366547451485678,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.5591195033946228,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.5649788391258515,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.35344694732607485,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.8068549107964404,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.7532575532692274,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.4840310275111559,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.9841015285965704,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.367885177108774,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.10805883738289612,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.10073135269673683,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.0484832333180871,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.4620018060240483,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.3182668009721006,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.5862966965083816,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.513279327263073,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.12549972534179688,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.9514991760253935,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.019904937744144036,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.24140701293944744,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.022460517883303055,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.3701522064209115,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.4896008859832888,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.4729995939320562,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.3214254854981178,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.01675714690014818,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.2727522971503702,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.15594379079868492,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.05642809186662945,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.02857262747628342,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.08180069535287549,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.03243969299326677,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.3040692953670274,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.11514123932886422,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.28219280616389086,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.2430246222223198,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.18000030517578125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.1399993896484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.1705949022774331,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.4486775901386464,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.4480589236705024,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.8603394396883957,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.9972254416756088,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.06733906604841078,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.6772472560668596,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.6449645540802074,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 3.905027530871885,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.1158559309161653,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.1137691154930907,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.5415907409557663,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.3420785464480005,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.5023298183455376,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.5749815870696349,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.1741423527467099,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.00649995803833292,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.006000137329099431,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.02059997558593807,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.09579990386962933,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.011849994659424823,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.04874999046325712,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.5983051580189191,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.5034585369939837,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.5542850955762901,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.14942324255518002,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.5992574559804398,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.3193469105116309,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.011428696768624444,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.022857121058872762,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.03681618103959483,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.07674471434042007,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.5492614212897151,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.4119427921109753,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.5863176868120211,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.10760360048436635,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.3300018310546875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.1999969482421875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.7883056820659484,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.542809358806895,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.5465465409972614,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.0587665621808129,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.16789202084772636,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.4920505028509714,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.29528808920981087,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.527276650026054,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.9461269465285036,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.12436898197062396,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.11916365082532687,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.3431636184633491,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.17696108392466492,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.9270412551480978,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.39755375820703653,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.0564544486925564,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.00450019836425497,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.039500045776364345,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.03686813354492813,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.3528559875488355,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.002385025024409515,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.31126544952392976,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.43343602900303146,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.2080599309865816,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.3779924254870948,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.7073414799370181,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.4206839464614309,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.6502846654803718,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.01714324951171875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.03357097080775667,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.024028493967619746,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.04244384108154342,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.4170253234853094,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.6836365357610452,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.17549294691374495,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.14892533438866395,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.7900009155273438,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.15999603271484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.8886861811355007,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.764398252841858,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.7713995640537208,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.7103475927756842,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.7405079564364092,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.2499755837262807,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.35850703611339796,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.8196299976229171,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.8457464474589513,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.09721991206433911,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.1056893722311325,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.6915825878684778,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.3956548516640179,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.1850151685708461,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.4607727051106236,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.3488077962894196,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.06649971008300781,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.5064994812011747,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.028631896972655113,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.3575440979003872,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.01603836059570085,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.4612015151977573,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.8250592171647142,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.3352155102155141,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.7347060968388996,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.4988528613092513,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.7319971832701833,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.5771363739775714,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.04142815726143967,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.010714939662388456,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.04402738725696298,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.011239647396182217,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.7455926672166879,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.571565681071462,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.207067972903353,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.18380783024500935,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.46000099182128906,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.3700008392333984,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 19.999648290755978,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.7962409695254857,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.7614556040225864,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -25.469746903450684,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -3.527055710501447,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -11.334734051243121,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -8.285382910455485,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -13.468463021579225,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 22.734080919350433,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.1290626287479668,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.09574541219999855,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -26.871677084094845,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -3.182202605729053,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -10.899743298945992,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -8.587775327640315,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -13.287492470601059,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.20949993133545064,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.6999999523162863,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.06239997863769631,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.6879999732971172,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.01554999351501607,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.14614999294281006,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -3.5226145355697236,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -17.563849466435897,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -3.119949087840567,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -13.135003609159156,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.5873092199190326,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -8.337319262601085,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.08928571428571441,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.0878573145185197,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.8926259326934058,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 6.488279234083933,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.6323668801976545,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -29.430934914827077,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.21000099182128906,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.6300010681152344,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 14.236703219525392,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.5205784144702186,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.5102990083071246,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -11.64869264390347,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.3635036265500453,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -5.656186601972912,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -4.543566984380654,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -3.661984116584893,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 16.971135848119843,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.1877567552477375,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.1760092001297129,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -13.05062282454763,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.0186505217776514,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -5.221195849675784,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -4.64583265337788,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -3.1328063179183907,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.13400001525878835,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.0489999771118157,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.062199974060060725,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.43340000152587876,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.007849998474121378,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.06414999008178768,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.7059099703858438,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -8.744659765228068,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.4537453412541081,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -5.872779719625476,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.0581446645334225,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -3.3812656528375395,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.0528571265084401,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.6614285877772739,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.3568594359401711,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 3.413599333231896,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.8219217146460025,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -17.68944371407152,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.8000030517578125,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -10.770004272460938,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 17.451261269764483,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.9503208714948697,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.8709504873583906,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -18.021908462260384,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.370335689345504,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -16.86357568807251,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -9.631709313831017,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -13.210122711885486,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 20.185693898358934,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.6174992122723886,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.5366606791809794,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -19.423838642904546,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.025482584573112,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -16.42858493577538,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -9.733974982828242,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -12.680944913218983,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.5625,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 5.768500518798831,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.20679992675781023,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.3134002685546875,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.015600013732907314,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.12540000915528537,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.251580196455582,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -16.47076526272464,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.126309915210345,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -14.198777553337582,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.8023977781383316,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -11.015614527635886,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.2878570556640625,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 3.42714364188058,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.5768357749905615,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 4.750475248979416,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.3334343125491337,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -25.63788999425477,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 6.4499969482421875,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -7.540000915527344,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 14.820910235137163,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 7.890341175236526,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 6.786151369914096,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -9.68796536741966,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 4.117443699994572,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 3.431616993612497,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 8.645181363394933,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -5.949503890347721,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 17.555342863731617,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 8.557519516014045,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 7.451861561736685,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -11.089895548063822,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 4.4038971525884545,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 4.398948105084754,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 8.810451624771282,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -4.98946709515684,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.43299980163574503,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -2.251999664306652,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.4291999816894503,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.1361997985839736,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.18090000152587038,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.8297499847412126,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 6.954838380849459,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -5.3969007736170855,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 6.470229214051959,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -10.555199650619329,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 7.934100792921896,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -10.918437037143768,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.15642874581473176,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.1278561183384488,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.27430630205797346,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.5869015806999247,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 5.677814291266515,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -6.637324838736692,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -9.779998779296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -37.80000305175781,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.203524285885604,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -7.765178885841284,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -6.712489626623828,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -13.12628791091418,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -5.039734978432222,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -12.488412484333733,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -4.298374925393912,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -19.971481327591142,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.5309083427088481,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -7.098000545063765,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -6.046779434801241,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -14.528218091558342,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -4.694881873659828,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -12.053421732036604,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -4.400640594391138,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -19.442303528924644,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.9815002441406477,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -11.806999969482433,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.0328646850585983,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -3.4374554443359386,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.08572334289550554,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.011456909179685226,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -3.5081346449318485,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -12.903607528096527,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -4.100307820511894,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -15.86979218266674,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -4.75126425225446,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -18.49993291963383,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.5042855398995538,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.682143075125558,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.5833127768431599,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.3035552666814807,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -4.087944555567368,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -15.800034352046488,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.7937170268502007,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.2052645870506677,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -12.02001953125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 12.16998291015625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -4.950677705058604,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -4.939831927211181,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -5.169192468909123,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 4.2819989928118085,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.638170045708399,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.32346791951386455,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.9473917962493861,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 8.058960377441249,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.2162450764641517,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -4.272653586433661,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -4.503482277086535,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.8800688121676465,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.293316940936008,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.1115228327832618,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.8451261272521595,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 8.588138176107751,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.5145019531249773,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.4319946289062955,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.5173992919922057,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 3.7343981933593113,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.32922302246095114,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.145456695556618,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.1639055472200575,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.026275045011383,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.4266934618308422,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.619412222132799,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.82734775292284,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.187228072704549,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.753570556640625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 4.285718645368306,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.2097384395145956,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.7468421759275761,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.162651996265852,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.05944843316640913,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.04852903570762079,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.14714046960496396,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 3.94000244140625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 20.17999267578125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.466496259587391,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.5839645584269526,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.6217944624267826,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 9.001973833111656,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.9015788757422492,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 6.9379117565882,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 2.0289444210818353,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 13.511412262979384,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.267936369007061,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.08321378235056631,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.043915729395806125,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 7.600043652467493,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 2.2464319805146413,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 7.372902508885327,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.9266787520846105,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 14.040590061645887,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.614500427246071,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.4409988403320142,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.2220001220703125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.39079956054689546,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.16224998474120866,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.745549850463874,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.2911644671418143,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 7.348019432629815,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.4582707748327817,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 7.787315087969593,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.540510623698065,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 7.948049267514534,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.11928667340959898,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.3278590611049115,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.013490335809647203,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.6112961574951492,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.1309511018834697,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 9.85292324690179,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.2796131652573518,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.10079280896085852,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.769989013671875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 7.350006103515625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.45058603510404,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.6399944195019769,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.6585522582479575,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 15.273666473516434,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.46241736884085327,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.6888211575779764,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.23642797484534128,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 5.218365047288529,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.283846593490412,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.027183921275542033,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.007157933574630793,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 13.87173629287227,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.11756426406846288,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.1238119098751032,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.13416230584811473,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 5.7475428459550315,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -3.3199996948242188,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -16.25700073242183,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.0350402832031023,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -5.652760009765643,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.2261648559570517,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.0355599975586074,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.7316430054882801,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 6.840128891531371,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.039020687273870536,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 3.6455585025842563,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.1705342195755577,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.4213311885222346,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.2542855398995538,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.0985674176897327,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.07763812614664678,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.2880927800478119,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.21691664394849397,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.633312036759495,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.2228072962776254,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.3071556091807469,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.02001953125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 20.3599853515625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -5.113648187209052,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -2.3537835610004,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.430874643429015,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 3.1429753452643094,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.209589913348287,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.06653576061602529,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 3.9969933080240114,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 8.346022690035415,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.3792155586146,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.686605220222881,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.7651644516064269,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.7410451646201475,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.8647368085758966,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.5015265129131503,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 3.894727639026785,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 8.875200488701918,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -6.055499267578057,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -26.916998291015602,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.3900268554688182,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 5.252028808593764,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.14621643066402612,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.2981680297850744,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.9095577514711572,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 6.906528056930117,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.19171010508243214,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.2891692498996914,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.02672604741125184,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 3.2734926881438198,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.839996337890625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.0771440778459827,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.13108536330700504,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.05130343270419502,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.0025745612158836195,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.6183444550976525,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.2366332780779099,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.062122826396279085,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.25,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -5.010002136230469,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -6.070752787641032,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -7.668936931175596,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -6.989663484304087,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.46413379343416317,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.600251935239129,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 4.035547010528617,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.5606969112700355,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -14.964916663532705,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -3.3363201590465796,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -7.001758590398078,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -6.323953292481499,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.9377963872099997,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.9451050400115193,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 4.470537762825742,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.6629625802672621,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -14.435738864866202,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.4539999008178697,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -8.69950008392334,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.7231999969482388,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -3.915600204467765,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.2478999900817911,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.1808000373840315,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.7456955184643839,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 3.874687956567122,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.3010936619229767,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -3.121325335796911,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.12821701084867954,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -4.806568659048409,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.09342847551618316,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.8620003291538785,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.13398876135237536,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.5673100752896758,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.3807550147915606,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -4.037700371735738,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.5152521160375442,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.6309566905478511,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -8.0400390625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -129.989990234375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -7.350269814006416,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -3.6770420889370437,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -3.1526412983797343,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -7.270721706384288,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.9447876105340498,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -5.712895421268172,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -3.785060510386497,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -27.650212758282557,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -4.615837185411964,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -3.0098637481595247,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.4869311065571473,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -8.67265188702845,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 2.2896407153064438,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -5.277904668971043,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -3.8873261793837237,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -27.121034959616054,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -11.396502685546807,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -74.71941833496089,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -4.669382324218759,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -21.95461303710931,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.6815249633789335,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 8.304340820312518,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.1878654463247198,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -7.165746037534483,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.46857124685259066,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -11.620837491201785,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.2720477386838684,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -18.350071037966856,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.5007149832589235,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 9.543566022600444,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.15997695365184583,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.386957371552189,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.732766350956183,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -11.84724229128997,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.1339969417947745,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.1251186469817862,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.1399993896484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -7.0,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -9.06606175679271,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -5.578317178540637,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -4.89215129924203,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -8.992820381256594,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.5590941099101414,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -3.12889158250643,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -5.593132633824336,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -28.752479232703305,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -6.331629128198257,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -4.911138837763119,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -4.2264411074194435,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -10.394750561900757,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.9039472146825354,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -2.6939008302093015,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -5.6953983028215625,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -28.223301434036806,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.6100000381469712,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -3.8930000305175767,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.3252000427246102,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.5672001647949187,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.2875209892290407,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -7.139712656758556,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.6470870771794743,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -10.468865436657314,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.0071430206298828125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.43642861502511154,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.2406255745846515,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.1198119233875525,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.7918884136873174,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -11.002829483688927,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.16660757501559287,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.2540417800169248,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -6.25,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -41.75,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -12.74799202628113,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -8.348673912241821,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -7.092675597407794,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -30.83542984417732,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.9032901087540957,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -11.367975902452143,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.8087495133965454,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -20.95317148016136,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -10.013559397686679,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -7.681495571464303,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -6.426965405585207,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -32.237360024821484,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.5584370039817053,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -10.932985150155016,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.911015182393772,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -20.423993681494856,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.1534996032714844,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -12.490999603271462,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.2887316894531295,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -6.88980377197268,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.06557662963865596,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.2948133087158453,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.005831157786286,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -13.562644383091083,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.1975213441500117,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -14.92837843009164,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.3217159735150155,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -15.4843401544673,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.31892830984932985,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 3.706428527832033,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.14856190027935234,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 3.3166592560098733,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.1275293888370577,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -14.211896317431538,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.10950702415542912,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.059838359438160404,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.970001220703125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -7.5999908447265625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -4.8799410956924305,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -2.4672826547775584,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.388585832058021,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.5442712902924987,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.9681987824919691,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.3255481910513964,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.182966703141453,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -5.991314601426012,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.1455084670979785,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.8001043140000395,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.7228756402354328,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.1423411096483362,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.6233456777195787,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.8905574387542714,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.2852323721386796,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -5.46213680275951,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.368499755859375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -7.358998870849604,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.34745208740235967,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.6178268432617244,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.11677486419677052,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.6215192413330044,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.3797543445732803,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.38691537940178655,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.8811793950887594,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -3.2448589112432975,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.2266946645135057,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -4.846637682275512,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.09714290073939758,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.8599995204380582,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.09655704656264774,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.6355277466192777,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.9752481290609563,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -3.7623717053101853,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.42660092512202585,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.2973619913268465,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.2700004577636719,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -4.470001220703125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.08340496154766175,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.2834896532462725,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.19225175458344,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -4.4605899644555524,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.2598548145074213,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -12.021671306479387,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.6435105447384237,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -11.45989708658729,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 2.6510276670467903,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.9506679940237914,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.8579619464060277,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -5.862520145099714,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.91500170973503,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -11.58668055418226,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.7457762137356494,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -10.930719287920788,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.24949989318847088,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.7985000610351562,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.027441329956047866,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.012960739135735366,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.06973247528076598,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.35992685317993534,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.7515787687585869,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -5.52182232193349,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.45618717948607834,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -6.864592669963643,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.3344162404183004,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -8.313662989576898,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.06214305332728798,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.31714194161551346,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.08712460973271252,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.6786656568329597,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.3856047853587068,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -6.383892366475507,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.21565239057389485,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.05318038326505148,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.2999992370605469,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.1000022888183594,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.9347383443231161,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.1601415051843644,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.17637015996499,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.4208875878066509,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.9892049379522483,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.44200959806379725,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.5307592961649519,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.313712894898301,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.799694284271336,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.8273198459618833,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.8420803517875783,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.8228177684508133,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.3340580427246405,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.8770003503609232,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.4284936271677258,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.842890693564803,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.17350006103515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.8780002593994141,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.015670547485349573,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.018073196411130255,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.02762701034546211,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.13207849502563818,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.2149179948832236,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.3502979603897449,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.5078190678843075,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.9356585379315172,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.5041172242062455,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.7893898845889877,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.004999705723353953,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.26857130868094314,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.0004182452742680365,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.436002197095247,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.506755461476871,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.45668475762484784,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.20124164428477853,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.09551686617546773,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.160003662109375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -2.5900115966796875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -3.918431318436544,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.0434158647834035,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.0286160240054243,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -3.536576681230885,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.18927745558989795,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.18710058200545054,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.00647947959570061,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -2.252860805704982,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.1839986898420918,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.3762375240058846,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.362905832182836,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -4.938506861875048,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.5341305603622892,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.6220913343025769,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.09578618940152595,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.7236830070384794,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.0029998779296818157,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.5544990539550838,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.11861175537109148,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.104098815917979,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.028255767822258804,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.07376228332518053,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.09733103301046153,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.208803977068862,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.02460217954214361,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.8744951855404803,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.10864739526929013,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.542057104949357,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.01928601946149522,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.7007162911551337,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.013384857284667095,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.4403761158914259,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.08601881684178103,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.3924039626078244,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.4373836556332449,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.6746125156976495,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.5500030517578125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 4.8600006103515625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.6181302833939037,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.6062360156010582,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.6204348835855855,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.06018336113358114,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.8279899817766676,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.196270886713922,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.546872407506104,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 3.832975648956239,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.1163023452005483,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.2734143563785771,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.2861450754081738,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.4621135417777427,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 2.172843086549058,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.6312616390110488,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.44460673850887744,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 4.362153447622742,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.9610000610351506,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 4.357500457763678,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.3798040771484352,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.5551376342773438,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.16358207702637628,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.7934758758544831,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.24815721323170337,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.18699657572966988,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.0792523536957006,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.839740931907107,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.22408095357515734,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.478976850072769,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.02285657610212022,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.6828558785574774,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.006272018673777691,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.31804332372641153,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.28999422183797474,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.048516002556397986,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.1123061211718892,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.39289253977832905,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.1399993896484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.0800018310546875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.7451663056376345,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.223837736976786,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 2.2723397132223377,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.2729953077188263,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.44766560810087785,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.6163477515658045,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.9359067852094745,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.808517410582457,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.9892663229568175,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.891016077754305,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 2.938049905044926,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.1289348729253361,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.7925187128732691,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.18135699926867943,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.8336411162122488,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 3.3376952092489596,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.3419998168945284,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.9020000457763615,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.13210479736328296,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.5937686157226523,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.04907405853272451,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.2511603546142567,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.2383529663934736,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.14893153200021825,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.0014869292036756576,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.7094420801766264,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.1034531642386991,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.1603507619260887,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.025714874267578125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.29999978201729904,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.02522235482841917,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.290662217836281,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.1522725537642433,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.0800261629779317,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.336139870899104,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.8012709896530983,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.04000091552734375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 3.720001220703125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.8841071215053082,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.7354947763227093,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.7585632239412554,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.5421307689025499,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.05073842020915098,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.712588425977369,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.308628698831238,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 5.65087296331741,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.14967449291085622,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.4026731171002282,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.4242734157638437,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.14020058825838788,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.2941146845632403,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 3.147579178274496,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.2063630298340122,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 6.180050761983912,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.4345001220703182,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.953000640869135,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.09432449340820881,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.3221032714843801,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.0025712585449326752,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.02609931945801236,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.3568624318951441,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.4751408792296417,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.05349484542549465,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.984467390627832,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.037103765440060776,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 3.2552483544204813,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.0035711015973771687,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.6799997602190291,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.0036694651994464422,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.5106579485853171,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.03269918656797488,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.8488503497982802,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.1220647796772939,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.5873996575166688,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.40000152587890625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 6.319999694824219,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.0799441225717086,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.8043605748357718,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.8513027378444171,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 8.296318749371245,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.35584331130088565,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 5.119000295726682,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 2.195068462369043,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 6.551174394635039,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.6544885060227434,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.13718223405825292,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.18559254602182929,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 6.8943885687270825,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.010990206528494362,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 5.553991048023809,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 2.0928027933718174,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 7.080352193301542,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.2259998321533203,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.4114997863769503,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.0666772460937608,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.6119004821777452,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.044730720520021805,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.22319461822509368,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.5934727675954043,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 7.226428463027146,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.42484548198630234,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 6.284826233879159,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.3954646218756519,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 5.82371094389631,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.006071363176618494,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.44785744803292404,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.013549347293481784,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.30949284545286826,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.34858520773761725,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 5.507625006382765,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.2373345415579512,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.182238006639695,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.060001373291015625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.3100013732910156,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.6672776869246952,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.4354546904198564,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.4391654098639508,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.6162611438942145,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.7462423960918008,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.048440635837955,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.15612628648639104,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.7033755663133476,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.0671549416697568,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.1026330311973753,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.104875601686539,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -2.0181913245383765,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.4013892913194095,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.6134498835408291,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.053860617489165374,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.1741977676468451,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.09300003051757955,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.5215000152587876,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.03616493225097628,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.08338096618652457,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.00868267059326655,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.03908994674682731,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.36342892692520223,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.5283963690083215,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.23469408592631247,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.5344434417534849,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.15660348456996154,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.6185870869339638,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.00571441650390625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.05428559439522873,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.015075068895845423,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.1144704594828414,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.136408386015352,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.704763652459639,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.4431725524666257,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.3474892684414793,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.05999755859375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.910003662109375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.588947202270985,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.20314460994876882,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.20765687301016467,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.8143893823409298,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.0856759207328528,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.3211878822937164,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.8410167061332574,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.09563560325594,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.145485426323467,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.4640337308287501,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.4580533188124236,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -2.2163195629850923,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.4305290255052441,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.7561786345908423,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.7387510371360317,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.6248134019224425,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.13750000000000284,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.7930000305175824,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.016763763427739775,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.016144638061525995,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.02164825439453466,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.1046960067749012,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.47219176753314773,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.2089638445781805,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.18275869764259323,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.1034382827244347,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.1923812070773856,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.8721289880272218,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.007857458932059136,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.1246427808489119,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.015340248024619196,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.2503555165592575,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.1329733156339885,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.7185870546649884,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.47502958863666445,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.15044519480027563,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.09000015258789062,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.2599983215332031,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.0756784674783146,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.8422896749886952,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.8545505339592983,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.0699258581487348,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.7840404820407043,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.5441907594367912,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.40823306544499616,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.2875992911228216,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.6587541611161374,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.509468015766214,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 2.5202607257818865,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -2.4718560387928967,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.43918737726831303,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.9791815117339162,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.3059673964477714,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.8167770897893245,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.15649986267089844,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.8565000534057674,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.008027343750001137,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.023197402954096447,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.017271766662595667,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.10075626373291158,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.481795014424069,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.1988494824536344,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.1933670927279696,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.5582840198875116,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.21224368944008365,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.30592400003122133,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.019999912806919706,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.26500020708356586,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.041103170274574774,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.4942298917639165,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.16697615962900647,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.06423619069653164,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.33847899463088527,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.6452187850630812,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -3.779998779296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -34.8900146484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -5.82984528476932,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -2.784148654774976,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.617106099869593,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.343162248307749,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.24025946739115867,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.25376949538505755,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.5086418537407873,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -9.65308862446268,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -3.0954126561748674,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -2.116970313997457,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.9513959080470054,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.0587679323364139,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.10459363738123173,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.6887602476821844,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.6109075227380139,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -9.123910825796177,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -5.2244995117187045,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -31.387002563476585,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.4599999999999227,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -8.146600341796898,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.4240499877929551,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.9647499084471747,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.19158652242230367,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.0862807308485216,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.4475316147524726,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -4.884376543220947,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.7990197638627521,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -7.050441083640536,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.4199981689453125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 4.660709926060267,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.12749758464985916,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.2574276884944346,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.5963083504833229,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -5.504024815378038,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.4190359461661606,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.07580996167331366,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.1299972534179688,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -2.3300018310546875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -3.7229619329242847,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.8595680372701762,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.837831332832729,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 5.889249641504246,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.7717382956776824,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.9496895180897926,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.8896902892913783,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.6102739135926405,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.9885293043298327,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.1923896964926572,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.1721211410101406,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 4.487319460860084,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.426885190905292,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.5146987657926667,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.7874246202941526,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.139451712259143,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.5325000762939425,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -2.555999755859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.19300003051758097,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.6160000610351517,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.007692642211907241,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.0927043914794865,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.5877125900912272,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.08466240708513428,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.8897003746010324,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.6349659866899735,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.2099510849913786,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -2.5843136931238853,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.01714270455496658,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.08785738263811371,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.051054569950452766,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.01597089312993827,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.00292648600524,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -2.067987813012051,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.19632251684283653,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.25856448585689285,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.3700103759765625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -16.0,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.5680102489451277,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.8406174451235158,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.6736816503930996,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -4.109435699543107,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.794998077835551,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -13.784631302549453,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.760880326697444,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -13.184370845477444,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 3.3024428775395798,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.5077957859010347,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 2.3393918422156865,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -5.51136588018727,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.4501449730631606,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -13.349640550252328,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.8631459956946697,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -12.655193046810941,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.2150001525878906,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -4.526500701904297,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.2537911987304824,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.9409249877929824,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.21227409362793992,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.0823013305663949,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.274040205597382,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -6.015507564690314,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.8399863405678332,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -7.89860624449984,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.6736724538882077,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -10.051961006943099,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.21071406773158508,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.1807120186941962,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.09232681105192375,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.920946020906428,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.668754452745679,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -7.8102118287270645,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.4062191264557058,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.3490664392504741,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.25,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -25.779998779296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.5905196112290243,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.660974106046619,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.6188726424876672,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.8830507353103974,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.7429898763535947,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -6.355233100269675,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.3502472995383314,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -9.392151772734959,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.1439130173654277,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.328152446824138,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.284582834310255,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -2.2849809159545598,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.398136771581203,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -5.920242347972549,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.452512968535558,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -8.862973974068456,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.5575012207031023,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -7.304502868652321,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.3970001220703239,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -5.664801025390602,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.07034988403319176,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.49714965820311363,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.05364364265795185,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -4.840333081671633,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.005677912266088825,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -5.152997229113444,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.3294446224487597,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -6.585929139824819,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.105712890625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.7264251708984375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.04394720798167295,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.9904654252207035,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.28631637694026324,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -5.904988678410149,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.040477218178685326,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.24652951840278836,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.6800003051757812,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -143.81999969482422,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.9508798267548153,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.2547346771942127,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.25337127285685046,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -4.417853434447738,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 2.0384700724091154,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.5989177767725247,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.4966338619204151,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.3267176787028383,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.21644719816036329,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.9219130179717316,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.9190814646794387,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -5.8197836150919,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 2.3833231771815058,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 3.0339085290696506,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.3943681929231886,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.8558954773693408,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.21749992370605753,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -137.74349975585938,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.0735707092285196,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -143.28642471313478,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.02624206542969887,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -152.42298183441162,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.6539860052472868,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.3523199572268876,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.0695608189567052,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.452918465137354,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.9285116840553114,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.6427996141217474,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.010951995849609375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -2.9509517124720976,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.04276109611929524,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.561832697313847,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.8065578695701774,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.34793083821629267,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.14525329728914682,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.8205630539024974,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.10000038146972656,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.020000457763671875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -5.998028358628426,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.4828161242471993,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.48876527771582,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 3.082433976243304,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.6443021653818048,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 5.188171603897628,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.10902251380928618,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.6688049307434731,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -3.2635957300339746,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.8156377834696804,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.8230550858932317,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.680503795599142,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.9891552701541961,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 5.623162356194754,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.006756844812059626,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.13962713207697064,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.0755000114440918,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.7872499465942369,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.0490000152587875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.3629000091552719,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.015650005340575035,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.11992500305176179,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.08133161430226021,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.6376593868374654,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.1695449110474705,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.1611521711006434,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.2644910635175135,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.4041808181257762,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.007142884390694659,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.22900009155273438,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.011970001609652225,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.7632578422492049,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.28686282191294765,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.05737365867324229,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.10902125942393992,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.799975216925984,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.3600006103515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.20999908447265625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -2.2214322032637845,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.6627330462101622,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.6679163289808221,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.12518703962429711,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.24321005544563068,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.8252318242847565,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.19357049257507963,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.421217963149601,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.5130004253306675,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 1.329911386987681,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.3336265208034104,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.527117220268459,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.588063160218022,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 2.2602225765818824,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.09130482357785397,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.8920401644830984,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.20149993896484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.9534996032714815,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.0010682678222622144,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.07676574707031136,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.031625957489012535,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.1427242660522552,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.7881294088170065,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.0709844714853922,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.5006850289954068,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.40171761044880405,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.5569464474467711,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.08825719488398942,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.02285712105887283,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.3007153102329798,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.04230369293351455,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.4060418523655869,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.4645848795373668,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.27100620542674925,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.17200786522655365,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.09456768197498988,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.value",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.760009765625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -6.029998779296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_1d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -3.413135537078238,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.429548346416032,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_5d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.3812491780195502,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 5.162471293101012,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_20d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.06114504157842582,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -3.7868375889189565,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_60d_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.2732252023342392,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -4.58975437726502,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_1d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.6787029084837859,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.762370005638513,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_5d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.7155389861969619,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 3.7605411124568495,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_20d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.4059981463508162,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -3.3518468366218306,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_60d_pp",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 1.1709595333370135,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -4.060576578598518,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma20",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.0785003662109318,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -5.443499755859392,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma50",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.30779998779297557,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -1.2916000366211051,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma200",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.11694999694825015,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.6846500396728459,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma20_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.15222457182075821,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -0.5723365561776435,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma50_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.2917684856222227,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -2.942844035685276,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma200_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.646044006157755,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -4.953161115926541,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_sma",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.05714307512555816,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.010716029575893238,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": 0.05542288641252657,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.14107933674643514,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.drawdown_from_63d_high_pct",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -0.43456445095624296,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": -3.447880839579776,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.volume_vs_previous20_ratio",
    "available_prior_observations": 17,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-09",
        "to": "2026-11-10",
        "change": -1.3481518501660614,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-03",
        "to": "2026-11-10",
        "change": 0.022861528428209765,
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
  },
  {
    "id": "observed.TNX.price",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  }
]
```

## 判断依据 · 盘前反弹是否可靠

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 盘前反弹是否可靠 |
| 事实指标引用 | ["observed.QQQ.price", "prices.QQQ.sma200", "prices.RSP.return_1d_pct"] |
| 推断与解释 | 盘前越过关键位属于必要而非充分条件，尚待开盘回踩。 |
| 反证与缺口 | 暂无常规时段VWAP、真实涨跌家数与成交承接；不因盘前触及即追涨。 |
| 确认条件 | SPY755附近、QQQ680–682在开盘后首次回踩守住，形成更高低点；RSP与参与面同步，收盘保持；进一步看SPY760.69的20日线。 |
| 失效条件 | 跌回755/680下且反抽失败则不升级；SPY744.86、QQQ667.05再破明显削弱修复。 |
| 观察期限 | 未来1–3个交易日 |
| 条件式指导 | 等待常规时段回踩与收盘保持，确认后再逐步提高方向风险；失效则撤销升级。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相对晨报新增盘前上涨与CNN34，收盘历史未改变。 |

## 判断依据 · 优先观察哪些板块

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 优先观察哪些板块 |
| 事实指标引用 | ["prices.SMH.return_5d_pct", "prices.XLF.return_5d_pct", "prices.XLV.return_5d_pct"] |
| 推断与解释 | 半导体短期修复增强，金融医疗保留跨期相对强度。 |
| 反证与缺口 | 芯片反弹可能使防御相对表现减弱；没有当期申赎证明。 |
| 确认条件 | XLF守58.26附近再看59.20；医疗/必需消费回踩保持20日线与相对SPY强度。 |
| 失效条件 | 失去支撑且相对收益转弱；信用新数据恶化时金融标签失效。 |
| 观察期限 | 未来1–3个交易日 |
| 条件式指导 | 等待常规时段回踩与收盘保持，确认后再逐步提高方向风险；失效则撤销升级。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相对晨报新增盘前上涨与CNN34，收盘历史未改变。 |

## 判断依据 · AI融资压力是否消失

| 要素 | 记录 |
| --- | --- |
| 评估问题 | AI融资压力是否消失 |
| 事实指标引用 | ["prices.SMH.sma200", "prices.NVDA.drawdown_from_63d_high_pct"] |
| 推断与解释 | 需求改善与融资压力并存；涨幅不能直接证明现金流问题解决。 |
| 反证与缺口 | SMH200日线522.62未收复，NVDA调查与高资本开支尚未消失。 |
| 确认条件 | SMH开盘回踩守490–493；NVDA守170.24并进一步收复178.67；CRWV维持高开区间更高低点，板块相对QQQ同步。 |
| 失效条件 | SMH跌回490–493且反抽失败、NVDA失170.24，或CRWV高开跌回51.02甚至48.73，撤销升级；不要等全部触发才管理风险。 |
| 观察期限 | 未来1–3个交易日 |
| 条件式指导 | 等待常规时段回踩与收盘保持，确认后再逐步提高方向风险；失效则撤销升级。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相对晨报新增盘前上涨与CNN34，收盘历史未改变。 |

## 判断依据 · 恐慌是否已转过热

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 恐慌是否已转过热 |
| 事实指标引用 | ["prices.^VIX.value", "prices.^VIX3M.value", "macro.BAMLH0A0HYM2.value"] |
| 推断与解释 | VIX回落与CNN34支持恐慌缓解，债市假日、旧信用值限制确认。 |
| 反证与缺口 | 暂无常规时段VWAP、真实涨跌家数与成交承接；不因盘前触及即追涨。 |
| 确认条件 | SPY755附近、QQQ680–682在开盘后首次回踩守住，形成更高低点；RSP与参与面同步，收盘保持；进一步看SPY760.69的20日线。 |
| 失效条件 | 跌回755/680下且反抽失败则不升级；SPY744.86、QQQ667.05再破明显削弱修复。 |
| 观察期限 | 未来1–3个交易日 |
| 条件式指导 | 等待常规时段回踩与收盘保持，确认后再逐步提高方向风险；失效则撤销升级。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相对晨报新增盘前上涨与CNN34，收盘历史未改变。 |

## AI需求支持下的芯片修复 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | TSMC月报与CRWV财报支持需求、AMD产品更新 |
| 事实：市场反应 | 盘前SMH约+4.93%、AMD约+7.62%、CRWV约+15.06% |
| 推断：解释 | 推断：需求信心恢复与超跌修复并存，不能从价格识别空头回补占比 |
| 受益篮子 | ["SMH", "AMD", "TSM", "CRWV"] |
| 受损篮子 | ["高融资成本的算力项目"] |
| 反证 | SMH仍低于200日线；收入增长尚不能覆盖全部融资与投资压力 |
| 下一催化剂 | 12日Nebius、17日NVDA及开盘承接 |
| 证据 | ["https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Third-Quarter-2026-Results/default.aspx", "https://www.sec.gov/Archives/edgar/data/1046179/000104617926000796/tsm-revenue20261110.htm", "https://ir.amd.com/news-events/press-releases/detail/1305/amd-showcases-6th-gen-amd-epyc-processors-to-lead-next-era-of-ai-and-enterprise-computing"] |

## 利率约束下的分化 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | CPI已发布；债市11日假日 |
| 事实：市场反应 | MSFT盘前修复弱于芯片，美元仍强 |
| 推断：解释 | 推断：长久期估值尚未全面摆脱贴现率约束 |
| 受益篮子 | ["XLF", "XLV", "XLP"] |
| 受损篮子 | ["高估值长久期篮子"] |
| 反证 | 金融也承受信用风险；今天利率旧值不是压力消退证据 |
| 下一催化剂 | 13日PPI |
| 证据 | ["https://www.bls.gov/schedule/2026/11_sched.htm", "https://www.sifma.org/resources/general/holiday-schedule"] |

## 地缘缓和与航运风险并存 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 俄乌换囚进展、海峡油轮事件报道；部分伊朗声称未独立确认 |
| 事实：市场反应 | WTI与Brent盘前高于晨报截面 |
| 推断：解释 | 推断：不能用外交标题直接推导运输正常化 |
| 受益篮子 | ["能源供应受益篮子（条件式）"] |
| 受损篮子 | ["航空与能源密集行业（条件式）"] |
| 反证 | 油价仍明显低于此前高位；换囚不是全面停火 |
| 下一催化剂 | 双方官方协议、航运通行与损害核验 |
| 证据 | ["https://apnews.com/article/7c8d1024302e0c6ad8be064eec852a64", "https://apnews.com/article/50075bc97e07d41fa3b66fc28858c06b"] |

## tc 报价（供应商时戳不等于成交时戳）

| 标的 | 价格 USD | 变化% | 观测时间 | 供应商时间 | 抓取时间 | 质量 |
| --- | --- | --- | --- | --- | --- | --- |
| SPY | 756.60 | 缺失 | 2026-11-11T12:03:26+00:00 | 2026-11-11T12:03:26+00:00 | 2026-11-11T12:02:51.745Z | ok |
| QQQ | 687.97 | 缺失 | 2026-11-11T12:03:20+00:00 | 2026-11-11T12:03:20+00:00 | 2026-11-11T12:02:51.745Z | ok |
| SMH | 507.48 | 缺失 | 2026-11-11T12:03:23+00:00 | 2026-11-11T12:03:23+00:00 | 2026-11-11T12:02:51.745Z | ok |
| NVDA | 175.35 | 缺失 | 2026-11-11T12:03:28+00:00 | 2026-11-11T12:03:28+00:00 | 2026-11-11T12:02:51.745Z | ok |
| MSFT | 535.00 | 缺失 | 2026-11-11T12:03:25+00:00 | 2026-11-11T12:03:25+00:00 | 2026-11-11T12:02:51.745Z | ok |
| AMZN | 271.78 | 缺失 | 2026-11-11T12:03:25+00:00 | 2026-11-11T12:03:25+00:00 | 2026-11-11T12:02:51.745Z | ok |
| GOOGL | 290.33 | 缺失 | 2026-11-11T12:03:07+00:00 | 2026-11-11T12:03:07+00:00 | 2026-11-11T12:02:51.745Z | ok |
| META | 647.23 | 缺失 | 2026-11-11T12:02:03+00:00 | 2026-11-11T12:02:03+00:00 | 2026-11-11T12:02:51.745Z | ok |

## 核心行情与风险代理

| 标的 | 价格/指数 | 单位 | 观测日 | 1日% | 5日% | 20日% | 质量 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 749.92 | USD_per_share | 2026-11-10 | -0.37 | -0.59 | -3.61 | ok |
| QQQ | 674.76 | USD_per_share | 2026-11-10 | -0.68 | -1.54 | -9.25 | ok |
| IWM | 280.58 | USD_per_share | 2026-11-10 | -0.68 | 0.28 | 1.40 | ok |
| RSP | 220.88 | USD_per_share | 2026-11-10 | -0.03 | 0.74 | 3.55 | ok |
| GLD | 369.36 | USD_per_share | 2026-11-10 | -2.68 | 2.81 | -3.23 | ok |
| GC=F | 4,030.20 | USD_per_troy_ounce | 2026-11-10 | -2.05 | 2.28 | -3.52 | ok |
| CL=F | 86.04 | USD_per_barrel | 2026-11-10 | -0.93 | -10.46 | -8.60 | ok |
| BZ=F | 91.49 | USD_per_barrel | 2026-11-10 | -1.17 | -11.69 | -13.44 | ok |
| TLT | 80.88 | USD_per_share | 2026-11-10 | -1.32 | -0.28 | 3.20 | ok |
| UUP | 29.15 | USD_per_share | 2026-11-10 | 0.62 | 0.48 | 0.45 | ok |
| HYG | 77.18 | USD_per_share | 2026-11-10 | -0.43 | 0.26 | 0.12 | ok |
| LQD | 103.88 | USD_per_share | 2026-11-10 | -0.75 | 0.15 | 1.30 | ok |
| ^VIX | 19.46 | index | 2026-11-10 | -2.31 | -6.58 | 27.44 | ok |
| ^VIX3M | 20.64 | index | 2026-11-10 | -1.01 | -2.96 | 14.92 | ok |
| ^VVIX | 96.63 | index | 2026-11-10 | -1.83 | -10.03 | 13.18 | ok |
| ^MOVE | 92.43 | index | 2026-11-10 | 7.50 | -7.54 | -8.57 | ok |
| NVDA | 168.89 | USD_per_share | 2026-11-10 | -5.47 | -18.29 | -26.09 | ok |
| MSFT | 533.16 | USD_per_share | 2026-11-10 | -2.20 | 2.34 | -1.89 | ok |
| AMZN | 270.87 | USD_per_share | 2026-11-10 | 1.48 | 8.05 | 4.75 | ok |
| GOOGL | 287.38 | USD_per_share | 2026-11-10 | -0.27 | 2.62 | -18.77 | ok |
| META | 641.39 | USD_per_share | 2026-11-10 | 0.00 | 3.28 | -15.88 | ok |
| CRWV | 48.73 | USD_per_share | 2026-11-10 | -0.51 | -9.32 | -37.37 | ok |
| MU | 725.11 | USD_per_share | 2026-11-10 | -1.10 | -15.20 | -23.92 | ok |
| DRAM | 40.64 | USD_per_share | 2026-11-10 | -2.73 | -14.69 | -23.09 | ok |
| VRT | 194.22 | USD_per_share | 2026-11-10 | -3.12 | -17.69 | -18.15 | ok |

## 跨资产风险解释

恐慌缓解、并非全面过热。CNN浏览器34/Fear，11日06:48:31EST更新，比晨报33高1点；指数部分组件仍为昨晚。VIX盘前18.63（11:48UTC）低于昨日收盘19.46，但不能与昨日VIX3M拼成实时期限比。昨日同日VIX/VIX3M约0.943，VVIX96.63，MOVE92.43单日+7.50%。SIFMA推荐11日美元债券市场休市，美股按tc日历正常；10年收益率代理4.983%最后观测仍为10日19:59UTC，不是今晚实时利率。FRED2年4.56%、10年4.88%、实际10年2.66%、HY334bp与IG91bp截至9日，不能证明CPI后信用压力已消失。盈亏平衡通胀2.20%截至10日，金融压力−0.5224截至10月30日。约11:53UTC WTI86.66、Brent92.75、黄金期货4055.60、美元102.523，连续合约并非结算；美元仍偏强，避险资产可能同时受贴现率压制。GPR113.95仍截至2日，官网标示9日更新但当前采集序列/替代文件未能补足，不据此判断今天战事降温。运输事件有报道称与伊朗宣称，部分伤损未经独立确认；换囚不是全面停火。不制造统一避险或战争指数。

## 宏观与地缘风险指标

| 指标 | 数值 | 单位 | 观测日 | 20次观测变化 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- | --- |
| DGS2 | 4.56 | percent | 2026-11-09 | -0.24 | lagged | https://fred.stlouisfed.org/series/DGS2 |
| BAMLH0A0HYM2 | 3.34 | percentage_points | 2026-11-09 | 0.23 | lagged | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| BAMLC0A0CM | 0.91 | percentage_points | 2026-11-09 | 0.08 | lagged | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| DGS10 | 4.88 | percent | 2026-11-09 | -0.36 | lagged | https://fred.stlouisfed.org/series/DGS10 |
| DFII10 | 2.66 | percent | 2026-11-09 | -0.25 | lagged | https://fred.stlouisfed.org/series/DFII10 |
| T10YIE | 2.20 | percent | 2026-11-10 | -0.13 | ok | https://fred.stlouisfed.org/series/T10YIE |
| STLFSI4 | -0.52 | index | 2026-10-30 | 0.24 | lagged | https://fred.stlouisfed.org/series/STLFSI4 |
| CBOE_VIX | 19.46 | index | 2026-11-10 | 4.19 | ok | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| GPRD | 113.95 | index | 2026-11-02 | -245.09 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_ACT | 129.82 | index | 2026-11-02 | -342.91 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_THREAT | 108.29 | index | 2026-11-02 | -240.96 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_MA7 | 158.85 | index | 2026-11-02 | -44.27 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_MA30 | 184.74 | index | 2026-11-02 | 13.98 | lagged | https://www.matteoiacoviello.com/gpr.htm |

## CNN Fear & Greed

```json
{
  "value": 34,
  "rating": "Extreme Fear",
  "observed_at": "2026-11-11T06:48:31-05:00",
  "retrieved_at": "2026-11-11T12:10:17.221674+00:00",
  "source": "https://www.cnn.com/markets/fear-and-greed",
  "quality": "verified_browser",
  "previous_close": 33,
  "one_week_ago": 19,
  "note": "本轮CNN浏览器直接核验；各组件时间不同，API418。"
}
```

## 19 板块与主题 ETF：价格量能证据

| 标的 | 板块 | 1日% | 5日% | 20日% | 相对SPY 1日pp | 相对SPY 5日pp | 相对SPY 20日pp | 成交量/前20日 | 观测日 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLK | 科技 | -1.15 | -4.31 | -13.94 | -0.78 | -3.72 | -10.33 | 0.83 | 2026-11-10 |
| XLE | 能源 | 0.44 | -6.70 | -7.43 | 0.80 | -6.12 | -3.82 | 0.89 | 2026-11-10 |
| XLF | 金融 | 0.52 | 1.92 | 6.33 | 0.89 | 2.51 | 9.94 | 0.82 | 2026-11-10 |
| XLI | 工业 | -0.09 | -1.51 | 0.04 | 0.27 | -0.92 | 3.65 | 0.59 | 2026-11-10 |
| XLV | 医疗 | 0.29 | 2.64 | 11.33 | 0.66 | 3.23 | 14.94 | 0.77 | 2026-11-10 |
| XLP | 必需消费 | 0.15 | 2.34 | 8.12 | 0.52 | 2.93 | 11.73 | 0.61 | 2026-11-10 |
| XLY | 可选消费 | 0.03 | 3.17 | 7.73 | 0.40 | 3.76 | 11.34 | 0.80 | 2026-11-10 |
| XLC | 通信 | 0.37 | 6.23 | -4.03 | 0.74 | 6.82 | -0.42 | 0.73 | 2026-11-10 |
| XLU | 公用事业 | -0.14 | 0.71 | 4.44 | 0.23 | 1.30 | 8.05 | 0.58 | 2026-11-10 |
| XLRE | 房地产 | -0.13 | 2.08 | 6.57 | 0.23 | 2.67 | 10.18 | 0.75 | 2026-11-10 |
| XLB | 材料 | -0.17 | 0.49 | 6.30 | 0.20 | 1.08 | 9.91 | 0.63 | 2026-11-10 |
| SMH | 半导体 | -0.78 | -6.73 | -17.77 | -0.41 | -6.14 | -14.16 | 0.85 | 2026-11-10 |
| IGV | 软件 | -1.11 | -2.27 | -9.60 | -0.75 | -1.68 | -5.99 | 0.72 | 2026-11-10 |
| XOP | 油气开采 | 0.79 | -8.35 | -12.16 | 1.15 | -7.77 | -8.55 | 1.58 | 2026-11-10 |
| OIH | 油服 | -0.35 | -6.69 | -7.98 | 0.02 | -6.11 | -4.37 | 0.76 | 2026-11-10 |
| ITA | 航空与国防 | 0.95 | 0.41 | 6.40 | 1.32 | 0.99 | 10.01 | 0.56 | 2026-11-10 |
| ARKX | 航天主题 | -0.33 | 0.07 | -4.80 | 0.04 | 0.65 | -1.19 | 3.34 | 2026-11-10 |
| KRE | 区域银行 | -0.49 | 0.29 | 5.84 | -0.12 | 0.88 | 9.45 | 0.70 | 2026-11-10 |
| SKYY | 云计算 | -0.50 | -3.87 | -12.58 | -0.14 | -3.28 | -8.97 | 0.81 | 2026-11-10 |

## 资金证据分层

收盘主体仍为11月10日，19ETF中8涨，不能当今晚广度。XLF+0.52%、XLV+0.29%、XLP+0.15%、XLC+0.37%，RSP−0.03%相对SPY−0.37%较稳；金融/医疗5日+1.92%/+2.64%。SMH昨收−0.78%、5日−6.73%，今晚盘前+4.93%才是增量，尚低于200日线522.62及20日线526.53。优先观察半导体修复能否扩散，而非只凭AMD/CRWV上涨升级整个软件与AI。XLE/XOP昨日+0.44%/+0.79%但5日仍跌；ITA在20日线上而低于200日线75.90。前20日相对量SPY0.84倍、QQQ0.75倍、SMH0.85倍、NVDA3.11倍，只反映交易活跃度。VanEck新页面更新到10日SMH NAV483.84、净资产634.8亿美元；缺精确连续份额与调整桥，不用两次四舍五入资产/NAV猜净流量。ICI最新仍是10日发布、截至4日一周：ETF总净发行498.30亿美元，国内股票308.68亿、债券138.89亿、商品1.29亿；此窗口早于5日大跌，不代表当前资金转向。机构持仓与当期单ETF净申赎缺失。

## 最近可核验 ETF 申赎窗口

| 标的 | 金额 USD million | 起始日 | 结束日 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- |
| US_DOMESTIC_EQUITY_ETFS | 30868 | 2026-10-29 | 2026-11-04 | public_report | https://www.ici.org/research/stats/etf_flows |
| US_BOND_ETFS | 13889 | 2026-10-29 | 2026-11-04 | public_report | https://www.ici.org/research/stats/etf_flows |
| US_COMMODITY_ETFS | 129 | 2026-10-29 | 2026-11-04 | public_report | https://www.ici.org/research/stats/etf_flows |

## Polymarket 搜索覆盖与限制

12:02UTC起按原清单及15组主动搜索覆盖Fed/衰退、AI泡沫/CEO/CoreWeave/AMD、Iran/Hormuz/Ukraine、关税/政府、航天、银行、原油与州数据中心禁令；每组limit10首批，AI泡沫/航天/伊朗等截断，AMD空结果不等于无事件。加入CRWV评级、俄乌能源协议与WTI阈值；不以未知正式事件时间填入upcoming，临近合约截止列参考栏并解释。

## Polymarket · 值得警惕的信号

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["AI bubble burst in 2026?", "期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。", "https://polymarket.com/event/ai-bubble-burst-by"] | [8.85, {"status": "comparable", "change_pp": -0.10000000000000009}] | {"spread": 0.0010000000000000009, "volume24h_usd": 69607.777555, "liquidity_usd": 128404.49761, "quality_flags": [], "retrieved_at": "2026-11-11T12:03:18.835390+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["多条件AI合约与实际融资分开", "AI估值/融资"] | ["多个实际阈值与信用持续恶化共同出现", "需求、回款与融资恢复且阈值未满足"] | [null, null] |
| ["CoreWeave downgraded by Moody's or S&P by December 31, 2026?", "2026年12月31日23:59ET前，Moody’s或S&P正式下调CoreWeave长期主体/企业家族或高级无担保债信用评级则Yes；仅负面展望/观察名单不算，不要求降至某统一评级档。成交很薄，不视为客观违约概率。", "https://polymarket.com/event/coreweave-downgraded-by-moodys-or-sp-by"] | [31.0, {"status": "no_baseline"}] | {"spread": 0.020000000000000018, "volume24h_usd": 135.8, "liquidity_usd": 447.7679, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"], "retrieved_at": "2026-11-11T12:03:29.635154+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["新发现评级下调合约，24h成交很薄", "算力融资成本"] | ["正式评级行动及实际融资成本共同转坏", "仅展望变化或评级不变；薄盘口不足确认"] | [null, null] |
| ["Jensen Huang announced resignation or removal by December 31, 2026?", "年末23:59美东前，黄仁勋/NVIDIA或授权代表正式明确宣布辞任或被撤去CEO，且预定在宣布后18个月内实施则Yes；不要求年内实际离任。临时休假、停职、条件式考虑、未被接受辞呈和媒体单独传闻不算。以官方信息优先；不得把调查直接视为离任。 合格辞任/撤职实际发生亦可能触发，需按专门规则核验；本次与早报hash相同。", "https://polymarket.com/event/jensen-huang-announced-resignation-or-removal-by-december-31"] | [16.5, {"status": "comparable", "change_pp": 1.0000000000000009}] | {"spread": 0.010000000000000009, "volume24h_usd": 302377.017262, "liquidity_usd": 205758.4528, "quality_flags": [], "retrieved_at": "2026-11-11T12:03:18.835390+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["治理事件仍未完结", "NVDA及芯片风险溢价"] | ["官方明确离任或约束升级", "公司维持治理安排且无新不利事实"] | [null, null] |

## Polymarket · 有参考价值的事件

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Strait of Hormuz traffic returns to normal by December 31?", "期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。", "https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31"] | [8.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.009999999999999995, "volume24h_usd": 29017.077648, "liquidity_usd": 219351.1514, "quality_flags": [], "retrieved_at": "2026-11-11T12:03:18.835390+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["实际通行量与外交表态分开", "油运/能源"] | ["Portwatch量持续改善并满足规则", "航运事件持续且量未恢复"] | [null, null] |
| ["Russia x Ukraine energy ceasefire agreement by November 15, 2026?", "11月15日23:59基辅时间前，俄乌双方同意暂停打击至少一类明确能源设施，双方官宣或可信报道共识确认；美国第三方单方声称不足。可限定地理范围，但仅一个设施不算；必须明确相互暂停，不是谈判/换囚。约定生效日可晚于截止。", "https://polymarket.com/event/russia-x-ukraine-energy-ceasefire-agreement-by"] | [4.5, {"status": "no_baseline"}] | {"spread": 0.010000000000000002, "volume24h_usd": 37198.069483, "liquidity_usd": 94646.0767, "quality_flags": [], "retrieved_at": "2026-11-11T12:03:18.835390+00:00", "contract_end_at": "2026-11-15T21:59:00+00:00"} | ["新能源协议合约；15日是截止非会议日", "能源供给/风险溢价"] | ["双方确认合格能源设施互停安排", "仅换囚或第三方声称"] | [null, null] |
| ["Russia x Ukraine ceasefire agreement by December 31, 2026?", "2026年末23:59ET前，双方官宣或可信共识确认相互暂停直接交战，包含明确生效日的全面暂停；仅限定目标/地点的局部能源安排不算。达成协议可先于实际生效，单方暂停不算。", "https://polymarket.com/event/russia-x-ukraine-ceasefire-agreement-by"] | [13.5, {"status": "no_baseline"}] | {"spread": 0.010000000000000009, "volume24h_usd": 7852.794611, "liquidity_usd": 85591.7488, "quality_flags": [], "retrieved_at": "2026-11-11T12:03:18.835390+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["全年全面停火协议与能源局部暂停定义不同", "军工/欧洲风险偏好"] | ["双边明确全面暂停及生效日", "仅局部或单方暂停"] | [null, null] |
| ["Will WTI Crude Oil (WTI) hit (HIGH) $110 in November?", "11月合资格交易时段，Pyth对ICE Europe WTI活跃月CLL的任一最终1分钟High达到110美元即Yes；按原值不取整，最后三个交易日换月。主数据不可用时依ICE官方日高低。与Yahoo NYMEX连续WTI代理不是同一可直接裁决序列。", "https://polymarket.com/event/what-price-will-wti-hit-in-november-2026"] | [6.5, {"status": "no_baseline"}] | {"spread": 0.010000000000000009, "volume24h_usd": 4688.567714999999, "liquidity_usd": 26905.1737, "quality_flags": [], "retrieved_at": "2026-11-11T12:03:18.835390+00:00", "contract_end_at": "2026-12-01T04:59:59.999000+00:00"} | ["月内WTI高点合约；不直接用Yahoo裁决", "通胀与油气"] | ["指定Pyth/ICE价格和实际供应压力同向", "供应改善且指定价格未触发"] | [null, null] |
| ["Will the Fed increase interest rates by 50+ bps after the December 2026 meeting?", "衡量12月8–9日该次FOMC前后联邦基金目标区间上限上调至少50bp；非标准变化向上取整到最近25bp对应档。按正式声明，若下一次会议结束仍无声明则按不变档处理。不是全年累计加息幅度。", "https://polymarket.com/event/fed-decision-in-december-20260729232808632"] | [9.950000000000001, {"status": "comparable", "change_pp": -0.20000000000000018}] | {"spread": 0.0010000000000000009, "volume24h_usd": 1351789.9977900002, "liquidity_usd": 367858.017, "quality_flags": [], "retrieved_at": "2026-11-11T12:03:18.835390+00:00", "contract_end_at": "2026-12-09T23:59:00+00:00"} | ["12月单次50+bp风险", "利率与长久期估值"] | ["官方政策及融资/利率同步趋紧", "数据转弱与实际政策不符"] | [null, null] |

## Polymarket · 将要发生的事件及概率

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Will the Fed increase interest rates by 25 bps after the December 2026 meeting?", "以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。", "https://polymarket.com/event/fed-decision-in-december-20260729232808632"] | [85.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.010000000000000009, "volume24h_usd": 877101.73328, "liquidity_usd": 701134.1328, "quality_flags": [], "retrieved_at": "2026-11-11T12:03:18.835390+00:00", "contract_end_at": "2026-12-09T23:59:00+00:00"} | ["12月25bp会议定价（超一周的重大背景）；会议日已核验，14:00为常规发布时间待复核", "风险贴现率"] | ["官方目标区间上调对应档", "不符合对应档"] | ["2026-12-09T14:00:00-05:00", "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm"] |

## Will the Fed increase interest rates by 50+ bps after the December 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 770450 / 3215009 |
| Yes 概率 % | 9.95 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [5.2, 9.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.20000000000000018} |
| 24h成交量 / 流动性 USD | [1351789.9977900002, 367858.017] |
| 价差 pp | 0.10 |
| 到期 | 2026-12-09T23:59:00+00:00 |
| 结算规则摘要 | 衡量12月8–9日该次FOMC前后联邦基金目标区间上限上调至少50bp；非标准变化向上取整到最近25bp对应档。按正式声明，若下一次会议结束仍无声明则按不变档处理。不是全年累计加息幅度。 |
| 规则指纹 | a05ecc7aefe678e9936425027277135b8c37cdaf659af595020eb1668ec48e58 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-11T12:00:55.523471Z |
| 抓取时间 | 2026-11-11T12:03:18.835390+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-december-20260729232808632 |

## Will the Fed increase interest rates by 25 bps after the December 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 770450 / 3215008 |
| Yes 概率 % | 85.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-1.0, 5.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [877101.73328, 701134.1328] |
| 价差 pp | 1.00 |
| 到期 | 2026-12-09T23:59:00+00:00 |
| 结算规则摘要 | 以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。 |
| 规则指纹 | 933a10a15eeec0ff1de30468fa20540301ed243f75cc3572d42946192f81a123 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-11T12:00:55.523471Z |
| 抓取时间 | 2026-11-11T12:03:18.835390+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-december-20260729232808632 |

## Jensen Huang announced resignation or removal by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1343940 / 6882826 |
| Yes 概率 % | 16.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [3.0, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 1.0000000000000009} |
| 24h成交量 / 流动性 USD | [302377.017262, 205758.4528] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 年末23:59美东前，黄仁勋/NVIDIA或授权代表正式明确宣布辞任或被撤去CEO，且预定在宣布后18个月内实施则Yes；不要求年内实际离任。临时休假、停职、条件式考虑、未被接受辞呈和媒体单独传闻不算。以官方信息优先；不得把调查直接视为离任。 合格辞任/撤职实际发生亦可能触发，需按专门规则核验；本次与早报hash相同。 |
| 规则指纹 | 967939ae08f1461b2a8b5a40c6c07828619958ef439b679055b7698fa1e18988 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-11T12:00:55.523471Z |
| 抓取时间 | 2026-11-11T12:03:18.835390+00:00 |
| 来源 | https://polymarket.com/event/jensen-huang-announced-resignation-or-removal-by-december-31 |

## AI bubble burst in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 691340 |
| Yes 概率 % | 8.85 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [2.8, 0.35] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.10000000000000009} |
| 24h成交量 / 流动性 USD | [69607.777555, 128404.49761] |
| 价差 pp | 0.10 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | fc153b2136a8dfbadcd169dce1add40690acb1748566b99716fe7ae8fcb07330 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-11T12:00:55.523471Z |
| 抓取时间 | 2026-11-11T12:03:18.835390+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## Russia x Ukraine energy ceasefire agreement by November 15, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1360126 / 6947935 |
| Yes 概率 % | 4.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, null] |
| 与上一快照可比变化 | {"status": "no_baseline"} |
| 24h成交量 / 流动性 USD | [37198.069483, 94646.0767] |
| 价差 pp | 1.00 |
| 到期 | 2026-11-15T21:59:00+00:00 |
| 结算规则摘要 | 11月15日23:59基辅时间前，俄乌双方同意暂停打击至少一类明确能源设施，双方官宣或可信报道共识确认；美国第三方单方声称不足。可限定地理范围，但仅一个设施不算；必须明确相互暂停，不是谈判/换囚。约定生效日可晚于截止。 |
| 规则指纹 | a3874db8482536581cb7832c287d198abdb207e6448a0fd10b7da294d17de561 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-11T12:02:55.503086Z |
| 抓取时间 | 2026-11-11T12:03:18.835390+00:00 |
| 来源 | https://polymarket.com/event/russia-x-ukraine-energy-ceasefire-agreement-by |

## Strait of Hormuz traffic returns to normal by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 455875 / 2176270 |
| Yes 概率 % | 8.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, -2.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [29017.077648, 219351.1514] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。 |
| 规则指纹 | b0c8ba27f4437b0d8ab819ae170bec118166232e39cdcaefb95bd352d29073d4 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-11T12:02:55.503086Z |
| 抓取时间 | 2026-11-11T12:03:18.835390+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31 |

## US x Iran Effective Ceasefire by November 15?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1337182 / 6831494 |
| Yes 概率 % | 52.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [6.0, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 4.5000000000000036} |
| 24h成交量 / 流动性 USD | [28329.091461999997, 96012.0704] |
| 价差 pp | 1.00 |
| 到期 | 2026-11-15T20:29:00+00:00 |
| 结算规则摘要 | 须完成连续14个伊朗标准时间日，美国未对伊朗陆地及内水实施命中目标的合资格空袭/地对地导弹攻击，且该14天首日在创建后至11月15日范围内；最后一次合资格行动次日为首日，无行动则创建日为首日。拦截碎片、威胁、海域/领空、地面入侵、网络、小型武器/部分小型袭击等不算。第14日后再留3个日历日报道窗口，按官方信息及可信报道综合裁定。不是双方全面停火，也不要求14天在15日前完成。 |
| 规则指纹 | c70e370d0e95bf9245a1a527f4f02bb307f13aa2766e1cc24004c7559bfb4b53 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-11T12:00:55.523471Z |
| 抓取时间 | 2026-11-11T12:03:18.835390+00:00 |
| 来源 | https://polymarket.com/event/us-x-iran-effective-ceasefire-begins-by-2-week-pause-20261108 |

## Russia x Ukraine ceasefire agreement by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 478472 / 2243897 |
| Yes 概率 % | 13.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-1.0, -2.0] |
| 与上一快照可比变化 | {"status": "no_baseline"} |
| 24h成交量 / 流动性 USD | [7852.794611, 85591.7488] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年末23:59ET前，双方官宣或可信共识确认相互暂停直接交战，包含明确生效日的全面暂停；仅限定目标/地点的局部能源安排不算。达成协议可先于实际生效，单方暂停不算。 |
| 规则指纹 | 2ea22f9548269db3205e41396a99073a2d5788dc4fde17989e34c8051ae6b75b |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-11T12:02:55.503086Z |
| 抓取时间 | 2026-11-11T12:03:18.835390+00:00 |
| 来源 | https://polymarket.com/event/russia-x-ukraine-ceasefire-agreement-by |

## Will WTI Crude Oil (WTI) hit (HIGH) $110 in November?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1250301 / 6172751 |
| Yes 概率 % | 6.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-3.0, -17.0] |
| 与上一快照可比变化 | {"status": "no_baseline"} |
| 24h成交量 / 流动性 USD | [4688.567714999999, 26905.1737] |
| 价差 pp | 1.00 |
| 到期 | 2026-12-01T04:59:59.999000+00:00 |
| 结算规则摘要 | 11月合资格交易时段，Pyth对ICE Europe WTI活跃月CLL的任一最终1分钟High达到110美元即Yes；按原值不取整，最后三个交易日换月。主数据不可用时依ICE官方日高低。与Yahoo NYMEX连续WTI代理不是同一可直接裁决序列。 |
| 规则指纹 | 97cca376098aad5ff8f5ece05abb9ae13f218bc5005dc802696a1f1922949a52 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-11T12:00:55.523471Z |
| 抓取时间 | 2026-11-11T12:03:18.835390+00:00 |
| 来源 | https://polymarket.com/event/what-price-will-wti-hit-in-november-2026 |

## AI bubble burst by June 30, 2027?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 4838928 |
| Yes 概率 % | 22.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, -0.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [4637.414615, 101231.8983] |
| 价差 pp | 1.00 |
| 到期 | 2027-07-01T03:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | bd0420587e08487fffa5050e7fd9b79ffff909a9f843d3f620207ee859462505 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-11T12:00:55.523471Z |
| 抓取时间 | 2026-11-11T12:03:18.835390+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## Tesla and SpaceX merger officially announced by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 192962 / 2252540 |
| Yes 概率 % | 9.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, -0.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [540.428573, 16916.0191] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59纽约时间前，Tesla或SpaceX正式宣布双方合并或一方收购另一方的控制权即Yes；无需在期限内完成交易。控制权通常为过半权益或等效治理权；少数股权投资及仅讨论不算。以公司公告或可信报道共识核验；旧URL中的june-30不是本合约期限。 |
| 规则指纹 | 909906ae3b6db7e473468713ea6a1e1e4cf4c931fe247c7d3d576e7986513008 |
| 质量 | ["volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-11T11:58:55.210128Z |
| 抓取时间 | 2026-11-11T12:03:18.835390+00:00 |
| 来源 | https://polymarket.com/event/tesla-and-spacex-merger-officially-announced-by-june-30 |

## CoreWeave downgraded by Moody's or S&P by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1219851 / 5939467 |
| Yes 概率 % | 31.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, 13.5] |
| 与上一快照可比变化 | {"status": "no_baseline"} |
| 24h成交量 / 流动性 USD | [135.8, 447.7679] |
| 价差 pp | 2.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59ET前，Moody’s或S&P正式下调CoreWeave长期主体/企业家族或高级无担保债信用评级则Yes；仅负面展望/观察名单不算，不要求降至某统一评级档。成交很薄，不视为客观违约概率。 |
| 规则指纹 | 040e522db15913bd31de0e1a7f935727361429e7c42b3c1fc5286a0cf1b0fc42 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-11T12:00:55.523471Z |
| 抓取时间 | 2026-11-11T12:03:29.635154+00:00 |
| 来源 | https://polymarket.com/event/coreweave-downgraded-by-moodys-or-sp-by |

## AI 压力：合约、经营与估值分开

一、特定AI泡沫合约2026为8.85%、2027年6月22.5%；前者同规则较晨报8.95%仅低0.10个百分点，不能称风险显著消失。合同需同一90日窗口内至少三项专门事件，不能用单股跌幅替代。Silicon Data H100指数仍为10日3.06美元/GPU小时，并非今晚新读数，也未触发≤1连续5日阈值。二、需求有支持：TSMC官方十月营收5868.9亿新台币、同比59.7%、环比14.7%，不得采用媒体“近六倍”的误写。CRWV营收36.61亿美元、营业利润2.07亿而净利息8.46亿，约90亿预付款是管理层未来三个月预期，不是已收到现金；盘前56.07较昨收48.73约+15.06%，较晨报反弹扩大。AMD官方发布第六代EPYC并披露Google TPU主机合作；这些是需求/竞争线索，不能证明NVDA订单已经被转走。NVDA盘前175.35重回170.24上，但治理调查未有结果；MSFT535仍低于538.70旧观察线。Alphabet拟在港新融资约30亿美元为Reuters引述知情人士，未取得发行完成公告，不入已发生净债务。Baird降级/砍目标价线索未取原研报，不把10–30%订单削减估计当事实。新发现CRWV降级合约仅约136美元24h成交、2个百分点价差，弱证据且不等于破产。三、本轮SEC五家公司定期披露列表全部重查，与晨报底稿版本相同。NVDA更新价格后的整体FCFF三情景、折现率和隐含增长为假设敏感性，非纯AI估值/客观概率；MSFT、AMZN、GOOGL、META完整租赁、净债务/现金流桥仍缺，保留估值不可用。

## NVDA · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | scenario_analysis |
| 财务底稿 | TTM 至 2026-07-26；最新 10-Q / filed 2026-08-26 |
| 披露检查 | {"checked_at": "2026-11-11T12:04:40.980997+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001045810.json", "latest_filing_date": "2026-08-26"} |
| 观测财务数据 | {"ttm_revenue_million": 302970, "revenue_quarters": [{"end": "2025-10-26", "value": 57006000000, "filed": "2025-11-19", "duration_days": 91}, {"end": "2026-01-25", "value": 68127000000, "filed": "2026-02-25", "duration_days": 91}, {"end": "2026-04-26", "value": 81615000000, "filed": "2026-05-20", "duration_days": 91}, {"end": "2026-07-26", "value": 96221000000, "filed": "2026-08-26", "duration_days": 91}], "cash_million": 22443.0, "liquid_investments_million": 34143.0, "debt_million": 33366.0, "finance_lease_million": 0, "diluted_shares_million": 24285.0, "latest_operating_income_million": 63734.0, "observed_end": "2026-07-26", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "Revenues", "latest_reported_revenue_million": 96221.0, "income_statement_window": "最近单季度", "ttm_bridge_note": "采用同版 FY2026全年 + FY2027半年 - FY2026半年；与四季逐项求和差1百万为披露舍入差。"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json", "https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。10-Q Note14 表明融资租赁费用不重大；模型按不重大近似零，不将其称为精确零负债。未确认担保仅作为压力情景，非已到期净债务。市场化股权42783和非市场化股权51157不作为类现金；非经营资产加回为0的保守假设。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | 无 |
| 价格 USD | 168.89 |
| 基期输入 USD million / million shares | {"revenue": 302970, "net_debt": -23220.0, "diluted_shares": 24285.0, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.22489815932838664, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## NVDA · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 98.77 | -41.52 | 14.00 | 60.00 | 12.00 | 68.42 |
| 基准 | 154.12 | -8.75 | 20.00 | 65.00 | 11.00 | 74.20 |
| 乐观 | 242.58 | 43.63 | 26.00 | 70.00 | 10.00 | 79.05 |

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
| 披露检查 | {"checked_at": "2026-11-11T12:04:43.253042+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0000789019.json", "latest_filing_date": "2026-10-28"} |
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
| 披露检查 | {"checked_at": "2026-11-11T12:04:45.685241+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001018724.json", "latest_filing_date": "2026-10-30"} |
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
| 披露检查 | {"checked_at": "2026-11-11T12:04:48.413479+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001652044.json", "latest_filing_date": "2026-10-29"} |
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
| 披露检查 | {"checked_at": "2026-11-11T12:04:51.592596+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001326801.json", "latest_filing_date": "2026-10-22"} |
| 观测财务数据 | {"revenue_million": 64601, "operating_cashflow_million": 32790, "reported_capex_including_finance_lease_principal_million": 34910, "company_defined_fcf_million": -2120, "diluted_shares_million": 2573, "reported_operating_income_million": 12988, "legal_charge_million": 9900, "observed_end": "2026-09-30", "published_at": "2026-10-21T16:01:00-04:00", "unit": "USD million; shares million", "noncancelable_commitments_million": 454520, "leases_not_commenced_million": 355730, "contingent_cloud_capacity_max_million": 14720, "restricted_cash_reclassified_million": 10800, "commitments_due_2026_million": 45850, "commitments_due_2027_million": 121410} |
| 来源 | ["https://www.prnewswire.com/news-releases/meta-reports-third-quarter-2026-results-302915964.html", "https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm", "https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Announces-Launch-of-Offering-of-Depositary-Shares-Representing-Series-A-Mandatory-Convertible-Preferred-Stock-and-Offering-of-Class-A-Common-Stock-in-Connection-with-Forward-Sale-Agreements/default.aspx", "https://www.prnewswire.com/news-releases/meta-announces-pricing-of-offering-of-depositary-shares-representing-series-a-mandatory-convertible-preferred-stock-and-offering-of-class-a-common-stock-in-connection-with-forward-sale-agreements-302920247.html"] |
| 口径 | 公司FCF扣除融资租赁本金，不能直接代替模型FCFF；融资租赁负债/新增资产未齐，不假设零。法律费用不全归AI经营。 |
| 主观假设说明 | 缺失 |
| 权益桥额外假设 | 无 |
| 缺失原因 | 沿用底稿的历史核验说明（其中“本次”指原核验日）；本轮最新定期财报列表检查见disclosure_check。22日10-Q已核验，本次无新增定期财报。27日普通股625美元定价、优先票息6.5%已核验；完整融资租赁负债/新增资产、优先权益/远期发行与现金到账桥未齐，不用不同承诺简单充当现有债务，暂停精确FCFF反推。 |

## 宽基反弹升级测试

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 盘前需求反弹与13日PPI |
| 关联标的 | ["SPY", "QQQ", "RSP"] |
| 确认条件 | SPY755附近、QQQ680–682在开盘后首次回踩守住，形成更高低点；RSP与参与面同步，收盘保持；进一步看SPY760.69的20日线。 |
| 失效条件 | 跌回755/680下且反抽失败则不升级；SPY744.86、QQQ667.05再破明显削弱修复。 |
| 观察期限 | 11月11日至13日常规时段 |
| 反证 | 暂无常规时段VWAP、真实涨跌家数与成交承接；不因盘前触及即追涨。 |
| 状态 | 盘前触及，待常规交易确认 |

## 半导体修复与NVDA治理分开

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | TSMC/CRWV需求证据与NVDA17日业绩 |
| 关联标的 | ["SMH", "AMD", "NVDA", "CRWV"] |
| 确认条件 | SMH开盘回踩守490–493；NVDA守170.24并进一步收复178.67；CRWV维持高开区间更高低点，板块相对QQQ同步。 |
| 失效条件 | SMH跌回490–493且反抽失败、NVDA失170.24，或CRWV高开跌回51.02甚至48.73，撤销升级；不要等全部触发才管理风险。 |
| 观察期限 | 11月11日至13日常规时段 |
| 反证 | SMH200日线522.62未收复，NVDA调查与高资本开支尚未消失。 |
| 状态 | 盘前触及，待常规交易确认 |

## 金融医疗相对强势观察

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 资金偏好与利率变化 |
| 关联标的 | ["XLF", "XLV", "XLP"] |
| 确认条件 | XLF守58.26附近再看59.20；医疗/必需消费回踩保持20日线与相对SPY强度。 |
| 失效条件 | 失去支撑且相对收益转弱；信用新数据恶化时金融标签失效。 |
| 观察期限 | 11月11日至13日常规时段 |
| 反证 | 芯片反弹可能使防御相对表现减弱；没有当期申赎证明。 |
| 状态 | 盘前触及，待常规交易确认 |

## 跨期比较与上期剧本复核

相对今晨同收盘日的新盘前增量：SPY已盘前越过755.42、QQQ越过680.35–682、SMH越过490–493、NVDA回到170.24上方；只是价格触及条件，开盘回踩、量能与收盘保持尚未发生，不能将剧本记为已成功。MSFT尚未修复538.70。CRWV由盘后51.42扩至盘前56.07，超过51.02旧高，但本次不能事先知道高开能否守住。相同ID+规则hash比较：Strait of Hormuz traffic returns to normal by December 31?：+0.00个百分点；Will the Fed increase interest rates by 25 bps after the December 2026 meeting?：+0.00个百分点；AI bubble burst in 2026?：-0.10个百分点；AI bubble burst by June 30, 2027?：+0.00个百分点；Tesla and SpaceX merger officially announced by December 31?：+0.00个百分点；Jensen Huang announced resignation or removal by December 31, 2026?：+1.00个百分点；US x Iran Effective Ceasefire by November 15?：+4.50个百分点；Will the Fed increase interest rates by 50+ bps after the December 2026 meeting?：-0.20个百分点。新发现合约作为首次核验基线；盘口小变动须与价差相比，不等于新独立事件。

## 可计算的跨期变化

```json
[
  {
    "mode": "daily",
    "baseline": "reports/daily/2026-11-10/20261111T000325.344361Z/evidence.json",
    "baseline_cutoff": "2026-11-11T00:03:07.954043+00:00",
    "close_change_pct": {
      "SPY": 0.0,
      "QQQ": 0.0,
      "IWM": 0.0,
      "RSP": 0.0,
      "GLD": 0.0,
      "GC=F": -0.2968680457413053,
      "CL=F": -0.3128219797284948,
      "BZ=F": -0.35940081915867284,
      "HYG": 0.0,
      "LQD": 0.0,
      "^VIX": 0.0,
      "^VIX3M": 0.0,
      "^VVIX": 0.0,
      "^MOVE": -0.001626058939929731,
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
        "change_pct": 0.688168900610564,
        "from_observed_at": "2026-11-10T23:50:18+00:00",
        "to_observed_at": "2026-11-11T12:03:26+00:00"
      },
      "QQQ": {
        "change_pct": 1.5438886510900307,
        "from_observed_at": "2026-11-10T23:50:33+00:00",
        "to_observed_at": "2026-11-11T12:03:20+00:00"
      },
      "SMH": {
        "change_pct": 3.9981966104473576,
        "from_observed_at": "2026-11-10T23:50:21+00:00",
        "to_observed_at": "2026-11-11T12:03:23+00:00"
      },
      "NVDA": {
        "change_pct": 3.2521938515040816,
        "from_observed_at": "2026-11-10T23:50:42+00:00",
        "to_observed_at": "2026-11-11T12:03:28+00:00"
      },
      "MSFT": {
        "change_pct": 0.0,
        "from_observed_at": "2026-11-10T23:50:16+00:00",
        "to_observed_at": "2026-11-11T12:03:25+00:00"
      },
      "AMZN": {
        "change_pct": 0.1547759433962126,
        "from_observed_at": "2026-11-10T23:50:19+00:00",
        "to_observed_at": "2026-11-11T12:03:25+00:00"
      },
      "GOOGL": {
        "change_pct": 0.5297783933517985,
        "from_observed_at": "2026-11-10T23:50:02+00:00",
        "to_observed_at": "2026-11-11T12:03:07+00:00"
      },
      "META": {
        "change_pct": 0.3441031921985749,
        "from_observed_at": "2026-11-10T23:49:54+00:00",
        "to_observed_at": "2026-11-11T12:02:03+00:00"
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
        "change": -0.46000000000000085,
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
      "3215009": {
        "status": "comparable",
        "change_pp": -0.20000000000000018
      },
      "3215008": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "6882826": {
        "status": "comparable",
        "change_pp": 1.0000000000000009
      },
      "691340": {
        "status": "comparable",
        "change_pp": -0.10000000000000009
      },
      "2176270": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "6831494": {
        "status": "comparable",
        "change_pp": 4.5000000000000036
      },
      "4838928": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "2252540": {
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
    "event": "11日美股正常常规交易；债市SIFMA假日，注意报价时点",
    "date": "2026-11-11T09:30:00-05:00",
    "source": "https://www.sifma.org/resources/general/holiday-schedule"
  },
  {
    "event": "10月PPI，北京13日21:30",
    "date": "2026-11-13T08:30:00-05:00",
    "source": "https://www.bls.gov/schedule/2026/11_sched.htm"
  },
  {
    "event": "NVIDIA Q3预计业绩16:20EST，电话会17:00EST",
    "date": "2026-11-17T16:20:00-05:00",
    "source": "https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/default.aspx"
  },
  {
    "event": "Nebius12日电话会08:00EST，沿用今晨官方核验记录；盘前业绩时间非精确分钟",
    "date": "2026-11-12T08:00:00-05:00",
    "source": "https://nebius.com/investor-events"
  },
  {
    "event": "俄乌正式全面/能源停火协议日期未定，合约截止不等于公告日期",
    "date": null,
    "source": "https://apnews.com/article/7c8d1024302e0c6ad8be064eec852a64"
  }
]
```

## 新闻事件去重与时间

| 事件 | 摘要 | 发生时间（未知留空） | 各来源发布时间 / 抓取时间 |
| --- | --- | --- | --- |
| 20261111-crwv | 财报收入增长支持需求，但利息负担仍高；今晚盘前反弹扩大。 | 缺失 | [{"source": "https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Third-Quarter-2026-Results/default.aspx", "published_at": null, "retrieved_at": "2026-11-11T12:10:17.221674+00:00"}] |
| 20261111-tsm | 十月营收同比59.7%、环比14.7%，不是近六倍。 | 缺失 | [{"source": "https://www.sec.gov/Archives/edgar/data/1046179/000104617926000796/tsm-revenue20261110.htm", "published_at": null, "retrieved_at": "2026-11-11T12:10:17.221674+00:00"}] |
| 20261111-amd | 发布第六代EPYC；Google TPU主机合作为另项官方披露。 | 缺失 | [{"source": "https://ir.amd.com/news-events/press-releases/detail/1305/amd-showcases-6th-gen-amd-epyc-processors-to-lead-next-era-of-ai-and-enterprise-computing", "published_at": null, "retrieved_at": "2026-11-11T12:10:17.221674+00:00"}] |
| 20261111-geo | 俄乌会谈同意大规模换囚，不等于全面停火。 | 缺失 | [{"source": "https://apnews.com/article/7c8d1024302e0c6ad8be064eec852a64", "published_at": "2026-11-11T09:39:45+00:00", "retrieved_at": "2026-11-11T12:10:17.221674+00:00"}] |
| 20261111-ship | 伊朗称油轮触雷；英国海事方面报告事件，部分具体伤损与责任未独立确认。 | 缺失 | [{"source": "https://apnews.com/article/50075bc97e07d41fa3b66fc28858c06b", "published_at": "2026-11-11T11:22:16+00:00", "retrieved_at": "2026-11-11T12:10:17.221674+00:00"}] |
| 20261111-goog | Reuters引述知情人士称拟港新发行约30亿美元债券，非已完成融资。 | 缺失 | [{"source": "https://www.streetinsider.com/Reuters/Alphabet%2Beyes%2B%243%2Bbillion%2BHong%2BKong%2C%2BSingapore%2Bbond%2Bsale%2C%2Bsources%2Bsay/27325764.html", "published_at": "2026-11-11T03:53:00-05:00", "retrieved_at": "2026-11-11T12:10:17.221674+00:00"}] |

## 覆盖范围与数据缺口

```json
[
  "tc报价与昨收一致且统一ts不能核验成交，另存独立Yahoo分钟包用于核心盘前状态，原包不覆盖。",
  "常规时段尚未开始，无当日VWAP/开盘30分钟/回踩成交数据；盘前上涨并不完成确认。",
  "缺真实全成分涨跌/均线广度、历史一致预期修正和CME独立动态概率。",
  "原新闻50条及AI主题50条均有截断；tc实际含多个快讯来源，去重后只使用可核验事件。Baird目标价及订单削减估计未取原研报，不作为经营事实。",
  "GPR实际数值仍至2日，官网9日更新提示与采集值不一致；替代XLS已取得但缺解析依赖。",
  "信用与实际利率截至9日，今天债市假日；旧数值不能证明CPI后风险消失。",
  "CNN API418，已通过官方浏览器补核；不以tc温度代替。",
  "当期单只ETF净申赎及机构持仓缺；发行人资产/NAV四舍五入不足推算。",
  "Polymarket主动搜索首批limit10且多主题截断；CRWV评级合约薄成交，新的能源协议合约不能混作全面停火；无法取得全盘口深度和准确最后成交时戳。",
  "四家公司完整FCFF输入仍缺；本次SEC定期披露检查不等于所有即时披露已全部覆盖。",
  "DRAM历史不满200日，缺失指标不补造；连续期货换月和交易时段口径不同。",
  "部分事件只有日期，具体发生和公告时刻保持null；Nebius未来安排沿用今晨官方核验，未重新声明精确公告分钟。",
  "ETF.com资金流工具链接本轮403，未核验付费功能或价格，不作为已验证订阅推荐。",
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
  "指标缺失/历史不足: prices.^VIX.volume_vs_previous20_ratio, prices.^VIX3M.volume_vs_previous20_ratio, prices.^VVIX.volume_vs_previous20_ratio, prices.^MOVE.volume_vs_previous20_ratio, prices.DRAM.sma200, prices.DRAM.distance_sma200_pct"
]
```

## 来源、时间与核验记录

```json
[
  {
    "url": "https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Third-Quarter-2026-Results/default.aspx",
    "checked_at": "2026-11-11T12:10:17.221674+00:00",
    "note": "本轮公开来源核验；具体发布日期/缺口见正文，checked_at为整理时刻，不冒充成交时间"
  },
  {
    "url": "https://www.sec.gov/Archives/edgar/data/1046179/000104617926000796/tsm-revenue20261110.htm",
    "checked_at": "2026-11-11T12:10:17.221674+00:00",
    "note": "本轮公开来源核验；具体发布日期/缺口见正文，checked_at为整理时刻，不冒充成交时间"
  },
  {
    "url": "https://ir.amd.com/news-events/press-releases/detail/1305/amd-showcases-6th-gen-amd-epyc-processors-to-lead-next-era-of-ai-and-enterprise-computing",
    "checked_at": "2026-11-11T12:10:17.221674+00:00",
    "note": "本轮公开来源核验；具体发布日期/缺口见正文，checked_at为整理时刻，不冒充成交时间"
  },
  {
    "url": "https://investor.nvidia.com/news/press-release-details/2026/Statement-from-NVIDIA-Board-of-Directors/default.aspx",
    "checked_at": "2026-11-11T12:10:17.221674+00:00",
    "note": "本轮公开来源核验；具体发布日期/缺口见正文，checked_at为整理时刻，不冒充成交时间"
  },
  {
    "url": "https://www.ici.org/research/stats/etf_flows",
    "checked_at": "2026-11-11T12:10:17.221674+00:00",
    "note": "本轮公开来源核验；具体发布日期/缺口见正文，checked_at为整理时刻，不冒充成交时间"
  },
  {
    "url": "https://www.bls.gov/schedule/2026/11_sched.htm",
    "checked_at": "2026-11-11T12:10:17.221674+00:00",
    "note": "本轮公开来源核验；具体发布日期/缺口见正文，checked_at为整理时刻，不冒充成交时间"
  },
  {
    "url": "https://www.sifma.org/resources/general/holiday-schedule",
    "checked_at": "2026-11-11T12:10:17.221674+00:00",
    "note": "本轮公开来源核验；具体发布日期/缺口见正文，checked_at为整理时刻，不冒充成交时间"
  },
  {
    "url": "https://www.silicondata.com/products/silicon-index/h100",
    "checked_at": "2026-11-11T12:10:17.221674+00:00",
    "note": "本轮公开来源核验；具体发布日期/缺口见正文，checked_at为整理时刻，不冒充成交时间"
  },
  {
    "url": "https://apnews.com/article/7c8d1024302e0c6ad8be064eec852a64",
    "checked_at": "2026-11-11T12:10:17.221674+00:00",
    "note": "本轮公开来源核验；具体发布日期/缺口见正文，checked_at为整理时刻，不冒充成交时间"
  },
  {
    "url": "https://apnews.com/article/50075bc97e07d41fa3b66fc28858c06b",
    "checked_at": "2026-11-11T12:10:17.221674+00:00",
    "note": "本轮公开来源核验；具体发布日期/缺口见正文，checked_at为整理时刻，不冒充成交时间"
  },
  {
    "url": "https://www.streetinsider.com/Reuters/Alphabet%2Beyes%2B%243%2Bbillion%2BHong%2BKong%2C%2BSingapore%2Bbond%2Bsale%2C%2Bsources%2Bsay/27325764.html",
    "checked_at": "2026-11-11T12:10:17.221674+00:00",
    "note": "本轮公开来源核验；具体发布日期/缺口见正文，checked_at为整理时刻，不冒充成交时间"
  },
  {
    "url": "https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/overview/",
    "checked_at": "2026-11-11T12:10:17.221674+00:00",
    "note": "10日NAV483.84、净资产63.48B；份额不完整"
  },
  {
    "url": "https://edition.cnn.com/markets/fear-and-greed",
    "checked_at": "2026-11-11T12:10:17.221674+00:00",
    "note": "浏览器34/Fear、11日06:48:31EST"
  },
  {
    "url": "https://www.matteoiacoviello.com/gpr.htm",
    "checked_at": "2026-11-11T12:10:17.221674+00:00",
    "note": "官网标9日更新；采集值仅2日，xls重取后解析缺xlrd，不假称已恢复"
  },
  {
    "url": "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm",
    "checked_at": "2026-11-11T12:13:46.462554+00:00",
    "note": "2026年12月8–9日会议；14:00为惯例时间，尚待正式当日日程复核"
  }
]
```

## 付费信源建议（未订阅）

```json
[]
```
